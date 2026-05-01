---
title: Strategic review / annual planning
type: agent-recipe
use_when: Yearly strategy cycle; multi-product roadmap; "where should we differentiate / commoditize / open-source / kill?"; portfolio review with the leadership team
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/wardley-maps/07-strategy-cycle-and-when-to-use.md
  - docs/distilled/wardley-maps/03-doctrine.md
  - docs/distilled/wardley-maps/04-climatic-patterns.md
  - docs/distilled/wardley-maps/05-gameplay.md
  - docs/distilled/wardley-maps/01-anatomy-of-a-map.md
  - docs/distilled/wardley-maps/02-evolution-stages.md
  - docs/distilled/principles/pmbok-7/04-focus-on-value.md
  - docs/distilled/synthesis/03-outcome-vs-output.md
load_tier3_optional:
  - docs/sources/wardley-maps/16-super-looper.md
  - docs/sources/wardley-maps/17-to-infinity-and-beyond.md
output_shape: map + climatic forecast + doctrine audit + 3-5 plays + measurement plan
license: CC-BY-SA-4.0
tags: [recipe, agent, strategy, wardley, annual-planning, roadmap]
---

# Strategic review / annual planning

## Use this when

Annual / quarterly strategy review; presenting a roadmap to the leadership team; rationalizing a portfolio of products / platforms; deciding what to invest in vs sunset. This is the **strategy cycle** in action — purpose → landscape → climate → doctrine → leadership (act) → loop.

## Cards to load

| Card | Why |
|---|---|
| Wardley: Strategy cycle | The full OODA-like loop |
| Wardley: Doctrine | Audit checklist before any gameplay |
| Wardley: Climatic patterns | Annotate the map with forecasted moves |
| Wardley: Gameplay | Pick plays that match the map |
| Wardley: Anatomy + Evolution | Foundations |
| PMBOK 7: Focus on value | Value = benefits ÷ cost |
| Synthesis: Output vs Outcome | Strategy that ships output but no outcome = waste |

## Prompt skeleton

```
You are helping a tech-lead run the strategy cycle for a portfolio.
Use Wardley's strategy-cycle structure; cite cards.

Inputs:
- PURPOSE: <organization's reason to exist; what wins look like>
- USERS: <user types and their needs; one or two anchors>
- CURRENT_PORTFOLIO: <list of products / platforms / capabilities; for
  each: rough evolution stage, profitability, strategic role>
- COMPETITIVE_LANDSCAPE: <what competitors are doing; market shifts>
- TIME_HORIZON: <next 1-3 years>
- CONSTRAINTS: <budget / regulatory / political>

Tasks:
1. **Purpose** — restate clearly. Reject vague ones.
2. **Landscape** — sketch a Wardley map (text-described): anchor on
   user need, decompose to value chain, position each component on
   the evolution axis.
3. **Climate** — annotate which components will move (and how fast)
   over the time horizon. Apply ≥ 3 climatic patterns explicitly:
   - Everything evolves
   - Inertia
   - Coevolution of practice and activity
4. **Doctrine** — audit the org against the doctrine phases. Score
   each phase low / medium / high. The lowest score is the priority
   gap — do not skip to gameplay.
5. **Leadership / Act** — propose 3-5 plays that match the map +
   climate. Per play: type (open-source / tower-and-moat / ILC /
   defensive / etc.), expected effect, opponent counter-play.
6. **Measurement** — define outcome-evidence per play (per Output vs
   Outcome synthesis); when to re-evaluate.
7. Output: map sketch + climate annotation + doctrine audit +
   plays + measurement plan.

Constraints:
- No play before doctrine audit. If doctrine is broken, fix that
  first.
- Do not promise outcomes that won't materialize within the time
  horizon. Be explicit about lag.
- Inertia is real. Plan the *transition*, not just the destination.
```

## Expected output

```
## Purpose
<one-paragraph clear restatement>

## Landscape (map sketch)
- Anchor: <user> needing <need>
- Value chain (top → bottom):
  - <component A> [stage: product]
  - <component B> [stage: custom]
  - <component C> [stage: commodity]
- Dependencies: <textual links>

## Climate (1-3 yr forecast)
- <component A>: will move from product → commodity (cite pattern)
- <component B>: stable; opponent X may accelerate it
- Inertia: <internal investments / contracts blocking moves>

## Doctrine audit
| Phase | Score | Gap |
|---|---|---|
| I — Communication | high | OK |
| II — Development | medium | one-method-fits-all in dev |
| III — Operation | low | bias not challenged |
| IV — Structure | medium | PST imbalance |
| V — Learning | medium | OK-ish |
| VI — Leading | high | OK |
**Priority fix:** Phase III (transparency / challenge assumptions)

## Plays (3-5)
1. **Open-source play** on component X (currently product → commoditize
   to undercut competitor Y's margin; we sell layer Z above).
2. ...

## Measurement
| Play | Outcome evidence | When to re-evaluate |
|---|---|---|
| 1 | competitor Y revenue on X drops | 12 months |
| ... |

## Re-loop trigger
- If <signal>, run the cycle early.
```

## Anti-pattern (do NOT use this recipe for)

- Sprint-level planning. Wardley operates above Scrum / Kanban.
- "Pick a single tactic" — gameplay needs map + climate + doctrine context.
- One-shot exercise. The cycle is iterative. If you run it once a year and forget, you're not doing strategy.

## Cross-refs

- [Build / buy / rent / outsource](03-build-buy-rent-outsource.md) — component-level decisions inside the strategy
- [Team / org redesign (PST)](06-team-org-redesign.md) — staffing once the strategy is set
- [Sprint Review prep](02-sprint-review-prep.md) — feeds outcome data back into the cycle
