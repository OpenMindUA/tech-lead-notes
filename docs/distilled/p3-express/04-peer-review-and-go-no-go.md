---
title: Peer review and go/no-go gates
type: pattern
framework: P3.express
source: docs/sources/p3-express/01-a-project-initiation/07-peer-review-project-initiation.md
source_url: https://p3.express/manual/v2/a/07/
license: CC-BY-4.0
authors_of_source: PTCoE — Nader K. Rad et al.
tags: [p3-express, peer-review, go-no-go, gate, quality, justification]
---

# Peer review and go/no-go gates

**TL;DR:** P3.express formalizes **two recurring patterns**: an **external peer review** of the management work (A07, B03, F03) and a **go/no-go decision** by the sponsor at each major boundary (A08, B04). They are deliberately distinct: peer review = *quality* of management; go/no-go = *justification* of the project.

## Peer review pattern

> Activities: **A07** (after Project Initiation), **B03** (every Monthly Initiation), **F03** (at Project Closure).

### How

1. The PM asks **another project manager in the same organization** to review the management activities done so far.
2. The reviewer looks at the artifacts (Project Description, Deliverables Map, Follow-Up Register, Health Register) and the activities that produced them.
3. The result — typically a score plus comments — goes into the **[Health Register](03-artifacts.md#4-health-register)**.

### Purpose

- An external eye catches issues the PM is too close to see.
- **Both parties learn** — the reviewer also benefits from seeing other projects.
- Builds a culture of **mutual coaching** between PMs in the same org.

### Common pitfalls

- Reviewer **hesitates to point out problems** (afraid of taking it personally) → trust + relationship matters; PM has to actively make it safe.
- Different reviewer each time is preferred — diversity of perspective.

### Cross-framework parallel

- **Scrum**: continuous through the team's own retrospectives + cross-team coaching by Scrum Masters.
- **PRINCE2**: formal stage-end reports + Project Assurance role.
- **Quality from the inside vs from the outside** — P3.express picks "outside, but still inside the org".

## Go/no-go decision pattern

> Activities: **A08** (after project initiation), **B04** (every Monthly Initiation).

### How

After project initiation (A08) and every monthly initiation (B04), the PM presents updated information to the **sponsor**, who decides:

- **Go** — proceed (next month / first execution).
- **No-go** — cancel the project.

### Why a recurring decision (not just at start)

- The justification can change. PRINCE2's [Continued Business Justification](../principles/prince2/01-continued-business-justification.md) principle is the broader pattern.
- Each Monthly Initiation refreshes the plan; a refreshed plan deserves a refreshed go/no-go.
- Counters the **sunk cost fallacy** — explicit gate creates a moment to reconsider.

### Why the sponsor decides

- The PM is too close (cognitive bias risk).
- The sponsor has **organizational power + strategy alignment** the PM doesn't.
- See [Roles → Sponsor](02-roles.md).

## Two-step gate at start (and at each month)

```
A07 / B03  →  Peer review of management work       (Health Register)
   │
   ▼
A08 / B04  →  Sponsor go/no-go decision             (kill or proceed)
   │
   ▼
A09 / continue execution
```

The peer review's **input** flows into the go/no-go: a low health score should make the sponsor more cautious about approving.

## When this applies

- Setting up the initial cadence of a P3.express project
- Coaching sponsors who confuse "approval" with "rubber-stamp"
- Deciding when to cancel a project that has lost justification
- Designing PMO support for cross-PM peer reviews

## Anti-patterns

- **No peer review** — the management quality goes unchecked
- **Same reviewer every time** — perspective collapses into one viewpoint
- **Peer review = formal critique** without the relationship that makes feedback safe
- **Go/no-go = rubber-stamp** by sponsor — defeats the gate's purpose
- **Health Register score ignored** when making go/no-go
- Scoring **never re-checked at F03** — closure should also be peer-reviewed

## Cross-refs

- [Cycle and activities](01-cycle-and-activities.md) — full code map
- [Artifacts → Health Register](03-artifacts.md#4-health-register)
- PRINCE2 §1 [Continued business justification](../principles/prince2/01-continued-business-justification.md) — same idea, different name
- PMBOK 7 §8 [Build quality in](../principles/pmbok-7/08-quality.md) — peer review = quality of the management system
- PMBOK 7 §4 [Focus on value](../principles/pmbok-7/04-focus-on-value.md) — go/no-go = re-evaluate value
- [Synthesis: "Done", quality, peer review](../synthesis/01-done-and-quality.md)

## Source

Full text: [`docs/sources/p3-express/01-a-project-initiation/07-peer-review-project-initiation.md`](../../sources/p3-express/01-a-project-initiation/07-peer-review-project-initiation.md) ·
[`A08`](../../sources/p3-express/01-a-project-initiation/08-make-a-go-no-go-decision.md) ·
[`B03`](../../sources/p3-express/02-b-monthly-initiation/03-have-monthly-initiation-peer-reviewed.md) ·
[`B04`](../../sources/p3-express/02-b-monthly-initiation/04-make-a-go-no-go-decision.md) ·
[`F03`](../../sources/p3-express/06-f-project-closure/03-have-project-closure-peer-reviewed.md)
