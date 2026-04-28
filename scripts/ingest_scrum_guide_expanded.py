"""Fetch the Scrum Guide Expanded (v2026.1), convert to markdown, and split
into chunks under docs/sources/scrum-guide-expanded/.

License of the source content: CC BY-SA 4.0
© 2025 Ralph Jocham, John Coleman, Jeff Sutherland
Source: https://scrumexpansion.org/scrum-guide-expanded/

Run:
    uv run --group ingest python scripts/ingest_scrum_guide_expanded.py

Notes:
- The source page renders almost everything as <h2>; there is no proper
  HTML hierarchy. We therefore declare an explicit list of "chapter
  headers" — H2s that group following H2s as their children.
- Children of a chapter header become files inside a per-chapter directory.
- A chapter header without children is emitted as a flat file.
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
RAW_FILE = RAW_SOURCES / "scrum-guide-expanded.md"
OUT = ROOT / "docs" / "sources" / "scrum-guide-expanded"

SOURCE_URL = "https://scrumexpansion.org/scrum-guide-expanded/"
SOURCE_ID = "scrum-guide-expanded"
SOURCE_TITLE = "Scrum Guide Expansion Pack (v2026.1)"
LICENSE = "CC-BY-SA-4.0"
AUTHORS = "Ralph Jocham, John Coleman, Jeff Sutherland"
PUBLICATION_YEAR = 2025  # © 2025; v2026.1 published 2026-01-18

# Ordered list of chapter-header H2 titles. has_children == True means
# subsequent (non-chapter-header) H2s become children of this chapter.
# Use exact text including curly apostrophes from the source HTML.
CHAPTER_HEADERS: list[tuple[str, bool]] = [
    ("Background", False),
    ("Purpose of the Scrum Guide Expansion Pack", False),
    ("Scrum in a Nutshell", False),
    ("Supporting and Complementary Theory", True),
    ("The Three Pillars of Scrum’s Empirical Process Control", True),
    ("The Scrum Values", False),
    ("More Supporting and Complementary Theory", True),
    ("The Scrum Roles in the Expansion Pack", True),
    ("The Scrum Artifacts in the Expansion Pack", True),
    ("The Scrum Events in the Expansion Pack", True),
    ("End Note", False),
    ("Acknowledgments", False),
    ("Attribution for the Scrum Guide Expansion Pack Collection", False),
    ("References", False),
]


def normalize(s: str) -> str:
    """Loose match: lowercase, ascii-folded, alnum-collapsed."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "", s.lower())
    return s


CHAPTER_LOOKUP: dict[str, tuple[str, bool, int]] = {
    normalize(name): (name, has_children, idx)
    for idx, (name, has_children) in enumerate(CHAPTER_HEADERS, start=1)
}


def fetch_and_convert() -> str:
    r = httpx.get(SOURCE_URL, timeout=60, follow_redirects=True)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    for selector in [
        "header", "footer", "nav", "script", "style", "noscript", "form",
        ".header", ".footer", ".nav", ".navigation", ".sidebar",
        ".social", ".share", ".cookie", ".cookies", ".comments",
    ]:
        for el in soup.select(selector):
            el.decompose()

    candidate = (
        soup.find("article")
        or soup.find("main")
        or soup.find(class_="entry-content")
        or soup.find("body")
    )
    container: Tag = candidate if isinstance(candidate, Tag) else soup

    # Resolve relative URLs to absolute
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

    text = md(str(container), heading_style="ATX", bullets="-")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    # Repair the source's smashed-together small-caps phrases
    fixes = {
        "TheWhyfor the Sprint": "The *Why* for the Sprint",
        "TheWhattoward theWhy": "The *What* toward the *Why*",
        "TheHowfor theWhat": "The *How* for the *What*",
    }
    for src, dst in fixes.items():
        text = text.replace(src, dst)
    return text.strip() + "\n"


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[®™©]", "", s)
    s = re.sub(r"[*_]", "", s)
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
    chapter: str
    chapter_idx: int
    section: str | None
    section_idx: int | None
    is_chapter_index: bool
    start: int
    end: int
    tags: list[str] = field(default_factory=list)


def parse_h1_h2(lines: list[str]) -> list[Heading]:
    pattern = re.compile(r"^(#{1,2})\s+(.+?)\s*$")
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
    """Group H2s under chapter headers."""
    chunks: list[Chunk] = []
    current_chapter: str | None = None
    current_chapter_idx = 0
    current_chapter_has_children = False
    section_idx = 0

    # Filter to H2s only and find their boundaries
    h2s = [h for h in headings if h.level == 2]
    for i, h in enumerate(h2s):
        next_line = h2s[i + 1].line_no if i + 1 < len(h2s) else total_lines
        norm = normalize(h.title)
        if norm in CHAPTER_LOOKUP:
            canonical, has_children, ch_idx = CHAPTER_LOOKUP[norm]
            current_chapter = canonical
            current_chapter_idx = ch_idx
            current_chapter_has_children = has_children
            section_idx = 0
            chunks.append(Chunk(
                title=canonical,
                chapter=canonical,
                chapter_idx=ch_idx,
                section=None,
                section_idx=None,
                is_chapter_index=has_children,
                start=h.line_no,
                end=next_line,
            ))
        else:
            if current_chapter is None:
                # Orphan H2 before any chapter header — wrap as its own chunk
                continue
            section_idx += 1
            chunks.append(Chunk(
                title=h.title,
                chapter=current_chapter,
                chapter_idx=current_chapter_idx,
                section=h.title,
                section_idx=section_idx,
                is_chapter_index=False,
                start=h.line_no,
                end=next_line,
            ))
            # If parent isn't a "has-children" chapter, this H2 is unexpected;
            # we still write it so no content is lost.
            if not current_chapter_has_children:
                pass

    # For "has-children" chapters, the chapter index chunk should end at the
    # first child's start.
    by_chapter_idx: dict[int, list[Chunk]] = {}
    for c in chunks:
        by_chapter_idx.setdefault(c.chapter_idx, []).append(c)
    for ch_idx, items in by_chapter_idx.items():
        # items[0] is the chapter heading itself
        if items[0].is_chapter_index and len(items) > 1:
            items[0].end = items[1].start

    return chunks


def chunk_path(c: Chunk) -> Path:
    chapter_dir_name = f"{c.chapter_idx:02d}-{slugify(c.chapter)}"
    if c.is_chapter_index:
        return OUT / chapter_dir_name / "index.md"
    if c.section is not None:
        filename = f"{c.section_idx:02d}-{slugify(c.section)}.md"
        return OUT / chapter_dir_name / filename
    # standalone chapter (no children)
    return OUT / f"{chapter_dir_name}.md"


def derive_tags(c: Chunk) -> list[str]:
    tags = ["scrum", "scrum-guide-expanded", "v2026.1"]
    if c.chapter:
        tags.append(slugify(c.chapter))
    if c.section:
        tags.append(slugify(c.section))
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
        ("chapter", c.chapter),
        ("chapter_index", c.chapter_idx),
        ("section", c.section),
        ("section_index", c.section_idx),
        ("source_url", SOURCE_URL),
        ("source_publication_year", PUBLICATION_YEAR),
        ("source_version", "v2026.1"),
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
    """docs/sources/scrum-guide-expanded/index.md = preamble before first H2."""
    first_h2 = next((h for h in headings if h.level == 2), None)
    end = first_h2.line_no if first_h2 else 0
    raw_preamble = src_lines[:end]

    cleaned: list[str] = []
    skipping_toc = False
    toc_anchor_re = re.compile(r"^\s*[-*+]\s+\[.+\]\(#[^)]+\)\s*$")
    for line in raw_preamble:
        if re.match(r"^\s*#{1,4}\s*Table of Contents\s*$", line, re.I) \
                or re.match(r"^\s*Table of Contents\s*$", line, re.I):
            skipping_toc = True
            continue
        if skipping_toc:
            if toc_anchor_re.match(line) or not line.strip():
                continue
            skipping_toc = False
        cleaned.append(line)
    preamble = "\n".join(cleaned).rstrip()

    fm = [
        "---",
        f"title: {SOURCE_TITLE}",
        f"source_id: {SOURCE_ID}",
        f"source_url: {SOURCE_URL}",
        f"source_publication_year: {PUBLICATION_YEAR}",
        "source_version: v2026.1",
        f"license: {LICENSE}",
        f"authors: {AUTHORS}",
        "tags: [front-matter, source-landing, scrum, scrum-guide-expanded]",
        "---",
        "",
    ]
    intro = (
        f"# {SOURCE_TITLE}\n\n"
        "Mirror of the *Scrum Guide Expansion Pack* (v2026.1) by "
        "Ralph Jocham, John Coleman and Jeff Sutherland — an adaptation of "
        "the original 2020 Scrum Guide.\n\n"
        f"- **Original (canonical):** <{SOURCE_URL}>\n"
        f"- **License:** [{LICENSE}](https://creativecommons.org/licenses/by-sa/4.0/) — "
        f"© {PUBLICATION_YEAR} {AUTHORS}\n"
        f"- **Snapshot date:** {date.today().isoformat()}\n"
        "- **Modification notice:** This is an adaptation of the 2020 Scrum Guide. "
        "Changes have been made from the original.\n\n"
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
    headings = parse_h1_h2(src_lines)

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
