---
title: Ticket discipline (developer + tech lead + DoD)
type: discipline
source: docs/sources/dora-metrics-jira/02-2-ticket-discipline-rules.md
license: CC-BY-SA-4.0
authors_of_source: openmind
tags: [dora, ticket-discipline, branch-naming, definition-of-done, decomposition, pull-requests]
---

# Ticket discipline

**TL;DR:** Discipline is the **prerequisite for trustworthy DORA
metrics**. Four general principles, strict naming/sizing for
developers, oversight rules for tech leads, and a **production-
gated Definition of Done**.

## General principles

1. **One ticket = one logical change.** If it needs more than one
   PR, split it.
2. **Size matters.** Ten half-day tickets beat one week-long ticket.
3. **A ticket is alive until the code is in production.** Don't
   close before actual deployment.
4. **Workflow needs automation.** Manual status drag-and-drop
   creates errors.

## Developer rules

### Branch naming
```
feature/PROJ-123-add-login-validation
bugfix/PROJ-456-fix-null-pointer-checkout
hotfix/PROJ-789-payment-timeout
chore/PROJ-321-update-dependencies
```
- Every branch contains a Jira key.
- **Forbidden:** keyless branches (`my-feature`), multiple keys in
  one branch (a signal to split).

### Commit messages
- First line: `PROJ-123: <imperative summary>`.
- Body: bulleted details.
- A commit linked to multiple tickets → split the work.

### Pull Requests
- Title starts with the key: `[PROJ-123] …`.
- Description references the ticket (Jira auto-links from title).
- **Size:** ≤400 lines; ideally ≤200.
- **One PR = one task = one logical increment.**
- **Forbidden:** combining unrelated changes; Draft >2 days;
  self-merging without review (except hotfixes with post-merge review).

### Status workflow

| Action | Status transition | Who moves it |
|---|---|---|
| Pick up the task | `To Do` → `In Progress` | manual or automation on branch creation |
| Open a PR | `In Progress` → `In Review` | automation on PR open |
| PR merged | `In Review` → `Ready for Deploy` | automation on merge |
| Production deploy | → `Done` (final) | automation on deployment event |

**The developer does not close the ticket manually before actual
deployment.**

### Working with bugs
- **Every production bug = a new ticket** (`Bug` type or
  `production-bug` label).
- **Don't reopen** old tickets — reopen breaks cycle-time stats.
- Created **at moment of detection**, not when work begins.
- For critical bugs add `incident` label → enables MTTR tracking.
- Close only after the **fix is actually deployed** to production.

### Developer don'ts

- ❌ Close a ticket "early" so it doesn't sit in the backlog
- ❌ Reopen a ticket instead of creating a new one
- ❌ Commit without a Jira key
- ❌ Keep one ticket open for multiple sprints
- ❌ Link a single ticket to dozens of PRs from different features

## Tech lead rules

### Decomposition (the 80% rule)
> If **more than 80% of sprint tasks** are completed in **1-2
> days**, metrics will be healthy. Tasks lasting 5+ days
> automatically degrade lead time and increase failure risk.

**Per-task pre-sprint check:**
- Has a clear Definition of Done.
- Can be completed in **1-3 days** by one person.
- No blocking dependencies.
- Testing approach is clear.

### Workflow oversight (weekly)
- Tickets with **no activity for >3 days** — why?
- Tickets in `In Review` for **>1 day** — who's blocking review?
- Tickets **without linked PRs/commits** — is work actually happening?
- PRs open **>2 days** without merge — why?

### Reviewing metrics
- **Weekly:** Development page; trend; outliers.
- **Per sprint (retro):** trends over 2-4 weeks; correlations;
  action items.
- **Per quarter:** compare against DORA benchmarks; set goals.

### Handling outliers
1. **Don't blame an individual** — it's a system signal.
2. Ask: was the task **too big**? **Blocked**? Without **clear DoD**?
3. Look for **patterns** — do similar tasks always exceed median?
4. **Fix the process, not the people.**

### Definition of Done (DORA-aware)

DoD must include:
- ✅ **Code is in production** (not just merged).
- ✅ Tests written and passing.
- ✅ Documentation updated.
- ✅ Acceptance criteria met.
- ✅ Production monitoring confirms it works.

> "Without enforcement, DoD degrades within 2-3 sprints."

### Tech lead don'ts

- ❌ Use DORA metrics to evaluate individual developers
- ❌ Optimize one metric at the expense of another
- ❌ Bulk-close tickets at sprint end
- ❌ Reopen old tickets instead of creating new ones
- ❌ Allow the team to bypass naming conventions

## When this applies

- Establishing or repairing ticket discipline in a team
- Onboarding new developers (30-40 minute session)
- Coaching tech leads on metrics review at retros
- Designing automation rules in Jira

## Cross-refs

- [DORA fundamentals](01-dora-fundamentals.md)
- [GitHub-side enforcement](03-github-side.md) — automation that
  enforces these rules
- Scrum: [Definition of Done (Increment)](../scrum-guide/16-increment.md)
- SGE: [Definition of Output Done](../scrum-guide-expanded/12-definition-of-output-done.md)
  — same idea, broader artifact framing
- Performance domain: [Project Work](../performance-domains/05-project-work.md)
  — follow-up items pattern

## Source

Full text: [`docs/sources/dora-metrics-jira/02-2-ticket-discipline-rules.md`](../../sources/dora-metrics-jira/02-2-ticket-discipline-rules.md)
