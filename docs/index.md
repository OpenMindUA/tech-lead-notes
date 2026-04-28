---
title: Tech Lead Notes
type: framework-landing
license_summary: mixed (CC BY 4.0 + CC BY-SA 4.0) — see each source
tags: [framework, landing, multi-source, tech-lead]
---

# Tech Lead Notes

Operational playbook for tech leads — a multi-source, three-tier
mirror of CC-licensed project-management, Scrum, and engineering-
effectiveness resources, split into navigable chunks with YAML
frontmatter so humans, search engines and LLM agents
can use them.

## Three tiers

| Tier | Content | When to use |
|------|---------|-------------|
| **1 — [Agent index](agent-index.md)** | One-line catalog of every concept. | Stuff into a system prompt. |
| **2 — [Distilled cards](distilled/index.md)** | Dense per-concept cards (TL;DR / core ideas / when applies / anti-patterns / cross-refs). | Fast topical lookup; RAG retrieval. |
| **3 — Full source text** (`sources/`) | Original documents preserved verbatim, split per chapter/section. | Verbatim citation; full nuance. |

For LLM-tooling: [`llms.txt`](llms.txt) is a structured catalog
([llmstxt.org](https://llmstxt.org)) and [`llms-full.txt`](llms-full.txt)
is the entire corpus concatenated for full-context loading.

## Sources

| Source | Author(s) | License | Status |
|--------|-----------|---------|--------|
| [PMBOK Guide — Underneath the Surface](sources/underneath-the-surface/index.md) | Nader K. Rad | CC BY 4.0 | included |
| [The 2020 Scrum Guide](sources/scrum-guide/index.md) | Ken Schwaber, Jeff Sutherland | CC BY-SA 4.0 | included |
| [Scrum Guide Expansion Pack (v2026.1)](sources/scrum-guide-expanded/index.md) | Ralph Jocham, John Coleman, Jeff Sutherland | CC BY-SA 4.0 | included |
| [DORA Metrics in Jira](sources/dora-metrics-jira/index.md) | openmind (self-authored) | CC BY-SA 4.0 | included |
| [NUPP — Nearly Universal Principles of Projects](sources/nupp/index.md) | PTCoE — Nader K. Rad et al. | CC BY 4.0 | included |
| [P3.express manual (v2)](sources/p3-express/index.md) | PTCoE — Nader K. Rad et al. | CC BY 4.0 | included |
| [micro.P3.express manual](sources/micro-p3-express/index.md) | PTCoE — Nader K. Rad et al. | CC BY 4.0 | included |

See [About the distilled tier](distilled/about.md) for the editorial
policy, what was changed, and license attribution rules.

## Sources to consider adding

CC-licensed candidates that fit the tech-lead audience but are not yet
ingested. Listed in rough priority. PRs welcome — see [`docs/sources.md`](sources.md)
for the "how to add a new source" checklist.

### Tier A — high fit, clean licensing

| Source | Author(s) / Owner | License | Why it fits | Notes |
|---|---|---|---|---|
| **[Kanban Guide](https://kanbanguides.org/)** | Daniel Vacanti, Yuval Yeret et al. | CC BY-SA 4.0 | Flow-based work for teams that don't fit a Sprint cadence; pairs naturally with DORA cycle-time / lead-time metrics. | ~5-8 chunks; tiny but high-leverage. |

### Tier B — useful but with caveats

| Source | License | Caveat |
|---|---|---|
| **[Open PM² Guide](https://www.open-pm2.org/)** (European Commission) | CC **BY-NC-SA** 4.0 | NonCommercial clause — incompatible with any commercial use of this repo or derivatives. Suitable only if the repo stays purely educational. |
| **[GitLab Handbook](https://handbook.gitlab.com/)** (selected chapters: Engineering, People Operations, Communication) | CC BY-SA 4.0 | Massive (~200+ pages); only worth ingesting selected chapters as an "engineering culture" tier. |
| **State of DevOps Report** (Google Cloud / DORA team) | typically CC BY 4.0, varies by year | Mostly charts and benchmarks; relatively little prose framework. Useful as DORA reference data, not as a "playbook". |

### Tier C — DO NOT add (license incompatibility)

| Source | Why excluded |
|---|---|
| **Google SRE Book / SRE Workbook** | CC BY-**NC-ND** 4.0 — "NoDerivatives" forbids the distillation tier. Mirroring full text is allowed but adds limited value without distilled cards. |
| **Liberating Structures** | CC BY-**NC**-SA 4.0 — NonCommercial clause. |
| **The Phoenix Project / The Unicorn Project / Accelerate / The Manager's Path / Staff Engineer / An Elegant Puzzle / Continuous Delivery / Modern Software Engineering** | All proprietary, all rights reserved. |
| **Agile Practice Guide** (PMI) | Proprietary. |
| **DSDM Manual / APMBoK / PRINCE2 Manual** | Proprietary. We rely on the UtS commentary's coverage instead. |

### How to add one

See [`docs/sources.md`](sources.md) → "Adding a new source" — short
6-step checklist (verify license, write ingest script, generate Tier-3,
optional Tier-2 cards, update manifest + nav).

## How agents should consume this

1. Load [`agent-index.md`](agent-index.md) in the system prompt
   for compact awareness of all topics.
2. For a specific question, fetch the relevant Tier-2 card by URL
   (e.g. `distilled/principles/pmbok-7/04-focus-on-value.md`).
3. For verbatim citation, follow the **Source** link inside the
   card to the Tier-3 chunk.
4. For full-corpus loading, fetch [`llms-full.txt`](llms-full.txt).

## Licensing

Each chunk and each card carries a `license:` field in its
frontmatter. The repository combines:

- **CC BY 4.0** material (Underneath the Surface) — usable in any
  derivative as long as attribution is preserved.
- **CC BY-SA 4.0** material (Scrum Guide and Scrum Guide Expanded
  when added) — derivatives must retain CC BY-SA.

Cross-source synthesis cards in `distilled/synthesis/` (when
present) are CC BY-SA because they incorporate material from
ShareAlike sources.
