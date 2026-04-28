---
title: GitHub-side enforcement (integration, hooks, Actions, OSS tools)
type: integration
source: docs/sources/dora-metrics-jira/03-3-managing-metrics-from-the-github-side.md
license: CC-BY-SA-4.0
authors_of_source: openmind
tags: [dora, github, husky, github-actions, gajira, branch-protection, oss-tooling]
---

# GitHub-side enforcement

**TL;DR:** Three maturity levels — **basic integration → local
hooks → server-side GitHub Actions**. Hooks alone are bypassable;
**GitHub Actions are the authoritative gate**. For most teams,
**`environment: production`** in a GitHub Actions workflow is
enough to populate Deployment Frequency in Jira automatically — no
`gajira-deploy` needed.

## Maturity ladder

### Level 1 — Basic GitHub ↔ Jira integration (minimum)

Components:
1. **GitHub for Jira** app (Atlassian Marketplace).
2. GitHub organization linked to Jira workspace.
3. Smart commits enabled.
4. Developers using Jira keys in branches/commits/PRs.

**Auto-populated:**
- Branch / commit / PR data on Jira work items.
- **Pull Request Cycle Time** starts being calculated.
- **Lead Time for Changes** starts being calculated (if there are deploys).
- **Deployment Frequency** populates automatically when GitHub
  Actions workflow uses `environment: production` (GitHub creates a
  Deployments-API record; the GitHub-for-Jira app picks it up).

**Not covered:**
- **Change Failure Rate** — needs a separate incident-marking process.
- **MTTR** — needs an incident management process.
- Discipline enforcement.

### Level 2 — Local hooks (Husky / pre-commit)

Fast feedback **before** push. Bypassable via `--no-verify` or
"don't install".

**Husky setup**
```bash
npm install --save-dev husky
npx husky init
```

**`.husky/commit-msg`** — Jira key in commit message
```bash
#!/bin/sh
commit_regex='^(PROJ|TEAM|INFRA)-[0-9]+:.+'
if ! grep -qE "$commit_regex" "$1"; then
    echo "❌ Commit message must start with Jira key (e.g., 'PROJ-123: Add login')"
    exit 1
fi
```

**`.husky/pre-push`** — Jira key in branch name (push-time because
branch can be renamed)
```bash
#!/bin/sh
branch=$(git rev-parse --abbrev-ref HEAD)
branch_regex='^(feature|bugfix|hotfix|chore)/[A-Z]+-[0-9]+'
if [[ "$branch" =~ ^(main|master|develop)$ ]]; then exit 0; fi
if ! [[ "$branch" =~ $branch_regex ]]; then
    echo "❌ Branch name must follow pattern: type/PROJ-123-description"
    exit 1
fi
```

**Alternative:** the language-agnostic `pre-commit` framework with
a `pygrep` rule in `.pre-commit-config.yaml`.

> **Important:** hooks are bypassable. **Hooks alone are not enough
> for strict enforcement.**

### Level 3 — Server-side GitHub Actions (authoritative)

Cannot be bypassed by a developer.

**PR title check (the minimum to have)**
```yaml
on:
  pull_request:
    types: [opened, edited, synchronize]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - run: |
          if [[ ! "${{ github.event.pull_request.title }}" =~ \[?[A-Z]+-[0-9]+\]? ]]; then
            echo "❌ PR title must contain Jira key (e.g., [PROJ-123])"
            exit 1
          fi
```

Make it required via **Branch protection rules → Require status
checks to pass**.

**Failed-deployment → incident ticket** (auto-populates CFR)
```yaml
on:
  workflow_run:
    workflows: ["Deploy to Production"]
    types: [completed]
jobs:
  create-incident:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    steps:
      - uses: atlassian/gajira-create@v3
        with:
          project: PROJ
          issuetype: Incident
          summary: "Failed production deployment: …"
          fields: '{"labels": ["incident", "production-bug"]}'
        env: { JIRA_BASE_URL: …, JIRA_USER_EMAIL: …, JIRA_API_TOKEN: … }
```

## Deployment events — `environment: production` vs `gajira-deploy`

**Default (recommended):** rely on GitHub Environments.
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production    # this alone syncs to Jira automatically
    steps: [...]
```

**Use `gajira-deploy` only when:**
- Workflow doesn't use `environment: production`.
- Third-party CI/CD (Jenkins, CircleCI, GitLab CI).
- Manual control over payload (e.g. associating one deploy with
  multiple Jira keys).

## Open-source DORA tools (when native Jira isn't enough)

| Tool | Notes |
|---|---|
| **Atlassian Compass** | Native Atlassian product; auto-tracks all 4 metrics with GitHub + CI/CD; with OpsGenie/PagerDuty also tracks MTTR + CFR. Best for Atlassian stack. |
| **Dorametrix** | Node.js service; webhooks from GitHub/Bitbucket/Jira; ready GitHub Actions. |
| **dora-exporter** | Prometheus exporter; GitHub deployment events + Jira; Grafana dashboards. |
| **Four Keys** (Google Cloud) | Original Google project; GitHub + GitLab; SQL-based; runs in GCP. |

## Recommended stack (balance of simplicity + effectiveness)

| Layer | What to use |
|---|---|
| Local | Husky + commit-msg hook + pre-push hook |
| CI | GitHub Action for PR title check + branch protection |
| Deploy | GitHub Actions with `environment: production` (no `gajira-deploy`) |
| Integration | GitHub for Jira app |
| Workflow | Jira Automation for auto-transitions |
| Incidents | Dedicated `Incident` issue type + GitHub Action on failed deploys |

> Sufficient for **full DORA in Jira without external services**.

## When this applies

- Setting up CI/CD-Jira integration from scratch
- Migrating from manual workflow management to automation
- Picking the right enforcement layer (don't skip server-side)
- Choosing whether to add `gajira-deploy` to existing workflows

## Anti-patterns

- Hooks-only enforcement — bypassable via `--no-verify`
- Adding `gajira-deploy` when `environment: production` would do
- Branch protection without the PR-title check as a required status
- No incident-creation Action → CFR stays at 0 even when prod breaks
- OSS tooling adopted before native Jira capabilities exhausted

## Cross-refs

- [Ticket discipline](02-ticket-discipline.md) — the rules these
  Actions enforce
- [Jira setup checklist](04-jira-setup-checklist.md)
- [DORA fundamentals](01-dora-fundamentals.md) — what the metrics
  actually measure

## Source

Full text: [`docs/sources/dora-metrics-jira/03-3-managing-metrics-from-the-github-side.md`](../../sources/dora-metrics-jira/03-3-managing-metrics-from-the-github-side.md)
