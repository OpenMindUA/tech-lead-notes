---
title: Build / buy / rent / outsource decision
type: agent-recipe
use_when: Deciding whether a component should be built in-house, bought as a product, rented as a utility, or outsourced — Wardley evolution stage as the primary lens
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/wardley-maps/01-anatomy-of-a-map.md
  - docs/distilled/wardley-maps/02-evolution-stages.md
  - docs/distilled/wardley-maps/03-doctrine.md
  - docs/distilled/wardley-maps/04-climatic-patterns.md
  - docs/distilled/wardley-maps/05-gameplay.md
  - docs/distilled/synthesis/06-tailoring-and-method-selection.md
load_tier3_optional:
  - docs/sources/wardley-maps/03-exploring-the-map.md
  - docs/sources/wardley-maps/05-the-play-and-a-decision-to-act.md
output_shape: stage-classification + decision-matrix + recommendation
license: CC-BY-SA-4.0
tags: [recipe, agent, wardley, build-vs-buy, evolution-stages]
---

# Build / buy / rent / outsource

## Use this when

Someone is asking "should we build this?" — for a database, an auth layer, a feature-flag service, an ML platform, a data pipeline, an LLM-gateway, an internal dev tool. Default human instinct ("we're special, we'll build") is usually wrong; default vendor instinct ("buy the SaaS") is usually right but not always. Wardley's evolution stage gives the principled answer.

## Cards to load

| Card | Why |
|---|---|
| Wardley: Anatomy of a map | Anchor on user need; this isn't an org-chart decision |
| Wardley: Evolution stages | Genesis / custom / product / commodity — the lens |
| Wardley: Doctrine | "Use appropriate methods" — ban one-size-fits-all |
| Wardley: Climatic patterns | Inertia is real; "everything evolves" |
| Wardley: Gameplay | Open-source play; tower & moat — rarely relevant but worth checking |
| Synthesis: Tailoring | Same insight in PM-method language |

## Prompt skeleton

```
You are helping a tech-lead decide whether to build, buy, rent or
outsource a specific component. Use Wardley evolution stages as the
primary lens; cite the relevant card for each conclusion.

Inputs:
- COMPONENT: <name + 1-paragraph description of what it does>
- ANCHOR_USER: <who the user is and what need this component serves>
- CURRENT_OPTIONS: <market alternatives — list 2-5 with rough cost / maturity>
- INTERNAL_CAPABILITY: <current team strengths / weaknesses re. this component>
- TIME_HORIZON: <when must this be live; how long will it live>
- INERTIA_FACTORS: <existing investments / contracts / political holds, if any>

Tasks:
1. Classify the component on the evolution axis (genesis / custom /
   product / commodity). Use Wardley's cheat-sheet questions
   (ubiquity, certainty, publication, emotional reaction).
2. List which alternatives correspond to each stage on the market.
3. Apply the build-vs-buy-vs-rent-vs-outsource rule for that stage.
4. Identify inertia factors and propose a transition plan if the
   stage classification conflicts with current internal practice.
5. Output: classification + decision matrix + 1-paragraph
   recommendation with stage-justified reasoning.

Constraints:
- Stage-stage. If the component is at commodity, do not recommend
  building it because of "we're unique" arguments — challenge those.
- If genesis-stage, do not recommend a SaaS purchase — none exists
  meaningfully yet.
- Be explicit about confidence: stage-on-axis is a band, not a point.
```

## Expected output

```
## Stage classification
Component: <name>
Stage: <genesis | custom | product (rental) | commodity (utility)>
Confidence: <low | medium | high> — based on <which cheat-sheet signals>

## Decision matrix
| Option | Fits stage? | Cost | Time to value | Long-term cost | Verdict |
|---|---|---|---|---|---|
| Build in-house | ... | ... | ... | ... | ... |
| Buy product (vendor X) | ... | ... | ... | ... | ... |
| Rent utility (vendor Y) | ... | ... | ... | ... | ... |
| Outsource to consultancy | ... | ... | ... | ... | ... |

## Recommendation
<1-paragraph stage-justified pick + transition plan if inertia is in the way>

## Inertia / risks
- <bullet list of what will resist this and how to mitigate>

## What we'd re-evaluate in 6-12 months
- <if stage is migrating, when to re-decide>
```

## Anti-pattern (do NOT use this recipe for)

- Picking *a specific vendor* once the build-vs-buy decision is made — that's a vendor RFP, different work.
- Architectural design within an in-house build — once you've decided to build, use a different recipe / approach.
- Annual portfolio review — that's a higher-altitude decision; use [Strategic review](08-strategic-review.md).

## Cross-refs

- [Pick a method for a new initiative](04-pick-a-method.md) — once you've picked build, what process to use
- [Strategic review / annual planning](08-strategic-review.md) — multiple build/buy decisions across portfolio
- [Team / org redesign (PST)](06-team-org-redesign.md) — who staffs each stage
