---
title: Kanban — flow metrics (the four mandatory)
type: metrics-card
framework: Kanban
source: docs/sources/kanban-guide/06-flow-metrics.md
source_url: https://kanbanguides.org/the-kanban-guide/
license: CC-BY-SA-4.0
authors_of_source: John Coleman, Daniel Vacanti et al.
tags: [kanban, kanban-guide, metrics, wip, throughput, cycle-time, work-item-age, sle]
---

# Kanban — flow metrics (the four mandatory)

**TL;DR:** Kanban requires **exactly four** flow metrics; everything else is optional and context-specific. The four feed the three practices — they're how you tell whether your DoW is delivering effectiveness, efficiency and predictability. Metrics in isolation are meaningless: each one must inform a Kanban practice.

## The four mandatory metrics

| Metric | Definition | Use |
|---|---|---|
| **WIP** | Items started but not finished. | Calibrate WIP limits; detect overcommitment. |
| **Throughput** | Items finished per unit of time (exact count, **not** revenue). | Capacity planning; trend over time. |
| **Work Item Age** | Elapsed time from `started` to *now* for in-progress items. | Triage signal — work the *oldest* item first; compare to SLE. |
| **Cycle Time** | Elapsed time from `started` to `finished` for completed items. | Build the SLE distribution; compare against forecasts. |

`started` and `finished` refer to the points the team established **in their DoW**. If the DoW has multiple started/finished pairs (e.g. design→done, dev→shipped), each metric is computed per pair.

You can rename them — Cycle Time may be called "Flow Time", Throughput "Delivery Rate" — provided they're used as defined.

## How they feed the three practices

- **Defining/visualizing** — display Throughput and Cycle Time history on or near the board.
- **Actively managing** — Work Item Age is the daily signal; pull the oldest aged item first.
- **Improving** — Throughput trend, Cycle Time distribution and WIP correlation drive DoW changes.

## Service Level Expectation (SLE)

Cycle Time history is what the **SLE** is built from — typically expressed as a percentile-and-period pair (e.g. "85% of items finish in ≤ 8 days"). Once calculated it lives **on the DoW**, visualized on the board. Use educated guesses until enough history accumulates.

## Beyond the minimum

The four are the **floor**, not the ceiling. Teams may add context-specific measures (Flow Efficiency, blocked time, queue time, Work Item Age distribution by class, etc.). The Open Guide to Kanban catalogs ~13 additional measures — see [its distilled set](../open-guide-to-kanban/index.md).

## Anti-patterns

- **Tracking story points instead of item count** — Kanban Throughput is item count; story points hide the variance, defeating SLE math.
- **Reporting Cycle Time without the percentile** — "average 6 days" is not an SLE; the 85th-percentile-and-below distribution is.
- **Burning down the in-progress backlog by "ageing out" items** — Work Item Age is a signal to act, not an excuse to expedite.
- **Vanity dashboards** — metrics that don't inform a Kanban practice are noise.

## Cross-refs

- [Three practices + DoW](01-three-practices-and-dow.md) — the consumers of these metrics
- DORA [Fundamentals](../dora-metrics-jira/01-dora-fundamentals.md) — Cycle Time vs Lead Time for Changes; same philosophy, different anchors
- DORA [Anti-patterns](../dora-metrics-jira/05-anti-patterns.md) — vanity-metric warnings apply identically
- Scrum Guide Expansion Pack [Definition of Output Done](../scrum-guide-expanded/12-definition-of-output-done.md) — `finished` corresponds to "Output Done"; Outcome Done is downstream

## Source

Full text: [`docs/sources/kanban-guide/06-flow-metrics.md`](../../sources/kanban-guide/06-flow-metrics.md).
