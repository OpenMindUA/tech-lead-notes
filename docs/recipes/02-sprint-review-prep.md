---
title: Sprint Review prep — output vs outcome
type: agent-recipe
use_when: Preparing a Sprint Review or stakeholder demo; defending "we shipped but the metric didn't move"; deciding whether the increment is worth showing
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/synthesis/03-outcome-vs-output.md
  - docs/distilled/scrum-guide-expanded/11-definition-of-outcome-done.md
  - docs/distilled/scrum-guide-expanded/12-definition-of-output-done.md
  - docs/distilled/scrum-guide/12-sprint-review.md
  - docs/distilled/scrum-guide-expanded/10-product-and-vision.md
load_tier3_optional:
  - docs/sources/scrum-guide-expanded/09-the-scrum-artifacts-in-the-expansion-pack/02-commitment-definition-of-outcome-done.md
output_shape: review-agenda + outcome-vs-output framing + stakeholder-message draft
license: CC-BY-SA-4.0
tags: [recipe, agent, sprint-review, outcome, output, scrum]
---

# Sprint Review prep — output vs outcome

## Use this when

The Sprint is about to end and you need to (a) build a Review agenda that's not just a demo, (b) honestly say what *outcome* moved (or didn't) vs what *output* shipped, (c) prepare for stakeholders asking "is this making money / saving time / changing user behavior?"

## Cards to load

| Card | Why |
|---|---|
| Synthesis: Output vs Outcome | The full distinction (output / outcome / impact / value) and operationalization |
| SGE: Definition of Outcome Done | New commitment, Product-level — what counts as outcome evidence |
| SGE: Definition of Output Done | Increment-level — what counts as shippable |
| Scrum 2020: Sprint Review | Canonical event purpose (inspect outcome, not demo theatre) |
| SGE: Product + Vision | Where the Outcome Done lives |

## Prompt skeleton

```
You are helping a tech-lead prepare a Sprint Review. Use only the
loaded cards as authority. Be ruthless about output-bias.

Inputs:
- SPRINT_GOAL: <text>
- INCREMENT: <list of items shipped>
- DOOD: <Definition of Output Done — pasted or linked>
- DOOC_DONE: <Definition of Outcome Done — pasted or linked, or "missing">
- METRIC_MOVEMENT: <observed user-behavior / business-metric change since last Review, if any>
- STAKEHOLDERS: <who attends>

Tasks:
1. Check each Increment item against the DoOD — anything not Output Done?
2. Map each item to an outcome the team aims at. If no DoOD card exists,
   call out the gap explicitly and recommend creating one.
3. Identify the gap: what shipped (output) vs what changed (outcome).
   Use the Synthesis card's failure-mode catalog.
4. Build a Review agenda:
   - Inspection of the Increment vs DoOD (5-10 min)
   - Outcome / metric-movement section (10-15 min) — with honest "no
     movement yet" if applicable
   - Backlog adaptation discussion (10-15 min)
5. Draft a 1-paragraph stakeholder message that distinguishes
   output-shipped from outcome-realized. Avoid "successfully delivered"
   framing if the outcome hasn't materialized.

Constraints:
- Do not present output as outcome.
- If Outcome Done isn't defined, say "we don't have an Outcome Done
  yet, here's the gap" — do not pretend.
```

## Expected output

```
## Sprint Review agenda
- 0:00 — Sprint Goal recap
- 0:05 — Increment inspection vs Definition of Output Done
  - Item A ✅, Item B ✅, Item C ⚠ (test coverage gap)
- 0:20 — Outcome inspection
  - Target outcome: <restated>
  - Evidence to date: <metric / no movement / too early>
- 0:35 — Backlog adaptation
- 0:55 — Q&A

## Output vs outcome
- Output: <bullet list>
- Outcome (observed): <bullet list — or "none observed yet because…">
- Outcome (expected when): <date / horizon>

## Stakeholder message draft
> This Sprint we shipped <X, Y, Z>. We do not yet see movement on
> <KPI>; per our Definition of Outcome Done that requires <≥N
> sessions / 4 weeks of usage>. We will report back at the next
> Review.

## Risks called out
- ...
```

## Anti-pattern (do NOT use this recipe for)

- Demos to a single PM internally. This recipe is for stakeholder-facing Reviews with mixed audience.
- "How do I make the metric look good?" — recipe is about honest reporting, not narrative engineering.
- Sprint Retrospective prep — different event, different inputs (use the team's own retro format).

## Cross-refs

- [PR review with DORA](01-pr-review-with-dora.md) — what fed into this Increment
- [Strategic review / annual planning](08-strategic-review.md) — yearly framing where outcomes accumulate
- [Stakeholder map](07-stakeholder-map.md) — who attends and what they care about
