---
title: AI / agent in the dev workflow
type: agent-recipe
use_when: Adding LLM-based tooling (code review bot, ticket assistant, doc generator, autonomous agent) to a Scrum / Kanban team — defining boundaries, accountability, and DORA implications
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/scrum-guide-expanded/06-artificial-intelligence.md
  - docs/distilled/dora-metrics-jira/02-ticket-discipline.md
  - docs/distilled/synthesis/01-done-and-quality.md
  - docs/distilled/scrum-guide-expanded/07-product-developer.md
  - docs/distilled/scrum-guide-expanded/12-definition-of-output-done.md
  - docs/distilled/wardley-maps/02-evolution-stages.md
load_tier3_optional:
  - docs/sources/scrum-guide-expanded/08-the-scrum-roles-in-the-expansion-pack/03-artificial-intelligence.md
output_shape: AI-role-charter + boundaries + DORA-implications + escalation rules
license: CC-BY-SA-4.0
tags: [recipe, agent, ai, llm, scrum, dora, boundaries]
---

# AI / agent in the dev workflow

## Use this when

The team is about to introduce (or has already introduced) an LLM-based agent — Copilot, Claude Code, custom GPT-Engineer, code-review bot, ticket-summarizer — and you want to set boundaries before incidents force the discussion. SGE explicitly recognizes AI as a Scrum role; use that framing.

## Cards to load

| Card | Why |
|---|---|
| SGE: AI as a role | Human-in-the-loop; ≥1 human Product Developer; AI is a role, not a license |
| DORA: Ticket discipline | What signals an AI-generated change vs a human one |
| Synthesis: Done & quality | DoD vs DoOD — AI can produce output, not validate outcome |
| SGE: Product Developer | Accountability sits with humans, not the agent |
| SGE: Definition of Output Done | What the AI must clear, same as a human |
| Wardley: Evolution stages | LLM tooling is in genesis-custom — pick methods accordingly |

## Prompt skeleton

```
You are helping a tech-lead set up AI / agent boundaries for a
delivery team. Use the loaded cards as authority. Be concrete.

Inputs:
- AI_TOOLING: <list: Copilot / Claude Code / custom agent / code-review
  bot / etc.>
- USE_CASES: <what the AI is allowed/expected to do — code completion,
  PR review, ticket summarization, autonomous bug fixes, etc.>
- TEAM_METHOD: <Scrum / Kanban / hybrid>
- CURRENT_DOOD: <pasted or "we don't have one">
- INCIDENT_HISTORY: <any AI-related incidents, hallucinated changes,
  bypassed reviews>
- CONSTRAINTS: <regulatory / IP / data-residency>

Tasks:
1. AI role charter (per SGE):
   - What AI participates in (events, artifacts).
   - What AI is *accountable* for — answer: nothing. Humans are.
   - Required ≥1 human Product Developer per AI contribution.
2. Boundaries:
   - Where AI can act autonomously (low-risk: doc fix, lint, test
     scaffold).
   - Where AI must propose-only (medium-risk: PR comments, refactors).
   - Where AI is forbidden (high-risk: production deploy, schema
     changes, security-sensitive code, data deletion).
3. DORA implications:
   - Ticket discipline: AI-generated commits must be flagged
     (`agent: claude-code` or similar) so CFR can be reconciled if
     an AI change causes incident.
   - Lead Time: AI may speed up Cycle Time; verify CFR doesn't rise.
   - PR review: AI's own PRs get *more* review, not less.
4. DoOD updates: any AI-touched change passes the same DoOD as a
   human change. No "AI-generated, exception".
5. Escalation rules: when does the team pause AI use?
   - 2+ AI-related incidents in 4 weeks
   - Hallucinated dependency / API
   - Data leak / IP / license issue
6. Output: charter + boundary table + DORA-flag rules + escalation
   triggers.

Constraints:
- Accountability stays with humans. Cite SGE.
- Do not promise that AI will "just speed things up" — measure CFR.
- Do not skip review of AI-generated code. Cite DORA discipline.
- Wardley framing: LLM tooling is genesis/custom — methods must
  match. Don't apply commodity-stage process to it.
```

## Expected output

```
## AI role charter
| Aspect | Rule |
|---|---|
| Accountability | Always a human Product Developer |
| Min human-in-loop | ≥ 1 reviewer per AI contribution |
| Events AI participates in | <list> |
| Events AI does NOT participate in | <list> |

## Boundary table
| Use case | Mode | Reviewer |
|---|---|---|
| Code completion (small) | autonomous | post-hoc PR |
| Doc fix | autonomous | post-hoc PR |
| Refactor (touches >10 files) | propose-only | senior reviewer |
| New endpoint | propose-only | TL + reviewer |
| Production deploy | forbidden | n/a |
| Schema migration | forbidden | n/a |
| Security-sensitive code | forbidden | n/a |
| Customer data handling | forbidden | n/a |

## DORA flagging rules
- Commit message includes `agent: <tool>` for AI-generated.
- AI-generated PRs labeled `ai-generated` in Jira.
- Monthly: cross-check CFR by author-type (human vs AI).
- If AI CFR > human CFR by >2x, escalate.

## DoOD addendum
- AI-touched changes pass the same DoOD. No exceptions.
- AI-generated tests do not count toward "test coverage" unless a
  human reviewer signs off.

## Escalation triggers
- 2+ AI-related incidents in 4 weeks → pause AI use until RCA.
- Hallucinated dependency in production → immediate pause + audit.
- License / IP issue → legal escalation.
```

## Anti-pattern (do NOT use this recipe for)

- "Replace developers with AI" — this recipe assumes SGE's human-in-the-loop. If your goal is replacement, you need a different framework (and probably different ethics consultation).
- Vendor selection. Picking which AI tool to buy is a different decision.
- Personal productivity setup ("how should I prompt Claude?"). This recipe is team-level governance.

## Cross-refs

- [PR review with DORA](01-pr-review-with-dora.md) — review AI-generated PRs
- [Incident post-mortem](05-incident-postmortem.md) — RCA when AI contributes to incident
- [Onboarding a new dev / TL](10-onboarding.md) — how to onboard new hires into AI-using team
