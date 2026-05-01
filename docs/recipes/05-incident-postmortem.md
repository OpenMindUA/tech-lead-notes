---
title: Incident post-mortem / risk register triage
type: agent-recipe
use_when: After a production incident — running a blameless post-mortem; deciding what goes into the risk register vs the follow-up register; spotting CFR/MTTR distortions before they enter the metrics
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/synthesis/05-risk-and-stability.md
  - docs/distilled/dora-metrics-jira/04-jira-setup-checklist.md
  - docs/distilled/dora-metrics-jira/05-anti-patterns.md
  - docs/distilled/performance-domains/08-uncertainty.md
  - docs/distilled/principles/nupp/03-always-be-proactive.md
  - docs/distilled/principles/pmbok-7/09-risk.md
load_tier3_optional:
  - docs/sources/dora-metrics-jira/05-appendix-common-pitfalls-and-how-to-avoid-them.md
  - docs/sources/underneath-the-surface/04-enriching-the-methodology/08-uncertainty.md
output_shape: timeline + cause-classification + risk-register entries + follow-up actions + DORA implications
license: CC-BY-SA-4.0
tags: [recipe, agent, incident, post-mortem, risk, dora, cfr, mttr]
---

# Incident post-mortem / risk register triage

## Use this when

A production incident just happened (or just got resolved). You need a structured post-mortem that (a) is blameless and proactive, (b) decides what enters the risk register vs the follow-up register, (c) makes sure the incident is correctly captured in DORA terms (CFR / MTTR) without being hidden or mislabeled.

## Cards to load

| Card | Why |
|---|---|
| Synthesis: Risk & stability | UtS sophistication ladder + DORA CFR/MTTR + SGE proactive risk |
| DORA: Jira setup checklist | How incidents should be modeled in tickets |
| DORA: Anti-patterns | "Hidden CFR", labeling hotfix as feature, etc. |
| UtS: Uncertainty performance domain | Risk register vs follow-up register |
| NUPP: Always be proactive | Avoid passive "we'll see if it happens again" |
| PMBOK 7: Optimize risk responses | Layered, continuous, cost-justified |

## Prompt skeleton

```
You are running a blameless post-mortem for a tech-lead. Use only
the loaded cards as authority. Be ruthlessly anti-blame and
ruthlessly pro-evidence.

Inputs:
- INCIDENT_SUMMARY: <one paragraph: what happened, user impact>
- TIMELINE: <chronological events with timestamps>
- DETECTION: <how was it detected; who alerted; how long was MTTD>
- RESOLUTION: <how was it fixed; deploy / rollback / config change; MTTR>
- ROOT_CAUSE_HYPOTHESIS: <best current understanding>
- RELATED_TICKETS: <Jira / Linear keys for the incident + the change that caused it>
- AFFECTED_SERVICES: <list>

Tasks:
1. Build a clean timeline with detection, mitigation, resolution
   marked. Compute MTTR. Identify gaps where MTTD was longer than
   it should have been.
2. Classify the cause: regression / config / capacity / dependency /
   data / process. Cite which sophistication-ladder rung this is on.
3. Decide for each follow-up:
   - Is it a *risk* (probabilistic, register entry) or a *follow-up*
     (concrete action, follow-up register)?
   - Use UtS distinction; cite the card.
4. Map to DORA:
   - This incident → CFR contribution (yes / no — only if it was a
     change-induced failure).
   - MTTR — is it captured correctly?
   - Anti-patterns to avoid: "Hidden CFR", "labeling hotfix as
     feature".
5. Propose 3-5 specific follow-up actions, each owned and with a
   due date. Distinguish proactive (eliminate cause) from reactive
   (mitigate symptoms).
6. Output: timeline + cause-classification + risk-register entries
   + follow-up actions + DORA implications.

Constraints:
- Do not name individuals as causes. Process / system focus.
- Do not propose "training" as a follow-up unless there's a clear
  knowledge gap — usually it's a process / tooling fix.
- "We'll be more careful" is not an action. Reject it explicitly.
```

## Expected output

```
## Timeline
- HH:MM — change deployed
- HH:MM — first error in logs
- HH:MM — alert fired (MTTD: …)
- HH:MM — on-call paged
- HH:MM — mitigation deployed
- HH:MM — fully resolved (MTTR: …)

## Cause classification
- Category: <regression | config | capacity | dependency | data | process>
- Ladder rung: <UtS sophistication ladder>
- Card: Synthesis: Risk & stability

## DORA implications
- CFR contribution: <yes / no — explain>
- MTTR: <value, captured correctly?>
- Anti-patterns checked: ✅ not labeled as feature; ✅ ticket carries
  incident label

## Risk register entries (probabilistic)
- <Risk> — likelihood: <…> impact: <…> mitigation owner: <…>

## Follow-up register entries (concrete actions)
| # | Action | Owner | Due | Type |
|---|---|---|---|---|
| 1 | Add alarm on metric X | <name> | <date> | proactive |
| 2 | Fix race in module Y | <name> | <date> | proactive |
| 3 | Document rollback path Z | <name> | <date> | reactive |

## What we will NOT do
- "Be more careful" — rejected (not actionable).
- Train the team on Y — rejected, the issue was missing observability,
  not knowledge.
```

## Anti-pattern (do NOT use this recipe for)

- Performance review / blame-finding. The recipe is built around blameless mode.
- Outage *during* the incident. This is for the post-mortem, not the active response. (For active response, follow your runbooks.)
- Routine bug triage. Use the team's normal triage process; this recipe is for incidents with user impact.

## Cross-refs

- [PR review with DORA](01-pr-review-with-dora.md) — what went wrong upstream
- [Forecasting & SLE](09-forecasting-and-sle.md) — incidents distort throughput; account for them
- [Strategic review](08-strategic-review.md) — patterns of incidents may signal stage / inertia issues
