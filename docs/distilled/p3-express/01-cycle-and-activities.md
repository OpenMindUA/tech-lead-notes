---
title: P3.express cycle and activity codes
type: methodology-overview
framework: P3.express
source: docs/sources/p3-express/index.md
source_url: https://p3.express/manual/v2/
license: CC-BY-4.0
authors_of_source: PTCoE — Nader K. Rad et al.
tags: [p3-express, cycle, activities, cadence, monthly, weekly, daily]
---

# P3.express cycle and activity codes

**TL;DR:** 33 activities in 7 groups. The project has a **monthly cycle** (B+E groups around continuous **weekly** C and **daily** D management), bracketed by **Project Initiation** (A) at the start and **Project Closure** (F) + **Post-Project Management** (G) at the end. Activity codes are stable references — agents and humans cite them directly (e.g. "follow A07 peer-review pattern").

## The full map

```
A — Project Initiation       (10 activities, A01..A10) ← run once at start
B — Monthly Initiation        (5,  B01..B05)            ← repeats each month
C — Weekly Management         (4,  C01..C04)            ← repeats each week
D — Daily Management          (2,  D01..D02)            ← repeats every day
E — Monthly Closure           (3,  E01..E03)            ← end of each month
F — Project Closure           (6,  F01..F06)            ← run once at end
G — Post-Project Management   (3,  G01..G03)            ← weeks/months after closure
```

## Activity index (codes you'll cite)

### A — Project Initiation (10 activities)

| Code | Activity |
|---|---|
| A01 | Appoint the sponsor |
| A02 | Appoint the project manager |
| A03 | Appoint key team members |
| A04 | Describe the project |
| A05 | Identify and plan deliverables |
| A06 | Identify risks and plan responses |
| **A07** | **Peer-review project initiation** *(quality gate)* |
| **A08** | **Make a go/no-go decision** *(sponsor's gate)* |
| A09 | Kick off the project |
| A10 | Conduct a focused communication |

### B — Monthly Initiation (5)

| Code | Activity |
|---|---|
| B01 | Have the team revise the plans |
| B02 | Revise the project description |
| **B03** | **Have Monthly Initiation peer-reviewed** |
| **B04** | **Make a go/no-go decision** |
| B05 | Conduct a focused communication |

### C — Weekly Management (4)

| Code | Activity |
|---|---|
| C01 | Measure performance |
| C02 | Plan responses to deviations |
| C03 | Identify and respond to new risks |
| C04 | Conduct a focused communication |

### D — Daily Management (2)

| Code | Activity |
|---|---|
| D01 | Manage follow-up items (risks, issues, change requests) |
| D02 | Accept completed deliverables |

### E — Monthly Closure (3)

| Code | Activity |
|---|---|
| E01 | Evaluate stakeholder satisfaction |
| E02 | Plan improvements |
| E03 | Conduct a focused communication |

### F — Project Closure (6)

| Code | Activity |
|---|---|
| F01 | Hand over the product |
| F02 | Evaluate stakeholder satisfaction |
| **F03** | **Have Project Closure peer-reviewed** |
| F04 | Archive project documents |
| F05 | Re-assign the team |
| F06 | Celebrate |

### G — Post-Project Management (3)

| Code | Activity |
|---|---|
| G01 | Evaluate the benefits |
| G02 | Generate ideas for new projects |
| G03 | Conduct a focused communication |

## Pattern recognition

Several activities **repeat across cycles** (focused communication appears in A10, B05, C04, E03, G03; peer review appears in A07, B03, F03; satisfaction evaluation in E01, F02; go/no-go in A08, B04). Treat them as **named patterns** rather than one-off activities — see the dedicated cards:

- [Peer review and go/no-go gates](04-peer-review-and-go-no-go.md)
- [Focused communication](05-focused-communication.md)

## When this applies

- New project on P3.express — use this map as the master cadence
- Coaching teams away from "ad-hoc" project rhythms toward defined cycles
- Mapping P3.express to a more verbose methodology (PRINCE2 stage equivalents, PMBOK phases)

## Anti-patterns

- Skipping **B-group** because "we already planned" — Monthly Initiation re-validates the plan against reality
- Treating **D02** (Accept completed deliverables) as paperwork — it's the formal close-the-loop on individual outputs
- Running C+D continuously but **never** doing E (Monthly Closure) — improvement loop is never triggered
- Going straight from F to next project without G — benefits never evaluated; lessons lost

## Cross-refs

- [P3.express overview (UtS-derived)](../methodologies/p3-express.md)
- [Roles](02-roles.md) · [Artifacts](03-artifacts.md)
- NUPP §6 [Use repeatable elements](../principles/nupp/06-repeatable-elements.md) — cadence as repeatable element
- PMBOK 7 §7 [Tailor based on context](../principles/pmbok-7/07-tailor.md) — gradual tailoring stance

## Source

Full text: [`docs/sources/p3-express/index.md`](../../sources/p3-express/index.md) and per-activity files under `docs/sources/p3-express/[01-07]-*-/`.
