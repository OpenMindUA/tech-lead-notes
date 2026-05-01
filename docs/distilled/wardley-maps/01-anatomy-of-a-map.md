---
title: Wardley Maps — anatomy of a map
type: framework-card
framework: Wardley Mapping
source: docs/sources/wardley-maps/02-finding-a-path.md
source_url: https://medium.com/wardleymaps
license: CC-BY-SA-4.0
authors_of_source: Simon Wardley
tags: [wardley-maps, strategy, anchor, value-chain, evolution, map-anatomy]
---

# Wardley Maps — anatomy of a map

**TL;DR:** A Wardley Map is a **value chain** plotted against an **evolution axis**. It is anchored on **user needs** at the top, decomposed into the components required to serve them, and each component is positioned horizontally by how evolved (commoditized) it is. Without an anchor, you don't have a map — you have a graph.

## The four constituents of a map (after Sun Tzu's five factors)

| Element | What it answers | In a map |
|---|---|---|
| **Purpose** | Why are we doing this? | The anchor — usually the user and their need |
| **Landscape** | What does the territory look like? | The map itself: components and their evolution |
| **Climate** | What rules act on the landscape? | Climatic patterns (see card 04) |
| **Doctrine** | What universal practices help? | Doctrine principles (see card 03) |
| **Leadership** | What do we choose to do? | Gameplay (see card 05) |

## Map axes

```
Visible (anchor / user need)
     │
     │   ●─────●─────●          ← components & dependencies
     │       \   /
     │        ●
     │       / \
     │      ●   ●
     │
Invisible ─────────────────────►
         genesis | custom | product | commodity
                           (evolution →)
```

- **Vertical (value chain):** dependency, top = visible to user (their **need**), bottom = invisible plumbing.
- **Horizontal (evolution):** how evolved each component is — *not* time, *not* maturity in the agile sense.

## Anchor first, always

> "An anchor — a user with a need — is what turns a graph into a map."

Without an anchor:
- You can't tell what's important.
- Position is meaningless (top vs bottom is arbitrary).
- You're describing structure, not strategy.

A map can have multiple anchors (different user types). Each gives a different perspective on the same landscape.

## Components

Each node represents a capability the value chain depends on. Components can be:
- **Activities** (what we do — "compute power", "send notification")
- **Practices** (how we do it — "agile", "DevOps")
- **Data** (information we use)
- **Knowledge** (e.g. "behaviour of a market")

All four evolve along the same horizontal axis, with stage names that differ slightly per type (see card 02).

## The components have dependencies, not flows

The lines on a map are **dependencies**, not data flows or process arrows. "A depends on B" means *A needs B to exist for A to function*. Reversing this misreads the map.

## When to use this card

- First time drawing a Wardley Map for a problem.
- Reviewing a "map" someone produced and asking *"is this actually a map?"* (no anchor → not a map).
- Onboarding a teammate to mapping vocabulary before doctrine / gameplay.

## Anti-patterns

- **No anchor.** Drawing components and dependencies without a user need at the top — you have a graph, not a map. Strategy will be incoherent.
- **Time on the X-axis.** Evolution is *not* time. A genesis-stage component can persist for decades; a commodity component reached commodity in months. Don't conflate.
- **Functional decomposition only.** Mapping internal structure (org chart) instead of value chain. The map should reflect *what the user needs*, not *how the team is organized*.
- **Treating arrows as flows.** The map is a dependency graph, not a sequence diagram.
- **One map fits all.** Different users → different anchors → different maps. Pick one anchor per map.

## Cross-refs

- [Evolution stages](02-evolution-stages.md) — what the X-axis actually means
- [Doctrine](03-doctrine.md) — practices that turn maps into action
- [Climatic patterns](04-climatic-patterns.md) — the rules of the landscape
- [Strategy cycle](07-strategy-cycle-and-when-to-use.md) — where mapping fits in the OODA-like loop
- PMBOK 7 / SGE: [Output vs Outcome synthesis](../synthesis/03-outcome-vs-output.md) — the user-need anchor here matches "outcome" framing

## Source

Full text: [Ch. 2 — Finding a path](../../sources/wardley-maps/02-finding-a-path.md), [Ch. 3 — Exploring the map](../../sources/wardley-maps/03-exploring-the-map.md).
