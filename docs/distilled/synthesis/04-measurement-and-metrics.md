---
title: Measurement, metrics, and Parkinson's law across frameworks
type: synthesis
license: CC-BY-SA-4.0
sources_combined: [underneath-the-surface, dora-metrics-jira]
tags: [synthesis, measurement, metrics, parkinsons-law, dora, kpis, vanity-metrics]
---

# Measurement, metrics, and Parkinson's law

**TL;DR:** Two laws govern all metrics work: **(1) what you
measure becomes the goal** (Parkinson / Goodhart), and **(2)
metrics must be read together, not in isolation** (DORA). Forecast
to completion is the only effective single-number metric. Use
multi-metric panels to avoid local optimization.

## The two governing laws

### Law 1 — *What you measure becomes the goal*

From Performance domain "Measurement":
- Lines of code → bloated code (the famous PD with **negative LOC**
  after cleanup is a feature, not a bug).
- "Items completed per iteration" → **conservative under-planning**
  (Parkinson: work expands to fill time available).
- Align metrics to **real organizational/project goals**, not
  proxies that game easily.

### Law 2 — *Read metrics together*

From DORA:
- High Deploy Frequency + High CFR = **noise** (or recklessness).
- Short Lead Time + poor stability = **velocity vanity**.
- DORA's four metrics are designed as **a set**: Velocity (Deploy
  Frequency, Lead Time) + Stability (CFR, MTTR).

## Headline metric — *Forecast to completion*

UtS Performance domain: **forecast-to-completion is the only
effective single number.** Examples:
- Money to finish the project.
- Date by which all "must-haves" can be delivered (DSDM).
- Probability of meeting a target (Monte Carlo in sensitive cases).

DORA equivalent: **trend** of the four metrics over 4-12 weeks,
not the absolute snapshot.

## Practical metric anti-patterns

| Anti-pattern | What goes wrong | Source |
|---|---|---|
| Optimize one DORA metric only | Other metric degrades; CFR or MTTR ignored | DORA fundamentals |
| Story points / velocity as the goal | Estimation inflation; Parkinson's law | UtS / Measurement |
| Lines of code as productivity | Bloated code; punishes refactor | UtS / Measurement |
| Metrics for **individuals** | Gaming + sandbagging; teams stop helping | DORA tech-lead don'ts |
| Single-channel report | Wrong audience misses signal | UtS / Measurement |
| Long detailed reports only | Ignored; embed a focused short version too | UtS / Measurement |
| Dashboard with no push | People don't visit; pair with notification | UtS / Measurement |
| MTTR from Jira ticket close time | Ticket close ≠ service restored — needs observability | DORA limitations |

## Recommended structure

### Metric stack (3 layers)

```
Outcomes  →  Definition of Outcome Done measures (SGE);
             customer / user / business behavior change
Outputs   →  DORA velocity metrics (Deploy Freq, Lead Time);
             Sprint Goal completion
Health    →  DORA stability metrics (CFR, MTTR);
             reopened items, overdue items, open bugs
```

### Cadence (DORA + UtS Measurement domain)

- **Daily** — Daily Scrum / standup for impediments and follow-up items
- **Weekly** — tech lead review of Development page; trends; outliers
- **Per sprint** — retrospective DORA review; correlation analysis;
  action items
- **Per quarter** — comparison against DORA benchmarks; goal-setting;
  methodology document review

### Reporting rules

- **Multi-audience reports.** Different formats per stakeholder type.
- **Short focused version + long detailed version** when the audience
  demands the latter.
- **Information radiator** (physical board) or **online dashboard
  with push notification** — never expect people to visit a dashboard
  on their own.

## Recovery and prevention rules (UtS Measurement)

- **Threshold ≠ ignore.** Below threshold means *this level decides*,
  not *no recovery needed*.
- **Drop correction before prevention** if forced to choose
  (firefighting culture is the failure mode).
- **Make this explicit** in the methodology if it isn't already.

## When this synthesis applies

- Designing engineering KPIs / OKRs
- Defending DORA adoption against "we already track velocity"
- Reviewing why metrics aren't moving despite team activity
- Resolving "what's our headline metric?" debates

## Cross-refs

- Performance domain: [Measurement](../performance-domains/06-measurement.md)
- DORA: [Fundamentals](../dora-metrics-jira/01-dora-fundamentals.md) ·
  [Anti-patterns](../dora-metrics-jira/05-anti-patterns.md)
- SGE: [Definition of Outcome Done](../scrum-guide-expanded/11-definition-of-outcome-done.md)
  (the "outcome" layer of the stack above)
- PMBOK 7: [Focus on value](../principles/pmbok-7/04-focus-on-value.md)
- See also: [Outcome vs Output synthesis](03-outcome-vs-output.md)
