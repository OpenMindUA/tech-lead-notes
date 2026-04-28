---
title: DSDM®
type: methodology
license_type: proprietary
source: docs/03-selecting-a-methodology/04-dsdm.md
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [methodology, dsdm, agile, moscow, timeboxed, multi-team]
---

# DSDM®

**TL;DR:** First-generation Agile method designed from scratch for
**large, multi-team IT development**. Structurally inspired by
PRINCE2. Centralized PM, **timeboxed** delivery, **MoSCoW**
prioritization.

- **Owner:** Agile Business Consortium (proprietary).
- **Domain:** IT development.
- **Approach:** adaptive only.
- **Scale:** large, multi-team.

## Roles (selected)

### Project level
- **Business Sponsor** — senior, owns justification and budget.
- **Business Visionary** — interprets business needs project-wide.
- **Project Manager** — day-to-day management.
- **Technical Coordinator** — cross-team technical coordination.

### Solution Development Team level (1+ teams)
- **Team Leader**
- **Business Ambassador** (in touch with Business Visionary)
- **Solution Developer**
- **Solution Tester**

### Support level
- **Technical Advisor** — e.g. security
- **Business Advisor** — e.g. legal/regulatory
- **DSDM Coach** — helps teams use the method (rare and notable —
  most methods leave methodology coaching unassigned; see
  [PMBOK §7 Tailor](../principles/pmbok-7/07-tailor.md))
- **Workshop Facilitator**

Plus a **Business Analyst** spanning project + team levels.

## Process

```
Pre-project        → Terms of Reference         (decision: invest?)
Feasibility        → Feasibility Assessment     (decision: keep going?)
Foundations        → Foundations Summary        (high-level plan; can repeat)
Evolutionary Development cycles → Increment
Deployment (same or lower frequency)
Post-project (benefits evaluation)
```

- **Closure** is implied in deployment; no standalone closure phase.
- **Timeboxed.** Whole project duration is fixed up-front; deliver
  as much as possible inside.
- **Deployment cadence.** Prefer many deployments to enable
  adaptation; balanced against business risk and user disruption.

## MoSCoW prioritization

| Tier | Meaning | Example |
|------|---------|---------|
| **M**ust-have | Without this, product unusable | security in a banking app |
| **S**hould-have | Workaround exists but painful | manual workaround for a missing feature |
| **C**ould-have | Nice-to-have, no problem if absent | dark theme |
| **W**on't-have-this-time | Excluded | … |

Mix rule: **≤60% must-have, ≥20% could-have** for flexibility.

Estimation rule:
- Optimistic case: deliver everything within the timebox.
- Pessimistic case: still deliver all must-have items.

Progress measure = forecast of items completable by end of project.
If forecast says we can't deliver all must-haves → cancel or
fundamentally restructure.

## Strengths

- Multi-team scaling is built-in (PRINCE2-inspired layering)
- MoSCoW + timebox combo guarantees a usable delivery
- Dedicated DSDM Coach role addresses the missing tailoring skill
  problem the author flags in PMBOK 7 §7
- Robust governance (Sponsor / Visionary) compared to Scrum

## Anti-patterns

- "Agile means no PM" — DSDM has a PM
- Skipping Foundations because "we want to start coding"
- Ignoring MoSCoW ratios (75% must-have → no flexibility)
- Treating timebox as a wish rather than a hard boundary

## Cross-refs

- [Scrum](scrum.md) — alternative for small teams
- [PRINCE2](prince2.md) — DSDM is structurally inspired by it
- PMBOK 7 §11 [Adaptability](../principles/pmbok-7/11-adaptability.md)
- PMBOK 7 §7 [Tailor based on context](../principles/pmbok-7/07-tailor.md) (DSDM Coach)
- Performance domain: [Delivery](../performance-domains/07-delivery.md)
  (incremental delivery, requirements/deliverables/activities)

## Source

Full text: [`docs/03-…/04-dsdm.md`](../../sources/underneath-the-surface/03-selecting-a-methodology/04-dsdm.md)
