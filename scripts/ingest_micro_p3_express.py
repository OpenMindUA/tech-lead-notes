"""Ingest the canonical micro.P3.express manual.

Source:  https://micro.p3.express/  (CC BY 4.0 — © PTCoE)
Output:  raw-sources/micro-p3-express.md + docs/sources/micro-p3-express/

6 activity groups (no group B), 23 activities. URL pattern:
    https://micro.p3.express/<letter><number>/

Designed for very small projects (1-4 team members).
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from lib.web_to_md import (  # noqa: E402
    Chunk,
    extract_main,
    fetch_html,
    html_to_markdown,
    reset_dir,
    slugify,
    write_chunk,
    write_concat,
)

SOURCE_ID = "micro-p3-express"
BASE = "https://micro.p3.express"
LICENSE = "CC-BY-4.0"
AUTHORS = "PTCoE — Nader K. Rad et al."
SOURCE_VERSION = "current"

# (group_letter, group_index, group_title, [(activity_index, activity_title)])
GROUPS = [
    ("a", 1, "Project Initiation", [
        (1, "Identify the high-level decision maker(s)"),
        (2, "Understand and distribute the hats"),
        (3, "Select tools and create a project repository"),
        (4, "Create a common understanding"),
        (5, "Have Project Initiation peer-reviewed"),
        (6, "Make a go/no-go decision"),
        (7, "Conduct a focused communication"),
    ]),
    ("c", 2, "Weekly Initiation", [
        (1, "Revise and refine the common understanding"),
        (2, "Have the Weekly Initiation peer-reviewed"),
        (3, "Make a go/no-go decision"),
        (4, "Conduct a focused communication"),
    ]),
    ("d", 3, "Daily Management", [
        (1, "Manage follow-up items"),
        (2, "Close completed deliverables"),
    ]),
    ("e", 4, "Weekly Closure", [
        (1, "Measure and report performance"),
        (2, "Evaluate stakeholder satisfaction"),
        (3, "Capture lessons and plan for improvements"),
        (4, "Consider swapping hats for the week"),
    ]),
    ("f", 5, "Project Closure", [
        (1, "Double-check and hand over the final output"),
        (2, "Evaluate stakeholder satisfaction"),
        (3, "Have the Project Closure peer-reviewed"),
        (4, "Consider swapping hats for Post-Project Management"),
        (5, "Archive the project documents"),
        (6, "Celebrate"),
        (7, "Conduct a focused communication"),
    ]),
    ("g", 6, "Post-Project Management", [
        (1, "Evaluate the benefits"),
        (2, "Generate new ideas"),
        (3, "Conduct a focused communication"),
    ]),
]

OUT = ROOT / "docs" / "sources" / SOURCE_ID
RAW = ROOT / "raw-sources" / "micro-p3-express.md"


def fetch_landing() -> Chunk:
    url = BASE + "/"
    print(f"  fetching {url} ...")
    html = fetch_html(url)
    inner = extract_main(html, url, anchor_on_h1=True)
    body = html_to_markdown(inner)
    return Chunk(
        out_path=OUT / "index.md",
        title="micro.P3.express manual",
        body=body,
        frontmatter={
            "title": "micro.P3.express manual",
            "source_id": SOURCE_ID,
            "source_url": BASE + "/",
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["micro-p3-express", "front-matter", "source-landing", "methodology"],
        },
    )


def fetch_group_index(letter: str, idx: int, title: str) -> Chunk:
    return Chunk(
        out_path=OUT / f"{idx:02d}-{letter}-{slugify(title)}" / "index.md",
        title=f"Group {letter.upper()} — {title}",
        body=f"# Group {letter.upper()} — {title}\n\nSee individual activity pages.",
        frontmatter={
            "title": f"Group {letter.upper()} — {title}",
            "source_id": SOURCE_ID,
            "chapter": title,
            "chapter_index": idx,
            "source_url": BASE + "/",
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["micro-p3-express", "activity-group", letter, slugify(title)],
        },
    )


def fetch_activity(letter: str, group_idx: int, group_title: str,
                   act_idx: int, act_title: str) -> Chunk:
    url = f"{BASE}/{letter}{act_idx}/"
    print(f"  fetching {url} ...")
    html = fetch_html(url)
    inner = extract_main(html, url, anchor_on_h1=True)
    body = html_to_markdown(inner)
    code = f"{letter.upper()}{act_idx}"
    out_path = (OUT / f"{group_idx:02d}-{letter}-{slugify(group_title)}"
                    / f"{act_idx:02d}-{slugify(act_title)}.md")
    return Chunk(
        out_path=out_path,
        title=f"{code} — {act_title}",
        body=body,
        frontmatter={
            "title": f"{code} — {act_title}",
            "source_id": SOURCE_ID,
            "chapter": group_title,
            "chapter_index": group_idx,
            "section": act_title,
            "section_index": act_idx,
            "activity_code": code,
            "source_url": url,
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["micro-p3-express", letter, slugify(group_title), code.lower()],
        },
    )


def main() -> None:
    print(f"Ingesting micro.P3.express from {BASE} ...")
    reset_dir(OUT)
    chunks = [fetch_landing()]
    for letter, gidx, gtitle, activities in GROUPS:
        chunks.append(fetch_group_index(letter, gidx, gtitle))
        for aidx, atitle in activities:
            chunks.append(fetch_activity(letter, gidx, gtitle, aidx, atitle))

    for c in chunks:
        write_chunk(c)
    write_concat(RAW, chunks)

    print(f"Wrote {len(chunks)} files under {OUT.relative_to(ROOT)}")
    print(f"Wrote raw concatenation to {RAW.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
