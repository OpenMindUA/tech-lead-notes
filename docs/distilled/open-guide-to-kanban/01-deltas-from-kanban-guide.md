---
title: Open Guide to Kanban — deltas from The Kanban Guide
type: comparison-card
framework: Kanban
source: docs/sources/open-guide-to-kanban/index.md
source_url: https://kanbanguides.org/open-guide-to-kanban/
license: CC-BY-SA-4.0
authors_of_source: John Coleman, Magdalena Firlit et al.
tags: [kanban, open-guide-to-kanban, deltas, comparison, oiv, outcomes, metrics]
---

# Open Guide to Kanban — deltas from The Kanban Guide

**TL;DR:** The Open Guide preserves *The Kanban Guide* verbatim (kept in regular type) and **adds** material in italics. Five categories of additions: (1) expanded metrics catalog, (2) Outcomes/Impact/Value (OIV) extension, (3) knowledge-work framing of definitions, (4) prioritization techniques in the appendix, (5) explicit WIP-control techniques. Read the canonical Kanban Guide first; treat the Open Guide as an enrichment layer.

## What stays identical

- The **three practices** (define/visualize, actively manage, improve).
- The **six minimum DoW elements**.
- The **four mandatory metrics** (WIP, Throughput, Work Item Age, Cycle Time / ETSF).
- The **WIP → pull system** logic.
- The **just-in-time improvement** stance.

## What's added

### 1. Expanded metrics catalog (~13 additional measures)

The Open Guide's metrics section adds, beyond the four mandatory:

- **BETFI** — Blocked Elapsed Time for Finished Items.
- **CQBT** — Cumulative Queueing or Buffer Time.
- **ETSF** — Elapsed Time from `Started` to `Finished` (this is the strict version of Cycle Time).
- **Flow Distribution** — visualization of work item types finished over time.
- **Flow Efficiency** — `(ETSF − non-value-adding time) / ETSF × 100`.
- **Number of Blockers** — current count of impediments.
- **Process Cycle Efficiency** — value-adding time / Time-to-Market.
- **SNFW** — *Started but Not Finished Work* (synonym for WIP).
- **Time to Market / Customer Lead Time** — order received → delivered.
- **TWIA / TETSNFI** — Total Work Item Age across all in-progress items.
- **Work Item Age (ETSNFI)** — formal definition.

If unsure where to start, the Open Guide recommends: **Time to Market**, plus per started/finished pair: SLE, Work Item Age, ETSF, Throughput.

### 2. Outcomes, Impact, and Value (OIV)

This is the largest substantive addition. Where The Kanban Guide treats *value* as the unit flowing through the system without further qualification, the Open Guide adds an explicit OIV section:

- **Customer outcomes** — measurable value: reduced Failure Demand, addressed customer jobs.
- **User outcomes** — behavioral changes solving problems.
- **Product Stakeholder outcomes** — adoption, retention, time-to-market trends.
- **Business Stakeholder Impact** — compliance, market share, satisfaction across products.
- **Outcomes for Kanban system members** — capability, technical debt, UX/CX debt, climate/culture.

Plus four supporting concepts:

- **Failure Demand** — demand caused by past failure (signal for improvement).
- **Time to Validated Value** — order received → value validated.
- **Value Validated / Value Invalidated** — items that did or did not deliver intended value at finished.

### 3. Knowledge-work framing

Definitions are rephrased for knowledge-work contexts (e.g. "Definition of Kanban *in the Context of Knowledge Work*"). Material consequence: the Open Guide is the version to point a software / R&D team at; The Kanban Guide is the version for cross-industry use (manufacturing, healthcare, logistics).

### 4. Appendix — prioritization and WIP control

The Open Guide's appendix adds practical techniques the canonical guide doesn't catalog:

- Controlling WIP techniques.
- Prioritization techniques for the "started" decision (when capacity opens, which item to pull).

### 5. Stricter quality language

DoW state policies in the Open Guide must be "explicit policies… *defect-free*", with example: fix known defects before moving an item to the next state. The canonical guide says only "explicit policies".

## When to read which

| Context | Read |
|---|---|
| First exposure to Kanban; cross-industry context | The Kanban Guide |
| Software / knowledge-work team adopting Kanban | Open Guide to Kanban |
| Team already on Kanban, wants richer measures | Open Guide §6 metrics + OIV |
| Coaching question about quality policies | Open Guide §5 (defect-free phrasing) |
| Authoritative reference for cross-team contracts | The Kanban Guide (smaller surface area = less argument) |

## Anti-patterns

- **Adopting all 13 supplementary metrics at once** — the four mandatory remain primary; everything else is opt-in by need.
- **OIV theater** — claiming Outcome metrics without an explicit *Value Validated* mechanism is the same anti-pattern as DoD-without-DoD-checks.
- **Treating Open Guide additions as required** — they're community guidance, not normative. The Kanban Guide remains the floor.

## Cross-refs

- [The Kanban Guide cards](../kanban-guide/index.md) — read first
- SGE [Definition of Outcome Done](../scrum-guide-expanded/11-definition-of-outcome-done.md) — same OIV concept under a different name
- DORA [Anti-patterns](../dora-metrics-jira/05-anti-patterns.md) — vanity-metric warnings apply identically
- Synthesis [Output vs Outcome](../synthesis/03-outcome-vs-output.md) — cross-framework outcome-vs-output positioning
- Synthesis [Measurement and metrics](../synthesis/04-measurement-and-metrics.md)

## Source

Full text: [`docs/sources/open-guide-to-kanban/`](../../sources/open-guide-to-kanban/index.md).
