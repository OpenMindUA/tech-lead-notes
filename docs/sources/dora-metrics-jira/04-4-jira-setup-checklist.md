---
title: 4. Jira Setup Checklist
source_id: dora-metrics-jira
chapter: 4. Jira Setup Checklist
chapter_index: 4
source_url: (self-authored)
source_version: 1.1
source_lines: 420-507
license: CC-BY-SA-4.0
authors: openmind
tags: [dora, metrics, jira, github, engineering-effectiveness, 4-jira-setup-checklist]
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
