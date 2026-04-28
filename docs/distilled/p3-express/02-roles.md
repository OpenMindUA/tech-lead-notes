---
title: P3.express roles
type: roles
framework: P3.express
source: docs/sources/p3-express/index.md
source_url: https://p3.express/manual/v2/
license: CC-BY-4.0
authors_of_source: PTCoE — Nader K. Rad et al.
tags: [p3-express, roles, sponsor, project-manager, team-leader, supplier]
---

# P3.express roles

**TL;DR:** Five named roles span two layers: **management team** (Sponsor + Project Manager + Customer PM if external) and **production teams** (Team Leader for internal, Supplier PM for external). The **perspective rule** — "you are *your* PM, but the customer's *supplier PM* and the supplier's *customer PM*" — is unique to P3.express.

## Role hierarchy

```
                ┌─────────────┐
                │   Sponsor   │  senior internal manager (preferably board member)
                └──────┬──────┘
                       │ reports to
                ┌──────┴──────────────┬─────────────────────────┐
                │  Project Manager    │  Customer Project Mgr   │ (if external customer)
                │  (your PM)          │  (their representative) │
                └──────┬──────────────┴─────────────────────────┘
                       │
            ┌──────────┴──────────────┐
            │                          │
    ┌───────┴────────┐       ┌────────┴────────────┐
    │ Team Leader(s) │       │ Supplier PM(s)      │
    │ (internal)     │       │ (external suppliers)│
    └───────┬────────┘       └────────┬────────────┘
            │                          │
       Production team           Production team
       (your org)               (supplier org)
```

## Role definitions

### Sponsor (A01)

- **Senior manager**, preferably a board member.
- **Highest** role in the project; PM reports to the sponsor.
- Accountable for **justification and outcome**; responsible for **funding** + **resourcing** + **high-level decisions**.
- Doesn't need to spend a lot of time, but **needs to be involved**.
- **Should not also be the PM** of the same project (unless single-person project).
- **Avoid** the same person sponsoring all projects (constants fade).
- Should be ready to **cancel the project** if it loses justification — protective ownership without sunk-cost bias.

### Project Manager (A02)

- Leads the **management team**.
- Accountable for project management activities.
- **Reports to** the sponsor *and* the customer's PM if there's an external customer.
- **Should not micro-manage**; same applies to the sponsor.

### Key team members (A03)

- Brought in by the PM at initiation.
- Includes **team leaders** (internal) and any **supplier project managers** (external).

### Team Leader (internal production teams)

- Leads an internal production team.
- Reports to **functional manager** (if any) and to the **PM**.

### Supplier Project Manager (external production teams)

- Leads a supplier's team.
- Reports to **internal supplier managers** and to the **PM** of the project.

## The perspective rule

> "Each organization involved in the project will have its own perspective. Everything in P3.express should be seen from **your perspective**."

Implications:

- Project Description's *justification* = **your** justification, not the customer's.
- Documents are kept **per-perspective**, not shared between organizations.
- Same person is your "Project Manager", but to the customer they are your "Supplier PM"; to your suppliers they are the "Customer PM".

P3.express **is not a single shared system** — it's a system **you** use within your organization's boundaries.

## When this applies

- Setting up a new P3.express project structure
- Multi-organization projects (you ↔ customer ↔ suppliers)
- Resolving "who reports to whom?" in the management team
- Evaluating whether the right people are in the right roles

## Anti-patterns

- Same person as **sponsor and PM** in a multi-person project — abstract sponsorship duties get drowned by day-to-day PM work
- Sponsor as a **rubber-stamp** rather than active participant
- Sponsor unable to **cancel** a project because of personal/political investment
- One sponsor for **all** projects in the org (the stewardship anti-pattern shifted up)
- Treating P3.express as a **shared methodology** between you and the customer — perspective rule says no
- Micromanagement by sponsor or PM
- PM with **no clear reporting relationship** to a sponsor

## Cross-refs

- PMBOK 7 §1 [Stewardship](../principles/pmbok-7/01-stewardship.md) — sponsor + PM as stewards
- PMBOK 7 §6 [Leadership behaviors](../principles/pmbok-7/06-leadership.md)
- Performance domain: [Team](../performance-domains/02-team.md) — sponsor/executive equivalents across frameworks
- [Synthesis: Roles across frameworks](../synthesis/07-roles-across-frameworks.md) — full mapping table
- micro.P3.express variant: [Hats, not roles](../micro-p3-express/02-hats-not-roles.md)

## Source

Full text: [`docs/sources/p3-express/index.md`](../../sources/p3-express/index.md) (Organization section)
and [`A01..A03`](../../sources/p3-express/01-a-project-initiation/index.md) activities.
