---
title: Anti-patterns and common pitfalls
type: anti-patterns
source: docs/sources/dora-metrics-jira/05-appendix-common-pitfalls-and-how-to-avoid-them.md
license: CC-BY-SA-4.0
authors_of_source: openmind
tags: [dora, anti-patterns, pitfalls, troubleshooting, deployment-frequency, lead-time, change-failure-rate]
---

# Anti-patterns and common pitfalls

**TL;DR:** Diagnostic table mapping symptom → likely cause →
solution for the most common DORA-in-Jira failures. Plus the
cross-cutting "do-nots" extracted from developer and tech-lead
discipline.

## Symptom → cause → solution

| Symptom | Likely cause | Solution |
|---------|--------------|----------|
| **Deployment Frequency = 0** | GitHub Environments not used | Add `environment: production` to the workflow |
| **Lead Time too high** | Tasks too large or stuck in `In Review` | Decomposition + reviewer SLA |
| **Cycle Time fluctuates** | Reopening old tickets | Forbid reopen; create new issues |
| **Metrics empty** | No Jira key in branches/commits | Add enforcement (hooks + GitHub Action) |
| **Change Failure Rate = 0** (suspicious) | Production bugs not labeled | `production-bug` label + automation |
| **Many overdue items** | Poor sprint planning | Decomposition + capacity checks |
| **Hooks bypassed via `--no-verify`** | Local enforcement only | Add a GitHub Action as the **authoritative gate** |

## Cross-cutting do-nots

### Developer do-nots
- Close a ticket "early" so it doesn't sit in the backlog.
- Reopen a ticket instead of creating a new one.
- Commit without a Jira key.
- Keep one ticket open for multiple sprints.
- Link a single ticket to dozens of PRs from different features.

### Tech lead do-nots
- Use DORA metrics to **evaluate individual developers**.
- **Optimize one metric** at the expense of another.
- Bulk-close tickets at sprint end.
- Reopen old tickets instead of creating new ones.
- Allow the team to bypass naming conventions.

## Reading-together checks (sanity)

| Combination | Diagnosis |
|---|---|
| High Deploy Freq + High CFR | Reckless velocity — improve quality before deploying more |
| High Deploy Freq + Low CFR + Low MTTR | Healthy "Elite" pattern |
| Low Lead Time + High CFR | Skipped quality gates |
| Low CFR + High MTTR | Few failures but recovery is slow when they happen |
| All metrics empty after 2 weeks | Setup verification (item 9 of the checklist) was never done |

## When this applies

- Triage during ongoing monitoring (weekly Development page review)
- Quarterly metrics health check
- Onboarding a tech lead — share this card as the "what could go
  wrong" guide
- Coaching team out of metric-gaming behaviors

## Cross-refs

- [DORA fundamentals — read-together principle](01-dora-fundamentals.md)
- [Ticket discipline — full do-not lists](02-ticket-discipline.md)
- [GitHub-side enforcement — server-side gate](03-github-side.md)
- NUPP [Don't do anything without clear purpose](../principles/nupp/05-clear-purpose.md)
  — metric-gaming is purposeless ceremony
- PMBOK 7 [Build quality in](../principles/pmbok-7/08-quality.md)
  — "what you measure becomes the goal" (Measurement domain)
- Performance domain: [Measurement](../performance-domains/06-measurement.md)
  — Parkinson's law, proxy-metric warning

## Source

Full text: [`docs/sources/dora-metrics-jira/05-appendix-common-pitfalls-and-how-to-avoid-them.md`](../../sources/dora-metrics-jira/05-appendix-common-pitfalls-and-how-to-avoid-them.md)
