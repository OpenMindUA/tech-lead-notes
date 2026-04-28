---
title: P3.express artifacts (4 documents)
type: artifacts
framework: P3.express
source: docs/sources/p3-express/index.md
source_url: https://p3.express/manual/v2/
license: CC-BY-4.0
authors_of_source: PTCoE — Nader K. Rad et al.
tags: [p3-express, artifacts, project-description, deliverables-map, follow-up-register, health-register, custodian]
---

# P3.express artifacts (4 documents)

**TL;DR:** Just **four** documents. Combined Follow-Up Register collapses what other methodologies split into 3-5 logs. Every deliverable and every follow-up item gets a **custodian** — a named person responsible until closure.

## The four artifacts

### 1. Project Description

- The high-level "what + why" of the project.
- Stable across the project — revised at **B02** when needed.
- [Template](https://p3.express/manual/v2/project-description.odt) (.odt).
- Authored from **your perspective** (see [Roles](02-roles.md) — perspective rule).

### 2. Deliverables Map

- **Hierarchical breakdown** of the building elements of the product.
- Free format — mind map, tree, list. **Not prescribed.**
- Optional dependency or priority annotations:
    - **Many dependencies** → schedule by network of dependencies
    - **Few dependencies** → priority-based ordering with improvisation
    - **Hybrid** common: dependency-based at higher levels, priority-based at lower levels
- Built and refined in workshops (A05).
- Use **noun phrases**, not verb phrases — the focus is on *deliverables*, not *work*.

### 3. Follow-Up Register

- **Single combined register** for **5 item types**:
    - Risks
    - Issues
    - Change requests
    - Improvement plans
    - Lessons learned
- [Spreadsheet template](https://p3.express/manual/v2/follow-up-register.ods) (.ods).
- Items **morph** as time passes (a future risk that occurs becomes an issue; closed → lesson).
- Updated daily (D01).
- Each item has a **custodian** (see below).

### 4. Health Register

- Stores results of **peer reviews** and **stakeholder satisfaction evaluations**.
- [Spreadsheet template](https://p3.express/manual/v2/health-register.ods) (.ods).
- Used at A07, B03, F03 (peer review) and E01, F02 (satisfaction).

## The Custodian rule (P3.express-specific)

Every item that needs follow-through has a **named custodian**:

- Each **deliverable** in the Deliverables Map has a custodian.
- Each **follow-up item** in the Follow-Up Register has a custodian.

The custodian:
- Tracks the item until it is **closed**.
- Reports on its status.
- Owns the response actions; can pull in others as needed.

> "Relying on your memory or on unstructured notes takes too much mental energy and runs the risk of forgetting items." — capture immediately + assign custodian.

## When this applies

- Setting up a P3.express project from scratch
- Choosing between separate registers (risks / issues / changes) and a unified one
- Coaching teams off ad-hoc Excel-everywhere into 4 well-known docs
- Tooling decisions (where to host the documents) — the manual recommends Nextcloud, CryptPad, and similar privacy-aware solutions

## Anti-patterns

- **Unified register split** into 5 separate documents "for cleanliness" — defeats the morph-in-place purpose
- Adding **lots of analysis** fields to the Follow-Up Register — keep it light
- **Follow-up items without custodians** — items pile up; nobody owns
- **Generic responses** ("we'll handle it") — must be measurable + actionable
- Storing **only on a single laptop** — capture-friendly access (mobile included) is a critical constraint
- Spending all time on **issues** (firefighting) and ignoring **risks** in the same register

## Cross-refs

- [Cycle and activities](01-cycle-and-activities.md) — when each artifact is touched
- [Peer review and go/no-go gates](04-peer-review-and-go-no-go.md) — Health Register's main consumer
- [Focused communication](05-focused-communication.md) — drives audience-specific reports
- Performance domain: [Project Work](../performance-domains/05-project-work.md) — follow-up items pattern (UtS framing)
- Performance domain: [Uncertainty](../performance-domains/08-uncertainty.md) — sophistication ladder; P3.express's combined register is **rung 1**
- [Synthesis: Risk and stability](../synthesis/05-risk-and-stability.md)

## Source

Full text: [`docs/sources/p3-express/index.md`](../../sources/p3-express/index.md) (Documents section)
and the activities that touch each artifact (A04, A05, A06, D01, A07, etc.).
