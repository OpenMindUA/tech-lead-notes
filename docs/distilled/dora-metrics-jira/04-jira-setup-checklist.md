---
title: Jira setup checklist
type: checklist
source: docs/sources/dora-metrics-jira/04-4-jira-setup-checklist.md
license: CC-BY-SA-4.0
authors_of_source: openmind
tags: [dora, jira, setup, checklist, automation, workflow, environments]
---

# Jira setup checklist

**TL;DR:** End-to-end actionable checklist for getting DORA metrics
working in Jira Premium with GitHub. Ten sections from
administrative setup through ongoing monitoring. Verification
expected **2-3 weeks** after setup.

## 1. Administrative setup
- Jira plan at **Premium** (required for the Development page).
- **Development** feature enabled in the project.
- *"View development tools"* permission for all team members.
- *"View aggregated data"* permission for tech lead and manager.
- Users with GitHub accounts mapped to Jira users.

## 2. GitHub integration
- **GitHub for Jira** app installed.
- GitHub organization linked to Jira workspace.
- All relevant repos included in integration.
- Smart commits enabled.
- OAuth link active (no sync errors).

## 3. GitHub Environments (for Deployment Frequency)
- Production workflow uses `environment: production`.
- Staging workflow uses `environment: staging`.
- Verified post-deploy: Jira tickets show the deployment.
- (Optional) Required reviewers configured on the production environment.

## 4. Workflow
- Statuses: `To Do`, `In Progress`, `In Review`, `Done` (minimum).
- Recommended: `Ready for Deploy`, `Blocked` for accuracy.
- `In Progress` ↔ `Blocked` transitions configured.
- **`Done` → `In Progress` transition forbidden** (only via new issue).
- **Definition of Done documented and bound to `Done` status.**

## 5. Issue types and fields
- **Incident** issue type created (or `incident` label configured).
- `production-bug` label set up.
- (Optional) Custom field **"Deployed Date"** for accurate MTTR.
- (Optional) Custom field **"Production Impact"** for severity.
- Required fields on creation: summary, description, acceptance criteria.

## 6. Jira Automation rules
- **Auto-transition to In Progress** on branch with ticket key creation.
- **Auto-transition to In Review** on PR open with ticket key.
- **Auto-transition to Done** on production deployment event.
- **Notify reviewer** on PR creation (Slack/email).
- **Reminder** for tickets in `In Review` >24 h.
- **Alert** for tickets with no activity >3 days.

## 7. GitHub side: hooks and actions
- **Husky / pre-commit** installed in the repo.
- **commit-msg** hook validates Jira key format.
- **pre-push** hook validates branch name.
- **GitHub Action** for Jira-key-in-PR-title check.
- **Branch protection rule** on `main`: required check = PR title check.
- **GitHub Action** for failed-prod-deploy → create incident ticket.
- **CODEOWNERS** for automatic reviewers.

## 8. Team: discipline and communication
- Naming conventions shared with team.
- Onboarding session completed (30-40 minutes).
- Definition of Done shared and visible.
- **10 minutes at retro for DORA metrics review.**

## 9. Verification (2-3 weeks after setup)
- **Pull Request Cycle Time** non-zero.
- **Lead Time for Changes** has real data.
- **Deployment Frequency** matches actual release cadence.
- 5 random work items show linked commits / PRs / deployments.
- **No "orphan" PRs** (without a Jira work item).
- **No tickets in `Done` without a deployment event.**
- **Reopen rate < 10%** of total closed tickets.

## 10. Ongoing monitoring
- Tech lead reviews Development page **weekly**.
- **Per sprint** — outlier review at retrospective.
- **Per quarter** — comparison against DORA benchmarks.
- **Per quarter** — review and update of the methodology document.

## When this applies

- Greenfield Jira project setup
- Repairing a project where DORA metrics show empty or wrong data
- Setting up a new team that joins an existing Jira instance
- Auditing readiness for a metrics-driven engineering org

## Anti-patterns

- Skipping verification — going live with metrics that don't actually
  measure what you think
- `Done → In Progress` transition allowed → reopen pollution
- Setup completed but team **never trained** on naming conventions
- Automation rules created but not monitored — silent rule failures
- DoD documented but not bound to the `Done` status — toothless

## Cross-refs

- [Ticket discipline](02-ticket-discipline.md) — what the team must
  *do* once setup is complete
- [GitHub-side enforcement](03-github-side.md) — items 3, 7
- [Anti-patterns](05-anti-patterns.md)

## Source

Full text: [`docs/sources/dora-metrics-jira/04-4-jira-setup-checklist.md`](../../sources/dora-metrics-jira/04-4-jira-setup-checklist.md)
