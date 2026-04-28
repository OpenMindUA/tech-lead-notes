"""Split the DORA-metrics-in-Jira methodology document into chunks.

Source is already clean Markdown authored in this repository, so no HTML
conversion is needed. The doc is split per top-level chapter (H2):
  - Introduction (1.x)
  - Ticket discipline (2.x)
  - GitHub side (3.x)
  - Jira setup checklist (4.x)
  - Appendix

Output: docs/sources/dora-metrics-jira/ — one file per chapter.
The whole doc is also preserved as the source landing's introduction.
"""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "raw-sources" / "dora-metrics-jira.md"
OUT = ROOT / "docs" / "sources" / "dora-metrics-jira"

SOURCE_ID = "dora-metrics-jira"
SOURCE_TITLE = "DORA Metrics in Jira: Methodology, Rules, and Setup"
LICENSE = "CC-BY-SA-4.0"
AUTHORS = "openmind"
DOC_VERSION = "1.1"


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[®™©]", "", s)
    s = re.sub(r"[*_`]", "", s)
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
    chapter_idx: int
    start: int
    end: int
    tags: list[str] = field(default_factory=list)


def parse_h2(lines: list[str]) -> list[Heading]:
    pattern = re.compile(r"^(#{2})\s+(.+?)\s*$")
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
        out.append(Heading(level=2, title=m.group(2).strip(), line_no=i))
    return out


def build_chunks(headings: list[Heading], total_lines: int) -> list[Chunk]:
    chunks: list[Chunk] = []
    for i, h in enumerate(headings):
        end = headings[i + 1].line_no if i + 1 < len(headings) else total_lines
        chunks.append(Chunk(
            title=h.title,
            chapter_idx=i + 1,
            start=h.line_no,
            end=end,
        ))
    return chunks


def derive_tags(c: Chunk) -> list[str]:
    base = ["dora", "metrics", "jira", "github", "engineering-effectiveness"]
    base.append(slugify(c.title))
    seen: set[str] = set()
    out: list[str] = []
    for t in base:
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
        ("chapter", c.title),
        ("chapter_index", c.chapter_idx),
        ("source_url", "(self-authored)"),
        ("source_version", DOC_VERSION),
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


def chunk_path(c: Chunk) -> Path:
    fname = f"{c.chapter_idx:02d}-{slugify(c.title)}.md"
    return OUT / fname


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
    """Source landing — preamble before first H2."""
    first_h2 = headings[0].line_no if headings else 0
    preamble = "\n".join(src_lines[:first_h2]).rstrip()

    fm = [
        "---",
        f"title: {SOURCE_TITLE}",
        f"source_id: {SOURCE_ID}",
        f"source_version: {DOC_VERSION}",
        f"license: {LICENSE}",
        f"authors: {AUTHORS}",
        "tags: [dora, metrics, jira, github, source-landing, self-authored]",
        "---",
        "",
    ]
    intro = (
        f"# {SOURCE_TITLE}\n\n"
        "Self-authored methodology document on using DORA (DevOps "
        "Research and Assessment) metrics in Jira for teams on the "
        "Jira + GitHub stack. Covers methodology, ticket discipline, "
        "GitHub-side enforcement, and Jira setup.\n\n"
        f"- **Origin:** authored as part of this repository (no upstream).\n"
        f"- **License:** [{LICENSE}](https://creativecommons.org/licenses/by-sa/4.0/) — © {AUTHORS}\n"
        f"- **Document version:** {DOC_VERSION}\n"
        f"- **Snapshot date:** {date.today().isoformat()}\n\n"
        "## Document preamble\n\n"
    )
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text(
        "\n".join(fm) + intro + preamble + "\n", encoding="utf-8"
    )


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    src_lines = text.splitlines()
    headings = parse_h2(src_lines)

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
