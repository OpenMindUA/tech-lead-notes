"""Ingest The Kanban Guide (canonical, minimal version).

Source:  https://kanbanguides.org/the-kanban-guide/  (CC BY-SA 4.0)
Output:  raw-sources/kanban-guide.md + docs/sources/kanban-guide/

Single-page document split by <h2> headings. The page wraps content in
<div class="content-body"> with the title/contributor block in a sibling
<header>; we scope to the body and split there.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from lib.web_to_md import (  # noqa: E402
    Chunk,
    fetch_html,
    html_to_markdown,
    reset_dir,
    slugify,
    split_by_h2,
    write_chunk,
    write_concat,
)

SOURCE_ID = "kanban-guide"
URL = "https://kanbanguides.org/the-kanban-guide/"
LICENSE = "CC-BY-SA-4.0"
AUTHORS = (
    "John Coleman, Daniel Vacanti, Colleen Johnson, Prateek Singh, "
    "Julia Wester, Christian Neverdal, Magdalena Firlit, Tom Gilb, "
    "Steve Tendon"
)
SOURCE_VERSION = "v2025.5 (May 2025)"
COPYRIGHT = "© 2019-2025 Orderly Disruption Limited, Daniel S. Vacanti, Inc."

OUT = ROOT / "docs" / "sources" / SOURCE_ID
RAW = ROOT / "raw-sources" / "kanban-guide.md"


def main() -> None:
    print(f"Ingesting Kanban Guide from {URL} ...")
    reset_dir(OUT)
    html = fetch_html(URL)
    _, sections = split_by_h2(
        html,
        URL,
        container_selector="div.content-body",
        drop_selectors=["div.alert", "a.position-absolute"],
        drop_link_text=["top"],
    )

    landing_body = (
        f"# The Kanban Guide ({SOURCE_VERSION})\n\n"
        f"Canonical, minimal Kanban reference. {COPYRIGHT}. "
        f"Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).\n\n"
        f"Authors: {AUTHORS}.\n\n"
        f"## Sections\n\n"
        + "\n".join(
            f"- [{title}]({i:02d}-{slugify(title)}.md)"
            for i, (title, _) in enumerate(sections, start=1)
        )
        + f"\n\nSource page: <{URL}>.\n"
    )

    chunks: list[Chunk] = []
    chunks.append(Chunk(
        out_path=OUT / "index.md",
        title="The Kanban Guide",
        body=landing_body,
        frontmatter={
            "title": f"The Kanban Guide ({SOURCE_VERSION})",
            "source_id": SOURCE_ID,
            "source_url": URL,
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["kanban", "kanban-guide", "source-landing", "framework"],
        },
    ))

    for i, (title, html_section) in enumerate(sections, start=1):
        body = html_to_markdown(html_section)
        chunks.append(Chunk(
            out_path=OUT / f"{i:02d}-{slugify(title)}.md",
            title=title,
            body=body,
            frontmatter={
                "title": title,
                "source_id": SOURCE_ID,
                "chapter": title,
                "chapter_index": i,
                "source_url": URL,
                "source_version": SOURCE_VERSION,
                "license": LICENSE,
                "authors": AUTHORS,
                "tags": ["kanban", "kanban-guide", slugify(title)],
            },
        ))

    for c in chunks:
        write_chunk(c)
    write_concat(RAW, chunks)

    print(f"Wrote {len(chunks)} files under {OUT.relative_to(ROOT)}")
    print(f"Wrote raw concatenation to {RAW.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
