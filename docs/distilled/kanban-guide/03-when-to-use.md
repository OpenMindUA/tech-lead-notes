---
title: Kanban — when to use (and when not)
type: decision-card
framework: Kanban
source: docs/sources/kanban-guide/03-why-use-kanban.md
source_url: https://kanbanguides.org/the-kanban-guide/
license: CC-BY-SA-4.0
authors_of_source: John Coleman, Daniel Vacanti et al.
tags: [kanban, kanban-guide, decision, fit, scrum, sprint, complement]
---

# Kanban — when to use (and when not)

**TL;DR:** Kanban applies wherever value flows through a workflow — knowledge-work industry doesn't matter. The decision is rarely "Scrum *or* Kanban"; it's "what do we want from flow?". Use Kanban when iteration cadence is the wrong unit of accountability, or **inside** Scrum when you need explicit flow vocabulary. Avoid forcing Kanban onto teams whose value delivery is genuinely batched (release trains, regulated change windows).

## What Kanban optimizes for

Kanban targets a **balance** of three properties:

- **Effectiveness** — delivering what stakeholders want when they want it.
- **Efficiency** — allocating economic resources optimally.
- **Predictability** — forecasting delivery within an acceptable degree of uncertainty.

The strategy isn't "go faster" — it's "ask the right questions sooner". Predictability matters as much as throughput.

## Good fits

- **Sustaining engineering / support / ops** — work arrives ad-hoc; iteration boundaries are arbitrary.
- **Mixed-priority queues** — bug-fix + feature + tech-debt streams that can't share a single Sprint Goal.
- **Service teams** — platform/SRE teams whose customers are other teams; cycle time is the contract.
- **Scaling Scrum** — multiple Scrum teams using Kanban metrics as the cross-team flow contract; SGE explicitly references this.
- **Pre-product-market-fit discovery** — backlog fluidity defeats Sprint commitments; Cycle Time + WIP limits keep discovery honest.

## Poor fits

- **Genuinely batched delivery** — regulated release windows, embedded firmware with hardware ship dates, certification gates. Continuous flow is a fiction here.
- **Teams without `started`/`finished` clarity** — without explicit DoW boundaries, every metric is meaningless.
- **As a "no-process" excuse** — Kanban is *more* discipline (WIP, SLE, policies), not less.

## Complement to Scrum

The Kanban Guide explicitly says Kanban can apply to "virtually any workflow" — that includes **inside a Sprint**. SGE's expansion makes this explicit; the 2020 Scrum Guide does not forbid it. Useful overlay:

- WIP limits inside the Sprint Backlog.
- SLE on a per-PBI basis to detect aged items mid-Sprint.
- Cycle Time as inspection material at Sprint Review and Retrospective.

This does not "replace" Scrum events — it gives them flow data.

## Hand-off to DORA

For software teams, treat **Kanban Cycle Time** and **DORA Lead Time for Changes** as a pair, not a duplication:

- Kanban Cycle Time is bounded by the team's chosen `started`/`finished` (often "in progress" → "deployed").
- DORA Lead Time is bounded by **commit → production**.
- If they diverge sharply, the gap is your batch / queueing time outside development. Investigate it.

## Anti-patterns

- "Scrum vs Kanban" decision framing — they answer different questions; mixing is the norm.
- Adopting Kanban *to abandon* a Sprint cadence the team finds painful, without diagnosing **why** the Sprint hurts. The pain is usually large WIP and unclear DoW — both still problems on a Kanban board.
- Treating Kanban as "no planning" — discovery, refinement and forecasting are still required; the SLE is a planning artifact.

## Cross-refs

- [Three practices + DoW](01-three-practices-and-dow.md)
- [Flow metrics](02-flow-metrics.md)
- Scrum Guide [The Sprint](../scrum-guide/09-the-sprint.md) — what stays Scrum even with Kanban overlay
- Synthesis [Tailoring and method selection](../synthesis/06-tailoring-and-method-selection.md)
- Synthesis [Measurement and metrics](../synthesis/04-measurement-and-metrics.md)

## Source

Full text: [`docs/sources/kanban-guide/03-why-use-kanban.md`](../../sources/kanban-guide/03-why-use-kanban.md), [`02-definition-of-kanban.md`](../../sources/kanban-guide/02-definition-of-kanban.md).
