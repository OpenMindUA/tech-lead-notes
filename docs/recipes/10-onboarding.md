---
title: Onboarding a new dev / TL
type: agent-recipe
use_when: First-week reading list for a new engineer or tech-lead joining the team; "what should I know about how we work?"; refresher after a long break
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/scrum-guide/01-scrum-definition.md
  - docs/distilled/scrum-guide/02-theory-and-pillars.md
  - docs/distilled/dora-metrics-jira/01-dora-fundamentals.md
  - docs/distilled/dora-metrics-jira/02-ticket-discipline.md
  - docs/distilled/synthesis/01-done-and-quality.md
  - docs/distilled/synthesis/07-roles-across-frameworks.md
  - docs/distilled/wardley-maps/01-anatomy-of-a-map.md
  - docs/distilled/principles/nupp/01-results-over-affiliations.md
load_tier3_optional:
  - docs/sources/scrum-guide/02-scrum-definition.md
output_shape: tailored-reading-list + day-by-day plan + checkpoint questions
license: CC-BY-SA-4.0
tags: [recipe, agent, onboarding, reading-list, day-1]
---

# Onboarding a new dev / TL

## Use this when

A new engineer or tech-lead joins the team. They don't need 10 sources at once — they need a curated path with day-by-day checkpoints, calibrated to their existing experience and the role they'll play.

## Cards to load

| Card | Why |
|---|---|
| Scrum 2020: Definition + Theory | Foundation; framework vocabulary |
| DORA: fundamentals + ticket discipline | What signals quality on this team |
| Synthesis: Done & quality | DoD vs DoOD vs Outcome Done — most-confused topic |
| Synthesis: Roles | What each title actually means here |
| Wardley: Anatomy of a map | One strategic frame they'll see in TL discussions |
| NUPP: Results over affiliations | Anti-tribalism; the team is method-pragmatic |

## Prompt skeleton

```
You are helping a tech-lead onboard a new team member. Build a
tailored, time-boxed reading + activity plan.

Inputs:
- NEW_HIRE: <name + role: junior dev / senior dev / tech lead / ...>
- BACKGROUND: <prior frameworks they know: Scrum / Kanban / SAFe /
  none / academia>
- TEAM_CONTEXT: <one paragraph: stack, current method, current
  initiatives>
- AVAILABLE_TIME: <full-time onboarding for first week / part-time>
- ROLE_FOCUS: <what they'll do day-to-day: feature work / platform /
  on-call / TL>

Tasks:
1. Tailor the reading list:
   - If brand-new to Scrum: start with Scrum Definition + Theory
     before anything else.
   - If experienced Scrum but new to this team: skip basics, jump
     to team's DoOD + DORA discipline.
   - If TL role: add Wardley anatomy + Synthesis: Roles + Stakeholder
     map recipe pointer.
2. Day-by-day plan (5 working days typical):
   - Day 1: framework vocabulary + team's DoW / DoOD
   - Day 2: ticket discipline + DORA basics
   - Day 3: synthesis cards (Done, Roles)
   - Day 4: shadow a Sprint Review or pair on a real PR
   - Day 5: open a small PR + retrospect onboarding
3. Checkpoint questions (one per day) to verify comprehension —
   not multiple-choice; open-ended.
4. Pointers to recipes they'll need later: PR review, Sprint Review,
   forecasting, etc. Don't dump them all on day 1.

Constraints:
- Don't dump 10 cards on day 1 — that's reading-not-learning.
- Day 4 must include a *real* activity, not just reading.
- Adjust depth to role: senior TLs need Wardley; junior devs do not.
```

## Expected output

```
## Profile-tailored summary
- Hire: <role>
- Background match: <experienced Scrum / new to Scrum / etc.>
- Path chosen: <"fast-track" / "foundation-first">

## Day-by-day plan
### Day 1 — vocabulary
- Read: Scrum 2020 definition + theory cards
- Read: Synthesis: Done & quality
- Activity: pair with a teammate during Daily Scrum
- Checkpoint: "What does 'Increment' mean on this team?
  How does it differ from 'Output Done'?"

### Day 2 — discipline
- Read: DORA fundamentals + ticket discipline
- Read: this team's DoOD doc
- Activity: review a recent merged PR end-to-end
- Checkpoint: "Why does this team enforce conventional commits?
  Which DORA metric does that protect?"

### Day 3 — context & roles
- Read: Synthesis: Roles across frameworks
- Read (TL only): Wardley anatomy of a map
- Activity: 1:1 with PM / PO
- Checkpoint: "Who's the Product Owner here vs the Stakeholders?"

### Day 4 — observe
- Activity: attend Sprint Review (or watch a recording)
- Activity: pair on triaging a Jira ticket
- Checkpoint: "What's an outcome the team's working on, vs an
  output it shipped last sprint?"

### Day 5 — act
- Activity: open a small PR (doc fix / typo / tiny feature)
- Activity: retrospect own onboarding; identify 1 gap
- Checkpoint: "What recipe / card would have helped you on
  day 1 if I had pointed it out?"

## Pointers for later
- Week 2-3: Forecasting & SLE; Stakeholder map (if TL role)
- Month 2: Strategic review (TL only); Team / org redesign
- On-demand: PR review with DORA discipline; Incident post-mortem
```

## Anti-pattern (do NOT use this recipe for)

- "Send them the whole `agent-index.md`." Information overload, no comprehension.
- Generic onboarding doc — this recipe is *role + background tailored*.
- Replacing pairing with reading. Day 4 + 5 are non-negotiably interactive.

## Cross-refs

- [PR review with DORA](01-pr-review-with-dora.md) — week 2 reading
- [Sprint Review prep](02-sprint-review-prep.md) — week 2-3 reading
- [Stakeholder map](07-stakeholder-map.md) — TL-role reading by month 2
- [AI / agent in the dev workflow](11-ai-in-dev-workflow.md) — if the team uses AI tooling
