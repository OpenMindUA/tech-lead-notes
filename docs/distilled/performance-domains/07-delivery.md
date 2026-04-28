---
title: Delivery (performance domain)
type: performance-domain
domain_number: 7
source: docs/04-enriching-the-methodology/07-delivery.md
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [performance-domain, delivery, requirements, wbs, pbs, user-story, definition-of-done, wip]
---

# Delivery — performance domain

**TL;DR:** **Requirements → Deliverables → Activities** is the
correct order in both predictive and adaptive projects. Limit WIP.
Verify each deliverable before delivery; never bet on a
single big-bang final delivery.

## Start with requirements

- Don't jump to the obvious solution. The "elevator is too slow"
  request was solved by adding a mirror — the real requirement was
  *prevent boredom*, not *increase speed*.
- Process: **Requirements → Deliverables → Activities.**
    - Predictive: most requirements identified up-front.
    - Adaptive: requirements identified gradually.
- When a stakeholder requests a *deliverable*, drill into the
  underlying *requirement*; consider alternative solutions.

### User stories (XP origin, common in Agile)

> As a [role], I want [action] so that [reason].

The "so that" reason works as a requirement and surfaces
constraints. Example: "log in as any user without their password"
becomes safer when the *why* (support investigation) is explicit —
"don't allow logging in as high-privilege admins" follows.

If the methodology is thin on requirements analysis, add it
proportionate to project size/complexity.

## Deliverable breakdowns

- Flat lists fail past trivial size.
- Hierarchical breakdowns (named differently per method):
    - **WBS** — *Work Breakdown Structure* (many)
    - **PBS** — *Product Breakdown Structure* (PRINCE2)
    - **Deliverables map** (P3.express)
- Micro-projects can stay flat (micro.P3.express). Larger projects
  benefit hugely from hierarchy. Most Agile methods lack one — add
  one for larger projects.

## When to deliver

- **Predictive:** mostly one final delivery. Some have stage-end
  deliveries when phases produce usable subsets.
- **Adaptive:** continuous delivery of usable **increments** that
  collect feedback. If full release isn't possible, give increments
  to representative users.
- **Increment definition.** A *usable* set of deliverables. All
  increments are deliverable sets, but not all deliverable sets
  are increments. **Adaptive needs incremental delivery** — without
  it, you can't generate useful feedback.

## Delivery risk

Single big-bang delivery is risky in any approach. Even predictive
projects should review deliverables with the customer/end users for
formal or informal approval throughout the project. Adjust the
methodology if it doesn't enforce this.

## Limit work in progress

- From Lean → strongly adopted in Agile, but applies to all projects.
- Optimal parallelism is usually much lower than people assume.
- Spread thin → easy to abandon hard items and start new ones; fix
  it now is usually cheaper than fixing it later.
- **"Finish before starting more."** Encourage this in your
  methodology — combine with informal acceptance gates from PM and
  customer.

## Quality of work (PM verification)

- PM checks completed deliverables for scope and quality
  alignment to requirements.
- PM doesn't need to be the technical expert — they verify against
  *previously defined scope and quality*.
- Defining scope/quality up-front (or just-in-time per
  deliverable):
    - **Product description** (PRINCE2)
    - Comments on the **deliverables map** (P3.express)
    - **User story acceptance criteria** + **Definition of Done**
      (Agile/Scrum)
- Tailor: adjust detail/formality, separate or merge artifacts.

## When this domain matters more

- Long projects without intermediate user contact
- Software products with high uncertainty about user reaction
- Heavy parallel-work cultures (lots of in-flight items)

## Anti-patterns

- Plans starting from activities or deliverables, skipping
  requirements
- Big-bang delivery at end, no intermediate verification
- WBS as a flat list of tasks
- "WIP limits don't apply, we're predictive"
- PM-as-technical-reviewer (instead of verifying against
  pre-agreed criteria)

## Cross-refs

- PRINCE2 §6 [Focus on products](../principles/prince2/06-focus-on-products.md)
- PMBOK 7 §11 [Adaptability](../principles/pmbok-7/11-adaptability.md)
- PMBOK 7 §12 [Enable change](../principles/pmbok-7/12-enable-change.md)
- Performance domain: [Project Work](05-project-work.md)

## Source

Full text: [`docs/04-…/07-delivery.md`](../../sources/underneath-the-surface/04-enriching-the-methodology/07-delivery.md)
