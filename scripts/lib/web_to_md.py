"""Shared helpers for HTML→Markdown ingestion of CC-licensed PM resources.

Used by ingest_nupp.py, ingest_p3_express.py, ingest_micro_p3_express.py
(and potentially others). Each ingest script supplies a list of URLs and
metadata; this module handles fetching, conversion, frontmatter rendering,
and writing chunks.
"""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md

USER_AGENT = (
    "Mozilla/5.0 (compatible; tech-lead-notes-ingest/1.0; +https://github.com/OpenMindUA/tech-lead-notes)"
)


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def fetch_html(url: str, timeout: float = 30.0) -> str:
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,*/*;q=0.5"}
    r = httpx.get(url, timeout=timeout, follow_redirects=True, headers=headers)
    r.raise_for_status()
    return r.text


def extract_main(html: str, url: str, *, anchor_on_h1: bool = False) -> str:
    """Pick the most likely main-content element and return its inner HTML
    with all relative URLs resolved to absolute against ``url``.

    When ``anchor_on_h1`` is True, the function locates the page's primary
    <h1> and keeps only its containing block + all following siblings inside
    the chosen wrapper. Use this for sites where the visible main element
    contains both nav and content as sibling divs (e.g. p3.express).
    """
    soup = BeautifulSoup(html, "html.parser")
    for selector in ("main", "article", ".content", "#content", "body"):
        node = soup.select_one(selector)
        if node is not None:
            break
    else:  # pragma: no cover
        node = soup
    if not isinstance(node, Tag):
        node = soup

    if anchor_on_h1:
        h1 = node.find("h1")
        if h1 is not None and isinstance(h1, Tag):
            h1_block = h1
            while h1_block.parent is not None and h1_block.parent is not node:
                h1_block = h1_block.parent
            collected = [h1_block]
            for sib in h1_block.find_next_siblings():
                collected.append(sib)
            wrapper = soup.new_tag("div")
            for el in collected:
                wrapper.append(el.extract())
            node = wrapper

    for a in node.find_all("a"):
        if isinstance(a, Tag) and a.get("href"):
            href = a["href"]
            if isinstance(href, str) and href.startswith(("/", "./", "../")):
                a["href"] = urljoin(url, href)
    return str(node)


def html_to_markdown(html: str) -> str:
    """Convert HTML to Markdown with conventions matching the rest of the
    repository (ATX headings, no escaped underscores, etc.)."""
    return md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "form", "input"],
        escape_underscores=False,
    ).strip()


@dataclass
class Chunk:
    out_path: Path
    title: str
    body: str
    frontmatter: dict


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


def render_frontmatter(fm: dict) -> str:
    lines = ["---"]
    for k, v in fm.items():
        if v is None or v == [] or v == "":
            continue
        lines.append(f"{k}: {yaml_value(v)}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def write_chunk(chunk: Chunk) -> Path:
    chunk.out_path.parent.mkdir(parents=True, exist_ok=True)
    body = chunk.body.rstrip() + "\n"
    chunk.out_path.write_text(
        render_frontmatter(chunk.frontmatter) + body, encoding="utf-8"
    )
    return chunk.out_path


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def write_concat(raw_path: Path, chunks: Iterable[Chunk]) -> None:
    """Write a single concatenated raw markdown snapshot to raw-sources/."""
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    parts = []
    for c in chunks:
        parts.append(f"\n\n<!-- chunk: {c.out_path.name} -->")
        parts.append(f"# {c.title}\n")
        parts.append(c.body.strip())
    raw_path.write_text("".join(parts).strip() + "\n", encoding="utf-8")
