---
title: Agent recipes — task-driven loading guides
type: recipe-set
license: CC-BY-SA-4.0
tags: [recipes, agent, task-driven, how-to-use]
---

# Agent recipes

Each recipe is a **task-driven loading guide**: which Tier-2 cards (and sometimes Tier-3 chunks) to load into an agent's context, what prompt skeleton to use, and what output to expect. Recipes are runtime-agnostic — the same recipe works whether you're using Claude Code, Cursor, Copilot, a custom agent, or just copy-pasting into a chat.

> **Why recipes exist.** The corpus (Tier 1-2-3) is large. Loading everything blows the context window and dilutes the answer. A recipe says: *"for this specific question, these are the cards that matter, this is the prompt that uses them."*

## How to use a recipe

1. Find the recipe that matches your task.
2. Load the listed Tier-2 cards into the agent (paste, link, or attach).
3. (Optional) Add the listed Tier-3 chunks for verbatim citation.
4. Use the prompt skeleton, filling in inputs.
5. Verify the output against the recipe's "expected output" shape.

## Recipes (by frequency)

### High-frequency (weekly+)

| # | Recipe | Use when |
|---|---|---|
| [01](01-pr-review-with-dora.md) | PR / change review with DORA discipline | Reviewing a PR before merge — checking branch / commit / PR hygiene + production-gated DoD |
| [02](02-sprint-review-prep.md) | Sprint Review prep — output vs outcome | Preparing demo or stakeholder review; defending "we shipped but no outcome moved yet" |
| [09](09-forecasting-and-sle.md) | Forecasting & SLE discussion | "Коли буде готово?" / replacing story-point estimation with flow-based forecasting |
| [05](05-incident-postmortem.md) | Incident post-mortem / risk register triage | After a production incident — blameless RCA + risk vs follow-up classification |

### Medium-frequency (monthly+)

| # | Recipe | Use when |
|---|---|---|
| [03](03-build-buy-rent-outsource.md) | Build / buy / rent / outsource decision | Whether to build a component in-house, buy SaaS, or rent a utility |
| [04](04-pick-a-method.md) | Pick a method for a new initiative | Spinning up a new project / product — Scrum / Kanban / P3.express / hybrid |
| [07](07-stakeholder-map.md) | Stakeholder map for a project | Project initiation; engagement plan; stakeholder conflict |
| [11](11-ai-in-dev-workflow.md) | AI / agent in the dev workflow | Adding LLM tooling to a Scrum / Kanban team — boundaries + DORA implications |

### Lower-frequency (quarterly+)

| # | Recipe | Use when |
|---|---|---|
| [08](08-strategic-review.md) | Strategic review / annual planning | Yearly strategy cycle; multi-product roadmap; portfolio review |
| [06](06-team-org-redesign.md) | Team / org redesign (PST + roles) | Reorg, hiring brief, splitting platform team from product teams |
| [10](10-onboarding.md) | Onboarding a new dev / TL | First-week reading list for a new engineer or tech-lead joining the team |

## Recipe format (what's in each file)

```yaml
---
title: <recipe name>
type: agent-recipe
use_when: <one-line trigger>
load_tier1: docs/agent-index.md
load_tier2:
  - docs/distilled/.../foo.md
  - docs/distilled/.../bar.md
load_tier3_optional:
  - docs/sources/.../baz.md
output_shape: <list / matrix / draft>
---
```

Body sections:
- **Use this when** — concrete trigger
- **Cards to load** — table with "why each card"
- **Prompt skeleton** — copy-paste ready, with `<PLACEHOLDERS>`
- **Expected output** — shape + example
- **Anti-pattern** — when *not* to use this recipe
- **Cross-refs** — related recipes

## Conventions

- **Placeholders are `<UPPERCASE>`**, not Jinja templates. Recipes are meant to be human-edited before use.
- **Cards are paths from repo root**, e.g. `docs/distilled/dora-metrics-jira/01-dora-fundamentals.md`. Most agent runtimes accept those directly.
- **Tier-3 chunks are optional**. Load them only when verbatim citation matters; otherwise the distilled cards are sufficient.
- **Output shape is enforced**. Recipes say what the answer should look like; deviating is fine but the agent should call it out.

## Building your own recipe

If a task isn't covered, write a new one:

1. Copy the format from an existing recipe (e.g. [01](01-pr-review-with-dora.md)).
2. Identify the 3-7 Tier-2 cards that matter.
3. Write a prompt skeleton with explicit constraints (what *not* to invent).
4. Test it on a real example.
5. Open a PR.

Don't add a recipe for a task that:
- Already has a single distilled card that fully covers it (just use the card).
- Is too narrow (one-off questions don't need recipes).
- Depends on a specific agent runtime (those belong in `examples/integrations/`, not here).

## Cross-refs

- [Tier 1 — Agent index](../agent-index.md) — full catalog
- [Tier 2 — Distilled cards](../distilled/index.md) — by source
- [Tier 3 — Full source text](../sources/) — verbatim
- [Sources manifest](../sources.md) — license + attribution
