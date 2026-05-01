"""Generate llms.txt and llms-full.txt for the 3-tier corpus.

Tiers:
- Tier 1 — docs/agent-index.md  (compact catalog, fits in a system prompt)
- Tier 2 — docs/distilled/...    (dense per-concept cards)
- Tier 3 — docs/01-…/, 02-…/, … (full original chunks)

llms.txt highlights tiers 1 and 2 prominently; tier 3 is included
section-by-section as deeper-detail anchors.

llms-full.txt concatenates the entire corpus (full original text +
distilled tier) for full-context loading.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

RAW_BASE = os.environ.get(
    "LLMS_RAW_BASE",
    "https://raw.githubusercontent.com/OpenMindUA/tech-lead-notes/main/docs",
)
SITE_BASE = os.environ.get(
    "LLMS_SITE_BASE", "https://openmindua.github.io/tech-lead-notes"
)
SOURCE_URL = "https://pmbok.guide/pmbok-guide--underneath-the-surface.md"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    fm: dict[str, str] = {}
    body = text
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip().strip('"')
        body = text[m.end():]
    return fm, body


def first_paragraph(body: str, max_len: int = 220) -> str:
    para: list[str] = []
    for line in body.splitlines():
        s = line.strip()
        if not s:
            if para:
                break
            continue
        if s.startswith("#"):
            continue
        if s.startswith(("- ", "* ", "1.", ">", "|")):
            if not para:
                continue
            break
        para.append(s)
        if sum(len(p) for p in para) > max_len:
            break
    text = " ".join(para)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_len:
        text = text[: max_len - 1].rsplit(" ", 1)[0] + "…"
    return text


def url_for(path: Path) -> str:
    rel = path.relative_to(DOCS).as_posix()
    return f"{RAW_BASE}/{rel}"


def collect(root: Path) -> list[Path]:
    """Sort with index.md first within each directory, then by filename."""
    files = [p for p in root.rglob("*.md") if p.name != "SUMMARY.md"]

    def key(p: Path):
        parts = list(p.relative_to(DOCS).parts)
        last = parts[-1]
        is_index = 0 if last == "index.md" else 1
        return (parts[:-1], is_index, last)

    return sorted(files, key=key)


def render_tier1() -> list[str]:
    out = ["## Tier 1 — Agent index", ""]
    p = DOCS / "agent-index.md"
    if p.exists():
        out.append(
            f"- [Agent index]({url_for(p)}): one-line catalog of every concept, principle, "
            "performance domain and methodology covered. Designed to fit in a system prompt; "
            "links out to Tier-2 cards."
        )
    out.append("")
    return out


def render_tier2() -> list[str]:
    out = ["## Tier 2 — Distilled cards", ""]
    distilled_root = DOCS / "distilled"
    if not distilled_root.exists():
        return out

    # Group by sub-directory: principles/pmbok-7, principles/nupp, etc.
    groups: dict[str, list[Path]] = {}
    for p in collect(distilled_root):
        rel = p.relative_to(distilled_root)
        if len(rel.parts) == 1:
            group = "_root"
        elif len(rel.parts) == 2:
            group = rel.parts[0]
        else:
            group = "/".join(rel.parts[:-1])
        groups.setdefault(group, []).append(p)

    group_order = [
        "_root",
        "principles/pmbok-7",
        "principles/nupp",
        "principles/prince2",
        "performance-domains",
        "methodologies",
        "scrum-guide",
        "scrum-guide-expanded",
        "dora-metrics-jira",
        "p3-express",
        "micro-p3-express",
        "kanban-guide",
        "open-guide-to-kanban",
        "wardley-maps",
        "synthesis",
    ]
    seen: set[str] = set()
    ordered = [g for g in group_order if g in groups]
    seen.update(ordered)
    for g in groups:
        if g not in seen:
            ordered.append(g)
            seen.add(g)

    titles = {
        "_root": "Distilled — overview, glossary, cross-references",
        "principles/pmbok-7": "Distilled — PMBOK 7 principles",
        "principles/nupp": "Distilled — NUPP principles",
        "principles/prince2": "Distilled — PRINCE2 principles",
        "performance-domains": "Distilled — performance domains",
        "methodologies": "Distilled — methodologies",
        "scrum-guide": "Distilled — Scrum Guide 2020",
        "scrum-guide-expanded": "Distilled — Scrum Guide Expansion Pack (v2026.1)",
        "dora-metrics-jira": "Distilled — DORA Metrics in Jira",
        "p3-express": "Distilled — P3.express manual (v2)",
        "micro-p3-express": "Distilled — micro.P3.express manual",
        "kanban-guide": "Distilled — The Kanban Guide (v2025.5)",
        "open-guide-to-kanban": "Distilled — Open Guide to Kanban (v2025.7)",
        "wardley-maps": "Distilled — Wardley Maps (Simon Wardley)",
        "synthesis": "Distilled — Synthesis (cross-source)",
    }

    for g in ordered:
        out.append(f"### {titles.get(g, g)}")
        out.append("")
        for p in groups[g]:
            fm, body = parse(p)
            title = fm.get("title", p.stem)
            desc = first_paragraph(body)
            out.append(f"- [{title}]({url_for(p)}): {desc}")
        out.append("")
    return out


def render_tier3() -> list[str]:
    """Walk docs/sources/<source-id>/ for each source.

    Each source gets a "### Source: <title>" header. Within a source, chunks
    are grouped under their `chapter:` frontmatter value (when set) so that
    flat files and chapter-directory files mix correctly. Files without a
    `chapter:` field (e.g. the source landing) appear under "(landing)".
    """
    out = ["## Tier 3 — Full original text (per source / chapter)", ""]
    sources_root = DOCS / "sources"
    if not sources_root.exists():
        return out
    for source_dir in sorted(d for d in sources_root.iterdir() if d.is_dir()):
        landing = source_dir / "index.md"
        source_title = source_dir.name
        if landing.exists():
            fm_l, _ = parse(landing)
            source_title = fm_l.get("title", source_dir.name)
        out.append(f"### Source: {source_title}")
        out.append("")

        files = [p for p in collect(source_dir) if p.name != "SUMMARY.md"]
        # Group by chapter, ordered by chapter_index when available.
        groups: dict[str, list[Path]] = {}
        chapter_idx: dict[str, int] = {}
        for p in files:
            fm, _ = parse(p)
            chapter = fm.get("chapter") or "(landing)"
            groups.setdefault(chapter, []).append(p)
            try:
                ci = int(fm.get("chapter_index", "999"))
            except ValueError:
                ci = 999
            chapter_idx.setdefault(chapter, ci if chapter != "(landing)" else -1)
        order = sorted(groups.keys(), key=lambda k: (chapter_idx[k], k))

        for chapter in order:
            out.append(f"#### {chapter}")
            out.append("")
            for p in groups[chapter]:
                fm, body = parse(p)
                title = fm.get("title", p.stem)
                desc = first_paragraph(body)
                out.append(f"- [{title}]({url_for(p)}): {desc}")
            out.append("")
    return out


def render_landing() -> list[str]:
    out = []
    p = DOCS / "index.md"
    if p.exists():
        fm, body = parse(p)
        title = fm.get("title", "Home")
        desc = first_paragraph(body)
        out.append(f"- [{title}]({url_for(p)}): {desc}")
        out.append("")
    return out


def build_llms_txt() -> str:
    lines: list[str] = []
    lines.append("# Tech Lead Notes")
    lines.append("")
    lines.append(
        "> Multi-source, three-tier mirror of CC-licensed project-management "
        "resources. Tier 1 = agent index (compact catalog); "
        "Tier 2 = distilled per-concept cards (TL;DR / core ideas / "
        "anti-patterns / cross-refs); Tier 3 = full original text per source. "
        "License per source — see each chunk's `license:` frontmatter field."
    )
    lines.append("")
    lines.extend(render_landing())
    lines.extend(render_tier1())
    lines.extend(render_tier2())
    lines.extend(render_tier3())

    lines.append("## Optional")
    lines.append("")
    raw_root = RAW_BASE.rsplit("/", 1)[0]
    lines.append(
        f"- [Full text concatenation]({raw_root}/llms-full.txt): "
        "every Tier-3 chunk merged into a single document."
    )
    lines.append(
        f"- [HTML site]({SITE_BASE}): rendered MkDocs site with search, navigation and tags."
    )
    lines.append(
        f"- [Original markdown source]({SOURCE_URL}): "
        "canonical upstream file."
    )
    lines.append("")
    return "\n".join(lines)


def build_llms_full() -> str:
    out: list[str] = []
    out.append("# Tech Lead Notes — Full Concatenation\n")
    out.append(
        "Multi-source mirror of CC-BY / CC-BY-SA project-management resources, "
        "with editorial distillation. See per-chunk frontmatter for source URL "
        "and license.\n"
    )
    out.append("\n---\n")
    out.append("\n## Tier 2 — Distilled cards\n")
    for p in collect(DOCS / "distilled") if (DOCS / "distilled").exists() else []:
        fm, body = parse(p)
        rel = p.relative_to(DOCS).as_posix()
        out.append(f"\n\n<!-- distilled-chunk: {rel} -->\n")
        out.append(f"<!-- title: {fm.get('title', '')} -->\n")
        if fm.get("license"):
            out.append(f"<!-- license: {fm['license']} -->\n")
        out.append("\n")
        out.append(body.strip())
        out.append("\n")
    out.append("\n---\n")
    out.append("\n## Tier 3 — Full original text (all sources)\n")
    sources_root = DOCS / "sources"
    if sources_root.exists():
        for source_dir in sorted(d for d in sources_root.iterdir() if d.is_dir()):
            for p in collect(source_dir):
                fm, body = parse(p)
                rel = p.relative_to(DOCS).as_posix()
                out.append(f"\n\n<!-- chunk: {rel} -->\n")
                out.append(f"<!-- title: {fm.get('title', '')} -->\n")
                if fm.get("source_id") or source_dir.name:
                    out.append(f"<!-- source_id: {fm.get('source_id', source_dir.name)} -->\n")
                if fm.get("chapter"):
                    out.append(f"<!-- chapter: {fm['chapter']} -->\n")
                if fm.get("section"):
                    out.append(f"<!-- section: {fm['section']} -->\n")
                if fm.get("license"):
                    out.append(f"<!-- license: {fm['license']} -->\n")
                out.append("\n")
                out.append(body.strip())
                out.append("\n")
    return "".join(out)


def main() -> None:
    txt = build_llms_txt()
    full = build_llms_full()
    (ROOT / "llms.txt").write_text(txt, encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(full, encoding="utf-8")
    (DOCS / "llms.txt").write_text(txt, encoding="utf-8")
    (DOCS / "llms-full.txt").write_text(full, encoding="utf-8")
    print("Wrote llms.txt and llms-full.txt at root and docs/.")


if __name__ == "__main__":
    main()
