---
title: 2. Ticket Discipline Rules
source_id: dora-metrics-jira
chapter: 2. Ticket Discipline Rules
chapter_index: 2
source_url: (self-authored)
source_version: 1.1
source_lines: 68-206
license: CC-BY-SA-4.0
authors: openmind
tags: [dora, metrics, jira, github, engineering-effectiveness, 2-ticket-discipline-rules]
---
## 2. Ticket Discipline Rules

### 2.1 General Principles

1. **One ticket = one logical change.** If a ticket needs more than one PR, split it.
2. **Size matters.** Ten half-day tickets beat one week-long ticket.
3. **A ticket is alive until the code is in production.** Don't close before actual deployment.
4. **Workflow needs automation** — manual status drag-and-drop creates errors.

### 2.2 Rules for Developers

#### Branch naming

Every branch contains a Jira key:

```
feature/PROJ-123-add-login-validation
bugfix/PROJ-456-fix-null-pointer-checkout
hotfix/PROJ-789-payment-timeout
chore/PROJ-321-update-dependencies
```

**Forbidden:**
- Branches without a key: `my-feature`, `quickfix`, `johns-branch`
- Multiple keys in one branch (a signal that the task should be split)

#### Commit messages

The first line of the commit contains a Jira key:

```
PROJ-123: Add email format validation on login form

- Added regex check for email format
- Show inline error message
- Added unit tests for edge cases
```

If a commit relates to multiple tickets — that's a problem, split the work.

#### Pull Requests

- Title starts with the key: `[PROJ-123] Add email validation`
- Description references the ticket (Jira auto-links from the key in the title)
- PR is no longer than 400 lines of changes, ideally up to 200
- One PR = one task = one logical increment

**Forbidden:**
- Combining unrelated changes in a single PR
- Leaving a PR in Draft for more than two days
- Merging your own PR without code review (except hotfixes with post-merge review)

#### Status workflow

| Developer action | Ticket status | Who moves it |
|------------------|---------------|--------------|
| Pick up the task | `To Do` → `In Progress` | Developer manually or automation on branch creation |
| Open a PR | `In Progress` → `In Review` | Automation on PR open |
| PR merged | `In Review` → `Ready for Deploy` | Automation on merge |
| Production deploy | `Done` (final) | Automation on deployment event |

The developer **does not close the ticket manually** before the actual deployment.

#### Working with bugs

A separate discipline that directly affects Change Failure Rate and MTTR:

- **Every production bug = a new ticket** with type `Bug` or label `production-bug`
- Don't reopen old tickets, even for similar issues — reopen breaks cycle time statistics
- A production bug is created **at the moment of detection**, not when work begins
- For critical bugs, add the `incident` label — this enables MTTR tracking
- Close a bug only after the fix is actually deployed to production

#### What developers should not do

- ❌ Close a ticket "early" so it doesn't sit in the backlog
- ❌ Reopen a ticket instead of creating a new one
- ❌ Commit without a Jira key
- ❌ Keep one ticket open for multiple sprints — better to split
- ❌ Link a single ticket to dozens of PRs from different features

### 2.3 Rules for Tech Lead

#### Task decomposition

**The 80% rule:** if more than 80% of sprint tasks are completed in 1-2 days, metrics will be healthy. Tasks lasting 5+ days automatically degrade lead time and increase failure risk.

**Before each sprint**, verify for every task:
- Has a clear definition of done
- Can be completed in 1-3 days by one person
- No blocking dependencies
- Testing approach is clear

#### Workflow oversight

Weekly (during retro/planning) check:
- Tickets with no activity for more than 3 days — why?
- Tickets in `In Review` for more than 1 day — who is blocking review?
- Tickets without linked PRs/commits — is work actually happening?
- PRs open for more than 2 days without merge — why?

#### Reviewing metrics

**Weekly:** look at the Development page, note the trend, find outliers.

**Per sprint (at retrospective):** trends over 2-4 weeks, correlations between metrics, action items.

**Per quarter:** compare against DORA benchmarks, set goals.

#### Handling outliers

When a ticket shows anomalous cycle time:

1. Don't blame an individual — it's a system signal
2. Ask: was the task too big? Blocked? Without clear DoD?
3. Look for patterns: do similar tasks always exceed the median?
4. Fix the process, not the people

#### Definition of Done

DoD must include:
- ✅ Code is in production (not just merged)
- ✅ Tests are written and passing
- ✅ Documentation is updated
- ✅ Acceptance criteria met
- ✅ Production monitoring confirms it works

Without enforcement, DoD degrades within 2-3 sprints.

#### What tech leads should not do

- ❌ Use DORA metrics to evaluate individual developers
- ❌ Optimize one metric at the expense of another
- ❌ Bulk-close tickets at sprint end
- ❌ Reopen old tickets instead of creating new ones
- ❌ Allow the team to bypass naming conventions

---
