---
title: Stakeholder map for a project
type: agent-recipe
use_when: Project initiation; new feature with multiple sponsors; engagement-plan refresh; conflict between conflicting stakeholders
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/synthesis/02-stakeholders-cross-source.md
  - docs/distilled/scrum-guide-expanded/04-stakeholder.md
  - docs/distilled/scrum-guide-expanded/05-supporter.md
  - docs/distilled/principles/pmbok-7/03-engage-stakeholders.md
  - docs/distilled/performance-domains/01-stakeholders.md
  - docs/distilled/p3-express/05-focused-communication.md
load_tier3_optional:
  - docs/sources/scrum-guide-expanded/08-the-scrum-roles-in-the-expansion-pack/01-stakeholder.md
  - docs/sources/scrum-guide-expanded/08-the-scrum-roles-in-the-expansion-pack/02-supporter.md
output_shape: stakeholder-register + power-interest matrix + engagement plan
license: CC-BY-SA-4.0
tags: [recipe, agent, stakeholders, engagement, communication]
---

# Stakeholder map for a project

## Use this when

A project / initiative is starting and you need to identify who matters, who's a Supporter (change agent), who's a passive consumer, and how to communicate with each group at the right cadence. Or: a project is mid-flight and a stakeholder conflict surfaced — time to remap.

## Cards to load

| Card | Why |
|---|---|
| Synthesis: Stakeholders | UtS register vs SGE 4th-role; Supporter as change agent |
| SGE: Stakeholder | 4th role definition |
| SGE: Supporter | Change-agent stakeholder; org-coherence |
| PMBOK 7: Engage stakeholders | Identify aggressively, communicate often, tailor channels |
| UtS: Stakeholders performance domain | Identify → Understand → Prioritize → Engage → Monitor (loop) |
| P3.express: Focused communication | Defined-message-to-defined-audience cadence |

## Prompt skeleton

```
You are helping a tech-lead build a stakeholder map. Use the loaded
cards as authority.

Inputs:
- PROJECT: <name + 1-paragraph context>
- PURPOSE / OUTCOME: <what the project is trying to change>
- KNOWN_PEOPLE: <list: name, role, org, current relationship>
- DECISIONS_PENDING: <what decisions need stakeholder buy-in soon>
- EXISTING_COMMUNICATION: <current cadence / channels, if any>

Tasks:
1. Build the register: for each stakeholder, capture:
   - Role / title
   - Interest in the project (low / med / high)
   - Influence / power (low / med / high)
   - Disposition (champion / supporter / neutral / skeptic / blocker)
   - Whether they're a *Supporter* (change agent) per SGE definition
2. Power-interest matrix: place each on a 2x2.
3. Engagement plan per quadrant:
   - High power + high interest → manage closely (P3.express
     focused communications, weekly).
   - High power + low interest → keep satisfied (monthly digest).
   - Low power + high interest → keep informed (Sprint Review
     attendance).
   - Low power + low interest → monitor.
4. Identify Supporters explicitly — they are change agents; brief
   them and use them.
5. Spot conflicts: stakeholders with conflicting interests. Propose
   sequencing of decisions to surface conflicts early, not late.
6. Output: register + matrix + engagement plan + conflict map.

Constraints:
- Do not collapse "stakeholder" and "user". A stakeholder may not be
  a user; a user may not have power.
- Do not skip the Supporter identification — it's the highest-leverage
  role per SGE.
- Cadence is per-quadrant, not uniform.
```

## Expected output

```
## Stakeholder register
| Name | Role | Interest | Power | Disposition | Supporter? |
|---|---|---|---|---|---|
| Alice | VP Eng | high | high | champion | yes |
| Bob | Legal | low | high | neutral | no |
| ... |

## Power-interest matrix
- High P / High I: <names>
- High P / Low I: <names>
- Low P / High I: <names>
- Low P / Low I: <names>

## Engagement plan
| Quadrant | Cadence | Channel | Owner |
|---|---|---|---|
| HP / HI | weekly | 1:1 + Sprint Review | PM |
| HP / LI | monthly | exec digest | PM |
| LP / HI | sprint | Sprint Review | TL |
| LP / LI | quarterly | newsletter | PMO |

## Supporters (change agents) — brief them first
- <name>: leverage by <…>
- <name>: leverage by <…>

## Conflict map
- <Stakeholder X> wants A; <Stakeholder Y> wants B. Surface in
  <which decision>, by <date>.
```

## Anti-pattern (do NOT use this recipe for)

- "RACI" matrix — different framing, more granular per-task. Stakeholder map is project-level.
- Vendor / supplier management — different power dynamics, contractual. Use a vendor-management framework.
- Internal team-staffing — that's [Team / org redesign](06-team-org-redesign.md).

## Cross-refs

- [Sprint Review prep](02-sprint-review-prep.md) — Review is a stakeholder event
- [Strategic review / annual planning](08-strategic-review.md) — stakeholder map drives annual cycle
- [Onboarding a new dev / TL](10-onboarding.md) — new TL needs stakeholder map on day 1
