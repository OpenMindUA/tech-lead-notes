---
title: Methodology comparison
type: comparison
source_url: https://pmbok.guide/pmbok-guide--underneath-the-surface.md
license: CC-BY-4.0
tags: [methodologies, comparison, distilled, decision-aid]
---

# Methodology comparison

Side-by-side decision aid based on the four methodologies the book
covers. None is universally right; pick by context. Use PMBOK 7's
principles + performance domains *across* whichever you choose.

## At a glance

| | P3.express | PRINCE2 | Scrum | DSDM |
|---|---|---|---|---|
| **License / IP** | open | AXELOS proprietary | open | Agile Business Consortium proprietary |
| **Self-label** | system | methodology | framework | methodology |
| **Project domain** | general | general | IT development | IT development |
| **Project size** | small / medium / large | medium / large / super-large | single team ≤10 | large multi-team |
| **Out of scope** | micro, mega | very small (untailored is too heavy) | non-IT, multi-team | small projects, non-IT |
| **Development approach** | predictive *or* adaptive | predictive (PRINCE2 Agile is the adaptive variant) | adaptive only | adaptive only |
| **Governance layers** | sponsor + PM + team | Project Board + PM + Team Manager | none (decentralized) | Project + Team + Support |
| **PM role** | yes (centralized) | yes (centralized) | **no** (decentralized) | yes (centralized) |
| **Tailoring stance** | gradual ongoing only | upfront mandatory + ongoing | limited — new roles break internal consistency | substantial structure |
| **Decision gates** | sponsor at init + every monthly init | Executive at project brief + PID + each stage boundary | none formal; Sprint Review collects feedback | pre-project, feasibility, foundations gates |
| **Cadence** | monthly + weekly + daily | stages | Sprint (≤1 month) | evolutionary cycles + deployments |
| **Closure** | yes + post-project | yes | none | implied in deployment + post-project |
| **Risk artifact** | follow-up register (combined) | risk register + others | not specified | not specified at this level |
| **Prioritization** | not mandated | not mandated | by value (Product Owner) | MoSCoW + ratios |
| **Coverage breadth** | full | full | subset | full |

## Selection heuristics

1. **Predictive product, multi-team, regulated** → **PRINCE2** (or
   PRINCE2 + tailored elements). Strong governance and stage gates.
2. **Adaptive software, single small team** → **Scrum** (or close
   second-generation derivative). Cheap to start.
3. **Adaptive software, multi-team, business-heavy** → **DSDM**.
   Built for that scale; MoSCoW + timebox give predictable
   delivery.
4. **Any size general project, low-ceremony preference** →
   **P3.express**. Predictive *or* adaptive; minimal upfront cost.
5. **Pilot projects, methodology-new teams** → start with
   **P3.express**, evolve. Switch as scale or governance demands.

## Cross-cutting cautions

- **Don't cherry-pick.** "PRINCE2-style stages with Scrum sprints"
  without the matching authority model and definition-of-done is
  the *Frankenstein system* the author warns about
  (see [PMBOK §7 Tailor](../principles/pmbok-7/07-tailor.md)).
- **Apply PMBOK 7 across all of them.** Principles + performance
  domains aren't a competing choice — they're the lens you put over
  whichever method you pick.
- **Some risks span multiple projects** (e.g. shared regulators,
  shared platforms). Handle them at portfolio level regardless of
  methodology choice (see
  [Uncertainty domain](../performance-domains/08-uncertainty.md)).

## Cross-refs

- [Methodologies index](index.md)
- Performance domain: [Development approach and life cycle](../performance-domains/03-development-approach.md)
- PMBOK 7 §11 [Adaptability](../principles/pmbok-7/11-adaptability.md)
- PMBOK 7 §7 [Tailor based on context](../principles/pmbok-7/07-tailor.md)
