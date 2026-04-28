---
title: DORA fundamentals
type: methodology
source: docs/sources/dora-metrics-jira/01-1-introduction-methodology-and-indicators.md
license: CC-BY-SA-4.0
authors_of_source: openmind
tags: [dora, fundamentals, four-metrics, performance-levels, jira-development-page]
---

# DORA fundamentals

**TL;DR:** DORA defines **four metrics** correlating with org-level
software performance. **Read them together** — Velocity ones
(Deployment Frequency, Lead Time) without Stability ones (CFR,
MTTR) are misleading. Out-of-the-box Jira Premium covers Deployment
Frequency + partial Lead Time; CFR and MTTR require process
discipline.

## The four metrics

| Metric | What it measures | Category |
|--------|------------------|----------|
| **Deployment Frequency** | How often code reaches production | Velocity |
| **Lead Time for Changes** | Time from commit to production | Velocity |
| **Change Failure Rate (CFR)** | % of deployments that broke production | Stability |
| **Mean Time to Restore (MTTR)** | Time to restore service after an incident | Stability |

## Performance levels

| Level | Deployment Frequency | Lead Time | MTTR |
|---|---|---|---|
| **Elite** | multiple per day | <1 hour | <1 hour |
| **High** | … | … | … |
| **Medium** | … | … | … |
| **Low** | <1 per month | (long) | (long) |

## Read-together principle

- High deploy frequency + high CFR = noise.
- Short lead time + poor stability = recklessness.
- Always evaluate Velocity alongside Stability.

## Jira Development page (Premium) — what it shows

- **Pull Request Cycle Time** — median time from first commit to PR
  merge; counts PRs linked to work items merged in the last 7 days.
- **Lead Time for Changes** — only when CI/CD is connected; without
  CI/CD shows *Open Bugs* instead.
- **Deployment Frequency** — average per week over 12 weeks (11
  past + current); requires at least one real deployment on a
  branch/commit/PR linked to a Jira work item.
- **Pull Requests** — open PRs among recent ones linked to Jira
  work items in last 30 days.
- **Vulnerabilities** — open critical security vulnerabilities from
  connected security tools.
- **Work Items / Bugs (supporting health):**
    - Reopened items → poor work quality / unclear DoD
    - Overdue items → planning or decomposition problems
    - Open bugs → technical debt

## Prerequisites for metrics to populate

1. Jira integrated with a CI/CD pipeline.
2. Integration with source control (GitHub / Bitbucket / GitLab).
3. **Work item keys in branch names, commit messages, and PRs.**
4. At least one real deployment on a branch/commit/PR linked to Jira.
5. *"View development tools"* permission for team members.

## Methodology limitations

- DORA tells **what** is happening, not **why**.
- Jira's MTTR reflects **ticket close time**, not actual service
  restoration — accurate MTTR requires observability tooling.
- DORA does not measure **developer experience** (cognitive load,
  flow state, feedback-loop quality).
- Out-of-the-box Jira covers Deployment Frequency + partial Lead
  Time; **CFR and MTTR require additional process discipline**.

## When this applies

- Setting up engineering effectiveness measurement
- Evaluating DevOps maturity
- Designing Sprint retrospective DORA review
- Defining engineering OKRs/KPIs

## Anti-patterns

- Reading any metric **in isolation**
- Using DORA to evaluate **individual** developers
- Optimizing **one metric** at the expense of another
- Treating **Jira MTTR** as authoritative without observability

## Cross-refs

- [Ticket discipline](02-ticket-discipline.md)
- [Jira setup checklist](04-jira-setup-checklist.md)
- [SGE Definition of Outcome Done](../scrum-guide-expanded/11-definition-of-outcome-done.md)
  — outcome measurement parallel
- PMBOK 7 [Build quality in](../principles/pmbok-7/08-quality.md)

## Source

Full text: [`docs/sources/dora-metrics-jira/01-1-introduction-methodology-and-indicators.md`](../../sources/dora-metrics-jira/01-1-introduction-methodology-and-indicators.md)
