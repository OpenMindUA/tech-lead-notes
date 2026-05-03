---
title: Uncertainty domains and method fit
type: synthesis
license: CC-BY-SA-4.0
sources_combined: [underneath-the-surface, scrum-guide-expanded, nupp, wardley-maps]
external_references: [cynefin, stacey-matrix]
tags: [synthesis, uncertainty, complexity, cynefin, stacey, method-selection, empiricism]
---

# Uncertainty domains and method fit

**TL;DR:** The corpus does not name "Cynefin" but builds the same
distinction. SGE explicitly flags four spaces — *ordered, complex,
chaotic*, plus the implied *complicated* — and warns that **the
space shifts over time, and pretending otherwise is "delusion of
predictability"**. Method choice follows: ordered/complicated work
rewards prediction (PMBOK-style planning); complex work demands
empiricism (Scrum, safe-to-fail experiments); chaotic work demands
stabilize-first (incident command, not planning). Wardley adds the
component-level evolution axis: the same project mixes domains
because components mature at different rates.

## The four domains — corpus mapping

External labels in parentheses are pointers to **Cynefin**
(Snowden) and the **Stacey matrix** (Ralph Stacey); neither is
ingested in this repo. In-repo material covers the same
distinctions under different vocabulary.

| Domain | What it means | In-repo language | External label |
|---|---|---|---|
| **Ordered / Clear** | Information available, cause→effect known and stable, repeatable best practice applies | UtS predictable lifecycle; PMBOK 7 risk register at minimum sophistication; P3.express follow-up register | Cynefin *Clear* / Stacey *Simple* |
| **Complicated** | Information available *to experts*; cause→effect knowable through analysis; multiple valid expert paths | PMBOK 7 layered risk responses; PRINCE2-style separate registers; UtS Uncertainty sophistication ladder steps 2-5 | Cynefin *Complicated* |
| **Complex** | "More unknowns than knowns; expertise necessary but insufficient; cause and effect coherent only in retrospect" — direct SGE quote | SGE empiricism + emergence; Scrum cadence; NUPP "always be proactive"; PMBOK 7 adaptive lifecycle | Cynefin *Complex* / Stacey *Complex* |
| **Chaotic** | Acute lack of information; no time to analyze; act → sense → respond | SGE: "spaces shift… chaos → complex → ordered or reverse"; DORA incident response (MTTR optimization, not prevention) | Cynefin *Chaotic* / Stacey *Chaotic* |

## Definition convergence

> "For complex work: **more unknowns than knowns**, expertise is
> necessary but **insufficient**, **cause and effect coherent only
> in retrospect**." — SGE foundational theory

> "Spaces shift over time (chaos → complex → ordered or reverse) —
> pause and verify which space you're actually in." — SGE

> "Product development often deals with unpredictability — Scrum is
> more useful than approaches with **delusions of predictability**."
> — SGE

> "Project complexity comes from three sources: people, non-linear
> interactions, and ambiguity/uncertainty." — PMBOK 7 §10 / UtS

> "Change is the norm. The map you have today is not the map you'll
> have in 3 years." — Wardley climatic patterns

## Diagnostic — which domain are you in?

| Signal | Likely domain |
|---|---|
| You have a runbook; followed it before; outcomes match expectations | Ordered |
| Senior expert can reason out the answer given enough analysis time | Complicated |
| Stakeholders disagree on what the problem even is; pilots produce surprising results; "what worked last quarter doesn't work now" | Complex |
| Service is down right now; revenue bleeding; can't reach decision-makers | Chaotic |
| You can't tell which of the above describes you | Confusion (Cynefin's 5th domain — pointer only, not in-repo) |

## Method selection follows domain

| Domain | Primary in-repo method | Why |
|---|---|---|
| Ordered | UtS predictable lifecycle, P3.express, PMBOK 7 plan-driven | Stable plan recovers cost of planning |
| Complicated | PMBOK 7 with full risk discipline; PRINCE2-style separate registers; sophistication ladder steps 2-5; expert-led design phases | Analysis pays off; layered responses cost-justified |
| Complex | Scrum / SGE empiricism; NUPP always-be-proactive; short safe-to-fail probes; Wardley pioneers gameplay | Plan outlives reality; learn faster than the landscape moves |
| Chaotic | DORA MTTR-first; incident command (out-of-corpus pointer); stabilize → diagnose → recover | No time to plan; act to escape chaos, then re-diagnose |

## Disorder / Confusion (external pointer, no corpus coverage)

Cynefin's fifth state — variously *Disorder*, *Confusion*, or
*Aporia* in Snowden's later writing — is **not a domain you operate
in; it's the state of not yet knowing which domain you're in**. The
corpus is silent on it: PMBOK 7 §10 lists three sources of
complexity assuming you can diagnose them; SGE says "verify which
space you're in" assuming you can.

Snowden's prescription (out of corpus, summarized for context):

1. Recognize Disorder as a state, not as an answer
2. Decompose the situation into parts
3. Diagnose each part into one of the four domains separately
4. Apply the matching method per part
5. Re-diagnose periodically — parts migrate between domains

Why this matters for method selection: a project that *feels*
Complex may actually be a Complicated component plus a Chaotic
incident plus an Ordered routine, all bundled together. Treating
the bundle as one "complex" thing applies empiricism where
expert-led analysis or incident command would have served better.

This card stops here on Disorder — deeper treatment would require
ingesting Snowden's writing, which is proprietary.

## The mistake the corpus warns about

SGE names it: **delusion of predictability** — applying ordered
methods to complex work because the org-chart, contracts, or
budget-calendar demand a Gantt. Symptoms:

- Detailed plan locked at kickoff, never re-baselined
- "We just need better estimates" (in a complex domain — no, you don't)
- Risk register set up at kickoff, never reviewed (UtS anti-pattern)
- "Agile is just chaos" (PMBOK 7 §11 anti-pattern) — confusing
  *empiricism* with *no method*

The mirror failure (less common in this corpus): treating ordered
work as complex — running discovery cycles on commoditized
infrastructure, or using Scrum where a checklist suffices.

## Domains shift mid-project

A single project usually spans multiple domains by component. From
the corpus:

- **Wardley evolution axis** — Genesis components are *Complex*
  (uncharted, learn-first, fail often). Custom-built and Product
  components are *Complicated* (engineering judgment). Commodity
  components are *Ordered* (standard practice, low failure
  tolerance).
- **Wardley pioneers / settlers / town planners** — three modes
  matched to the three domains (Wardley card 06).
- **SGE explicitly:** spaces shift; verify periodically; the
  inspect-adapt cadence exists *because* the domain might have
  moved since last sprint.

This is why pure-method shops fail: a real project mixes domains,
so a single method (only PMBOK, only Scrum) misfits parts of the
work.

## When this synthesis applies

- Diagnosing why a project feels "wrong" — wrong method for the
  domain
- Choosing between predictable and adaptive lifecycles (PMBOK 7 §11)
- Justifying empiricism to a stakeholder who wants firm dates
- Designing a quarterly check: have the domains shifted under us?
- Picking risk-register sophistication (UtS Uncertainty ladder)
- Mixing methods on one program (different teams, different domains)

## Anti-patterns (universal)

- Picking method before diagnosing domain
- Treating "Complex" as a permanent label (ignoring shifts back to
  ordered as components mature)
- Treating "Chaotic" as a posture rather than a temporary state
- Confusing *Complicated* (expert-knowable) with *Complex*
  (emergent) — the most common diagnostic error
- Single methodology dogma: applying it across all domains
- Reading Cynefin as a 4-box static taxonomy (it's a sense-making
  flow with shifts and a 5th *Confusion* domain)

## External references (not ingested)

- **Cynefin framework** (Dave Snowden, 1999–) — five domains:
  Clear, Complicated, Complex, Chaotic, plus *Disorder /
  Confusion* (the meta-state of not yet knowing which of the four
  applies). Sense-making flow with explicit shift rules.
  Proprietary.
- **Stacey matrix** (Ralph Stacey, 1996–) — 2×2 over agreement
  among stakeholders × certainty about cause-effect. Yields
  Simple / Complicated / Complex / Chaotic regions. Academic
  proprietary.

These are listed in [`docs/index.md`](../../index.md) under
*Other methods worth knowing*. This card covers the same
conceptual ground using only ingested CC sources.

## Cross-refs

- PMBOK 7: [Navigate complexity](../principles/pmbok-7/10-complexity.md) ·
  [Adaptability and resiliency](../principles/pmbok-7/11-adaptability.md) ·
  [Optimize risk responses](../principles/pmbok-7/09-risk.md) ·
  [System interactions](../principles/pmbok-7/05-system-interactions.md)
- Performance domain: [Uncertainty](../performance-domains/08-uncertainty.md)
- SGE: [Foundational theory](../scrum-guide-expanded/02-foundational-theory.md)
- NUPP: [Always be proactive](../principles/nupp/03-always-be-proactive.md)
- Wardley: [Climatic patterns](../wardley-maps/04-climatic-patterns.md) ·
  [Pioneers, Settlers, Town Planners](../wardley-maps/06-pioneers-settlers-town-planners.md) ·
  [Gameplay](../wardley-maps/05-gameplay.md)
- Synthesis: [Risk and stability](05-risk-and-stability.md) ·
  [Tailoring and method selection](06-tailoring-and-method-selection.md)
