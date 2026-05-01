"""Ingest Simon Wardley's "Wardley Maps" book.

Source:  https://medium.com/wardleymaps  (CC BY-SA 4.0, original)
Mirror:  https://github.com/jsell-rh/wardley-maps-book-md  (markdown copy,
         CC BY-SA 4.0, unofficial; used here for clean ingest)

Output:  raw-sources/wardley-maps.md + docs/sources/wardley-maps/

Unlike the HTML-scraping ingest scripts (kanban, p3.express, etc.), the
upstream is already markdown — one file per chapter. We fetch each chapter
verbatim, rewrite relative image links to the upstream raw URL (we do not
host a copy of the 250+ figures), and wrap with our standard frontmatter.

Note: the book is unfinished. The mirror reflects the state of Simon's
public Medium series at the time of conversion. We document this in the
landing index and in docs/sources.md.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from lib.web_to_md import (  # noqa: E402
    Chunk,
    reset_dir,
    slugify,
    write_chunk,
    write_concat,
)

SOURCE_ID = "wardley-maps"
ORIGINAL_URL = "https://medium.com/wardleymaps"
MIRROR_REPO = "jsell-rh/wardley-maps-book-md"
MIRROR_BRANCH = "main"
MIRROR_CONTENT_BASE = (
    f"https://raw.githubusercontent.com/{MIRROR_REPO}/{MIRROR_BRANCH}/book/content"
)
MIRROR_REPO_URL = f"https://github.com/{MIRROR_REPO}"
LICENSE = "CC-BY-SA-4.0"
AUTHORS = "Simon Wardley"
SOURCE_VERSION = "Medium series, mirrored 2024"
COPYRIGHT = "© Simon Wardley"

USER_AGENT = (
    "Mozilla/5.0 (compatible; tech-lead-notes-ingest/1.0; "
    "+https://github.com/OpenMindUA/tech-lead-notes)"
)

# Hardcoded chapter list — stable filenames in the upstream mirror.
CHAPTER_FILES = [
    "chapter-01-on-being-lost.md",
    "chapter-02-finding-a-path.md",
    "chapter-03-exploring-the-map.md",
    "chapter-04-doctrine.md",
    "chapter-05-the-play-and-a-decision-to-act.md",
    "chapter-06-getting-started.md",
    "chapter-07-finding-a-new-purpose.md",
    "chapter-08-keeping-the-wolves-at-bay.md",
    "chapter-09-charting-the-future.md",
    "chapter-10-i-wasnt-expecting-that.md",
    "chapter-11-a-smorgasbord-of-the-slightly-useful.md",
    "chapter-12-the-scenario.md",
    "chapter-13-something-wicked-this-way-comes.md",
    "chapter-14-to-thine-own-self-be-true.md",
    "chapter-15-on-the-practice-of-scenario-planning.md",
    "chapter-16-super-looper.md",
    "chapter-17-to-infinity-and-beyond.md",
    "chapter-18-better-for-less.md",
    "chapter-19-on-playing-chess.md",
]
LICENSE_FILE = "LICENSE"  # at /book/LICENSE in upstream

OUT = ROOT / "docs" / "sources" / SOURCE_ID
RAW = ROOT / "raw-sources" / "wardley-maps.md"


def fetch_text(url: str, timeout: float = 30.0) -> str:
    headers = {"User-Agent": USER_AGENT, "Accept": "text/plain,*/*;q=0.5"}
    r = httpx.get(url, timeout=timeout, follow_redirects=True, headers=headers)
    r.raise_for_status()
    return r.text


_IMG_RE = re.compile(r"(!\[[^\]]*\])\(\./images/([^)]+)\)")
# Inter-chapter links in the upstream point at `chapter-NN-slug.md` filenames.
# We rename to `NN-slug.md` (without the `chapter-` prefix) — rewrite refs.
_CHAPTER_LINK_RE = re.compile(r"\]\((?:\./)?chapter-(\d+)-([a-z0-9-]+)\.md\)")


def rewrite_images(md: str) -> str:
    """Rewrite `./images/foo.jpg` to the upstream raw URL.

    We deliberately do NOT host a copy of the figures (200+ JPGs); they live
    in the upstream mirror. Atrributing back is the right thing for a CC-BY-SA
    derivative anyway.
    """
    return _IMG_RE.sub(
        lambda m: f"{m.group(1)}({MIRROR_CONTENT_BASE}/images/{m.group(2)})",
        md,
    )


def rewrite_chapter_links(md: str) -> str:
    """`chapter-02-finding-a-path.md` → `02-finding-a-path.md`."""
    return _CHAPTER_LINK_RE.sub(lambda m: f"]({m.group(1)}-{m.group(2)}.md)", md)


def extract_title(md: str, fallback: str) -> str:
    """First `# Heading` line, else fallback."""
    for line in md.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return fallback


def chapter_index(filename: str) -> int:
    m = re.match(r"chapter-(\d+)-", filename)
    if not m:
        raise ValueError(f"unexpected filename: {filename}")
    return int(m.group(1))


def main() -> None:
    print(f"Ingesting Wardley Maps from {MIRROR_REPO_URL} ...")
    reset_dir(OUT)

    chunks: list[Chunk] = []

    # Fetch chapters
    fetched: list[tuple[int, str, str, str]] = []  # (idx, slug-from-fname, title, body)
    for fname in CHAPTER_FILES:
        url = f"{MIRROR_CONTENT_BASE}/{fname}"
        idx = chapter_index(fname)
        print(f"  fetching ch.{idx:02d} {fname}")
        body = rewrite_chapter_links(rewrite_images(fetch_text(url)))
        title = extract_title(body, fallback=fname.removesuffix(".md"))
        # Strip any leading H1 from body so the frontmatter title is canonical;
        # we keep the H1 in the body too for readability matching other sources.
        slug_from_title = slugify(title)
        fetched.append((idx, slug_from_title, title, body))

    # Landing index
    landing_lines = [
        f"# Wardley Maps",
        "",
        f"Simon Wardley's book on **strategic mapping**, published on Medium "
        f"under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) "
        f"and mirrored to markdown by the [{MIRROR_REPO}]({MIRROR_REPO_URL}) "
        f"project. {COPYRIGHT}.",
        "",
        f"**Original source:** <{ORIGINAL_URL}>  ",
        f"**Markdown mirror used for this ingest:** <{MIRROR_REPO_URL}>",
        "",
        "> The book is **unfinished** — Simon stopped publishing on Medium before "
        "completing all planned chapters. What follows is the 19-chapter state of "
        "the public series at the time of conversion. Figures (200+) are hosted "
        f"in the upstream mirror; image links here point to "
        f"`raw.githubusercontent.com/{MIRROR_REPO}/...`.",
        "",
        "## Chapters",
        "",
    ]
    for idx, slug, title, _ in fetched:
        landing_lines.append(f"- [Chapter {idx} — {title}]({idx:02d}-{slug}.md)")
    landing_lines += [
        "",
        f"- [License](20-license.md)",
        "",
    ]
    landing_body = "\n".join(landing_lines)

    chunks.append(Chunk(
        out_path=OUT / "index.md",
        title="Wardley Maps",
        body=landing_body,
        frontmatter={
            "title": "Wardley Maps",
            "source_id": SOURCE_ID,
            "source_url": ORIGINAL_URL,
            "mirror_url": MIRROR_REPO_URL,
            "source_version": SOURCE_VERSION,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["wardley-maps", "strategy", "source-landing", "framework"],
        },
    ))

    for idx, slug, title, body in fetched:
        chunks.append(Chunk(
            out_path=OUT / f"{idx:02d}-{slug}.md",
            title=title,
            body=body,
            frontmatter={
                "title": title,
                "source_id": SOURCE_ID,
                "chapter": title,
                "chapter_index": idx,
                "source_url": ORIGINAL_URL,
                "mirror_url": f"{MIRROR_CONTENT_BASE}/{CHAPTER_FILES[idx-1]}",
                "source_version": SOURCE_VERSION,
                "license": LICENSE,
                "authors": AUTHORS,
                "tags": ["wardley-maps", "strategy", slug],
            },
        ))

    # License chunk (numbered 20 to keep it last regardless of chapter count)
    license_url = (
        f"https://raw.githubusercontent.com/{MIRROR_REPO}/{MIRROR_BRANCH}/book/LICENSE"
    )
    print(f"  fetching LICENSE")
    license_text = fetch_text(license_url)
    license_body = (
        "# License\n\n"
        f"Original: <{ORIGINAL_URL}> · Mirror: <{MIRROR_REPO_URL}>\n\n"
        "```\n" + license_text.strip() + "\n```\n"
    )
    chunks.append(Chunk(
        out_path=OUT / "20-license.md",
        title="License",
        body=license_body,
        frontmatter={
            "title": "License",
            "source_id": SOURCE_ID,
            "source_url": ORIGINAL_URL,
            "mirror_url": MIRROR_REPO_URL,
            "license": LICENSE,
            "authors": AUTHORS,
            "tags": ["wardley-maps", "license"],
        },
    ))

    for c in chunks:
        write_chunk(c)
    write_concat(RAW, chunks)

    print(f"Wrote {len(chunks)} files under {OUT.relative_to(ROOT)}")
    print(f"Wrote raw concatenation to {RAW.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
