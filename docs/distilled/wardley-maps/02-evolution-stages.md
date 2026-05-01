---
title: Wardley Maps — evolution stages
type: framework-card
framework: Wardley Mapping
source: docs/sources/wardley-maps/03-exploring-the-map.md
source_url: https://medium.com/wardleymaps
license: CC-BY-SA-4.0
authors_of_source: Simon Wardley
tags: [wardley-maps, strategy, evolution, genesis, custom, product, commodity]
---

# Wardley Maps — evolution stages

**TL;DR:** Every component on a map sits in one of four evolution stages — **genesis → custom-built → product (incl. rental) → commodity (incl. utility)**. The stage tells you *how* to treat it: build, buy, outsource, replace. Mis-stage and your strategy fights physics.

## The four stages (activities)

| Stage | Characteristics | Example today |
|---|---|---|
| **I. Genesis** | Novel, rare, uncertain; high failure rate; "wonder" reaction | Early quantum compute |
| **II. Custom-built** | Bespoke; small numbers; emerging understanding; expensive | In-house ML platform tailored to one company |
| **III. Product (+ rental)** | Repeatable, well-defined; many providers compete on features | SaaS CRM, managed Postgres |
| **IV. Commodity (+ utility)** | Ubiquitous, standardized, rented per-use, "boring" | Electricity, AWS S3, container runtime |

Each component evolves **left to right** under competitive pressure, *eventually* reaching commodity unless something disrupts it.

## Stage names per component type

| Type | I | II | III | IV |
|---|---|---|---|---|
| Activity | Genesis | Custom-built | Product / Rental | Commodity / Utility |
| Practice | Novel | Emerging | Good | Best |
| Data | Unmodelled | Divergent | Convergent | Modelled / Standardized |
| Knowledge | Concept | Hypothesis | Theory | Accepted |

## How to position a component

Wardley's cheat-sheet questions for each component:
- How **ubiquitous** is it (rare → ubiquitous)?
- How **certain** are we about it (uncertain → fits universally)?
- How **published** is the underlying knowledge (novel → standardized)?
- What's our **emotional reaction** ("wonder" → "boring")?

Triangulate the four answers to place it on the X-axis. **Ranges, not points** — components occupy a fuzzy band, not an exact position.

## Why the stage dictates strategy

| Stage | What you should do | What you should NOT do |
|---|---|---|
| Genesis | Experiment, R&D, accept failure | Try to ROI it; outsource it |
| Custom | Build in-house with experts | Buy a product (none exists yet); commodify it prematurely |
| Product | Buy off-the-shelf, configure | Rebuild it in-house ("Not Invented Here") |
| Commodity | Rent, treat as utility, automate | Build it; differentiate on it |

> "**Use appropriate methods.**" — Doctrine — match build vs buy vs rent vs outsource to the stage. Single methodology = guaranteed waste.

## How stages map to team types (see card 06)

| Stage | Team type that fits |
|---|---|
| Genesis / Custom | **Pioneers** — explorers, tolerant of ambiguity |
| Product | **Settlers** — turn the prototype into a robust offering |
| Commodity | **Town Planners** — industrialize, optimize, scale |

## When to use this card

- Build vs buy vs rent decisions.
- Auditing a portfolio: "are we treating commodity components as if they were custom?"
- Spotting "we'll never standardize this" mistakes (it's commodity, you don't have a choice).
- Communicating *why* an in-house effort is wasteful (or correctly bold).

## Anti-patterns

- **Confusing evolution with maturity.** A "mature" Scrum team can still be using genesis-stage tooling. Stage refers to the *thing*, not the team.
- **Outsourcing the wrong stage.** Outsourcing genesis activity = funding an experiment with no managerial visibility. Outsourcing custom-built = your provider can't deliver. Outsourcing commodity = right answer almost always.
- **Building a commodity in-house.** "We'll write our own database." Almost always wrong.
- **Buying a genesis component.** It doesn't exist as a product yet — you'd be buying a label.
- **One-size-fits-all engineering.** Same SDLC for genesis (R&D) and commodity (operations) — both suffer.
- **Ignoring inertia.** Internal teams resist the shift from custom→product→commodity (their jobs depend on it). Doctrine: expect it, plan for it.

## Cross-refs

- [Anatomy of a map](01-anatomy-of-a-map.md) — where the X-axis comes from
- [Climatic patterns](04-climatic-patterns.md) — *everything evolves* (the law underlying the stages)
- [Pioneers, Settlers, Town Planners](06-pioneers-settlers-town-planners.md) — team structures that match stages
- [Gameplay](05-gameplay.md) — moves that exploit or accelerate evolution
- Underneath the Surface: [Tailoring synthesis](../synthesis/06-tailoring-and-method-selection.md) — same insight in PM language ("methods must match context")

## Source

Full text: [Ch. 3 — Exploring the map](../../sources/wardley-maps/03-exploring-the-map.md).
