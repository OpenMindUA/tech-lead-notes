---
title: Output vs Outcome and value validation across frameworks
type: synthesis
license: CC-BY-SA-4.0
sources_combined: [underneath-the-surface, scrum-guide-expanded, dora-metrics-jira]
tags: [synthesis, output, outcome, value, value-validation, definition-of-outcome-done]
---

# Output vs Outcome — value validation across frameworks

**TL;DR:** **Output** = what the project builds. **Outcome** = what
changes in the world for stakeholders. Most failures look like
"successful delivery" while the **outcome doesn't materialize**.
PMBOK 7 introduces the distinction; SGE operationalizes it via the
Definition of Outcome Done; DORA emphasizes velocity-paired-with-
stability metrics; together they form a measurable framework for
"did we actually create value?"

## The distinction

| Term | Definition | Owned by |
|---|---|---|
| **Output** | The thing built (Increment, document-management system) | Scrum Team / Product Developers |
| **Outcome** | The change for users / stakeholders the output enables (efficient document access) | usually program / portfolio level |
| **Impact** | Organizational results from accumulated outcomes (revenue, market share, compliance) | organization / portfolio |
| **Value** | Benefits ÷ cost; benefits-to-cost ratio | portfolio level |

PMBOK 7 §12 frames the project as **change enabler** — its outputs
must produce outcomes via adoption.

SGE separates the artifacts:
- **Increment** is the output (commits to **Definition of Output Done**).
- **Product** delivers outcomes (commits to **Definition of Outcome Done**).

DORA partitions metrics:
- Velocity (Deployment Frequency, Lead Time) tracks **output throughput**.
- Stability (CFR, MTTR) tracks **outcome quality** (did production work?).

## Operationalization patterns

### Definition of Outcome Done (SGE)

> Observable evidence measures (quantitative or qualitative) required
> to demonstrate **realized benefits** — value validation.

Categories:
- **Customer outcomes** — satisfaction, cost reduction, jobs solved
- **User outcomes** — task completion efficiency, feature engagement
- **Product Stakeholder outcomes** — release / learn / pivot times
- **Business impact** — compliance, market share, cost reduction
- **Scrum Team outcomes** — psychological flow, technical debt,
  capacity

> "**Favor direct evidence over circumstantial evidence.**"

Owned by: **Product Owner** (final say); helped by Scrum Master.

### DORA's four metrics as outcome proxies

DORA reads **all four together** because:
- Deploy Frequency + Lead Time alone = velocity vanity
- + CFR + MTTR = velocity grounded in stability

> "DORA tells **what** is happening, not **why**." — outcome-quality
> proxy, not full causation.

### PMBOK 7's prescription

- "**Output ≠ Outcome.**" Don't celebrate output delivery if outcome
  fails to materialize.
- Project still has responsibilities for outcomes:
    1. Understand *why* the project exists.
    2. Align activities to outcome intent.
    3. Provide info up to program/portfolio for outcome management.
- Reframe PM as **change enabler**.

## Universal rules

| Rule | Source |
|---|---|
| Define measures **before** realization, not after | SGE Definition of Outcome Done |
| **Read metrics together**, never in isolation | DORA |
| Avoid local optimization that hurts the system | UtS / Performance domain Measurement; SGE Systems Thinking |
| **What you measure becomes the goal** (Parkinson) | UtS / Measurement |
| Outcome may take **months** after output ships | PMBOK 7 §12; SGE Vision |
| **Sprint Review** is **not** a release gate | Scrum 2020 / SGE |
| **Stop putting items in progress; start finishing** | SGE / Scrum Master mantra |

## Common failure modes

- **Output Bias.** Team ships every Sprint; Product never moves
  market metrics → no outcome.
- **Vanity metrics.** Counting story points / lines of code / items
  closed instead of user behavior change.
- **Hidden CFR.** Production bugs unlabeled → CFR=0 looks great →
  reality is broken.
- **Output Done without Outcome Done.** Increments meeting DoOD;
  no Definition of Outcome Done; team doesn't know if anything
  worked.
- **Story points as outcome.** Velocity confused with progress
  toward outcomes.

## When this synthesis applies

- Setting up Product KPIs / OKRs that aren't vanity
- Defending against management pressure to "just ship more"
- Designing both DoOD (Output) and Definition of Outcome Done
- Connecting DORA discipline to Product strategy
- Reporting up to program / portfolio level

## Cross-refs

- PMBOK 7: [Focus on value](../principles/pmbok-7/04-focus-on-value.md) ·
  [Enable change](../principles/pmbok-7/12-enable-change.md)
- Performance domain: [Delivery](../performance-domains/07-delivery.md) ·
  [Measurement](../performance-domains/06-measurement.md)
- SGE: [Definition of Outcome Done](../scrum-guide-expanded/11-definition-of-outcome-done.md) ·
  [Definition of Output Done](../scrum-guide-expanded/12-definition-of-output-done.md) ·
  [Product (artifact)](../scrum-guide-expanded/10-product-and-vision.md)
- DORA: [Fundamentals](../dora-metrics-jira/01-dora-fundamentals.md) ·
  [Anti-patterns](../dora-metrics-jira/05-anti-patterns.md)
- Scrum 2020: [Increment](../scrum-guide/16-increment.md) ·
  [Sprint Review](../scrum-guide/12-sprint-review.md)
