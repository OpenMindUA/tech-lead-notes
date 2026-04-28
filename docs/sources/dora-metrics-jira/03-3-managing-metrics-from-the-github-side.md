---
title: 3. Managing Metrics from the GitHub Side
source_id: dora-metrics-jira
chapter: 3. Managing Metrics from the GitHub Side
chapter_index: 3
source_url: (self-authored)
source_version: 1.1
source_lines: 207-419
license: CC-BY-SA-4.0
authors: openmind
tags: [dora, metrics, jira, github, engineering-effectiveness, 3-managing-metrics-from-the-github-side]
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
