# Product Document Playbook

## Discovery Questions

Ask only the questions needed to remove the biggest ambiguity:

- Who is the primary user, buyer, and internal stakeholder?
- What painful job are they trying to complete?
- What happens today without this product or feature?
- Why does this matter now?
- What business result should change?
- What data, user feedback, or sales signal proves this problem exists?
- What constraints are fixed: deadline, team, stack, budget, compliance, channels?
- What would make this product bet obviously fail?

## Product Strategy Spine

Use this before writing the PRD:

| Element | Question | Output |
| --- | --- | --- |
| User | Who is served first? | Narrow segment and persona |
| Problem | What urgent pain exists? | Problem statement |
| Insight | What do we believe that others miss? | Differentiated thesis |
| Bet | What product move follows? | Product hypothesis |
| Metric | How will we know? | KPI and guardrails |
| Roadmap | What sequence learns fastest? | Now/Next/Later or quarterly plan |

## PRD Quality Bar

Strong requirements:

- Describe behavior that can be tested.
- Include success, empty, error, permission, and degraded states.
- Name data sources and lifecycle events.
- Connect every feature to a user story or business metric.
- Exclude tempting but nonessential scope.

Weak requirements:

- Use words such as "fast", "easy", "smart", "modern", or "seamless" without a measurable definition.
- Skip analytics and observability.
- Treat AI output quality as subjective.
- Promise roadmap dates without capacity or dependencies.

## AI Product Addendum

For AI-agent products, include:

- Task boundary: what the agent owns, suggests, or escalates.
- Tool/data access: APIs, permissions, retrieval sources, rate limits.
- Evaluation: golden tasks, rubrics, pass thresholds, regression tests.
- Safety: privacy, financial/legal/medical boundaries, hallucination checks.
- Human control: review, undo, audit trail, confidence display.
- Cost and latency: acceptable limits and fallback behavior.

## Review Loop

Run review in this order:

1. Strategy review: is the bet worth making?
2. Customer review: does the pain and workflow match reality?
3. Engineering review: is scope feasible and testable?
4. Data review: are metrics instrumentable?
5. Risk review: are assumptions and mitigations explicit?
