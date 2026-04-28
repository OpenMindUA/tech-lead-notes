---
title: Tailoring and methodology selection across frameworks
type: synthesis
license: CC-BY-SA-4.0
sources_combined: [underneath-the-surface, scrum-guide-expanded]
tags: [synthesis, tailoring, methodology-selection, frankenstein, cargo-cult, hybrid-approach]
---

# Tailoring and methodology selection

**TL;DR:** Every framework explicitly addresses tailoring, and they
converge on **don't cherry-pick** ("Frankenstein"). They diverge on
**when to tailor** (PRINCE2: upfront required; P3.express: gradual
only) and on **immutability** (Scrum is *purposefully incomplete*
but rules are immutable; PMBOK 7 invites adaptation everywhere).
Methodology choice depends on **product nature, project size,
domain, coverage scope** — not team preference.

## Universal rules

1. **Tailoring ≠ cherry-picking.** UtS PMBOK 7 §7 / PRINCE2 §7 /
   NUPP §1: mixing surface-level practices from different frameworks
   without internal consistency yields a non-functional system
   ("Frankenstein").
2. **Cargo cult is the failure mode.** NUPP §5: doing a practice
   because everyone does it, without articulating its purpose for
   *your* project, produces ceremony with no benefit.
3. **System design, not artifact selection.** Tailoring is a
   separate skill many PMs lack; DSDM addresses this with a
   dedicated **DSDM Coach** role.
4. **Driven by product / context, not preference.** SGE: "team /
   org / customer preference does not justify the choice" of
   approach.

## When to tailor (per methodology)

| Methodology | Tailoring stance |
|---|---|
| **P3.express** | Use as-is; **gradual ongoing** tailoring |
| **PRINCE2** | **Upfront required** + ongoing |
| **PMBOK Guide (any edition)** | Two-step: org-level partial tailoring + project-level final |
| **Scrum** | **Minimal** — adding new roles or removing events breaks internal consistency ("the result is not Scrum") |
| **DSDM** | Substantial structure + DSDM Coach role |
| **SGE** | Inspect-and-adapt the PM system itself; bounded autonomy |

## "Hybrid approach" — caveat

PMBOK 7 §11 (Adaptability):
- **Predictive vs adaptive is decided by the product, not by team
  preference.**
- The author argues **hybrid approaches don't really exist** within
  a single project: any predictive subset blocks adaptation of the
  whole.
- Only valid form of "mixing": **decompose the product into
  independent parts**, each delivered as a separate (mono-approach)
  project = a **program**, not a hybrid project.

SGE agrees on practice ("Scrum is purposefully incomplete; processes
and methods may be employed within the framework") without using
"hybrid" terminology.

## Methodology selection heuristics

(From UtS Methodology comparison + Scrum Guide constraints + DORA
prescriptive stack.)

| Context | Pick |
|---|---|
| Predictive product, multi-team, regulated | **PRINCE2** |
| Adaptive software, single small team (≤10) | **Scrum 2020** (or PRINCE2 Agile, or DSDM) |
| Adaptive software, multi-team, business-heavy | **DSDM** |
| Any size general project, low ceremony | **P3.express** |
| Pilot / methodology-new teams | Start with **P3.express**, evolve |
| Engineering effectiveness measurement | Add **DORA** on top of any methodology |
| Modern Scrum with explicit theory + extensions | **SGE** as overlay on Scrum 2020 |

## Tailoring-as-system-design checklist

Per UtS PMBOK 7 §7 + Performance domain Planning:

- Is each artifact **purposeful** (NUPP §5 counterfactual test —
  imagine the world without it; is the difference worth the effort)?
- Is it **internally consistent** (no Frankenstein pieces)?
- Does the **investment pay back** (PMBOK 7 §8 quality test
  generalized)?
- Will it **adapt over time** (Scrum / SGE: adaptive PM system regardless of product)?
- Is **tailoring kept upfront-minimum** (PMBOK 7 §7) so the team can
  enrich based on real experience?

## Combining PMBOK 7 across all methodologies

> Principles + performance domains apply **regardless** of which
> methodology you pick — they're a **lens**, not a competing choice.

Example overlays:
- Scrum + PMBOK 7 §1 Stewardship → reinforces servant leadership
  for the Scrum Master
- PRINCE2 + PMBOK 7 §3 Engage stakeholders → richer Project Board
  practice
- DORA + PMBOK 7 §8 Build quality in → DORA stability metrics as
  evidence of built-in quality
- P3.express + PMBOK 7 §7 Tailor based on context → P3.express
  *gradual* tailoring matches the principle's "minimum upfront" rule

## Anti-patterns (universal)

- "We use Scrum **but** we skip [event]" — ScrumBut
- "PRINCE2 is too expensive" — usually un-tailored PRINCE2
- "We're agile, no PM needed" — only true for Scrum derivatives,
  not Agile generally (DSDM has a PM)
- Cherry-picking artifacts from multiple frameworks
- Heavy upfront tailoring in a minimalist method
- Templates filled in mechanically (cargo cult)
- Tailoring left to a single PM with no system-design skill

## When this synthesis applies

- Choosing a methodology for a new project
- Defending against fashion-driven Agile rollouts
- Resolving "we'll just take parts of each" instincts
- Coaching teams on minimum-viable tailoring upfront

## Cross-refs

- PMBOK 7: [Tailor based on context](../principles/pmbok-7/07-tailor.md) ·
  [Adaptability and resiliency](../principles/pmbok-7/11-adaptability.md)
- PRINCE2: [Tailor to suit the project](../principles/prince2/07-tailor-to-project.md)
- NUPP: [Don't do anything without clear purpose](../principles/nupp/05-clear-purpose.md) ·
  [Results over affiliations](../principles/nupp/01-results-over-affiliations.md)
- Methodologies: [Comparison](../methodologies/comparison.md) ·
  [P3.express](../methodologies/p3-express.md) ·
  [PRINCE2](../methodologies/prince2.md) ·
  [Scrum](../methodologies/scrum.md) · [DSDM](../methodologies/dsdm.md)
- Scrum 2020: [Scrum definition (immutable rules)](../scrum-guide/01-scrum-definition.md)
- SGE: [Purpose & departures](../scrum-guide-expanded/01-purpose-and-departures.md)
- Performance domain: [Development approach and life cycle](../performance-domains/03-development-approach.md)
