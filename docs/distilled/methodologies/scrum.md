---
title: Scrum
type: methodology
license_type: open
source: docs/03-selecting-a-methodology/03-scrum.md
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [methodology, scrum, agile, sprint, decentralized, framework]
---

# Scrum

**TL;DR:** First-generation Agile **framework** for IT development,
single team ≤10 people. Decentralized PM (no PM role). Covers a
**subset** of project management — no initiation, no closure.
Lightweight; very heavy tailoring is required outside its niche.

- **Self-label:** *framework* (not "methodology" — Agile-community
  taboo on the word).
- **License:** open / non-proprietary.
- **Domain:** IT development.
- **Approach:** adaptive only.
- **Adding new roles** (especially a PM) breaks Scrum's design.

## Roles (3)

- **Scrum Master** — guards proper use of Scrum, facilitates,
  unblocks. Focuses on *context*, not content.
- **Product Owner** — single business-side hub; orders the
  Product Backlog by value.
- **Developers** — anyone doing technical work (programmers,
  DBAs, designers, architects, …); also contribute to PM.

PM is **decentralized** — distributed across the three roles.

## Process

```
Initial Product Backlog (Product Owner)
Sprint cycle (fixed duration ≤ 1 month):
  Sprint Planning (≤ 8 h)            → Sprint Backlog + Sprint Goal
  Working + Daily Scrum (15 min)     → Increment
  Sprint Review (≤ 4 h)              → feedback collection
  Sprint Retrospective (≤ 3 h)       → improvement decisions
```

- **No initiation, no closure.** Considered an issue by some, a
  feature by others; reflects subset coverage.
- **Sprint = fixed duration.** Ends on time even if items unfinished;
  unfinished items return to the Product Backlog.
- **Definition of Done.** Items must be 100% complete; otherwise
  return to backlog. Required for reliable feedback.
- **Sprint Review** is one feedback channel — not enough alone for
  true adaptation. Real users (or representatives) need the
  Increment too.

## Artifacts

- **Product Backlog** — value-ordered list, evolves throughout.
- **Sprint Backlog** — items selected for the current Sprint +
  Sprint Goal.
- **Increment** — usable output from the Sprint.

## Strengths

- Simple, low-overhead PM layer for small Agile teams
- Strong feedback rhythm (per-sprint review + retrospective)
- Decentralized PM removes a role and bottleneck
- Definition of Done forces real completion

## Anti-patterns

- Adding a Project Manager to a Scrum team (breaks the model)
- Scaling Scrum to large/multi-team projects via heavy tailoring
  (use a method designed for that scale: DSDM, PRINCE2)
- Using Scrum on non-IT or strictly predictive projects
- Treating Sprint Review as the only feedback loop
- Velocity-as-target (see [Measurement](../performance-domains/06-measurement.md))

## Cross-refs

- [DSDM](dsdm.md) — alternative for large adaptive projects
- PMBOK 7 §11 [Adaptability](../principles/pmbok-7/11-adaptability.md)
- Performance domain: [Team](../performance-domains/02-team.md)
  (decentralized PM debate)

## Source

Full text: [`docs/03-…/03-scrum.md`](../../sources/underneath-the-surface/03-selecting-a-methodology/03-scrum.md)
