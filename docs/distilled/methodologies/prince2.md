---
title: PRINCE2®
type: methodology
license_type: proprietary
source: docs/03-selecting-a-methodology/02-prince2.md
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [methodology, prince2, maximalist, general-purpose, stages, business-case]
---

# PRINCE2®

**TL;DR:** Sophisticated, **maximalist**, general-purpose, predictive
methodology. Out-of-the-box defaults target large/super-large
projects; **must be tailored** before use. Three management layers,
seven principles, two-stage decision before execution starts.

- **Owner / IP:** AXELOS Limited (proprietary).
- **Tailoring stance:** mandatory upfront; ongoing as well.
- **Approach support:** predictive (adaptive variant exists:
  PRINCE2 Agile®).
- **Principles:** see [PRINCE2 principles distilled](../principles/prince2/index.md).

## Roles (selected)

### Directing layer — Project Board
- **Executive** — business-oriented; final decision-maker; owns
  the outcomes.
- **Senior User(s)** — represents users on the board.
- **Senior Supplier(s)** — represents suppliers/teams on the board.

### Managing layer
- **Project Manager** — day-to-day management; meets time/cost/
  quality/risk/benefit targets.
- **Project Support** — assists the PM.

### Delivering layer
- **Team Manager(s)** — leads internal/external production teams.

**Tailoring rules.** You can split or merge roles. **You may not
merge Project Manager and Executive** — conflict of interest, and
the roles differ in nature.

PRINCE2 manuals attach a responsibility matrix to each activity.

## Processes

```
Starting Up a Project (SU)        ← appoint Executive, PM; create project brief
  → decision: outline business case justifies further investment?
Initiating a Project (IP)         ← detailed initial plan + Project Initiation Documentation (PID)
  → decision: refined business case justifies execution?
Stage cycle:
  Managing a Stage Boundary (SB)  ← detail next stage, refresh business case
  Controlling a Stage (CS)        ← day-to-day management
    Managing Product Delivery (MP)← team-level execution
  + escalate exceptions to Directing a Project (DP)
Closing a Project (CP)            ← when finished or justification lost
```

**Two-step go decision.** Cheap rough study (SU + project brief),
then full study (IP + PID). Reject early if obviously unjustifiable.

**Stage gates.** Before each stage: refresh plan and business case,
Executive decides *continue*.

**Manage by exception.** PM acts within tolerances. Escalations go
to Directing a Project for board decision.

## Artifacts (selected)

- **Project Brief** — outline + outline business case.
- **Project Initiation Documentation (PID)** — comprehensive
  baseline.
- **Business Case** — refreshed at every stage gate.
- **Product Description** — scope/quality criteria per product.

## Strengths

- Strong governance and authority structure
- Continuous business-case re-checking
- Clear separation of layers (direction / management / delivery)
- Mature artifact set, comprehensive responsibilities matrix

## Anti-patterns

- Using it untailored on a small/medium project ("too expensive")
- Merging Executive and PM roles
- Treating PID as a one-time document
- Skipping stage gates "to save time"
- Cherry-picking artifacts without the underlying authority model

## Cross-refs

- [PRINCE2 principles distilled](../principles/prince2/index.md)
- PMBOK 7 §7 [Tailor based on context](../principles/pmbok-7/07-tailor.md)
- Performance domain: [Planning](../performance-domains/04-planning.md) (stages, meta-plans)

## Source

Full text: [`docs/03-…/02-prince2.md`](../../sources/underneath-the-surface/03-selecting-a-methodology/02-prince2.md)
