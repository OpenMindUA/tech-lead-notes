---
title: "Done", quality, and peer review across frameworks
type: synthesis
license: CC-BY-SA-4.0
sources_combined: [underneath-the-surface, scrum-guide, scrum-guide-expanded, dora-metrics-jira]
tags: [synthesis, done, definition-of-done, quality, peer-review, dod, doutd, doomd]
---

# "Done", quality, and peer review across frameworks

**TL;DR:** Every framework defines "done" as a **commitment** that
prevents premature closure. They agree on the **principle** (built-in,
not inspected; enforced by visible criteria; evolves over time) but
differ in **what level** the criterion attaches to (item / increment
/ product) and **whether release counts**.

## Mapping

| Framework | Concept | Attached to | Production-gated? |
|---|---|---|---|
| **PMBOK 7** | "Build quality into processes and deliverables" principle | the system + product | implicit |
| **PMBOK 7 / Performance domain Delivery** | Product description (PRINCE2), DoD (Agile/Scrum), comments on deliverables map (P3.express) | per deliverable | up to method |
| **P3.express** | peer review at intervals, custodian per deliverable | system + each deliverable | release implied at closure |
| **Scrum 2020** | **Definition of Done** (commitment of Increment) | Increment | **No** — release is not gated by Sprint Review |
| **Scrum Guide Expansion Pack** | **Definition of Output Done** + Acceptance Criteria + (Outcome Criteria) | Increment + per-PBI + per-PBI optional outcome | No — DoOD weakened during Sprint not allowed; Increments may release pre-Review |
| **SGE** | **Definition of Outcome Done** (Product-level commitment) | the **Product** | "value validation" via observable evidence |
| **DORA in Jira** | DoD must include "code is in production" | per ticket workflow | **Yes** — ticket alive until deployed |

## Quality bars (3 levels in modern Scrum + DORA)

```
Item        →  Acceptance Criteria (per-PBI)        SGE
Increment   →  Definition of Output Done (DoOD)      Scrum / SGE / DORA
Product     →  Definition of Outcome Done (DoOD)     SGE
```

**Don't conflate them.** AC are PBI-specific; DoOD is the shippable
quality bar; Definition of Outcome Done is value validation.

## Common rules across all sources

- **Built-in, not bolted on.** PMBOK 7 §8: prevention over inspection.
  Scrum: DoD must be met before an item can be in the Increment. DORA:
  "without enforcement, DoD degrades within 2-3 sprints."
- **Visible criteria.** All frameworks insist DoD/DoOD must be
  documented and shared — invisible "done" is no done at all.
- **Multi-team coherence.** Scrum/SGE: multiple Scrum Teams on one
  Product **share** the DoOD as a minimum.
- **Continuous improvement.** SGE adds explicit accountability for
  **improving** the DoOD. Scrum 2020 retros also touch DoD. DORA
  recommends quarterly review.
- **Investment must pay back.** PMBOK 7 §8: "untailored quality is
  too expensive" → if quality cost > rework saved, tailoring is wrong.

## Where frameworks diverge

| Question | Scrum 2020 | SGE | DORA |
|---|---|---|---|
| Can an item be "Done" but not released? | **Yes** (Increment can ship later) | **Yes** | **No** ("alive until in production") |
| Quality gate at Sprint Review? | **No** — release decoupled | **No** | n/a |
| Per-item Acceptance Criteria? | not formalized | **explicit** | implied (DoD per ticket) |
| Production-monitoring required? | not specified | implied | **Required** in DoD |

## When this synthesis applies

- Designing a multi-team product's quality stack (Scrum + DORA)
- Resolving "is this done?" disputes — pick the right level
- Migrating from "merged = done" to "deployed = done" (DORA)
- Defining outcome measurement in addition to output completeness

## Anti-patterns (universal)

- One DoD/DoOD across many products that differ in technology
- DoD that survives multiple sprints without retrospective review
- Treating Sprint Review as the **release gate** (Scrum says no)
- "Done" without **production verification** (DORA says no)
- Acceptance Criteria duplicating DoOD instead of adding PBI-specific
  detail
- DoOD met but **no outcome measurement** → output without value

## Cross-refs (per-source cards)

- PMBOK 7: [Build quality in](../principles/pmbok-7/08-quality.md)
- Performance domain: [Delivery](../performance-domains/07-delivery.md)
- Scrum 2020: [Increment + DoD](../scrum-guide/16-increment.md) ·
  [Sprint Review](../scrum-guide/12-sprint-review.md)
- SGE: [Definition of Output Done](../scrum-guide-expanded/12-definition-of-output-done.md) ·
  [Definition of Outcome Done](../scrum-guide-expanded/11-definition-of-outcome-done.md) ·
  [Product Backlog extensions (AC)](../scrum-guide-expanded/13-product-backlog-extensions.md)
- DORA: [Ticket discipline (DoD section)](../dora-metrics-jira/02-ticket-discipline.md) ·
  [Anti-patterns](../dora-metrics-jira/05-anti-patterns.md)
- P3.express peer reviews: [Methodology card](../methodologies/p3-express.md)
