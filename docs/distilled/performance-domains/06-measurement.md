---
title: Measurement (performance domain)
type: performance-domain
domain_number: 6
source: docs/04-enriching-the-methodology/06-measurement.md
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [performance-domain, measurement, kpi, forecast, reporting, parkinsons-law]
---

# Measurement — performance domain

**TL;DR:** Measure to direct work and to evaluate it. Use **forecast
to completion** as the headline metric. **What you measure becomes
the goal** — choose proxies that align with real value.

## Recovering from deviations

- Methodologies use **thresholds** to decide *who* recovers from a
  deviation, not *whether* recovery is needed.
    - Below threshold → team decides
    - Medium → PM decides
    - Above → escalate to higher level
- Common error: thinking "below threshold = no recovery needed".
  Untreated small deviations pile up and become hard to fix.

## Correction vs prevention

- **Corrective action** — fix the deviation now.
- **Preventive action** — fix the root cause so it can't recur.
- Most teams correct and skip prevention → endless firefighting.
- If forced to drop one, **drop correction, keep prevention**.
- Make this explicit in the methodology if it isn't.

## Targets

- Frequent **justification check** is essential. If your method
  lacks one, add it.
- Classical targets: scope, time, cost, quality. Sometimes risk,
  benefits.
- Tune frequency/depth of these checks to *your* project sensitivity.

## Proper measurements

- **What you measure becomes the goal.** Bad proxies create bad
  behavior:
    - Lines of code → bloated code; the great programmer with
      *negative* LOC after cleanup is the cautionary tale.
    - "Items completed per iteration" → conservative under-planning
      (Parkinson's law: work expands to fill the time available).
- Align metrics to real organizational/project goals.
- Direct value measurement (e.g. strategic alignment) is hard;
  fall back to project-target proxies, then refine in portfolio
  management.
- **Forecast-to-completion is the only effective measurement.**
  Example: how much money to finish the project, given current data.

## Reporting

- Audiences differ → multiple report types.
- Verify the message lands; iterate the report if it doesn't.
- People are busy and easily bored → short focused reports.
- If a stakeholder demands long detailed reports for comfort,
  attach a short focused version too.
- Boards / dashboards / *information radiators* are options.
  Don't assume people will visit a dashboard — push a
  notification or short summary.

## When this domain matters more

- Performance-bonus or contract structures with bad-proxy risk
- Long projects with drift between plan and reality
- Multi-stakeholder reporting demands

## Anti-patterns

- Correcting symptoms without preventing root cause
- Threshold = "ignore" rather than "delegate"
- LOC / story-point velocity as primary measure
- Single report style for all audiences
- Long detailed reports as the only output
- Dashboards with no push, no notifications

## Cross-refs

- PMBOK 7 §4 [Focus on value](../principles/pmbok-7/04-focus-on-value.md)
- PMBOK 7 §8 [Build quality in](../principles/pmbok-7/08-quality.md)
- Performance domain: [Project Work](05-project-work.md), [Planning](04-planning.md)

## Source

Full text: [`docs/04-…/06-measurement.md`](../../sources/underneath-the-surface/04-enriching-the-methodology/06-measurement.md)
