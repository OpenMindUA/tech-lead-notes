"""Fetch the Scrum Guide (2020) HTML, convert to markdown, and split into chunks
under docs/sources/scrum-guide/.

License of the source content: CC BY-SA 4.0
© 2020 Ken Schwaber and Jeff Sutherland
Source: https://scrumguides.org/scrum-guide.html

Run:
    uv run --group ingest python scripts/ingest_scrum_guide.py

The script writes:
- raw-sources/scrum-guide.md         the full markdown snapshot (committed)
- docs/sources/scrum-guide/           one file per H2, with H3 children split for
                                      sections that have multiple H3s
"""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md

ROOT = Path(__file__).resolve().parent.parent
RAW_SOURCES = ROOT / "raw-sources"
RAW_FILE = RAW_SOURCES / "scrum-guide.md"
OUT = ROOT / "docs" / "sources" / "scrum-guide"

SOURCE_URL = "https://scrumguides.org/scrum-guide.html"
SOURCE_ID = "scrum-guide"
SOURCE_TITLE = "The 2020 Scrum Guide"
LICENSE = "CC-BY-SA-4.0"
AUTHORS = "Ken Schwaber, Jeff Sutherland"
PUBLICATION_YEAR = 2020

# H2 sections whose H3 children should each become a separate file.
SPLIT_BY_H3 = {
    "Scrum Theory",
    "Scrum Team",
    "Scrum Events",
    "Scrum Artifacts",
}


def fetch_and_convert() -> str:
    """Fetch the page and return clean markdown of the article body."""
    r = httpx.get(SOURCE_URL, timeout=30, follow_redirects=True)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    # Strip elements that don't belong to the article body
    for selector in [
        "header", "footer", "nav", "script", "style", "noscript",
        ".header", ".footer", ".nav", ".navigation", ".sidebar",
        ".social", ".share", ".cookie", ".cookies",
    ]:
        for el in soup.select(selector):
            el.decompose()

    # Take whichever container most plausibly holds the content.
    candidate = (
        soup.find("article")
        or soup.find("main")
        or soup.find("body")
    )
    container: Tag = candidate if isinstance(candidate, Tag) else soup

    # Make relative URLs absolute so mkdocs --strict doesn't try to resolve
    # them as local docs.
    for tag_name, attr in (("a", "href"), ("img", "src")):
        for el in container.find_all(tag_name):
            if not isinstance(el, Tag):
                continue
            val = el.get(attr)
            if isinstance(val, list):
                val = val[0] if val else None
            if isinstance(val, str) and not val.startswith(
                ("http://", "https://", "mailto:", "#")
            ):
                el[attr] = urljoin(SOURCE_URL, val)

    # Convert to markdown. ATX headings, no auto-link mangling.
    text = md(
        str(container),
        heading_style="ATX",
        bullets="-",
        strip=["a"] if False else None,  # keep links
    )

    # Tidy up whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip() + "\n"


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[®™©]", "", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


@dataclass
class Heading:
    level: int
    title: str
    line_no: int


@dataclass
class Chunk:
    title: str
    h1: str | None
    h2: str | None
    h3: str | None
    start: int
    end: int
    chapter_idx: int
    section_idx: int | None = None
    sub_idx: int | None = None
    tags: list[str] = field(default_factory=list)


def parse_headings(lines: list[str]) -> list[Heading]:
    pattern = re.compile(r"^(#{1,3})\s+(.+?)\s*$")
    in_code = False
    out: list[Heading] = []
    for i, line in enumerate(lines):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = pattern.match(line)
        if not m:
            continue
        out.append(Heading(level=len(m.group(1)),
                           title=m.group(2).strip(),
                           line_no=i))
    return out


def build_chunks(headings: list[Heading], total_lines: int) -> list[Chunk]:
    """For Scrum Guide we treat each H2 as a chapter (H1 is the document title)."""
    chunks: list[Chunk] = []
    chapter_idx = 0
    section_idx = 0
    sub_idx = 0
    current_h2: str | None = None

    chunk_starts: list[int] = []
    for idx, h in enumerate(headings):
        if h.level == 2:
            chunk_starts.append(idx)
        elif h.level == 3:
            # Find parent H2
            parent_h2 = None
            for prev in reversed(headings[:idx]):
                if prev.level == 2:
                    parent_h2 = prev.title
                    break
                if prev.level == 1:
                    break
            if parent_h2 in SPLIT_BY_H3:
                chunk_starts.append(idx)

    for ci, hidx in enumerate(chunk_starts):
        h = headings[hidx]
        if ci + 1 < len(chunk_starts):
            end_line = headings[chunk_starts[ci + 1]].line_no
        else:
            end_line = total_lines

        if h.level == 2:
            chapter_idx += 1
            current_h2 = h.title
            section_idx = 0
            sub_idx = 0
            split_active = current_h2 in SPLIT_BY_H3
            if split_active:
                # H2 chunk = intro before first H3
                for inner in headings[hidx + 1:]:
                    if inner.level <= 2:
                        break
                    if inner.level == 3:
                        end_line = inner.line_no
                        break
        elif h.level == 3:
            section_idx += 1
            sub_idx = section_idx

        chunk = Chunk(
            title=h.title,
            h1=None,  # Scrum Guide H1 is the doc title; we don't propagate it
            h2=current_h2 if h.level >= 2 else None,
            h3=h.title if h.level == 3 else None,
            start=h.line_no,
            end=end_line,
            chapter_idx=chapter_idx,
            section_idx=section_idx if h.level == 3 else None,
            sub_idx=sub_idx if h.level == 3 else None,
        )
        chunks.append(chunk)
    return chunks


def chunk_path(c: Chunk) -> Path:
    chapter_dir = f"{c.chapter_idx:02d}-{slugify(c.h2 or '')}"
    if c.h3 is not None:
        filename = f"{c.sub_idx:02d}-{slugify(c.h3)}.md"
        return OUT / chapter_dir / filename
    if c.h2 in SPLIT_BY_H3:
        return OUT / chapter_dir / "index.md"
    filename = f"{chapter_dir}.md"
    return OUT / filename


def derive_tags(c: Chunk) -> list[str]:
    tags = ["scrum", "scrum-guide-2020"]
    if c.h2:
        tags.append(slugify(c.h2))
    if c.h3:
        tags.append(slugify(c.h3))
    seen: set[str] = set()
    out: list[str] = []
    for t in tags:
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out


def yaml_value(v: object) -> str:
    if isinstance(v, list):
        if not v:
            return "[]"
        return "[" + ", ".join(yaml_value(x) for x in v) + "]"
    if isinstance(v, int):
        return str(v)
    if v is None:
        return "null"
    s = str(v)
    if any(ch in s for ch in [":", "#", "'", '"', "[", "]", "{", "}"]) or s.strip() != s:
        return '"' + s.replace('"', '\\"') + '"'
    return s


def render_frontmatter(c: Chunk) -> str:
    fields: list[tuple[str, object]] = [
        ("title", c.title),
        ("source_id", SOURCE_ID),
        ("chapter", c.h2),
        ("chapter_index", c.chapter_idx),
        ("section", c.h3),
        ("section_index", c.sub_idx),
        ("source_url", SOURCE_URL),
        ("source_publication_year", PUBLICATION_YEAR),
        ("source_lines", f"{c.start + 1}-{c.end}"),
        ("license", LICENSE),
        ("authors", AUTHORS),
        ("tags", c.tags),
    ]
    lines = ["---"]
    for k, v in fields:
        if v is None or v == [] or v == "":
            continue
        lines.append(f"{k}: {yaml_value(v)}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def write_chunk(c: Chunk, src_lines: list[str]) -> Path:
    path = chunk_path(c)
    path.parent.mkdir(parents=True, exist_ok=True)
    body = src_lines[c.start:c.end]
    while body and not body[-1].strip():
        body.pop()
    text = "\n".join(body).rstrip() + "\n"
    path.write_text(render_frontmatter(c) + text, encoding="utf-8")
    return path


def write_landing(src_lines: list[str], headings: list[Heading]) -> None:
    """Source landing at docs/sources/scrum-guide/index.md."""
    # Preamble = lines from start to first H2 (the section before "Purpose...")
    first_h2 = next((h for h in headings if h.level == 2), None)
    preamble_end = first_h2.line_no if first_h2 else 0
    raw_preamble = src_lines[:preamble_end]

    # Strip "Table of Contents" block (intra-page anchors no longer resolve
    # after splitting into separate files).
    cleaned: list[str] = []
    skipping_toc = False
    toc_anchor_re = re.compile(r"^\s*[-*+]\s+\[.+\]\(#[^)]+\)\s*$")
    for line in raw_preamble:
        if re.match(r"^\s*Table of Contents\s*$", line, re.I):
            skipping_toc = True
            continue
        if skipping_toc:
            if toc_anchor_re.match(line) or not line.strip():
                continue
            # First non-TOC, non-empty line ends skipping
            skipping_toc = False
        cleaned.append(line)
    preamble = "\n".join(cleaned).rstrip()

    fm = [
        "---",
        f"title: {SOURCE_TITLE}",
        f"source_id: {SOURCE_ID}",
        f"source_url: {SOURCE_URL}",
        f"source_publication_year: {PUBLICATION_YEAR}",
        f"license: {LICENSE}",
        f"authors: {AUTHORS}",
        "tags: [front-matter, source-landing, scrum]",
        "---",
        "",
    ]
    intro = (
        f"# {SOURCE_TITLE}\n\n"
        "Mirror of the *2020 Scrum Guide* by Ken Schwaber and Jeff Sutherland, "
        "split into chunks for use as a knowledge base for agents.\n\n"
        f"- **Original (canonical):** <{SOURCE_URL}>\n"
        f"- **License:** [{LICENSE}](https://creativecommons.org/licenses/by-sa/4.0/) — "
        f"© {PUBLICATION_YEAR} {AUTHORS}\n"
        f"- **Snapshot date:** {date.today().isoformat()}\n\n"
        "## Front matter from the original\n\n"
    )
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text(
        "\n".join(fm) + intro + preamble + "\n", encoding="utf-8"
    )


def main() -> None:
    print(f"Fetching {SOURCE_URL} ...")
    text = fetch_and_convert()
    RAW_SOURCES.mkdir(parents=True, exist_ok=True)
    RAW_FILE.write_text(text, encoding="utf-8")
    print(f"Wrote raw markdown to {RAW_FILE.relative_to(ROOT)} ({len(text)} chars)")

    src_lines = text.splitlines()
    headings = parse_headings(src_lines)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    chunks = build_chunks(headings, total_lines=len(src_lines))
    for c in chunks:
        c.tags = derive_tags(c)

    write_landing(src_lines, headings)
    written: list[Path] = []
    for c in chunks:
        written.append(write_chunk(c, src_lines))
    print(f"Wrote {len(written)} chunks under {OUT.relative_to(ROOT)}")
    for p in written:
        print(" -", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
