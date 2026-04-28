"""Ingest the canonical P3.express manual (v2).

Source:  https://p3.express/manual/v2/  (CC BY 4.0 — © PTCoE)
Output:  raw-sources/p3-express.md + docs/sources/p3-express/

7 activity groups (A-G), 33 total activities. URL pattern:
    https://p3.express/manual/v2/<a-g>/<01-10>/
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

SOURCE_ID = "p3-express"
BASE = "https://p3.express"
MANUAL = "/manual/v2"
LICENSE = "CC-BY-4.0"
AUTHORS = "PTCoE — Nader K. Rad et al."
SOURCE_VERSION = "v2"

# (group_letter, group_index, group_title, [(activity_index, activity_title)])
GROUPS = [
    ("a", 1, "Project Initiation", [
        (1, "Appoint the sponsor"),
        (2, "Appoint the project manager"),
        (3, "Appoint key team members"),
        (4, "Describe the project"),
        (5, "Identify and plan deliverables"),
        (6, "Identify risks and plan responses"),
        (7, "Peer-review project initiation"),
        (8, "Make a go/no-go decision"),
        (9, "Kick off the project"),
        (10, "Conduct a focused communication"),
    ]),
    ("b", 2, "Monthly Initiation", [
        (1, "Have the team revise the plans"),
        (2, "Revise the project description"),
        (3, "Have Monthly Initiation peer-reviewed"),
        (4, "Make a go/no-go decision"),
        (5, "Conduct a focused communication"),
    ]),
    ("c", 3, "Weekly Management", [
        (1, "Measure performance"),
        (2, "Plan responses to deviations"),
        (3, "Identify and respond to new risks"),
        (4, "Conduct a focused communication"),
    ]),
    ("d", 4, "Daily Management", [
        (1, "Manage follow-up items"),
        (2, "Accept completed deliverables"),
    ]),
    ("e", 5, "Monthly Closure", [
        (1, "Evaluate stakeholder satisfaction"),
        (2, "Plan improvements"),
        (3, "Conduct a focused communication"),
    ]),
    ("f", 6, "Project Closure", [
        (1, "Hand over the product"),
        (2, "Evaluate stakeholder satisfaction"),
        (3, "Have Project Closure peer-reviewed"),
        (4, "Archive project documents"),
        (5, "Re-assign the team"),
        (6, "Celebrate"),
    ]),
    ("g", 7, "Post-Project Management", [
        (1, "Evaluate the benefits"),
        (2, "Generate ideas for new projects"),
        (3, "Conduct a focused communication"),
    ]),
]

OUT = ROOT / "docs" / "sources" / SOURCE_ID
RAW = ROOT / "raw-sources" / "p3-express.md"


def fetch_landing() -> Chunk:
    url = BASE + MANUAL + "/"
    print(f"  fetching {url} ...")
    html = fetch_html(url)
    inner = extract_main(html, url, anchor_on_h1=True)
    body = html_to_markdown(inner)
    return Chunk(
        out_path=OUT / "index.md",
        title="P3.express manual (v2)",
        body=body,
        frontmatter={
            "title": "P3.express manual (v2)",
            "source_id": SOURCE_ID,
            "source_url": url,
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["p3-express", "front-matter", "source-landing", "methodology"],
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
            "source_url": f"{BASE}{MANUAL}/{letter}/",
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["p3-express", "activity-group", letter, slugify(title)],
        },
    )


def fetch_activity(letter: str, group_idx: int, group_title: str,
                   act_idx: int, act_title: str) -> Chunk:
    url = f"{BASE}{MANUAL}/{letter}/{act_idx:02d}/"
    print(f"  fetching {url} ...")
    html = fetch_html(url)
    inner = extract_main(html, url, anchor_on_h1=True)
    body = html_to_markdown(inner)
    code = f"{letter.upper()}{act_idx:02d}"
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
            "tags": ["p3-express", letter, slugify(group_title), code.lower()],
        },
    )


def main() -> None:
    print(f"Ingesting P3.express from {BASE}{MANUAL} ...")
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
