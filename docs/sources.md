---
title: Sources manifest
type: manifest
tags: [manifest, sources, licensing, attribution]
---

# Sources manifest

This repository is a multi-source mirror with editorial distillation.
This page is the **single source of truth** for what is included,
who authored it, under what license, and how the repository's
licensing combines from all of them.

## Included sources

### 1. PMBOK Guide — Underneath the Surface

- **Author:** Nader K. Rad
- **Type:** Book / commentary on PMBOK 7th Edition
- **Original URL:** <https://pmbok.guide/>
- **Canonical markdown:** <https://pmbok.guide/pmbok-guide--underneath-the-surface.md>
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Snapshot date:** 2023-06-08
- **Local Tier 3 path:** [`docs/sources/underneath-the-surface/`](sources/underneath-the-surface/index.md)
- **Local Tier 2 distillation:** [`docs/distilled/principles/`](distilled/index.md), `performance-domains/`, `methodologies/`, `glossary.md`, `cross-references.md`
- **Files:** 51 chunks
- **Notes:** Independent commentary, not the official PMBOK Guide. Author is a core PMBOK 7 development-team member.

### 2. The 2020 Scrum Guide

- **Authors:** Ken Schwaber, Jeff Sutherland
- **Type:** Canonical framework definition
- **Original URL:** <https://scrumguides.org/scrum-guide.html>
- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Publication year:** 2020 (November)
- **Local Tier 3 path:** [`docs/sources/scrum-guide/`](sources/scrum-guide/index.md)
- **Local Tier 2 distillation:** [`docs/distilled/scrum-guide/`](distilled/scrum-guide/index.md)
- **Files:** 23 chunks · 17 distilled cards
- **Notes:** The framework is **immutable** per the End Note — "implementing only parts of Scrum is possible, the result is not Scrum". Distillation here adds anti-patterns and cross-refs, not corrections.

### 3. Scrum Guide Expansion Pack (v2026.1)

- **Authors:** Ralph Jocham, John Coleman, Jeff Sutherland
- **Type:** Adaptation of the 2020 Scrum Guide; explicit departures noted
- **Original URL:** <https://scrumexpansion.org/scrum-guide-expanded/>
- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Version:** v2026.1 (January 18, 2026)
- **Local Tier 3 path:** [`docs/sources/scrum-guide-expanded/`](sources/scrum-guide-expanded/index.md)
- **Local Tier 2 distillation:** [`docs/distilled/scrum-guide-expanded/`](distilled/scrum-guide-expanded/index.md)
- **Files:** 57 chunks · 16 distilled cards
- **Notes:** Modification notice (per the original): "This is an adaptation of the 2020 Scrum Guide. Changes have been made from the original."

### 4. DORA Metrics in Jira

- **Author:** openmind (self-authored as part of this repository)
- **Type:** Methodology document
- **Original URL:** *(self-authored, no upstream)*
- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (chosen for compatibility with Scrum sources)
- **Document version:** 1.1
- **Local Tier 3 path:** [`docs/sources/dora-metrics-jira/`](sources/dora-metrics-jira/index.md)
- **Local Tier 2 distillation:** [`docs/distilled/dora-metrics-jira/`](distilled/dora-metrics-jira/index.md)
- **Files:** 6 chunks · 6 distilled cards

### 5. NUPP — Nearly Universal Principles of Projects

- **Authors:** PTCoE — Nader K. Rad et al.
- **Type:** Open principle set (6 principles)
- **Original URL:** <https://nupp.guide/>
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Local Tier 3 path:** [`docs/sources/nupp/`](sources/nupp/index.md)
- **Local Tier 2 distillation:** [`docs/distilled/principles/nupp/`](distilled/principles/nupp/index.md) — synthesis cards originally derived from the *Underneath the Surface* commentary now cross-link to this canonical text.
- **Files:** 7 chunks · 7 existing distilled cards

### 6. P3.express manual (v2)

- **Authors:** PTCoE — Nader K. Rad et al.
- **Type:** Open minimalist project-management methodology
- **Original URL:** <https://p3.express/manual/v2/>
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Version:** v2
- **Local Tier 3 path:** [`docs/sources/p3-express/`](sources/p3-express/index.md)
- **Local Tier 2 distillation:** distilled cards pending; existing methodology card at [`distilled/methodologies/p3-express.md`](distilled/methodologies/p3-express.md) (UtS-derived) cross-links here.
- **Files:** 41 chunks (7 activity groups × 1-10 activities; 33 activities total)
- **Notes:** Closes the maximalist (PRINCE2) / framework (Scrum) / minimalist (P3.express) triad already cross-referenced throughout the *Underneath the Surface* distilled cards.

### 7. micro.P3.express manual

- **Authors:** PTCoE — Nader K. Rad et al.
- **Type:** Variant of P3.express designed for very small projects (1-4 people)
- **Original URL:** <https://micro.p3.express/>
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Local Tier 3 path:** [`docs/sources/micro-p3-express/`](sources/micro-p3-express/index.md)
- **Local Tier 2 distillation:** distilled cards pending.
- **Files:** 34 chunks (6 activity groups × 2-7 activities; 27 activities total)
- **Notes:** Replaces P3.express's monthly cycle with weekly only; introduces the **hats** concept (people swap hats between roles) for tiny teams.

### 8. The Kanban Guide

- **Authors:** John Coleman, Daniel Vacanti, Colleen Johnson, Prateek Singh, Julia Wester, Christian Neverdal, Magdalena Firlit, Tom Gilb, Steve Tendon
- **Type:** Canonical, minimal definition of Kanban as a flow-optimization strategy
- **Original URL:** <https://kanbanguides.org/the-kanban-guide/>
- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Version:** v2025.5 (May 1, 2025)
- **Local Tier 3 path:** [`docs/sources/kanban-guide/`](sources/kanban-guide/index.md)
- **Local Tier 2 distillation:** [`docs/distilled/kanban-guide/`](distilled/kanban-guide/index.md)
- **Files:** 11 chunks · 4 distilled cards
- **Notes:** Pairs with the Open Guide to Kanban the same way SG2020 pairs with the Scrum Guide Expansion Pack — same authors and DOM shape on `kanbanguides.org`. The four mandatory flow metrics (WIP, Throughput, Work Item Age, Cycle Time) are the floor; everything else is opt-in.

### 9. Open Guide to Kanban

- **Authors:** John Coleman, Magdalena Firlit, Nigel Thurlow, Jose Casal, Martin Hinshelwood, Andy Carmichael, Jim Benson, Michael Forni, Christian Neverdal, Nader Talai, Steve Tendon
- **Type:** Community-expanded adaptation of The Kanban Guide for hybrid / knowledge-work contexts
- **Original URL:** <https://kanbanguides.org/open-guide-to-kanban/>
- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Version:** v2025.7 (July 2, 2025)
- **Local Tier 3 path:** [`docs/sources/open-guide-to-kanban/`](sources/open-guide-to-kanban/index.md)
- **Local Tier 2 distillation:** [`docs/distilled/open-guide-to-kanban/`](distilled/open-guide-to-kanban/index.md)
- **Files:** 12 chunks · 2 distilled cards
- **Notes:** Adaptation notice from upstream: preserves *The Kanban Guide* verbatim (regular type) and adds material in italics — expanded metrics catalog (~13 measures), Outcomes/Impact/Value extension, knowledge-work framing, prioritization appendix.

### 10. Wardley Maps

- **Author:** Simon Wardley
- **Type:** Book on strategic mapping (situational awareness, value-chain × evolution, doctrine, gameplay)
- **Original URL:** <https://medium.com/wardleymaps>
- **Markdown mirror used for ingest:** <https://github.com/jsell-rh/wardley-maps-book-md>
- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Version:** Medium series, 19 chapters, mirrored 2024
- **Local Tier 3 path:** [`docs/sources/wardley-maps/`](sources/wardley-maps/index.md)
- **Local Tier 2 distillation:** [`docs/distilled/wardley-maps/`](distilled/wardley-maps/index.md)
- **Files:** 19 chapter chunks + license · 7 distilled cards
- **Notes:** The book is **unfinished** — Simon stopped publishing on Medium before completing all planned chapters. Figures (200+) are not copied locally; image links point to the upstream raw mirror at `raw.githubusercontent.com/jsell-rh/wardley-maps-book-md/...`. The mirror is unofficial but its CC-BY-SA 4.0 license and explicit attribution to Simon match what we need. Wardley Maps occupies the **strategy layer** above the delivery / lifecycle / metrics frameworks already in the repo (Scrum / Kanban / P3.express / DORA).

## License combinations

The repository combines content under two Creative Commons licenses:

| License | Sources | Tier 2 cards derived from these only |
|---------|---------|---------------------------------------|
| **CC BY 4.0** | Underneath the Surface, NUPP, P3.express, micro.P3.express | `distilled/principles/` (PMBOK 7, NUPP, PRINCE2), `distilled/performance-domains/`, `distilled/methodologies/`, `distilled/glossary.md`, `distilled/cross-references.md`, `distilled/p3-express/`, `distilled/micro-p3-express/` |
| **CC BY-SA 4.0** | Scrum Guide, Scrum Guide Expansion Pack, DORA Metrics in Jira, The Kanban Guide, Open Guide to Kanban, Wardley Maps | `distilled/scrum-guide/`, `distilled/scrum-guide-expanded/`, `distilled/dora-metrics-jira/`, `distilled/kanban-guide/`, `distilled/open-guide-to-kanban/`, `distilled/wardley-maps/`, `distilled/synthesis/` (cross-source) |

### How CC BY-SA 4.0 affects mixed content

- CC BY-SA's **ShareAlike** clause requires derivatives that
  incorporate CC BY-SA material to remain CC BY-SA.
- Therefore the [synthesis tier](distilled/synthesis/index.md), which
  combines CC-BY (UtS / NUPP / P3.express / micro.P3.express) +
  CC-BY-SA (Scrum / SGE / DORA / Kanban Guide / Open Guide to Kanban)
  material, is **CC BY-SA 4.0**.
- The full-corpus dump [`llms-full.txt`](llms-full.txt) is also
  effectively **CC BY-SA 4.0** because it concatenates ShareAlike
  sources.

### Per-chunk licensing

Every chunk and every distilled card carries a `license:` field in
its frontmatter. **Treat that field as authoritative**, not this
manifest. The manifest summarizes; the frontmatter governs.

## Attribution boilerplate

When citing material from this repository, attribute the **upstream
author** of the source plus a pointer to this repository.

Examples:

- *"Distilled from Nader K. Rad's PMBOK Guide: Underneath the
  Surface (CC BY 4.0). See <https://pmbok.guide/>."*
- *"Distilled from the 2020 Scrum Guide by Ken Schwaber and Jeff
  Sutherland (CC BY-SA 4.0). See <https://scrumguides.org/scrum-guide.html>."*
- *"Distilled from the Scrum Guide Expansion Pack v2026.1 by Ralph
  Jocham, John Coleman and Jeff Sutherland (CC BY-SA 4.0). See
  <https://scrumexpansion.org/scrum-guide-expanded/>."*
- *"From the DORA Metrics in Jira methodology by openmind
  (CC BY-SA 4.0)."*
- *"Distilled from The Kanban Guide by John Coleman, Daniel Vacanti
  et al. (CC BY-SA 4.0). See <https://kanbanguides.org/the-kanban-guide/>."*
- *"Distilled from the Open Guide to Kanban by John Coleman,
  Magdalena Firlit et al. (CC BY-SA 4.0). See
  <https://kanbanguides.org/open-guide-to-kanban/>."*
- *"Distilled from Wardley Maps by Simon Wardley (CC BY-SA 4.0).
  Originally published at <https://medium.com/wardleymaps>;
  markdown mirror at <https://github.com/jsell-rh/wardley-maps-book-md>."*

## What's not affiliated

This repository is **not affiliated with or endorsed by**:
- Nader K. Rad
- Project Management Institute (PMI)
- Scrum.org / Scrum Alliance
- AXELOS / PRINCE2 Foundation
- Agile Business Consortium (DSDM)
- European Commission (PM²)
- Atlassian, Google Cloud (DORA), Orderly Disruption Limited,
  Daniel S. Vacanti Inc., or any other organization whose product is
  referenced

PMI and PMBOK are registered marks of the Project Management
Institute, Inc. PRINCE2® and PRINCE2 Agile® are registered marks of
AXELOS Limited. DSDM® is a registered mark of the Agile Business
Consortium Limited.

## Adding a new source

To add a new CC-licensed source to this repository:

1. Verify the upstream license (CC BY or CC BY-SA preferred for
   compatibility).
2. Add a copy or fetch script under `raw-sources/` and
   `scripts/ingest_<id>.py`.
3. Generate Tier 3 chunks under `docs/sources/<source-id>/`.
4. (Optional) Write Tier 2 distilled cards under
   `docs/distilled/<source-id>/` with each card carrying the
   correct `license:` and `authors_of_source:` frontmatter.
5. Add the source to this manifest, to `docs/index.md`, and to
   `mkdocs.yml` nav.
6. If the new source is CC BY-SA, no upgrade needed; if CC BY,
   no upgrade needed; mixing into synthesis cards inherits CC
   BY-SA.
7. If the new source is **not** CC BY or CC BY-SA, evaluate
   compatibility carefully before merging.
