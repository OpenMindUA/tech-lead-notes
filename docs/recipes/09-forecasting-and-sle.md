---
title: Forecasting & SLE discussion
type: agent-recipe
use_when: "Коли буде готово?"; replacing story-point estimation with flow-based forecasting; explaining variance to stakeholders; debating estimation alternatives
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/kanban-guide/02-flow-metrics.md
  - docs/distilled/kanban-guide/01-three-practices-and-dow.md
  - docs/distilled/open-guide-to-kanban/01-deltas-from-kanban-guide.md
  - docs/distilled/dora-metrics-jira/01-dora-fundamentals.md
  - docs/distilled/synthesis/04-measurement-and-metrics.md
  - docs/distilled/performance-domains/06-measurement.md
load_tier3_optional:
  - docs/sources/kanban-guide/06-flow-metrics.md
  - docs/sources/open-guide-to-kanban/06-inform-flow-optimization-with-appropriate-measures-or-metrics.md
output_shape: SLE-construction + forecast-with-confidence + estimation-replacement-plan
license: CC-BY-SA-4.0
tags: [recipe, agent, forecasting, sle, kanban, flow-metrics, estimation]
---

# Forecasting & SLE discussion

## Use this when

A stakeholder asks "коли це буде готово?" and the team's answer is uncertain. Or: leadership wants to "improve estimation accuracy" and the obvious answer ("more story points!") is wrong. Or: someone wants to set an SLE for the team and doesn't know how. Use Kanban flow metrics + DORA Lead Time as the spine.

## Cards to load

| Card | Why |
|---|---|
| Kanban: Flow metrics | The four mandatory: WIP, Throughput, Work Item Age, Cycle Time |
| Kanban: Three practices + DoW | SLE lives on the DoW |
| Open Guide deltas | Expanded metrics catalog (~13) for context-specific cases |
| DORA: fundamentals | Cycle Time vs Lead Time for Changes — same philosophy, different anchors |
| Synthesis: Measurement | Parkinson's law + read-together rule + 3-layer stack |
| UtS: Measurement perf domain | Forecast to completion; metrics align with goals |

## Prompt skeleton

```
You are helping a tech-lead build a forecast (or replace estimation
with flow-based forecasting). Use the loaded cards as authority.

Inputs:
- TEAM_HISTORY: <last N weeks of Throughput, Cycle Time, WIP if
  available; or "we have no history">
- SCOPE: <list of items to forecast; each item ideally same size as
  past items>
- STAKEHOLDER_QUESTION: <"when will X be done?" / "what can we
  commit to by Q3?" / "how do we set an SLE?">
- CURRENT_ESTIMATION: <story points / hours / "we just guess">
- CONSTRAINTS: <hard deadline / regulatory / external dep>

Tasks:
1. If history exists:
   - Compute Throughput trend (last 4-12 weeks).
   - Compute Cycle Time distribution; pick a percentile (typical:
     85th).
   - Express SLE as "85% of items finish in ≤ N days" (or weeks).
2. Forecast the question:
   - "When?" → use Throughput + scope size + Monte Carlo (or simple
     N / Throughput) with explicit confidence interval.
   - "What by date?" → invert: how many items can we finish by D
     with 85% confidence?
3. If no history exists:
   - Recommend establishing the four mandatory flow metrics first
     (Cycle Time, Throughput, WIP, Work Item Age).
   - Use educated-guess SLE for ~4-8 weeks until history accumulates.
   - Cite the Kanban Guide rule.
4. Replacement plan if the team currently uses story points:
   - Keep counting items, drop the points.
   - Track SLE drift; revise quarterly.
5. Output: SLE statement + forecast (with confidence) + replacement
   plan + anti-patterns to avoid.

Constraints:
- Reject single-number forecasts. Always express with percentile /
  range.
- Reject "average Cycle Time" — distribution matters; use percentiles.
- Don't promise predictability without history. Say so.
- "Crunch to hit the date" is not a forecast; it's a sacrifice. Flag.
```

## Expected output

```
## SLE
> 85% of items finish in ≤ 8 calendar days from `started` to `finished`
> (per the team's DoW: dev-started → prod-deployed).

Caveats: based on N weeks of history; revise after the next 4 weeks.

## Forecast
- Question: <restated>
- Method: <Throughput + scope / Monte Carlo>
- Result:
  - 50% confidence: <date / count>
  - 85% confidence: <date / count>
  - 95% confidence: <date / count>
- Assumptions: WIP cap unchanged; team composition stable; no
  category-jumps in item size.

## Replacement plan (if estimating today)
1. This Sprint: keep both story points and item count.
2. Sprints +1..+4: build SLE from item count. Compare.
3. Sprint +5: drop story points; communicate to stakeholders.
4. Quarterly: revise SLE.

## Anti-patterns to avoid
- Average Cycle Time → use percentile.
- Vanity dashboards (no link to a Kanban practice).
- Promising the 95% date without WIP control.
- "Speed up the process" by skipping reviews — reduces Cycle Time
  but inflates CFR. Read DORA together.
```

## Anti-pattern (do NOT use this recipe for)

- Single-shot, fixed-scope projects with no history. Forecasting needs flow data.
- "How long will this *feature* take?" before discovery / refinement. SLE applies to similar-sized items, not unbounded features.
- Performance management ("are people fast enough?"). Flow metrics are about the system, not individuals.

## Cross-refs

- [PR review with DORA](01-pr-review-with-dora.md) — Cycle Time per PR
- [Pick a method](04-pick-a-method.md) — Kanban as forecast spine; sometimes Scrum sprints add nothing
- [Sprint Review prep](02-sprint-review-prep.md) — communicate forecast at the Review
