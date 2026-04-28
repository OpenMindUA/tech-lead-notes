"""Split the source MD book into wiki-style chunks with YAML frontmatter.

Output goes under docs/sources/underneath-the-surface/. Each H1 → directory,
each H2 → file. Exception: H2 sections listed in SPLIT_BY_H3 are split further
by H3, one file per H3.

Only the per-source output directory is wiped on regeneration; the rest of
docs/ (distilled/, agent-index.md, other sources) is preserved.
"""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "raw-sources" / "pmbok-guide--underneath-the-surface.md"
DOCS = ROOT / "docs"
SOURCE_ID = "underneath-the-surface"
OUT = DOCS / "sources" / SOURCE_ID
SOURCE_URL = "https://pmbok.guide/pmbok-guide--underneath-the-surface.md"
LICENSE = "CC-BY-4.0"
AUTHOR = "Nader K. Rad"
SOURCE_DATE = "2023-06-08"

# H2 titles whose H3 children should each become a separate file.
SPLIT_BY_H3 = {
    "PMBOK 7 principles",
    "NUPP principles",
    "PRINCE2® principles",
}


@dataclass
class Heading:
    level: int  # 1, 2, or 3
    title: str
    line_no: int  # 0-indexed line of the heading itself


@dataclass
class Chunk:
    """A piece of the book that becomes one output file."""
    title: str
    h1: str | None
    h2: str | None
    h3: str | None
    start: int  # inclusive line index of heading
    end: int    # exclusive line index (next heading or EOF)
    chapter_idx: int
    section_idx: int | None = None
    sub_idx: int | None = None
    tags: list[str] = field(default_factory=list)


def slugify(text: str) -> str:
    """Lowercase, strip marks, replace non-alnum with '-'."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_headings(lines: list[str]) -> list[Heading]:
    pattern = re.compile(r"^(#{1,3})\s+(.+?)\s*$")
    headings: list[Heading] = []
    in_code = False
    for i, line in enumerate(lines):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = pattern.match(line)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        headings.append(Heading(level=level, title=title, line_no=i))
    return headings


def build_chunks(headings: list[Heading], total_lines: int) -> list[Chunk]:
    chunks: list[Chunk] = []
    chapter_idx = 0
    current_h1: str | None = None
    section_idx = 0
    current_h2: str | None = None
    sub_idx = 0
    split_h3_active = False  # True when current H2 is a SPLIT_BY_H3 section

    # We'll iterate headings and emit a chunk whose range ends at the next heading
    # of the same or shallower level (H1 ends at next H1, H2 ends at next H2/H1, etc.)
    # Implementation: emit chunk per heading, with end = next heading line; merge later.

    # Indices of headings that start chunks
    chunk_starts: list[int] = []
    for idx, h in enumerate(headings):
        if h.level == 1:
            chunk_starts.append(idx)
        elif h.level == 2:
            chunk_starts.append(idx)
        elif h.level == 3:
            # Only emit H3 chunks when the parent H2 is in SPLIT_BY_H3
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
        # Determine end line: start of next chunk-start heading, or EOF
        if ci + 1 < len(chunk_starts):
            end_line = headings[chunk_starts[ci + 1]].line_no
        else:
            end_line = total_lines

        # Update parents
        if h.level == 1:
            chapter_idx += 1
            current_h1 = h.title
            current_h2 = None
            section_idx = 0
            sub_idx = 0
            split_h3_active = False
        elif h.level == 2:
            section_idx += 1
            current_h2 = h.title
            sub_idx = 0
            split_h3_active = current_h2 in SPLIT_BY_H3
        elif h.level == 3:
            sub_idx += 1

        # If this H2 is a SPLIT_BY_H3 section, the H2 itself becomes an index-only
        # chunk that ends just before its first H3 child. We'll still emit it,
        # and its body is the intro text before the first H3.
        if h.level == 2 and split_h3_active:
            # Find first H3 inside this H2
            for inner in headings[hidx + 1:]:
                if inner.level <= 2:
                    break
                if inner.level == 3:
                    end_line = inner.line_no
                    break

        chunk = Chunk(
            title=h.title,
            h1=current_h1,
            h2=current_h2 if h.level >= 2 else None,
            h3=h.title if h.level == 3 else None,
            start=h.line_no,
            end=end_line,
            chapter_idx=chapter_idx,
            section_idx=section_idx if h.level >= 2 else None,
            sub_idx=sub_idx if h.level == 3 else None,
        )
        chunks.append(chunk)

    return chunks


def chunk_path(c: Chunk) -> Path:
    chapter_dir = f"{c.chapter_idx:02d}-{slugify(c.h1 or 'intro')}"
    if c.h3 is not None:
        section_dir = f"{c.section_idx:02d}-{slugify(c.h2 or '')}"
        filename = f"{c.sub_idx:02d}-{slugify(c.h3)}.md"
        return OUT / chapter_dir / section_dir / filename
    if c.section_idx is None:
        return OUT / chapter_dir / "index.md"
    if c.h2 in SPLIT_BY_H3:
        section_dir = f"{c.section_idx:02d}-{slugify(c.h2 or '')}"
        return OUT / chapter_dir / section_dir / "index.md"
    filename = f"{c.section_idx:02d}-{slugify(c.h2 or '')}.md"
    return OUT / chapter_dir / filename


def derive_tags(c: Chunk) -> list[str]:
    tags: list[str] = []
    if c.h1:
        tags.append(slugify(c.h1))
    if c.h2:
        tags.append(slugify(c.h2))
    if c.h3:
        tags.append(slugify(c.h3))
    if c.h2 in SPLIT_BY_H3 or c.h3 and c.h2 in SPLIT_BY_H3:
        tags.append("principle")
    if c.h1 == "Enriching the Methodology":
        tags.append("performance-domain")
    if c.h1 == "Selecting a Methodology":
        tags.append("methodology")
    # de-dup, preserve order
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
        ("chapter", c.h1),
        ("chapter_index", c.chapter_idx),
        ("section", c.h2),
        ("section_index", c.section_idx),
        ("subsection", c.h3),
        ("subsection_index", c.sub_idx),
        ("source_url", SOURCE_URL),
        ("source_date", SOURCE_DATE),
        ("source_lines", f"{c.start + 1}-{c.end}"),
        ("license", LICENSE),
        ("author", AUTHOR),
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
    body_lines = src_lines[c.start:c.end]
    # Strip trailing empty lines
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()
    body = "\n".join(body_lines).rstrip() + "\n"
    content = render_frontmatter(c) + body
    path.write_text(content, encoding="utf-8")
    return path


def write_landing(src_lines: list[str], headings: list[Heading]) -> None:
    """Source-local landing page at OUT/index.md (preamble + intro)."""
    first_h1_line = next(h.line_no for h in headings if h.level == 1)
    preamble = "\n".join(src_lines[:first_h1_line]).rstrip()
    fm_lines = [
        "---",
        "title: PMBOK Guide — Underneath the Surface",
        f"source_id: {SOURCE_ID}",
        f"source_url: {SOURCE_URL}",
        f"source_date: {SOURCE_DATE}",
        f"license: {LICENSE}",
        f"author: {AUTHOR}",
        "tags: [front-matter, source-landing]",
        "---",
        "",
    ]
    intro = (
        "# PMBOK Guide — Underneath the Surface\n\n"
        "Mirror of Nader K. Rad's *PMBOK Guide: Underneath the Surface*, "
        "split into navigable chunks with YAML frontmatter.\n\n"
        f"- **Original (canonical):** <{SOURCE_URL}>\n"
        f"- **License:** [{LICENSE}](https://creativecommons.org/licenses/by/4.0/) — © {AUTHOR}\n"
        f"- **Source snapshot date:** {SOURCE_DATE}\n\n"
        "## Front matter from the book\n\n"
    )
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text(
        "\n".join(fm_lines) + intro + preamble + "\n", encoding="utf-8"
    )


def write_summary(chunks: list[Chunk]) -> None:
    """Per-source SUMMARY.md (mdBook-style backup nav)."""
    lines: list[str] = ["# Summary", ""]
    for c in chunks:
        rel = chunk_path(c).relative_to(OUT).as_posix()
        if c.h3 is not None:
            indent = "    "
            lines.append(f"{indent}- [{c.title}]({rel})")
        elif c.section_idx is not None:
            indent = "  "
            lines.append(f"{indent}- [{c.title}]({rel})")
        else:
            lines.append(f"- [{c.title}]({rel})")
    (OUT / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    src_lines = text.splitlines()
    headings = parse_headings(src_lines)

    # Wipe only this source's output, never the rest of docs/
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
    write_summary(chunks)

    print(f"Wrote {len(written)} chunk files under {OUT}")
    for p in written:
        print(" -", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
