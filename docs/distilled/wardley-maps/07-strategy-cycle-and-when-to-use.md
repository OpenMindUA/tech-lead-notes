---
title: Wardley Maps — strategy cycle and when to use
type: framework-card
framework: Wardley Mapping
source: docs/sources/wardley-maps/16-super-looper.md
source_url: https://medium.com/wardleymaps
license: CC-BY-SA-4.0
authors_of_source: Simon Wardley
tags: [wardley-maps, strategy, strategy-cycle, ooda, when-to-use]
---

# Wardley Maps — strategy cycle and when to use

**TL;DR:** Wardley's **strategy cycle** is an OODA-like loop: *purpose → landscape → climate → doctrine → leadership (act)*, then back. Strategy is **iterative**, not a one-shot plan. Wardley Mapping is the right tool when you need **situational awareness** for non-trivial decisions; it is overkill for short-cycle delivery decisions covered by Scrum/Kanban.

## The strategy cycle (the "super looper")

```
        ┌──────────────────► PURPOSE ◄──────────────────┐
        │                       │                       │
        │                       ▼                       │
        │                  LANDSCAPE  ────► (map)       │
        │                       │                       │
        │                       ▼                       │
        │                   CLIMATE   ────► (forecast)  │
        │                       │                       │
        │                       ▼                       │
        │                  DOCTRINE   ────► (audit)     │
        │                       │                       │
        │                       ▼                       │
        │                  LEADERSHIP ────► (act)       │
        │                       │                       │
        └───────────────────────┴───────────────────────┘
                       (iterate; the world moved)
```

- **Purpose** — why do we exist? Who's the user? What's the moral imperative?
- **Landscape** — draw the map.
- **Climate** — annotate climatic patterns; forecast moves.
- **Doctrine** — audit universal practices; close gaps.
- **Leadership / Act** — choose plays (gameplay), execute, observe.
- **Loop** — the act changed the world; remap.

Cadence: depends on the organization. Yearly is typical for the *full* cycle; the act loop runs continuously.

## Relationship to OODA

| OODA | Wardley cycle |
|---|---|
| Observe | Landscape (map) |
| Orient | Climate (forecast) + Doctrine (audit) |
| Decide | Leadership (pick plays) |
| Act | Execute the play |

Wardley adds **purpose** as an explicit prefix and makes orientation richer (climate + doctrine, not just observe-orient).

## When Wardley Mapping is the right tool

✅ **Good fit:**
- Multi-year strategic decisions (build vs buy, market entry, platform direction).
- "Where should we differentiate?" / "What should we open-source?" questions.
- Diagnosing why a strategy keeps failing (usually doctrine or stage mis-fit).
- Aligning leadership across a large org via shared map vocabulary.
- Portfolio decisions across multiple business lines.
- Spotting next waves: where is something *just* commoditizing?

❌ **Wrong fit:**
- Sprint-to-sprint delivery decisions — Scrum / Kanban already cover this.
- Short-term incident response — DORA / SRE practices, not maps.
- Pure execution problems where direction is settled — just do the work.
- Single-component tactical questions (use a checklist, not a map).

## Mapping it to this repo

Wardley operates *above* the frameworks already in this repo:

| Layer | Question | Frameworks |
|---|---|---|
| **Strategy** (years) | What landscape? Which plays? | **Wardley Maps** |
| **Portfolio / programme** (months-years) | How do we orchestrate work? | PMBOK 7, NUPP |
| **Project / product cycle** (months) | How do we run the lifecycle? | P3.express, Scrum, micro.P3.express |
| **Delivery flow** (sprints / continuous) | How do we ship value? | Scrum, Kanban, Open Guide to Kanban |
| **Engineering effectiveness** (continuous) | Are we delivering reliably? | DORA |
| **Universal principles** (cross-cutting) | Which patterns to honour? | Underneath the Surface, NUPP |

A tech lead typically lives at the lower layers but *needs* awareness of the upper ones to defend non-obvious decisions ("why do we keep this in-house?", "why are we open-sourcing?", "why is that team allowed to be slow?").

## Common misuses

- **Mapping for mapping's sake.** A map without an act is a wall poster. Loop or stop.
- **Single annual map.** The world moves; the map should be updated quarterly at least.
- **Mapping at the wrong altitude.** Mapping a sprint backlog is silly; mapping a single line of code is meaningless. Map at the strategy / capability layer.
- **Treating maps as predictions.** They're forecasts under climate. Wrong forecasts mean *update*, not *abandon mapping*.
- **No leader owns it.** If the strategy cycle has no owner, it doesn't run. Mapping is leadership work.

## Cross-refs

- [Anatomy of a map](01-anatomy-of-a-map.md), [Evolution stages](02-evolution-stages.md), [Doctrine](03-doctrine.md), [Climatic patterns](04-climatic-patterns.md), [Gameplay](05-gameplay.md), [PST](06-pioneers-settlers-town-planners.md) — the cycle's components
- DORA [fundamentals](../dora-metrics-jira/01-dora-fundamentals.md) — how acts get measured
- NUPP / [Tailoring synthesis](../synthesis/06-tailoring-and-method-selection.md) — choosing methods per context
- Scrum 2020 + SGE — what the act loop typically uses inside the strategy cycle

## Source

Full text: [Ch. 16 — Super looper](../../sources/wardley-maps/16-super-looper.md), [Ch. 17 — To infinity and beyond](../../sources/wardley-maps/17-to-infinity-and-beyond.md).
