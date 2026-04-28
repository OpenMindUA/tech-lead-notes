---
title: About the distilled tier
type: editorial-note
license_summary: mixed (CC BY 4.0 + CC BY-SA 4.0) — see each card's frontmatter
tags: [distilled, editorial, disclaimer, attribution]
---

# About the distilled tier

## What this is

The Tier-2 distilled cards (everything under `docs/distilled/`)
are **editorial summaries** of the seven CC-licensed sources
listed in [`docs/sources.md`](../sources.md). The full original
text is preserved in Tier 3 (`docs/sources/<source-id>/…`) and
remains the canonical reference. Each distilled card carries a
**Source** link back to the corresponding Tier-3 chunk.

## Sources covered (and where each set of cards lives)

| Source | License | Distilled location |
|--------|---------|--------------------|
| PMBOK Guide — Underneath the Surface | CC BY 4.0 | `principles/`, `performance-domains/`, `methodologies/`, `glossary.md`, `cross-references.md` |
| The 2020 Scrum Guide | CC BY-SA 4.0 | `scrum-guide/` |
| Scrum Guide Expansion Pack (v2026.1) | CC BY-SA 4.0 | `scrum-guide-expanded/` |
| DORA Metrics in Jira (self-authored) | CC BY-SA 4.0 | `dora-metrics-jira/` |
| NUPP — Nearly Universal Principles of Projects | CC BY 4.0 | existing `principles/nupp/` cards (UtS-derived) cross-link to the canonical text in Tier 3 |
| P3.express manual (v2) | CC BY 4.0 | `p3-express/` |
| micro.P3.express manual | CC BY 4.0 | `micro-p3-express/` |

Cross-source synthesis cards live under
[`synthesis/`](synthesis/index.md) and are CC BY-SA 4.0
(ShareAlike inherits when CC BY-SA material is incorporated).

## What we changed

Distillation transforms the original prose into a fixed
agent-friendly shape. Where the original mixes principles,
anecdotes, opinions, worked stories and historical commentary,
the cards strip narrative and impose:

- **TL;DR** — one or two sentences of essence
- **Core ideas** — actionable points only
- **When this applies** — decision contexts
- **Anti-patterns** — failure modes the original warns against
- **Cross-refs** — related concepts inside this corpus
- **Source** — link back to the full Tier-3 chunk

### Specific transformations applied

1. **Anecdotes removed.** Several sources (notably *Underneath
   the Surface*) contain stories that illustrate a principle
   ("There was a middle-aged lady...", "I worked for a company
   that had concrete projects..."). The lesson behind each story
   is restated as a rule; the story itself is dropped from the
   card. The full anecdote remains in the Tier-3 chunk.
2. **Structure imposed.** The original prose flows; cards use a
   uniform shape with bullet lists and section headings.
3. **Wording paraphrased.** Most sentences in the cards are not
   verbatim from the source. They are *our* restatement, designed
   to be terse and unambiguous for retrieval-augmented use.
4. **Synthesis added.** Some cards combine related material from
   multiple parts of one source, or — in the
   [synthesis tier](synthesis/index.md) — across **multiple
   sources** (e.g. "Done across Scrum/SGE/DORA").
5. **Mild editorial corrections.** A small number of obvious
   slips in the originals (e.g. a passage saying "the other 12
   areas" immediately after listing 10 areas) are silently
   corrected to match the surrounding facts.
6. **Anti-patterns restated.** The originals often warn against
   failure modes through stories; cards extract the warning as a
   bullet under "Anti-patterns".
7. **Cross-source navigation added.** Cards link to related
   distilled cards from *other* sources where the topic spans
   frameworks (e.g. SGE Definition of Output Done ↔ DORA
   production-gated DoD ↔ PMBOK 7 Build quality in).

### What we do not attempt

- Add new project-management content the sources don't cover.
- Disagree with the original authors (e.g. UtS author's stance
  on "hybrid" approaches is preserved as written).
- Cite passages verbatim — for direct quotation use the Tier-3
  chunk.
- Reconcile genuine disagreements *between* sources — when SGE
  diverges from SG2020, both are presented faithfully; when
  PMBOK 7 disagrees with PRINCE2, both positions are kept.

## License and attribution

The repository combines content under two CC licenses:

- **CC BY 4.0** sources: Underneath the Surface, NUPP,
  P3.express, micro.P3.express. Cards derived **only** from these
  sources can stay CC BY 4.0.
- **CC BY-SA 4.0** sources: Scrum Guide, Scrum Guide Expansion
  Pack, DORA Metrics in Jira (self-authored under this license).
  Cards derived from any of these — and any cross-source
  synthesis card — are **CC BY-SA 4.0** (ShareAlike inherits).

The `license:` field in each card's YAML frontmatter is
**authoritative per file**. See
[`docs/sources.md`](../sources.md) for the complete license map
and attribution boilerplate.

This repository is **not affiliated with or endorsed by**
Nader K. Rad, PTCoE, PMI, AXELOS, the Agile Business Consortium,
the European Commission, Atlassian, Google Cloud, or any other
organization whose work is referenced. PMI and PMBOK are
registered marks of the Project Management Institute, Inc.
PRINCE2® and PRINCE2 Agile® are registered marks of AXELOS
Limited. DSDM® is a registered mark of the Agile Business
Consortium Limited.

## Verification

Cards have been spot-checked against their sources for the most
synthesis-heavy claims (lists, comparison tables, glossary
definitions). For any decision that depends on precise wording,
**read the linked Tier-3 chunk** rather than relying on the card.

If you find a divergence between a card and the source, please
treat the source as authoritative and open an issue / PR against
this repository.

## How to consume

| Goal | Where to look |
|------|---------------|
| Stuff the catalog into an LLM system prompt | Tier 1: [`agent-index.md`](../agent-index.md) |
| Get the actionable substance of a topic fast | Tier 2: distilled cards (this section) |
| Walk a topic across **multiple** frameworks | Tier 2: [`synthesis/`](synthesis/index.md) |
| Verbatim quotation, citation, full nuance | Tier 3: full original chunks under [`docs/sources/`](../sources/) |
| Bulk-load whole corpus into context | [`llms-full.txt`](../llms-full.txt) |
| Indexable URL list for retrieval clients | [`llms.txt`](../llms.txt) |

## Versioning and refresh

- **Tier 3** is regenerated on every push by ingest scripts in
  `scripts/`. For sources fetched from the web (Scrum Guide,
  Scrum Guide Expanded, NUPP, P3.express, micro.P3.express) the
  build is **best-effort** — if upstream is unreachable, CI falls
  back to the committed snapshot in `raw-sources/` and emits a
  warning.
- A monthly workflow
  ([`.github/workflows/monthly-refresh.yml`](https://github.com/OpenMindUA/tech-lead-notes/blob/main/.github/workflows/monthly-refresh.yml))
  fetches all upstream sources and **opens a PR** if the committed
  snapshot has drifted — so upstream changes appear as a
  reviewable diff rather than being silently absorbed.
- **Tier 2** distilled cards are written by humans and committed
  to this repository. They are **not** regenerated from sources.
  When upstream changes structurally (renamed sections, removed
  content), distilled cards may lag and need manual refresh.
