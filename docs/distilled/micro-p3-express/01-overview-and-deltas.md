---
title: micro.P3.express overview and deltas vs P3.express
type: methodology-overview
framework: micro.P3.express
source: docs/sources/micro-p3-express/index.md
source_url: https://micro.p3.express/
license: CC-BY-4.0
authors_of_source: PTCoE — Nader K. Rad et al.
tags: [micro-p3-express, overview, scale, deltas, weekly-cycle]
---

# micro.P3.express overview and deltas vs P3.express

**TL;DR:** Designed for **1-7 team members**. Replaces P3.express's monthly cycle with a **weekly-only** cadence. Replaces named roles with **hats** that one person can swap. Tooling/repository setup is explicit (A3). Use it for tiny teams; if you scale beyond 7, switch to P3.express.

## When to use micro.P3.express vs P3.express

| Use micro.P3.express when... | Use P3.express when... |
|---|---|
| Team is **1-7 people** | Team is small / medium / large (8+) |
| Project is short or seasonally part-time | Project is long-running with stable team |
| You want minimal upfront tooling | Org already has standard tooling/PMO |

For **stretched micro-projects** that span a long time at low utilization, the manual recommends replacing the weekly cycle with a **monthly cycle** (effectively walking back toward full P3.express).

## Activity map (6 groups, 27 activities)

```
A — Project Initiation     (7 activities, A1..A7)
C — Weekly Initiation      (4, C1..C4)         ← weekly only; no Monthly
D — Daily Management       (2, D1..D2)
E — Weekly Closure         (4, E1..E4)
F — Project Closure        (7, F1..F7)
G — Post-Project Mgmt      (3, G1..G3)
```

> Note: there is **no Group B**. P3.express's Monthly cycle (B + E) collapses into micro's Weekly cycle (C + E).

### Project Initiation (A1-A7)

| Code | Activity |
|---|---|
| A1 | Identify the high-level decision maker(s) |
| **A2** | **Understand and distribute the hats** *(replaces P3's role appointments)* |
| **A3** | **Select tools and create a project repository** *(new vs P3.express)* |
| A4 | Create a common understanding |
| A5 | Have Project Initiation peer-reviewed |
| A6 | Make a go/no-go decision |
| A7 | Conduct a focused communication |

### Weekly Initiation (C1-C4)

C1 Revise common understanding · C2 Peer review · C3 Go/no-go · C4 Focused comm

### Daily Management (D1-D2)

D1 Manage follow-up items · D2 Close completed deliverables

### Weekly Closure (E1-E4)

E1 Performance · E2 Satisfaction · E3 Lessons + improvements · **E4 Consider swapping hats for the week** *(unique to micro)*

### Project Closure (F1-F7)

F1 Hand over · F2 Satisfaction · F3 Peer review · **F4 Consider swapping hats for Post-Project Management** · F5 Archive · F6 Celebrate · F7 Focused comm

### Post-Project Management (G1-G3)

G1 Benefits · G2 New ideas · G3 Focused comm

## Key deltas vs P3.express

| Aspect | P3.express | micro.P3.express |
|---|---|---|
| Team size | small / medium / large | 1-7 |
| Roles | Sponsor + PM + Team Leaders + Supplier PMs | **4 hats** (PM, Investor, Creator, User) — see [Hats card](02-hats-not-roles.md) |
| Cycles | Monthly (B+E) + Weekly (C) + Daily (D) | Weekly (C+E) + Daily (D) only |
| Group B | exists (Monthly Initiation, 5 activities) | **absent** |
| Tooling activity | implicit | **explicit** (A3) |
| Hat-swap activities | n/a | **E4** + **F4** |
| Total activities | 33 | 27 |

## When this applies

- Solo founder + 1-2 helpers building something
- Small in-house tool with a tiny team
- Stretched part-time project — start with micro, switch to monthly cycle if it lasts
- Coaching tiny teams that find P3.express too heavy

## Anti-patterns

- Using micro for a **10+ person** team — wears thin; switch to P3.express
- Skipping **A3** ("we'll figure out the tools later") — friction kills capture discipline
- **Same person wears all 4 hats forever** without ever rotating (E4/F4) — entrenches one perspective; defeats the hat-rotation purpose
- Skipping the weekly cycle as "too formal for our small team" — kills the inspect-and-adapt rhythm

## Cross-refs

- [P3.express distilled](../p3-express/index.md) — the full version
- [P3.express cycle and activities](../p3-express/01-cycle-and-activities.md) — for comparison
- [Hats, not roles](02-hats-not-roles.md)
- NUPP §2 [Preserve and optimize energy](../principles/nupp/02-preserve-energy.md) — spirit of "minimal upfront overhead"
- PMBOK 7 §7 [Tailor based on context](../principles/pmbok-7/07-tailor.md) — tailoring across project sizes

## Source

Full text: [`docs/sources/micro-p3-express/index.md`](../../sources/micro-p3-express/index.md) and per-activity files under `docs/sources/micro-p3-express/[01-06]-*-/`.
