---
title: PR / change review with DORA discipline
type: agent-recipe
use_when: Reviewing a pull request before merge — checking branch / commit / PR hygiene that powers DORA metrics, and verifying production-gated DoD
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/dora-metrics-jira/01-dora-fundamentals.md
  - docs/distilled/dora-metrics-jira/02-ticket-discipline.md
  - docs/distilled/dora-metrics-jira/03-github-side.md
  - docs/distilled/dora-metrics-jira/05-anti-patterns.md
  - docs/distilled/synthesis/01-done-and-quality.md
load_tier3_optional:
  - docs/sources/dora-metrics-jira/02-2-ticket-discipline-rules.md
output_shape: review-checklist + per-line comments + merge recommendation
license: CC-BY-SA-4.0
tags: [recipe, agent, pr-review, dora, ticket-discipline]
---

# PR / change review with DORA discipline

## Use this when

A PR is open and you want a review that goes beyond "does the code work?" to also catch: missing Jira link, branch-name vs ticket mismatch, commit messages that won't parse for Lead Time, missing production-gated checks, work that should be split, or anti-patterns that will distort the team's DORA numbers.

## Cards to load

| Card | Why |
|---|---|
| DORA fundamentals | The four metrics; why a single PR matters for Lead Time + CFR |
| Ticket discipline | Branch / commit / PR conventions; production-gated DoD definition |
| GitHub-side enforcement | What integrations / hooks / Actions should already be enforcing |
| Anti-patterns | Symptom→cause→solution table for common ticket-discipline failures |
| Synthesis: Done & quality | DoD vs DoOD vs Definition of Outcome Done — where this PR's "done" sits |

## Prompt skeleton

```
You are reviewing a pull request for a tech-lead. Apply DORA discipline
and the team's Definition of Output Done. Use only the loaded cards as
authority; cite which card backs each finding.

Inputs:
- PR_URL: <PR URL or #number>
- DIFF: <pasted diff or path>
- LINKED_TICKET: <Jira/Linear key or "none">
- TARGET_ENV: <staging|production>

Tasks:
1. Verify ticket linkage (branch name, commit prefixes, PR title).
2. Check commit messages against the team's conventional-commit /
   ticket-prefix rules.
3. Identify if this PR mixes concerns that should split (more than
   one ticket; tests + refactor + feature in one).
4. Check that production-gated DoD items are addressed: tests added,
   monitoring touched if behavior changed, rollback plan if risky.
5. Flag any change that will distort DORA metrics (e.g. squash that
   loses the deploy timestamp; CFR-hiding by labeling a hotfix as
   feature).
6. Output: review checklist + per-line comments + merge recommendation
   (approve / request-changes / block).

Constraints:
- Do not invent rules not in the cards.
- If a rule isn't covered by the cards, say so explicitly.
```

## Expected output

```
## Review summary
Recommendation: <approve | request-changes | block>
DORA risk: <low | medium | high>

## Findings
| # | Severity | Finding | Card |
|---|---|---|---|
| 1 | high | Branch name `feat-stuff` doesn't include ticket key | ticket-discipline |
| 2 | med  | Commit "wip" violates conventional commits | ticket-discipline |
| 3 | low  | No test added for new branch in `auth.py:42` | DoD synthesis |

## Per-line comments
- `auth.py:42` — Add a test for the new code path. Per Definition of Output Done, behavior changes require tests.
- ...

## Merge gates
- [ ] Ticket linked
- [ ] Conventional commit messages
- [ ] Tests cover changed behavior
- [ ] CFR-relevant? if yes, link incident
```

## Anti-pattern (do NOT use this recipe for)

- Pure design / architecture review of a large change — use a different recipe (or invoke `code-review` separately).
- "Is this code clean?" — DORA discipline is orthogonal to code quality. The cards don't speak to readability, naming, or design patterns.
- Rubber-stamping. The checklist is a *floor*, not a ceiling.

## Cross-refs

- [Sprint Review prep — output vs outcome](02-sprint-review-prep.md) — what comes after merge
- [Forecasting & SLE](09-forecasting-and-sle.md) — how this PR's Cycle Time enters the SLE
- DORA Tier-3 source: [`docs/sources/dora-metrics-jira/`](../sources/dora-metrics-jira/index.md)
