---
title: Uncertainty (performance domain)
type: performance-domain
domain_number: 8
source: docs/04-enriching-the-methodology/08-uncertainty.md
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [performance-domain, risk, uncertainty, monte-carlo, register, portfolio]
---

# Uncertainty — performance domain

**TL;DR:** Risk management is the dominant topic. Choose the
sophistication that matches the project; default to simpler.
Sensitive risks belong at the **portfolio** level, not project.

## Sophistication ladder (pick the lowest that suffices)

1. **Single combined register (P3.express *follow-up register*).**
   Risks + issues + change requests + improvement plans + lessons
   learned in one place.
   - Reasons:
     - one process covers all of them
     - items morph: a risk that occurs becomes an issue, then a
       lesson learned when closed
2. **Separate risk register (PRINCE2, many).** Spreadsheet with
   risk analysis and planned responses.
3. **Two tables — risks ↔ responses with many-to-many.** A response
   may cover several risks; a risk may need several responses.
4. **Cause / effect split.** A cause produces multiple effects;
   risks have multiple causes.
5. **Graph model.** Move from tables to a graph for the most
   complex / mega-projects.

**Default:** when in doubt, pick the simpler one.

## Quantitative analysis

- Responses must be cost-justified. Insurance €1k/month vs
  millions-of-euro damage is justifiable; vs €2k damage, not.
- Most projects can judge justification intuitively or ad-hoc.
- For sensitive projects, use **Monte Carlo** to compute
  probabilistic outputs before/after responses.
    - Example: P(finish ≤ 22 months) is 85% baseline; spending €80k
      on responses raises it to 98%. Decide if worth it.
- Quantitative analysis is resource-heavy — confirm need before
  adopting.

## Higher management levels

- **Some risks span multiple projects.** They should be managed
  centrally, not duplicated in every project.
- Portfolio management should:
    - maintain an org-wide risk list with responses, available to
      all projects
    - regularly review project-level risks to spot cross-project
      ones and lift them to the portfolio layer
- If your org has no portfolio management:
    - The book is blunt: *implement portfolio management.* No
      shortcut.
    - Practical workaround until then: PMs across projects meet
      monthly to share lessons and high-level risks.
- Distinction: project management = *doing things right*;
  portfolio management = *doing the right things*.

## When this domain matters more

- High-uncertainty, high-impact projects
- Multi-project orgs with cross-cutting risk exposure
- Regulatory/safety-critical contexts (health, aerospace,
  construction)

## Anti-patterns

- Multiple separate registers in a small project (over-engineered)
- Single combined register in a mega-project (under-engineered)
- Monte Carlo simulations on routine projects (waste)
- Each project rediscovering the same org-wide risks
- Risk register set up at kickoff, never reviewed
- Continuing without portfolio management indefinitely

## Cross-refs

- PMBOK 7 §9 [Optimize risk responses](../principles/pmbok-7/09-risk.md)
- PMBOK 7 §5 [System interactions](../principles/pmbok-7/05-system-interactions.md)
- NUPP §3 [Always be proactive](../principles/nupp/03-always-be-proactive.md)
- Performance domain: [Project Work](05-project-work.md) (follow-up register)

## Source

Full text: [`docs/04-…/08-uncertainty.md`](../../sources/underneath-the-surface/04-enriching-the-methodology/08-uncertainty.md)
