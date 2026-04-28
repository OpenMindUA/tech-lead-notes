---
title: "Appendix: Common Pitfalls and How to Avoid Them"
source_id: dora-metrics-jira
chapter: "Appendix: Common Pitfalls and How to Avoid Them"
chapter_index: 5
source_url: (self-authored)
source_version: 1.1
source_lines: 508-522
license: CC-BY-SA-4.0
authors: openmind
tags: [dora, metrics, jira, github, engineering-effectiveness, appendix-common-pitfalls-and-how-to-avoid-them]
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
