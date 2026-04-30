---
title: Kanban — three practices and the Definition of Workflow
type: practice-card
framework: Kanban
source: docs/sources/kanban-guide/05-kanban-practices.md
source_url: https://kanbanguides.org/the-kanban-guide/
license: CC-BY-SA-4.0
authors_of_source: John Coleman, Daniel Vacanti et al.
tags: [kanban, kanban-guide, practices, dow, definition-of-workflow, wip, sle]
---

# Kanban — three practices and the Definition of Workflow

**TL;DR:** Kanban is three practices working in tandem — **Define and visualize the workflow**, **Actively manage items**, **Improve the workflow**. The shared explicit understanding of what flows through the system is the **Definition of Workflow (DoW)** — the single fundamental concept everything else hangs from. Without a DoW, none of the other elements have a referent.

## The three practices

1. **Defining and visualizing the workflow** — make the DoW explicit and put it on a Kanban board.
2. **Actively managing items** — control WIP, watch ageing items against the SLE, unblock work.
3. **Improving the workflow** — continually refine the DoW; changes can be small or significant, just-in-time, no required cadence.

These work *together*. Skipping any of them means it isn't Kanban — it's a board.

## Six minimum DoW elements

The DoW must include **all** of these (order doesn't matter):

1. **Work items** — definition of the units of value flowing through the system.
2. **Started / finished points** — explicit boundaries; a workflow may have more than one started/finished pair.
3. **States** — defined intermediate states between started and finished. Anything between is **WIP**.
4. **WIP control** — explicit policy for how WIP is bounded.
5. **Explicit policies** — for how items can move through each state.
6. **SLE (Service Level Expectation)** — a forecast like "85% of items will finish in ≤ 8 days", based on historical cycle time (educated guess if no history). Visualize on the DoW.

Multiple DoWs are allowed and often needed (different teams, different organizational levels, different work item types).

## Active management — what it actually means

- **Control WIP.** Operate neither above nor below the agreed limit. WIP control creates a **pull system** — start work only when there's capacity.
- **Don't let items age unnecessarily** — use SLE as the reference; older-than-SLE items get attention first.
- **Unblock blocked work** — review actively, regularly (continuous, periodic, or both).
- **Acceptable WIP exceptions** must be made part of the DoW.

## When this applies

- Knowledge work where the workflow already exists and you want to optimize it without restructuring teams.
- Teams that don't fit a fixed iteration cadence (support, ops, sustaining engineering).
- **Inside** a Scrum Sprint — Scrum doesn't forbid WIP limits or flow boards; Kanban gives the missing flow vocabulary.

## Anti-patterns

- "Kanban board" without WIP limits — visualization without control is monitoring, not Kanban.
- DoW that only covers item types and states — missing SLE and explicit policies means the team can't tell normal from late.
- Scheduling DoW changes for "the next retro" — the Kanban Guide explicitly rejects this. Improvements are **just-in-time**.
- Treating SLE as a deadline. It's a probabilistic forecast; missing it is a signal to investigate, not a failure.

## Cross-refs

- [Flow metrics](02-flow-metrics.md) — the 4 measures that feed active management
- [When to use Kanban](03-when-to-use.md) — fit and complement to Scrum/DORA
- Scrum Guide [Increment + DoD](../scrum-guide/16-increment.md) — DoD vs DoW: DoD is the quality bar for items reaching done; DoW also defines flow constraints (WIP, policies, SLE)
- DORA [Lead Time for Changes](../dora-metrics-jira/01-dora-fundamentals.md) — overlaps with Cycle Time but anchored at commit→deploy
- PMBOK 7 §8 [Build quality in](../principles/pmbok-7/08-quality.md) — explicit policies as quality-in-the-process

## Source

Full text: [`docs/sources/kanban-guide/05-kanban-practices.md`](../../sources/kanban-guide/05-kanban-practices.md).
