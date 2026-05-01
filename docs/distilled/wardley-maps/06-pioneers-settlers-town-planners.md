---
title: Wardley Maps — Pioneers, Settlers, Town Planners
type: framework-card
framework: Wardley Mapping
source: docs/sources/wardley-maps/04-doctrine.md
source_url: https://medium.com/wardleymaps
license: CC-BY-SA-4.0
authors_of_source: Simon Wardley
tags: [wardley-maps, strategy, pioneers-settlers-town-planners, organization, attitude]
---

# Wardley Maps — Pioneers, Settlers, Town Planners

**TL;DR:** Different evolution stages need fundamentally different **attitudes** in the people working on them. **Pioneers** explore the unknown (genesis/custom). **Settlers** turn prototypes into robust products (product). **Town Planners** industrialize and scale (commodity). One org needs all three; mixing them in one team breaks all three.

## The three populations

| Population | Stage they thrive in | Mindset | Outputs |
|---|---|---|---|
| **Pioneers** | Genesis, custom-built | "Show me the strange." Comfortable with chaos, ambiguity, failure. Rapid prototyping. | Working hypotheses, ugly proofs of concept, novel discoveries |
| **Settlers** | Product / rental | "Make it useful, repeatable." Pattern recognition, product mindset, customer-centric. | Documented products, patterns, MVPs that became real products |
| **Town Planners** | Commodity / utility | "Make it boring at scale." Engineering rigour, operational excellence, automation. | Utility services, standards, platforms with five-nines |

This is **attitude × aptitude** (doctrine card 03 phase IV). Aptitude = what they're good at (engineering, design, finance). Attitude = how they engage uncertainty (PST). Both matter; both vary independently.

## Why one team can't do all three

- **Pioneers in a Town Planner role** — ship a "prototype" to production at scale; everything breaks; ops burn.
- **Town Planners in a Pioneer role** — over-engineer the proof of concept; a 3-month learning experiment becomes an 18-month platform build.
- **Settlers without Pioneers above them** — nothing new flows in; product line stagnates.
- **Settlers without Town Planners below** — products never reach commodity; profitability never scales.

> "**Use appropriate people.**" — same insight as "use appropriate methods" (card 02), at the staffing level.

## Theft (the hand-off)

The system works only if there's a **deliberate hand-off** between populations:

```
Pioneers ──theft──► Settlers ──theft──► Town Planners
```

- **Pioneer→Settler theft:** Settlers spot a Pioneer prototype that's working and *take it*, productizing it. Pioneers move on to the next genesis.
- **Settler→Town Planner theft:** Town Planners spot a Settler product that's reached commodity-fit, *take it*, and turn it into utility. Settlers move to the next product wave.

If theft is blocked (politics, ego, bad incentive design), the org accumulates orphan prototypes (Pioneers can't let go), aged products (Settlers won't industrialize), and over-engineered playgrounds (Town Planners working on things that should still be experimental).

## Common org-design mistakes

- **One product team to rule them all.** Stage III (product) thinking applied to genesis-stage R&D and to commodity ops. Three failure modes.
- **PST as job titles.** It's an *attitude*, not a fixed identity. People can shift; teams should be staffed by attitude per current goal.
- **Skipping Settlers.** Common in startups: Pioneers ship to prod (no Settlers), Town Planners are demanded once scale hits, but the missing Settler layer means there's no productized form to scale. Result: rewrites.
- **Town Planners as "ops"-only.** They're not the on-call team — they're the team that builds the platforms ops depends on. Treating them as a tier-2 cost center is a major waste.
- **Pioneers as "innovation lab" sandboxed.** Innovation labs that don't have *theft* designed in produce demos, not products.

## How this maps to other frameworks

- **Scrum / SGE** — single Scrum Team with cross-functional members can serve product stage well; pioneers and town planners typically sit *outside* a single Scrum Team (R&D group, platform engineering org).
- **DORA** — Town Planner work is what produces the high-DORA-metric platforms that everyone else builds on. Pioneer work shouldn't be measured by deploy frequency.
- **NUPP** — pioneers operate in irreducible uncertainty; settlers in reducible; town planners with near-zero uncertainty. Pick lifecycle accordingly.
- **DevOps / Platform engineering** — modern "platform team" ≈ Town Planners. "Stream-aligned team" ≈ Settlers. "Enabling team" ≈ part-Pioneer, part-Settler.

## When to use this card

- Designing or redesigning a tech org.
- Diagnosing a "we ship slow / we don't innovate / we have outages" complaint — it's almost always a PST imbalance.
- Allocating people to a new initiative (which attitude does it need?).
- Hiring brief — make attitude explicit, not just aptitude (skills).

## Anti-patterns

- **One-team-fits-all** — see above.
- **Conflating PST with seniority.** A junior Pioneer can be brilliant; a senior Town Planner is a real career, not a "promotion to ops".
- **Theft without context.** Stealing too early (Pioneer prototype taken before validated) or too late (Settler product taken when growth is over) — both waste.
- **No one wants to be a Town Planner.** Cultural problem; if your org rewards only Pioneers, your commodity layer is broken.

## Cross-refs

- [Evolution stages](02-evolution-stages.md) — the staging that PST aligns to
- [Doctrine](03-doctrine.md) — phase IV "think aptitude *and* attitude"
- [Roles synthesis](../synthesis/07-roles-across-frameworks.md) — how PST relates to Scrum/SGE/DORA roles
- Underneath the Surface / [Tailoring synthesis](../synthesis/06-tailoring-and-method-selection.md) — same "match method to context" logic

## Source

Full text: [Ch. 4 — Doctrine](../../sources/wardley-maps/04-doctrine.md), [Ch. 18 — Better for less](../../sources/wardley-maps/18-better-for-less.md).
