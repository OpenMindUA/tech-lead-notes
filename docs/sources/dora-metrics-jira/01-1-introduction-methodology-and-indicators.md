---
title: "1. Introduction: Methodology and Indicators"
source_id: dora-metrics-jira
chapter: "1. Introduction: Methodology and Indicators"
chapter_index: 1
source_url: (self-authored)
source_version: 1.1
source_lines: 7-67
license: CC-BY-SA-4.0
authors: openmind
tags: [dora, metrics, jira, github, engineering-effectiveness, 1-introduction-methodology-and-indicators]
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
