---
title: Risk, uncertainty, incidents, and stability across frameworks
type: synthesis
license: CC-BY-SA-4.0
sources_combined: [underneath-the-surface, scrum-guide-expanded, dora-metrics-jira]
tags: [synthesis, risk, uncertainty, incidents, change-failure-rate, mttr, follow-up-register]
---

# Risk, uncertainty, incidents, and stability

**TL;DR:** All frameworks treat risk as **uncertainty that can
impact the project (positive or negative)**. They differ on
**operationalization**: PMBOK 7 prescribes layered cost-justified
responses; SGE adds proactive risk management as a Scrum mandate;
P3.express keeps risks in a unified follow-up register; DORA
measures stability through CFR + MTTR. Together they form a
spectrum from **prevention** (PMBOK/SGE) to **detection-and-recovery**
(DORA).

## Definition convergence

> **Risk** = any uncertainty (positive or negative) that can impact
> the project. — PMBOK 7 §9 / UtS

> "**A risk is any factor that could result in a future adverse
> consequence.** Since risk exposure remains unpredictable even as
> time elapses, anticipation is key." — SGE

> Risk exposure includes: market risk, problem-solution fit,
> Product-market fit, technology, signal detection, responsiveness,
> compliance, remediation, poor trade-off decisions. — SGE

## Mapping — which framework owns which slice

| Slice | Framework |
|---|---|
| **Identify risks** continuously (workshops + meeting end-of-agenda) | PMBOK 7 §9 / UtS Performance domain Uncertainty |
| **Layered responses** (prevent / reduce exposure / capacity-build / minimize impact / transfer) | PMBOK 7 §9 |
| **Proactivity as principle** | NUPP §3 / Scrum (empiricism) / SGE |
| **Combined register** (risk + issue + change request + improvement + lesson) | P3.express follow-up register |
| **Separate risk register** | PRINCE2 |
| **Many-to-many risks↔responses** (advanced) | UtS Uncertainty domain ladder |
| **Monte Carlo** for sensitive cases | UtS Uncertainty domain |
| **Cross-project risks** in portfolio | UtS Uncertainty domain |
| **Stability metrics** (CFR, MTTR) | DORA |
| **Failed deployment → incident ticket** | DORA GitHub Action |
| **Production-bug labeling** | DORA |
| **Sprint scope renegotiation** without changing Sprint Goal | Scrum / SGE |

## Layered response design (PMBOK 7 §9, with DORA additions)

For a single risk type:

| Layer | Example (production reliability) |
|---|---|
| 1. **Prevent in plan** | Code review + pre-commit hooks (DORA L1-L2) |
| 2. **Reduce exposure** | Branch protection rules; only `environment: production` deploys (DORA L3) |
| 3. **Capacity-build** | Test automation; CI checks for many risks at once |
| 4. **Reduce impact** | Feature flags; canary releases (lowers MTTR) |
| 5. **Transfer** | Insurance; SLAs / penalties |

DORA's CFR + MTTR measure the residual risk of layers 1-4 having
worked.

## Sophistication ladder (UtS Uncertainty domain)

When picking a register:

1. **Single combined register** (P3.express follow-up register) — risks
   morph: future uncertainty → issue when it occurs → lesson learned
   when closed.
2. **Separate risk register** (PRINCE2-style) — when item types need
   distinct workflows.
3. **Two tables, risks ↔ responses, many-to-many** — for complex
   programs.
4. **Cause / effect split** — even more advanced.
5. **Graph model** — mega-projects only.

> Default to the simpler one when in doubt.

## Cost-justification rule

| Source | Rule |
|---|---|
| PMBOK 7 §9 | Investment in a response must be justified by the risk reduction value |
| SGE | Risks evaluated via empirical evidence; flexibility valued over commitments |
| DORA | OSS tooling adoption only after native Jira capabilities are exhausted |

## Quantitative analysis

- Most projects don't need it. Intuition is fine.
- **Sensitive** projects: extract data + run **Monte Carlo** to
  compute probabilistic outputs before/after responses.
- DORA's stability metrics give a **lagging** quantitative view —
  treat them as proxies, not predictions.

## Cross-project risks → portfolio

- **Some risks span projects** (shared regulators, platforms,
  vendors). Manage centrally; project layer reports up.
- "Project management = doing things right; portfolio management =
  doing the right things."
- DORA recommends quarterly review against benchmarks — at the
  portfolio level when multiple teams share the platform.

## Common anti-patterns (universal)

- Risk identification only at kickoff
- Single-layer response (only insurance, only training)
- Treating risk only as **negative** (positive risks ignored)
- Risk-response cost > risk reduction
- DORA CFR = 0 in a real production system → **bugs unlabeled**
- "We covered safety in onboarding" → no project-specific plan
- Risk register set up at kickoff, never reviewed
- Bypassable enforcement (hooks without server-side actions)

## When this synthesis applies

- Designing a project's overall risk discipline
- Adding DORA stability metrics to an existing risk framework
- Choosing register sophistication for a new project
- Resolving "what's a risk vs an issue?" arguments (P3.express
  unifies the artifact)
- Multi-product programs with shared platform risks

## Cross-refs

- PMBOK 7: [Optimize risk responses](../principles/pmbok-7/09-risk.md) ·
  [System interactions](../principles/pmbok-7/05-system-interactions.md)
- Performance domain: [Uncertainty](../performance-domains/08-uncertainty.md)
- NUPP: [Always be proactive](../principles/nupp/03-always-be-proactive.md)
- SGE: [Foundational theory (empiricism, complexity)](../scrum-guide-expanded/02-foundational-theory.md)
- DORA: [Fundamentals (4 metrics)](../dora-metrics-jira/01-dora-fundamentals.md) ·
  [GitHub-side enforcement (incident tickets)](../dora-metrics-jira/03-github-side.md) ·
  [Anti-patterns (CFR=0 diagnosis)](../dora-metrics-jira/05-anti-patterns.md)
- P3.express follow-up register: [Methodology card](../methodologies/p3-express.md)
