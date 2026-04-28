---
title: Development approach and life cycle (performance domain)
type: performance-domain
domain_number: 3
source: docs/04-enriching-the-methodology/03-development-approach-and-life-cycle.md
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [performance-domain, predictive, adaptive, agile, hybrid, life-cycle]
---

# Development approach and life cycle — performance domain

**TL;DR:** Predictive vs adaptive is decided by the **product**, not
by team preference. "Hybrid" is mostly a misnomer; only valid form
is **multiple parallel projects** with different approaches per
independent product part. Match the **PM life cycle** to the
chosen development approach.

## Development approach

### Predictive
- Specify, design, build the whole output up-front.
- Right when the output is fully knowable (Mars rover, bridge,
  data-center upgrade, hospital-equipment software).

### Adaptive (Agile)
- Build subsets, expose to end users, collect real feedback,
  decide next step.
- Right when output value depends on user reaction (most consumer
  software).
- Requires usable **increments** so feedback is meaningful (abstract
  half-deliverables don't count).

### Selection rule
- **Driven by the product, not preferences.** Team / org / customer
  preference does not justify the choice.
- Diagnostic: can you specify, design, and build subsets *without*
  the rest? If no → predictive. (Foundation depends on full design;
  bridge cannot be built incrementally.)
- Not every IT project is adaptive. Predictive when no human
  perception involved or no room for trial-and-error (avionics,
  Mars rover, hospital firmware).

### "Hybrid" — caveat
- The author argues hybrid approaches don't really exist within a
  single project: any predictive subset blocks adaptation of the
  whole.
- The only valid mixing is **product decomposition into independent
  parts** delivered as separate projects, each pure-approach. That
  is a *program*, not a hybrid project.
- "Hybrid" labels often arise from cargo-cult mixing of
  surface-level practices (PMBOK 7 still includes the term despite
  the author's objection).

## Project life cycle

- The PM **life cycle** must match the development approach.
    - **Cyclic** PM life cycle works for both adaptive and (more
      or less) linear predictive development.
    - **Linear** PM life cycle works only for predictive.
- Some methods support both approaches (P3.express); some support
  only adaptive (DSDM). Pick a methodology that matches the
  development approach.

## Product life cycle

- The project life cycle is a *subset* of the product life cycle.
- Project decisions must consider the product's wider context
  (e.g. spend €50k more for €2k/month operating-cost savings →
  decision belongs at customer-org level, but project should
  surface the option).

## When this domain matters more

- Choosing a methodology for a new project
- Resisting fashion-driven Agile rollouts on inappropriate projects
- Composing programs that span both predictive and adaptive parts

## Anti-patterns

- "Agile by default" / "Predictive by default" without product analysis
- Team / org preference as decision driver
- Calling a mix of practices "hybrid" without examining dynamics
- Using adaptive without true incremental delivery
- Mismatched PM life cycle vs development approach

## Cross-refs

- PMBOK 7 §11 [Adaptability](../principles/pmbok-7/11-adaptability.md)
- PMBOK 7 §7 [Tailor based on context](../principles/pmbok-7/07-tailor.md)
- Methodology selection: [Methodologies](../methodologies/index.md)

## Source

Full text: [`docs/04-…/03-development-approach-and-life-cycle.md`](../../sources/underneath-the-surface/04-enriching-the-methodology/03-development-approach-and-life-cycle.md)
