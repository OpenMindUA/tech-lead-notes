---
title: Roles and accountabilities across frameworks
type: synthesis
license: CC-BY-SA-4.0
sources_combined: [underneath-the-surface, scrum-guide, scrum-guide-expanded, dora-metrics-jira]
tags: [synthesis, roles, accountabilities, sponsor, executive, product-owner, scrum-master, tech-lead]
---

# Roles and accountabilities across frameworks

**TL;DR:** Same project responsibilities are split across **wildly
different role names** across frameworks. The mapping table below
collapses the noise. Three universal patterns: a **business
authority** (Sponsor/Executive/PO), a **delivery facilitator**
(PM/Scrum Master), and **delivery talent** (Team Manager/Developer/
Product Developer). DORA adds a **Tech Lead** layer for
discipline + metrics oversight.

## Cross-framework role map

| Function | UtS / PRINCE2 | UtS / DSDM | UtS / P3.express | Scrum 2020 | SGE | DORA |
|---|---|---|---|---|---|---|
| **Senior business authority** | Executive (Project Board) | Business Sponsor | Sponsor | (implicit, above PO) | (implicit) | (org level) |
| **User-side rep on board** | Senior User | Business Visionary / Business Ambassador | (via stakeholders) | — | Stakeholder subtype | — |
| **Supplier-side rep on board** | Senior Supplier | Technical Coordinator | (Supplier PMs) | — | Stakeholder subtype | — |
| **Day-to-day project authority** | Project Manager | Project Manager | Project Manager | (decentralized) | (decentralized) | Tech Lead (effective PM role for delivery discipline) |
| **Product/value authority** | Senior User+Executive (combined) | Business Visionary | (PM + sponsor) | **Product Owner** | **Product Owner** (must be human) | (PO equivalent) |
| **Methodology coach** | (informal) | **DSDM Coach** | (informal) | **Scrum Master** | **Scrum Master** (must be human, change agent) | (often Tech Lead) |
| **Delivery role(s)** | Team Manager(s) + workers | Solution Developer / Tester | Team Leaders / workers | **Developers** | **Product Developer** (human or AI; ≥1 human) | Developers / SREs |
| **Stakeholder (external)** | implicit | various | Stakeholder | implicit (via PO) | **Stakeholder (4th role)** + **Supporter** subtype | various |

## Three universal accountability patterns

### Pattern A — Business authority
Always one person (or small group). Owns **why** and **value**.

- PRINCE2 Executive — final decision on Business Case
- DSDM Business Sponsor — justification + budget
- P3.express Sponsor — high-level decisions + resources
- Scrum / SGE Product Owner — value, Backlog ordering (one person,
  not a committee, must be human in SGE)

Common rule: **single person, not a committee.** SGE goes further:
**must be human** (cannot be AI).

### Pattern B — Delivery facilitator
Removes obstacles, coaches the team, doesn't dictate technical
decisions.

- UtS PMBOK 7 §1 — PM as facilitator / steward / chief project
  facilitator
- PRINCE2 / DSDM Project Manager
- P3.express Project Manager
- Scrum / SGE Scrum Master (servant leader; **change agent at all
  org levels** in SGE)
- DORA Tech Lead — workflow oversight, decomposition, metrics review

Common rule: **don't be a boss**; remove impediments; coach.

### Pattern C — Delivery talent
Cross-functional team that creates the Increment / output.

- PRINCE2 Team Managers + workers
- DSDM Solution Developer / Tester
- P3.express Team Leaders + workers
- Scrum **Developers** (inclusive — programmers, researchers, etc.)
- SGE **Product Developer** (may be human or automated; ≥1 human;
  champions of technical quality, discovery, delivery, value
  validation)
- DORA Developers + SREs

Common rule: **cross-functional, self-managing, accountable for
quality.**

## Where DORA Tech Lead fits

DORA's Tech Lead **isn't** a separate role on a Scrum Team — but in
a DORA-disciplined org with Scrum, Tech Lead duties are typically
performed by:
- Decomposition (1-3 day items) → Scrum Team in refinement /
  Product Owner / Scrum Master
- Workflow oversight (no activity, stuck PRs) → Scrum Master
  (effectiveness accountability)
- Metrics review at retro → whole Scrum Team
- Outlier handling (don't blame; ask system questions) → Scrum
  Master + Product Owner

In a non-Scrum context (e.g. Kanban + DORA), Tech Lead is a real
named role with all of the above on one person.

## Roles that often confuse

- **Project Manager**: name reused across frameworks for very
  different scopes. PRINCE2 PM has Board above + Team Managers
  below; P3.express PM is more direct. **Always check actual
  responsibilities + authorities, not the title.** (UtS Performance
  domain Team)
- **Stakeholder**: SG2020 mentions but doesn't define. SGE
  promotes to a 4th role with subtypes.
- **Supporter**: SGE-only. A Stakeholder subtype that is a
  **change agent** for the Scrum adoption.
- **AI / Artificial Intelligence**: SGE-only as Product Developer
  with **human-in-the-loop** mandate.

## Self-management vs external management

Three positions exist:

| Position | Who holds it |
|---|---|
| **Centralized PM** (dedicated PM team) | UtS Performance domain Team / DSDM / PRINCE2 |
| **Decentralized PM** (no dedicated PM; activities distributed) | Scrum / Scrum derivatives |
| **Self-managing within bounded autonomy** | SGE explicit theory; ≈ Scrum + bounded by events / accountabilities / artifacts / commitments / pillars / values / org needs |

> "Project management always exists" — even when there's no Project
> Manager role. (UtS)

## Anti-patterns (universal)

- **Adding a Project Manager on top of Scrum's three accountabilities**
- **Committee Product Owner / Scrum Master**
- **AI Product Owner or AI Scrum Master** (SGE: must be human)
- **Domain SME promoted to PO** without product mgmt skills (often
  better as Product Developer)
- **Scrum Master as administrator / scribe / taskmaster**
  (SGE explicit list of behaviors NOT to be)
- **Single Project Manager doing 100% of tailoring** — system
  design is a separate skill (DSDM Coach exists for this reason)
- **Title-based assumptions** — always check actual authorities

## When this synthesis applies

- Designing org structure around a multi-framework adoption
- Hiring or coaching people into roles
- Resolving "who decides X?" disputes
- Migrating from PRINCE2 / DSDM / classical PM into Scrum + DORA
- Job description drafting and competency frameworks

## Cross-refs

- UtS Performance domain: [Team](../performance-domains/02-team.md)
- PMBOK 7: [Stewardship](../principles/pmbok-7/01-stewardship.md) ·
  [Leadership](../principles/pmbok-7/06-leadership.md)
- Scrum 2020: [Scrum Team](../scrum-guide/04-scrum-team.md) ·
  [Developers](../scrum-guide/05-developers.md) ·
  [Product Owner](../scrum-guide/06-product-owner.md) ·
  [Scrum Master](../scrum-guide/07-scrum-master.md)
- SGE: [Stakeholder](../scrum-guide-expanded/04-stakeholder.md) ·
  [Supporter](../scrum-guide-expanded/05-supporter.md) ·
  [AI](../scrum-guide-expanded/06-artificial-intelligence.md) ·
  [Product Developer](../scrum-guide-expanded/07-product-developer.md) ·
  [PO extensions](../scrum-guide-expanded/08-product-owner.md) ·
  [SM extensions](../scrum-guide-expanded/09-scrum-master.md)
- DORA: [Ticket discipline (Tech Lead rules)](../dora-metrics-jira/02-ticket-discipline.md)
- Methodology cards (role lists per method): [P3.express](../methodologies/p3-express.md) ·
  [PRINCE2](../methodologies/prince2.md) · [DSDM](../methodologies/dsdm.md)
