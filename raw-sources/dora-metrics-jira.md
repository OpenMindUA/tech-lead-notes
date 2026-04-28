# DORA Metrics in Jira: Methodology, Rules, and Setup

**Purpose:** unified methodology for using DORA metrics in Jira to accurately track engineering effectiveness in teams that use the Jira + GitHub stack.

---

## 1. Introduction: Methodology and Indicators

### 1.1 What is DORA

DORA (DevOps Research and Assessment) is a Google Cloud research group that defined four key metrics correlating with overall organizational performance in software engineering. These metrics have become the industry standard for assessing DevOps maturity.

The core principle: **metrics must be read together, not in isolation**. High deployment frequency means little if change failure rate is also high; short lead time means little if production stability is poor.

### 1.2 The Four DORA Metrics

| Metric | What it measures | Category |
|--------|------------------|----------|
| **Deployment Frequency** | How often code reaches production | Velocity |
| **Lead Time for Changes** | Time from commit to production | Velocity |
| **Change Failure Rate** | % of deployments that broke production | Stability |
| **Mean Time to Restore (MTTR)** | Time to restore service after an incident | Stability |

DORA classifies teams into four levels: **Elite**, **High**, **Medium**, **Low**. Elite teams deploy multiple times a day with lead time under one hour and MTTR under one hour. Low teams deploy less than once a month.

### 1.3 How Jira Calculates Metrics on the Development Page

The Development page in Jira Premium shows both DORA metrics and supporting health indicators.

**Pull Request Cycle Time**
Median time from first commit to PR merge. Counts all pull requests linked to work items merged in the last 7 days. Indicates code review process efficiency.

**Lead Time for Changes**
Time from a commit on a branch until the code reaches a deployable state (e.g., passes all pre-release tests). The metric appears only when a CI/CD tool is connected. Without CI/CD, Open Bugs is shown instead.

**Deployment Frequency**
Average number of production deployments per week, calculated over 12 weeks (11 past weeks + the current one). Appears only after at least one real deployment on a branch / commit / PR linked to a Jira work item.

**Pull Requests**
Number of open PRs among the most recent PRs linked to Jira work items in the past 30 days.

**Vulnerabilities**
Number of open critical security vulnerabilities from connected security containers.

**Work Items and Bugs**
Not part of DORA but critical health signals:
- Reopened work items = poor work quality / unclear definition of done
- Overdue work items = planning or decomposition problems
- Open bugs = technical debt

### 1.4 Prerequisites for Metrics to Work

1. Jira integrated with a CI/CD pipeline
2. Integration with a source control system (GitHub, Bitbucket, GitLab)
3. Work item keys in branch names, commit messages, and PRs
4. At least one real deployment on a branch / commit / PR linked to Jira
5. "View development tools" permission for team members

### 1.5 Methodology Limitations

- DORA tells **what** is happening but not **why**
- MTTR in Jira reflects when a ticket was closed, not when service was actually restored — accurate MTTR requires observability tooling
- Metrics don't measure developer experience (cognitive load, flow state, feedback loop quality)
- Out-of-the-box Jira covers Deployment Frequency and partially Lead Time — Change Failure Rate and MTTR require additional process discipline

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

## 3. Managing Metrics from the GitHub Side

Three levels of maturity, from minimal to full control.

### 3.1 Basic GitHub ↔ Jira Integration (minimum)

For most teams, this is enough for Jira metrics to work:

1. **GitHub for Jira app** from the Atlassian Marketplace
2. GitHub organization linked to Jira workspace
3. Smart commits enabled
4. Developers using Jira keys in branches / commits / PRs

**What you get automatically:**
- Branch / commit / PR data appears on Jira work items
- Pull Request Cycle Time starts being calculated
- Lead Time for Changes starts being calculated (if there are deploys)
- **Deployment Frequency populates automatically** if your GitHub Actions workflow uses `environment: production` (GitHub creates a deployment record via its Deployments API, and the GitHub for Jira app picks it up)

**What you don't get:**
- Change Failure Rate — requires a separate incident-marking process
- MTTR — requires an incident management process
- Discipline enforcement (handle separately)

### 3.2 Local Enforcement: Pre-Commit / Pre-Push Hooks

Fast feedback for developers before they push. The simplest approach is via [husky](https://typicode.github.io/husky/) (Node.js) or [pre-commit](https://pre-commit.com/) (language-agnostic).

#### Husky setup

```bash
npm install --save-dev husky
npx husky init
```

#### Hook for commit message (`.husky/commit-msg`)

```bash
#!/bin/sh
commit_regex='^(PROJ|TEAM|INFRA)-[0-9]+:.+'
error_msg="❌ Commit message must start with Jira key (e.g., 'PROJ-123: Add login')"

if ! grep -qE "$commit_regex" "$1"; then
    echo "$error_msg"
    exit 1
fi
```

#### Hook for branch name (`.husky/pre-push`)

The check runs on push because branch names can be changed after creation:

```bash
#!/bin/sh
branch=$(git rev-parse --abbrev-ref HEAD)
branch_regex='^(feature|bugfix|hotfix|chore)/[A-Z]+-[0-9]+'

# Exclude main branches
if [[ "$branch" =~ ^(main|master|develop)$ ]]; then
    exit 0
fi

if ! [[ "$branch" =~ $branch_regex ]]; then
    echo "❌ Branch name must follow pattern: type/PROJ-123-description"
    echo "   Allowed types: feature, bugfix, hotfix, chore"
    exit 1
fi
```

#### Alternative: pre-commit framework

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: jira-key-in-commit
        name: Check Jira key in commit message
        entry: '^[A-Z]+-[0-9]+: .+'
        language: pygrep
        stages: [commit-msg]
```

**Important:** hooks can be bypassed via `git commit --no-verify` or simply by not installing them. Hooks alone are not enough for strict enforcement.

### 3.3 Server-Side Enforcement: GitHub Actions

GitHub Actions run on the server side and **cannot be bypassed** by a developer. This is the authoritative gate.

#### PR title check (the minimum to have)

```yaml
name: Enforce Jira ticket in PR

on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check PR title contains Jira key
        run: |
          if [[ ! "${{ github.event.pull_request.title }}" =~ \[?[A-Z]+-[0-9]+\]? ]]; then
            echo "❌ PR title must contain Jira key (e.g., [PROJ-123])"
            exit 1
          fi
          echo "✅ Jira key found in PR title"
```

This check can be made required via **branch protection rules** → "Require status checks to pass".

#### Creating an incident ticket on a failed deployment

```yaml
name: Report production incident

on:
  workflow_run:
    workflows: ["Deploy to Production"]
    types: [completed]

jobs:
  create-incident:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    steps:
      - name: Create Jira incident
        uses: atlassian/gajira-create@v3
        with:
          project: PROJ
          issuetype: Incident
          summary: "Failed production deployment: ${{ github.event.workflow_run.head_commit.message }}"
          fields: '{"labels": ["incident", "production-bug"]}'
        env:
          JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}
          JIRA_USER_EMAIL: ${{ secrets.JIRA_USER_EMAIL }}
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
```

This automatically populates Change Failure Rate.

#### When you need gajira-deploy

A separate action for sending deployment events is needed **only** when:

- Your workflow doesn't use `environment: production`
- You use third-party CI/CD (Jenkins, CircleCI, GitLab CI)
- You need manual control over the payload (e.g., explicitly associating a deploy with multiple Jira keys)

In other cases, just using GitHub Environments is enough — sync to Jira happens automatically through the GitHub for Jira app.

GitHub Environments example (recommended):

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production    # ← this alone is enough for automatic sync to Jira
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        run: ./deploy.sh
```

If you do need `gajira-deploy`:

```yaml
- name: Send deployment to Jira
  uses: atlassian/gajira-deploy@v1
  with:
    environment: production
    state: successful
    issue: ${{ steps.extract-key.outputs.jira-key }}
  env:
    JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}
    JIRA_USER_EMAIL: ${{ secrets.JIRA_USER_EMAIL }}
    JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
```

### 3.4 Open-Source Solutions for Full DORA

When native Jira isn't enough:

- **Atlassian Compass** — Atlassian's native product. Automatically tracks all four DORA metrics when GitHub and CI/CD are connected. With OpsGenie / PagerDuty, also tracks MTTR and Change Failure Rate. Best option for the Atlassian stack.
- **Dorametrix** — Node.js service that collects DORA metrics from GitHub / Bitbucket / Jira webhooks. Has ready-made GitHub Actions.
- **dora-exporter** — Prometheus exporter that collects GitHub deployment events and Jira tickets, exports metrics to Prometheus, visualizes via Grafana.
- **Four Keys** (Google Cloud) — the original Google project. Works with GitHub and GitLab. SQL-based, runs in GCP.

### 3.5 Recommended Stack

For a team that wants a balance of simplicity and effectiveness:

| Layer | What to use |
|-------|-------------|
| **Local** | Husky + commit-msg hook + pre-push hook |
| **CI** | GitHub Action for PR title check + branch protection rules |
| **Deploy** | GitHub Actions with `environment: production` (no gajira-deploy) |
| **Integration** | GitHub for Jira app |
| **Workflow** | Jira Automation for auto-transitions |
| **Incidents** | Dedicated `Incident` issue type + GitHub Action on failed deploys |

This is enough for full DORA metrics in Jira without external services.

---

## 4. Jira Setup Checklist

### 4.1 Administrative Setup

- [ ] Jira plan at the **Premium** level (required for the Development page)
- [ ] **Development** feature enabled in the project (Space settings → Features)
- [ ] **"View development tools"** permission granted to all team members
- [ ] **"View aggregated data"** permission granted to tech lead and manager
- [ ] Users with GitHub accounts mapped to Jira users

### 4.2 GitHub Integration

- [ ] **GitHub for Jira** app installed from the Atlassian Marketplace
- [ ] GitHub organization linked to Jira workspace
- [ ] All relevant repositories included in the integration
- [ ] Smart commits enabled
- [ ] OAuth link between accounts active (no sync errors)

### 4.3 GitHub Environments (for Deployment Frequency)

- [ ] Production workflow uses `environment: production`
- [ ] Staging workflow uses `environment: staging`
- [ ] Verified: after a deploy, Jira tickets show the deployment in the Development panel
- [ ] (Optional) Required reviewers configured on the production environment

### 4.4 Workflow

- [ ] Workflow has statuses: `To Do`, `In Progress`, `In Review`, `Done` (minimum)
- [ ] Recommended additions: `Ready for Deploy`, `Blocked` for better accuracy
- [ ] Configured `In Progress` ↔ `Blocked` transitions from regular statuses
- [ ] `Done` → `In Progress` transition forbidden (only via creating a new issue)
- [ ] Definition of Done documented and bound to the `Done` status

### 4.5 Issue Types and Fields

- [ ] **Incident** issue type created or `incident` label configured
- [ ] `production-bug` label set up for post-deployment bugs
- [ ] (Optional) Custom field **"Deployed Date"** for accurate MTTR
- [ ] (Optional) Custom field **"Production Impact"** for severity
- [ ] Required fields on creation: summary, description, acceptance criteria

### 4.6 Jira Automation

Create the following automation rules (Project settings → Automation):

- [ ] **Auto-transition to In Progress** when a branch with the ticket key is created
- [ ] **Auto-transition to In Review** when a PR with the ticket key is opened
- [ ] **Auto-transition to Done** when a deployment event arrives in production
- [ ] **Notify reviewer** on PR creation (Slack/email)
- [ ] **Reminder** for tickets sitting in `In Review` more than 24 hours
- [ ] **Alert** for tickets with no activity for more than 3 days

### 4.7 GitHub Side: Hooks and Actions

- [ ] **Husky / pre-commit** installed in the repository
- [ ] **commit-msg hook** validates the message format with a Jira key
- [ ] **pre-push hook** validates branch name
- [ ] **GitHub Action** for checking the Jira key in PR title
- [ ] **Branch protection rule** on main: required status check = PR title check
- [ ] **GitHub Action** for creating an incident ticket on failed production deploys
- [ ] CODEOWNERS file for automatic reviewers

### 4.8 Team: Discipline and Communication

- [ ] Naming conventions for branches / commits / PRs shared with the team
- [ ] Onboarding session completed (30-40 minutes)
- [ ] Definition of Done shared and visible
- [ ] 10 minutes allocated at retro for DORA metrics review

### 4.9 Verification (2-3 weeks after setup)

- [ ] **Pull Request Cycle Time** shows a non-zero value
- [ ] **Lead Time for Changes** has real data
- [ ] **Deployment Frequency** shows a real cadence matching actual releases
- [ ] In 5 random work items, you can see linked commits / PRs / deployments
- [ ] No "orphan" PRs (without a Jira work item)
- [ ] No tickets in `Done` without a deployment event
- [ ] Reopen rate < 10% of total closed tickets

### 4.10 Ongoing Monitoring

- [ ] Tech lead reviews the Development page weekly
- [ ] Per sprint — detailed outlier review at retrospective
- [ ] Per quarter — comparison against DORA benchmarks
- [ ] Per quarter — review and update of this document

---

## Appendix: Common Pitfalls and How to Avoid Them

| Symptom | Likely cause | Solution |
|---------|--------------|----------|
| Deployment Frequency = 0 | GitHub Environments not used | Add `environment: production` to the workflow |
| Lead Time too high | Tasks too large or stuck in `In Review` | Decomposition + reviewer SLA |
| Cycle Time fluctuates | Reopening old tickets | Forbid reopen, create new issues |
| Metrics empty | No Jira key in branches/commits | Add enforcement (hooks + GitHub Action) |
| Change Failure Rate = 0 (suspicious) | Production bugs not labeled | `production-bug` label + automation |
| Many overdue items | Poor sprint planning | Decomposition + capacity checks |
| Hooks bypassed via `--no-verify` | Local enforcement only | Add a GitHub Action as the authoritative gate |

---

**Document version:** 1.1
