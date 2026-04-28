"""Ingest the canonical NUPP (Nearly Universal Principles of Projects) text.

Source:  https://nupp.guide/  (CC BY 4.0 — © PTCoE / Nader K. Rad et al.)
Output:  raw-sources/nupp.md + docs/sources/nupp/

Each principle has a stable URL (/nup1/ ... /nup6/) — no TOC parsing needed.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from lib.web_to_md import (
    Chunk,
    extract_main,
    fetch_html,
    html_to_markdown,
    render_frontmatter,
    reset_dir,
    write_chunk,
    write_concat,
)

SOURCE_ID = "nupp"
BASE = "https://nupp.guide"
LICENSE = "CC-BY-4.0"
AUTHORS = "PTCoE — Nader K. Rad et al."
SOURCE_VERSION = "2024"  # NUPP is stable; the site doesn't carry a version

PRINCIPLES = [
    (1, "Prefer results and the truth to affiliations", "/nup1/"),
    (2, "Preserve and optimize energy and resources", "/nup2/"),
    (3, "Always be proactive", "/nup3/"),
    (4, "A chain is only as strong as its weakest link", "/nup4/"),
    (5, "Don't do anything without a clear purpose", "/nup5/"),
    (6, "Use repeatable elements", "/nup6/"),
]

OUT = ROOT / "docs" / "sources" / SOURCE_ID
RAW = ROOT / "raw-sources" / "nupp.md"


def fetch_chunk(idx: int, title: str, path: str) -> Chunk:
    url = BASE + path
    print(f"  fetching {url} ...")
    html = fetch_html(url)
    inner = extract_main(html, url)
    body = html_to_markdown(inner)
    out_path = OUT / f"{idx:02d}-nup{idx}-{slugified(title)}.md"
    return Chunk(
        out_path=out_path,
        title=f"NUP{idx} — {title}",
        body=body,
        frontmatter={
            "title": f"NUP{idx} — {title}",
            "source_id": SOURCE_ID,
            "section": title,
            "section_index": idx,
            "source_url": url,
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["nupp", "principle", f"nup{idx}", slugified(title)],
        },
    )


def slugified(s: str) -> str:
    from lib.web_to_md import slugify
    return slugify(s)


def fetch_landing() -> Chunk:
    url = BASE + "/"
    print(f"  fetching {url} ...")
    html = fetch_html(url)
    inner = extract_main(html, url)
    body = html_to_markdown(inner)
    return Chunk(
        out_path=OUT / "index.md",
        title="NUPP — Nearly Universal Principles of Projects",
        body=body,
        frontmatter={
            "title": "NUPP — Nearly Universal Principles of Projects",
            "source_id": SOURCE_ID,
            "source_url": BASE + "/",
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["nupp", "front-matter", "source-landing"],
        },
    )


def main() -> None:
    print(f"Ingesting NUPP from {BASE} ...")
    reset_dir(OUT)
    chunks = [fetch_landing()]
    for idx, title, path in PRINCIPLES:
        chunks.append(fetch_chunk(idx, title, path))

    for c in chunks:
        write_chunk(c)
    write_concat(RAW, chunks)

    print(f"Wrote {len(chunks)} files under {OUT.relative_to(ROOT)}")
    print(f"Wrote raw concatenation to {RAW.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
