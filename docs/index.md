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

## Recipes — task-driven loading guides

Don't know which cards to load for a specific task? Use a [**recipe**](recipes/index.md). Each recipe says: *for this question, these are the cards, this is the prompt, this is what the answer should look like.* Eleven covering PR review, Sprint Review prep, build-vs-buy, method selection, post-mortems, org redesign, stakeholder mapping, strategic review, forecasting, onboarding, and AI-in-dev-workflow.

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
| [The Kanban Guide](sources/kanban-guide/index.md) | John Coleman, Daniel Vacanti et al. | CC BY-SA 4.0 | included |
| [Open Guide to Kanban](sources/open-guide-to-kanban/index.md) | John Coleman, Magdalena Firlit et al. | CC BY-SA 4.0 | included |
| [Wardley Maps](sources/wardley-maps/index.md) | Simon Wardley | CC BY-SA 4.0 | included |

See [About the distilled tier](distilled/about.md) for the editorial
policy, what was changed, and license attribution rules.

## Related sources & methods

A curated list of sources and methods that come up in the PM /
tech-lead context. Not all of them will ever be ingested — some live
here as pointers, useful when the situation calls for them. License
is metadata; it only blocks ingestion when it actually conflicts
(NoDerivatives, or NonCommercial if this repo is ever used
commercially).

### Candidates considered

| Source | When it helps | License | Status |
|---|---|---|---|
| **[Army Design Methodology](https://armypubs.army.mil/)** (ATP 5-0.1, US Army) | Framing ill-structured problems where stakeholders disagree on what the problem even is; multi-week strategy sessions with a dedicated team. | Public domain (US gov work) | **Not planned** — niche audience fit; the framing terrain is partly covered by Wardley Maps; military-doctrine prose needs heavy translation for a tech-lead context. Revisit if a "strategic framing" recipe gains demand. |
| **[Open PM² Guide](https://www.open-pm2.org/)** (European Commission) | Full EU-style PM framework for regulated / public-sector projects; phase gates, governance artifacts. | CC BY-NC-SA 4.0 | **Not planned** — NonCommercial clause blocks any commercial reuse of this repo or derivatives; narrow audience for this catalog. |
| **[GitLab Handbook](https://handbook.gitlab.com/)** (selected chapters: Engineering, People Operations, Communication) | Engineering culture, async-first / handbook-first communication, remote operating model. | CC BY-SA 4.0 | **Candidate** — broad fit, but ~200+ pages; only worth ingesting selected chapters as an "engineering culture" tier. |
| **State of DevOps Report** (Google Cloud / DORA team) | Reference benchmarks for DORA metrics (deploy frequency, lead time, MTTR, change-fail rate) by industry and performance tier. | typically CC BY 4.0, varies by year | **Candidate as reference data** — mostly charts and benchmarks; low prose value, high reference-numbers value. |
| **Google SRE Book / SRE Workbook** | SRE practices: error budgets, SLO/SLI design, toil reduction, on-call. | CC BY-NC-ND 4.0 | **Pointer only** — NoDerivatives forbids the distillation tier; mirroring full text without cards adds limited value. |
| **Liberating Structures** | Facilitation patterns (1-2-4-All, Troika Consulting, etc.) for groups making decisions under uncertainty. | CC BY-NC-SA 4.0 | **Not planned** — NonCommercial clause; relatively narrow within the core tech-lead workflow. |

### Other methods worth knowing

A non-exhaustive pointer list of methods that come up in our recipes
or cards as external references. Listed so a reader knows where to
look; not catalogued here in any depth.

- **Cynefin framework** (Dave Snowden) — sense-making for the type of
  problem at hand (Clear / Complicated / Complex / Chaotic) before
  picking a method. Proprietary.
- **Continuous Discovery Habits** (Teresa Torres) — hypothesis-driven
  product discovery, opportunity solution trees, weekly user
  touchpoints. Proprietary.
- **Team Topologies** (Skelton & Pais) — four team types and three
  interaction modes, framed around cognitive load. Proprietary.
- **Accelerate** (Forsgren, Humble, Kim) — research foundation
  underneath the DORA metrics. Proprietary.

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

- **CC BY 4.0** material (Underneath the Surface, NUPP, P3.express,
  micro.P3.express) — usable in any derivative as long as attribution
  is preserved.
- **CC BY-SA 4.0** material (Scrum Guide, Scrum Guide Expansion Pack,
  DORA Metrics in Jira, The Kanban Guide, Open Guide to Kanban,
  Wardley Maps) — derivatives must retain CC BY-SA.

Cross-source synthesis cards in `distilled/synthesis/` are CC BY-SA
because they incorporate material from ShareAlike sources.
