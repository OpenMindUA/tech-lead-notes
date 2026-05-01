---
title: Pick a method for a new initiative
type: agent-recipe
use_when: Spinning up a new project / product / team — choosing Scrum / Kanban / P3.express / micro.P3.express / hybrid based on context; resisting cargo-cult adoption
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/methodologies/comparison.md
  - docs/distilled/methodologies/p3-express.md
  - docs/distilled/methodologies/scrum.md
  - docs/distilled/methodologies/prince2.md
  - docs/distilled/methodologies/dsdm.md
  - docs/distilled/kanban-guide/03-when-to-use.md
  - docs/distilled/synthesis/06-tailoring-and-method-selection.md
  - docs/distilled/wardley-maps/02-evolution-stages.md
  - docs/distilled/principles/nupp/06-repeatable-elements.md
load_tier3_optional:
  - docs/sources/underneath-the-surface/03-selecting-a-methodology/index.md
output_shape: context-fit-matrix + recommended method (with tailoring) + alternatives
license: CC-BY-SA-4.0
tags: [recipe, agent, methodology, tailoring, scrum, kanban, p3-express]
---

# Pick a method for a new initiative

## Use this when

A new initiative is about to start (project, product line, internal tool, refactor program). Someone says "we'll use Scrum because that's what we do" — you want to verify that's the right choice, or pick something else with reasoning.

## Cards to load

| Card | Why |
|---|---|
| Methodologies comparison | The side-by-side table |
| P3.express / Scrum / PRINCE2 / DSDM cards | Per-method specifics |
| Kanban: when to use | Flow vs sprint; complement vs replacement |
| Synthesis: Tailoring | "Tailor in" not "tailor out"; system design |
| Wardley: Evolution stages | Stage of the *thing being built* dictates method |
| NUPP: Repeatable elements | Don't reinvent — but also don't cargo-cult |

## Prompt skeleton

```
You are helping a tech-lead pick a delivery method for a new
initiative. Use the loaded cards as authority. Resist defaults.

Inputs:
- INITIATIVE: <name + 1-paragraph description; what's being built and why>
- TEAM_SIZE: <number of people; co-located / distributed>
- DURATION: <expected timeframe>
- DELIVERABLE_NATURE: <product / project / continuous-flow / one-off>
- EVOLUTION_STAGE: <genesis / custom / product / commodity if known>
- CUSTOMER_TYPE: <internal / external / multiple>
- EXISTING_PRACTICES: <what the team currently does; what other teams in the org do>
- CONSTRAINTS: <regulatory / legal / political / org-mandates>

Tasks:
1. Classify the initiative along the comparison-card axes:
   adaptive vs predictive, scope-fixed vs scope-emergent, single-team
   vs multi-team, IT vs general.
2. Match to the closest canonical method, then ask: should this be
   tailored, hybridized, or replaced with something else?
3. If the evolution stage is known, cross-check with Wardley's "use
   appropriate methods" doctrine. (Genesis → ad-hoc + research; Custom
   → agile / Scrum; Product → Scrum or P3.express; Commodity → ITIL-
   style ops, not project method at all.)
4. Output: context-fit matrix, primary recommendation with tailoring
   notes, and 1-2 viable alternatives with the trade-off.

Constraints:
- Do not pick by familiarity ("the team knows Scrum") unless context
  justifies it. Cite the cargo-cult anti-pattern from Tailoring synthesis.
- Do not over-engineer. If the initiative is small and short, prefer
  micro.P3.express over Scrum.
- Distinguish "method" from "ceremonies" — Kanban can complement Scrum.
```

## Expected output

```
## Context fit
| Axis | This initiative |
|---|---|
| Adaptive vs predictive | <…> |
| Single vs multi-team | <…> |
| Scope-fixed vs emergent | <…> |
| IT vs general | <…> |
| Wardley stage | <…> |

## Recommendation
**Primary:** <method name> with tailoring: <bullets>
**Why:** <2-3 sentences citing comparison + tailoring synthesis>

## Alternatives
1. <method> — <why one might prefer this; what you'd give up>
2. <method> — <why one might prefer this; what you'd give up>

## Anti-patterns avoided
- Cargo-cult Scrum because "team knows it"
- Ceremonies-first ("we'll do Daily Scrum and figure out the rest")
- Predictive method on emergent scope
```

## Anti-pattern (do NOT use this recipe for)

- Mid-project methodology change — that's a separate "tailoring re-design" task, with sunk-cost considerations.
- "Should we add Scrum Master?" — too granular; this recipe answers method-level questions.
- Choosing a project-management tool (Jira / Linear / Trello) — orthogonal.

## Cross-refs

- [Build / buy / rent / outsource](03-build-buy-rent-outsource.md) — pre-method decision
- [Team / org redesign (PST)](06-team-org-redesign.md) — staffing the method
- [Forecasting & SLE](09-forecasting-and-sle.md) — once method is picked, how to estimate
