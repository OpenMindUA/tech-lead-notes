---
title: Team / org redesign (PST + roles)
type: agent-recipe
use_when: Reorg, hiring brief, splitting platform team from product teams, deciding who staffs which initiative; matching attitude (Pioneer / Settler / Town Planner) to evolution stage
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/wardley-maps/06-pioneers-settlers-town-planners.md
  - docs/distilled/wardley-maps/03-doctrine.md
  - docs/distilled/wardley-maps/02-evolution-stages.md
  - docs/distilled/synthesis/07-roles-across-frameworks.md
  - docs/distilled/scrum-guide-expanded/04-stakeholder.md
  - docs/distilled/scrum-guide-expanded/05-supporter.md
  - docs/distilled/scrum-guide/04-scrum-team.md
load_tier3_optional:
  - docs/sources/wardley-maps/04-doctrine.md
  - docs/sources/wardley-maps/18-better-for-less.md
output_shape: PST audit + team-design + hiring brief + theft hand-offs
license: CC-BY-SA-4.0
tags: [recipe, agent, org-design, pst, pioneers-settlers-town-planners, roles]
---

# Team / org redesign (PST + roles)

## Use this when

A reorg is on the table; or you're hiring; or you're trying to figure out why one team ships nothing new while another keeps shipping demos that never industrialize. Wardley's Pioneer / Settler / Town Planner attitude × aptitude lens almost always exposes the problem.

## Cards to load

| Card | Why |
|---|---|
| Wardley: PST | Three populations matched to evolution stages |
| Wardley: Doctrine (phase IV) | "Think aptitude *and* attitude" |
| Wardley: Evolution stages | Stages drive PST staffing |
| Synthesis: Roles across frameworks | PRINCE2 / DSDM / P3.express / Scrum / SGE / DORA mapping |
| SGE: Stakeholder + Supporter | New 4th role + change-agent role |
| Scrum 2020: Scrum Team | Single-team rules and limits |

## Prompt skeleton

```
You are helping a tech-lead diagnose / redesign team structure. Use
attitude (Pioneer / Settler / Town Planner) crossed with aptitude
(skills) as the primary lens.

Inputs:
- CURRENT_TEAMS: <list of teams; for each: size, mission, current
  evolution stage of their work>
- PEOPLE: <optional roster; or just attitude-mix description>
- COMPLAINT_OR_GOAL: <what triggered this — "we ship slow", "no
  innovation", "outages", "rewrites", "want to spin up X">
- CONSTRAINTS: <budget / hiring freeze / political>

Tasks:
1. PST audit: classify each team's *current* attitude mix (Pioneer-
   heavy / Settler-heavy / Town Planner-heavy / mixed).
2. Map each team to the evolution stage of its *work* (genesis /
   custom / product / commodity).
3. Spot mismatches:
   - Pioneers staffing a Town Planner job → fragility, outages.
   - Town Planners staffing a Pioneer job → over-engineering, slow R&D.
   - Settler-only orgs → can't innovate, can't industrialize.
4. Diagnose the theft (hand-off) chain: where is it broken?
   Pioneers can't let go? Settlers refuse to industrialize? Town
   Planners ignored?
5. Propose a redesign with:
   - Clear team boundaries by stage.
   - Hiring brief specifying *attitude* not just skills.
   - Theft hand-off mechanics (who steals from whom, when).
6. Output: audit + redesign + hiring brief + risks.

Constraints:
- Do not propose a single team that does all stages — that's the
  most common anti-pattern.
- PST is attitude, not seniority. Don't confuse "senior" with "Town
  Planner" or "junior" with "Pioneer".
- If the constraint is hiring-freeze, propose attitude shifts within
  existing team (Settlers can be coached up to Town Planning) before
  recommending hires.
```

## Expected output

```
## PST audit
| Team | Stage of work | Attitude mix today | Mismatch? |
|---|---|---|---|
| Platform | commodity | Pioneer-heavy (3) Settler (1) | YES — wrong attitude |
| Product | product | Settler (4) | OK |
| R&D | genesis / custom | Settler-heavy | YES — needs Pioneers |

## Theft hand-off audit
- Pioneer → Settler: <broken / works>
- Settler → Town Planner: <broken / works>
- Where's the orphan work?

## Redesign proposal
- Team A: rename / split / refocus to <stage>; hire <attitude>
- Team B: ...
- Theft mechanics: <who steals from whom; explicit moments>

## Hiring brief (attitude-explicit)
- For Team A: 2x Town Planner (engineering rigour, ops mindset).
  Skills: Kubernetes, observability, SRE.
- For Team C: 1x Pioneer (comfortable with chaos).
  Skills: rapid prototyping, ML / data exploration.

## Risks
- Politically: Town Planners often don't want the "ops" label.
  Frame their role as "platform builders".
- Theft requires letting-go culture; design incentives so Pioneers
  hand off and don't sit on a pet prototype.
```

## Anti-pattern (do NOT use this recipe for)

- Performance reviews / firing decisions. PST is a design tool, not a personnel weapon.
- "How big should the team be?" alone — that's a Conway / cognitive-load question; PST is orthogonal.
- Diversity / inclusion org work — different lens, complementary but separate.

## Cross-refs

- [Build / buy / rent / outsource](03-build-buy-rent-outsource.md) — staffing follows stage; this recipe assumes stage is decided
- [Strategic review / annual planning](08-strategic-review.md) — yearly reorg cadence
- [Stakeholder map](07-stakeholder-map.md) — Stakeholder + Supporter roles
