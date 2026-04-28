---
title: Planning (performance domain)
type: performance-domain
domain_number: 4
source: docs/04-enriching-the-methodology/04-planning.md
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [performance-domain, planning, schedule, cpm, kanban, meta-plan, pmo, knowledge-areas]
---

# Planning — performance domain

**TL;DR:** All projects plan — adaptive ones plan *differently*, not
*less*. Plan continually, cover all 10 knowledge areas, separate
**plan** (artifacts) from **meta-plan** (how-to-plan).

## Planning per development approach

| Approach | Up-front plan | Detail timing |
|----------|---------------|---------------|
| Predictive | detailed *or* high-level | full upfront, or per stage |
| Adaptive | very high-level only | full only just before execution |

**Why we plan:** to direct work, and to enable monitor-and-control.
A plan is judged in the context of its development approach and
methodology — same plan can be good in one setup, bad in another.

## Continual planning

- Plan once, never revise → useless plan.
- All approaches require continuous re-planning.

## What gets planned (10 knowledge areas, from PMBOK 6 era)

A reusable checklist:
1. Integration
2. Scope
3. Schedule
4. Cost
5. Quality
6. Resources
7. Communications
8. Risk
9. Procurement
10. Stakeholders

Diagnostic: when someone shows you "the plan" and it is just a
schedule, ask where the other 9 areas are planned.

## Schedule types

- **Dependency-based** — Critical Path Method (CPM) or a similar
  method. For projects with hard precedence (build floor → wall →
  paint). Tools: Primavera P6, MS Project.
- **Priority-based.** For projects whose elements aren't
  strongly dependent — pick by priority and work through.
- **Adaptive projects require priority-based.** If you can't
  produce a true priority-based schedule, the product probably
  shouldn't be developed adaptively.
- Predictive can use either type.

## Levels: plans and meta-plans

- **Plan** = the artifact (e.g. a *risk register* listing risks and
  responses).
- **Meta-plan** = how you'll plan/monitor/control (e.g. a *risk
  management plan* describing techniques, workflows, artifacts).
- Methodologies embed some meta-planning. PRINCE2 expects explicit
  meta-plans; P3.express does not but you can add them where
  attention is needed (e.g. a *procurement strategy* if procurement
  is sensitive).
- Centralize meta-plans for reuse across projects (a *Center of
  Excellence* or *PMO*). Projects adjust them; useful general
  adjustments feed back to the center. This is the
  organization-level step of PMBOK 7's two-step tailoring.
- Caveat: "PMO" is a vague term. Don't let a PMO duplicate or
  collide with project-level PM.

## When this domain matters more

- Long-running, regulated, multi-team projects
- Initial methodology rollout (build the meta-plan library)
- Drafting an enterprise PMO scope and remit

## Anti-patterns

- Calling a Gantt "the plan"
- Big upfront plan, never updated
- "Agile = no planning"
- Single PMO doing project-level work
- Identical detail across all knowledge areas regardless of
  project sensitivity

## Cross-refs

- PRINCE2 §4 [Manage by stages](../principles/prince2/04-manage-by-stages.md)
- PMBOK 7 §7 [Tailor based on context](../principles/pmbok-7/07-tailor.md)
- Performance domain: [Project Work](05-project-work.md), [Measurement](06-measurement.md)

## Source

Full text: [`docs/04-…/04-planning.md`](../../sources/underneath-the-surface/04-enriching-the-methodology/04-planning.md)
