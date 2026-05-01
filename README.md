# Tech Lead Notes

Operational playbook for tech leads — a multi-source, three-tier
mirror of CC-licensed project-management, Scrum, and engineering-
effectiveness resources, split into navigable chunks with YAML
frontmatter for humans, search engines, LLM agents, and tools like
[Context7](https://context7.com).

- **Sources:** 10 (Underneath the Surface, Scrum Guide 2020, Scrum
  Guide Expansion Pack v2026.1, DORA Metrics in Jira, NUPP,
  P3.express, micro.P3.express, The Kanban Guide, Open Guide to
  Kanban, Wardley Maps)
- **License:** mixed CC BY 4.0 + CC BY-SA 4.0 — see [LICENSE](./LICENSE)
  and [`docs/sources.md`](./docs/sources.md)
- **Repository name:** *(placeholder — set the final name in
  `mkdocs.yml`, `LICENSE`, `README.md` once decided)*

## Three tiers

| Tier | Content | When to use |
|---|---|---|
| **1 — [Agent index](./docs/agent-index.md)** | One-line catalog of every concept | Stuff into an LLM system prompt |
| **2 — [Distilled cards](./docs/distilled/index.md)** | Dense per-concept cards (TL;DR / core ideas / when applies / anti-patterns / cross-refs) | RAG retrieval; fast topical lookup |
| **3 — [Full source text](./docs/sources/)** | Original documents, split per chapter/section | Verbatim citation; full nuance |

Plus **[recipes](./docs/recipes/index.md)** — task-driven loading
guides for 11 common tech-lead tasks (PR review with DORA, Sprint
Review prep, build-vs-buy, method selection, post-mortems, org
redesign, stakeholder mapping, strategic review, forecasting,
onboarding, AI-in-dev-workflow). Each recipe says which Tier-2
cards to load + the prompt skeleton + expected output shape.

For LLM tooling: [`llms.txt`](./llms.txt) is a structured catalog
([llmstxt.org](https://llmstxt.org)); [`llms-full.txt`](./llms-full.txt)
is the entire corpus concatenated.

## Sources

| Source | Authors | License | Tier-3 size | Tier-2 cards |
|---|---|---|---|---|
| [Underneath the Surface](./docs/sources/underneath-the-surface/index.md) | Nader K. Rad | CC BY 4.0 | 51 | 47 |
| [The 2020 Scrum Guide](./docs/sources/scrum-guide/index.md) | Schwaber, Sutherland | CC BY-SA 4.0 | 23 | 17 |
| [Scrum Guide Expansion Pack v2026.1](./docs/sources/scrum-guide-expanded/index.md) | Jocham, Coleman, Sutherland | CC BY-SA 4.0 | 57 | 16 |
| [DORA Metrics in Jira](./docs/sources/dora-metrics-jira/index.md) | openmind (self-authored) | CC BY-SA 4.0 | 6 | 6 |
| [NUPP](./docs/sources/nupp/index.md) | PTCoE — Nader K. Rad et al. | CC BY 4.0 | 7 | 7 |
| [P3.express manual (v2)](./docs/sources/p3-express/index.md) | PTCoE — Nader K. Rad et al. | CC BY 4.0 | 41 | 6 |
| [micro.P3.express manual](./docs/sources/micro-p3-express/index.md) | PTCoE — Nader K. Rad et al. | CC BY 4.0 | 34 | 3 |
| [The Kanban Guide](./docs/sources/kanban-guide/index.md) | Coleman, Vacanti et al. | CC BY-SA 4.0 | 11 | 4 |
| [Open Guide to Kanban](./docs/sources/open-guide-to-kanban/index.md) | Coleman, Firlit et al. | CC BY-SA 4.0 | 12 | 2 |
| [Wardley Maps](./docs/sources/wardley-maps/index.md) | Simon Wardley | CC BY-SA 4.0 | 21 | 7 |

Cross-source [synthesis cards](./docs/distilled/synthesis/index.md)
combine material from multiple sources (CC BY-SA, 7 cards).

## Repository layout

```
docs/
  index.md                       framework landing
  agent-index.md                 Tier 1
  sources.md                     manifest of all sources + license map
  llms.txt, llms-full.txt        LLM-facing index + full corpus
  distilled/                     Tier 2
    index.md, about.md
    glossary.md
    cross-references.md
    principles/{pmbok-7,nupp,prince2}/
    performance-domains/
    methodologies/
    scrum-guide/
    scrum-guide-expanded/
    dora-metrics-jira/
    p3-express/
    micro-p3-express/
    kanban-guide/
    open-guide-to-kanban/
    wardley-maps/
    synthesis/                   cross-source cards (CC BY-SA)
  sources/                       Tier 3
    underneath-the-surface/
    scrum-guide/
    scrum-guide-expanded/
    dora-metrics-jira/
    nupp/
    p3-express/
    micro-p3-express/
    kanban-guide/
    open-guide-to-kanban/
    wardley-maps/

raw-sources/                     pristine markdown snapshots
  pmbok-guide--underneath-the-surface.md  (also at repo root for compat)
  scrum-guide.md
  scrum-guide-expanded.md
  dora-metrics-jira.md
  nupp.md
  p3-express.md
  micro-p3-express.md
  kanban-guide.md
  open-guide-to-kanban.md
  wardley-maps.md

scripts/
  split_book.py                   UtS → docs/sources/underneath-the-surface
  ingest_scrum_guide.py           Scrum Guide HTML → MD → chunks
  ingest_scrum_guide_expanded.py  SGE HTML → MD → chunks
  split_dora_metrics.py           DORA doc → chunks
  ingest_nupp.py                  NUPP → chunks
  ingest_p3_express.py            P3.express HTML → MD → chunks
  ingest_micro_p3_express.py      micro.P3.express HTML → MD → chunks
  ingest_kanban_guide.py          The Kanban Guide HTML → MD → chunks
  ingest_open_kanban_guide.py     Open Guide to Kanban HTML → MD → chunks
  ingest_wardley_maps.py          Wardley Maps GitHub MD mirror → chunks
  build_llms_txt.py               regenerates llms.txt and llms-full.txt
  lib/web_to_md.py                shared HTML→MD helpers (used by ingest_*)

mkdocs.yml                        MkDocs Material configuration
pyproject.toml                    uv project (docs + ingest dependency groups)
.github/workflows/gh-pages.yml    build & deploy
```

## Local development

```bash
# install everything
uv sync --group docs --group ingest

# regenerate any source's chunks
uv run python scripts/split_book.py
uv run python scripts/ingest_scrum_guide.py
uv run python scripts/ingest_scrum_guide_expanded.py
uv run python scripts/split_dora_metrics.py
uv run python scripts/ingest_nupp.py
uv run python scripts/ingest_p3_express.py
uv run python scripts/ingest_micro_p3_express.py
uv run python scripts/ingest_kanban_guide.py
uv run python scripts/ingest_open_kanban_guide.py
uv run python scripts/ingest_wardley_maps.py

# regenerate llms.txt / llms-full.txt — required before mkdocs serve/build
# because docs/llms.txt and docs/llms-full.txt are gitignored build artifacts
LLMS_RAW_BASE=https://raw.githubusercontent.com/OpenMindUA/tech-lead-notes/main/docs \
LLMS_SITE_BASE=https://openmindua.github.io/tech-lead-notes \
  uv run python scripts/build_llms_txt.py

# preview the site
uv run mkdocs serve         # http://127.0.0.1:8000

# build & strict-check
uv run mkdocs build --strict
```

## Using with LLMs / Context7

Recommended consumption pattern:

1. Load [`docs/agent-index.md`](./docs/agent-index.md) into the
   system prompt for compact awareness of all topics.
2. For a specific question, fetch the matching Tier-2 card by URL
   (e.g. `docs/distilled/scrum-guide/14-product-backlog.md`).
3. For verbatim citation, follow the **Source** link inside the
   card to the Tier-3 chunk.
4. For full-corpus loading, fetch [`llms-full.txt`](./llms-full.txt).

Every chunk has a stable raw `.md` URL on
`raw.githubusercontent.com/<user>/<repo>/main/...` once published.

## Frontmatter schema

Each chunk and card carries YAML frontmatter, e.g.:

```yaml
---
title: Sprint Planning
type: event
framework: Scrum
source: docs/sources/scrum-guide/06-scrum-events/02-sprint-planning.md
source_url: https://scrumguides.org/scrum-guide.html
license: CC-BY-SA-4.0
authors_of_source: Ken Schwaber, Jeff Sutherland
tags: [scrum, scrum-guide-2020, sprint-planning, sprint-goal, sprint-backlog]
---
```

The `license:` field is **authoritative per file**. See
[`docs/sources.md`](./docs/sources.md) for the canonical license
map.

## Editorial policy

The Tier-2 distilled tier is a **derivative work**: paraphrased,
restructured, stripped of anecdotes. See
[`docs/distilled/about.md`](./docs/distilled/about.md) for full
disclosure of what was changed and what was preserved. The Tier-3
full text is preserved verbatim.

## License summary

This repository combines two CC licenses. The full mapping is in
[`LICENSE`](./LICENSE) and [`docs/sources.md`](./docs/sources.md).

- **CC BY 4.0** — Underneath the Surface and its derivatives
- **CC BY-SA 4.0** — Scrum Guide, Scrum Guide Expanded, DORA doc,
  and any cross-source synthesis (ShareAlike inherits)
- **MIT** — Python scripts and MkDocs configuration

## Trademarks

PMI, PMBOK, PRINCE2, DSDM, Scrum, Atlassian, Jira, GitHub are marks
of their respective owners. This repository is **not affiliated
with or endorsed by** any of them.
