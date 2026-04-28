---
title: About the distilled tier
type: editorial-note
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [distilled, editorial, disclaimer, attribution]
---

# About the distilled tier

## What this is

The Tier-2 distilled cards (everything under `docs/distilled/`)
are an **editorial summary** of Nader K. Rad's
*PMBOK Guide: Underneath the Surface*. The original full text is
preserved in Tier 3 (`docs/01-…/` … `docs/05-…/`) and remains the
canonical reference. Each distilled card carries a **Source** link
back to the corresponding Tier-3 chunk.

## What we changed

The original text mixes principles, anecdotes, personal opinions,
worked stories and historical commentary. For agent and reference
use, the cards strip out most narrative and re-shape what remains
into a fixed structure:

- **TL;DR** — one or two sentences of essence
- **Core ideas** — actionable points only
- **When this applies** — decision contexts
- **Anti-patterns** — failure modes the original warns against
- **Cross-refs** — related concepts inside this corpus
- **Source** — link back to the full Tier-3 chunk

Specific transformations applied:

1. **Anecdotes removed.** The book contains many stories
   ("There was a middle-aged lady...", "I worked for a company that
   had concrete projects..."). The lesson behind each story is
   restated as a rule; the story itself is dropped from the card.
   The full anecdote remains in the Tier-3 chunk.
2. **Structure imposed.** The original prose flows; cards use a
   uniform shape with bullet lists and section headings.
3. **Wording paraphrased.** Most sentences in the cards are not
   verbatim from the book. They are *our* restatement, designed to
   be terse and unambiguous for retrieval-augmented use.
4. **Synthesis added.** Some cards combine related material from
   multiple parts of the book (e.g. cross-references to a principle
   developed earlier; a methodology comparison table).
5. **Mild editorial corrections.** A small number of obvious slips
   in the original (e.g. a passage saying "the other 12 areas"
   immediately after listing 10 areas) are silently corrected to
   match the surrounding facts.
6. **Anti-patterns restated.** The book often warns against a
   failure mode through a story; cards extract the warning as a
   bullet under "Anti-patterns".

We do **not** attempt to:

- Add new project-management content the book doesn't cover
- Disagree with the author's positions (his stance on "hybrid"
  approaches, agile community, role of project manager, etc. is
  preserved)
- Cite passages verbatim — for direct quotation use the Tier-3
  chunk

## License and attribution

- Original text: © Nader K. Rad, licensed CC-BY-4.0,
  available at <https://pmbok.guide/>.
- Distilled cards in this repository: derivative work, licensed
  **CC-BY-4.0** (same terms). When citing, please credit:
    > Distilled summary of Nader K. Rad's *PMBOK Guide:
    > Underneath the Surface* (CC-BY-4.0). See full text at
    > <https://pmbok.guide/pmbok-guide--underneath-the-surface.md>.
- This repository is **not affiliated with or endorsed by**
  Nader K. Rad, PMI, AXELOS, the European Commission, or any of
  the organizations whose methodologies are referenced.
- PMI and PMBOK are registered marks of the Project Management
  Institute, Inc. PRINCE2® and PRINCE2 Agile® are registered marks
  of AXELOS Limited. DSDM® is a registered mark of the Agile
  Business Consortium Limited.

## Verification

Cards have been spot-checked against the source for the most
synthesis-heavy claims (lists, comparison tables, glossary
definitions). For any decision that depends on precise wording,
**read the linked Tier-3 chunk** rather than relying on the card.

If you find a divergence between a card and the source, please
treat the source as authoritative and open an issue / PR against
this repository.

## How to consume

| Goal | Tier |
|------|------|
| Stuff the catalog into an LLM system prompt | Tier 1: [`agent-index.md`](../agent-index.md) |
| Get the actionable substance of a topic fast | Tier 2: distilled cards (this section) |
| Verbatim quotation, citation, full nuance | Tier 3: full original chunks |
| Bulk-load whole corpus into context | [`llms-full.txt`](../llms-full.txt) |

## Versioning

The corpus is regenerated automatically on every push from the
canonical Tier-3 source by `scripts/split_book.py`. The Tier-2
distilled cards are written by humans and committed to this
repository. They are not regenerated from the source — if the
upstream book is revised at <https://pmbok.guide/>, the Tier-3
chunks update automatically but the Tier-2 cards may lag and need
a manual refresh.
