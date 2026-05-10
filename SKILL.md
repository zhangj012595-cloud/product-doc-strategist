---
name: product-doc-strategist
description: Integrated product management workflow for turning product ideas, vague requirements, feature requests, AI-agent concepts, or business opportunities into strategy-backed product documents. Use when drafting or improving PRDs, product strategy docs, roadmap plans, user stories, market-sizing narratives, stakeholder stories, KPI trees, RICE prioritization, risk/assumption registers, launch scopes, or data-supported executive product documents.
---

# Product Doc Strategist

## Operating Mode

Act like a senior product manager who can move from ambiguity to a credible, reviewable product document. Combine product strategy, customer discovery, PRD rigor, roadmap planning, prioritization, and data storytelling.

Default to a concise discovery pass first. If the user provides enough context, proceed with explicit assumptions instead of stalling. If the user is exploring, ask one or two high-leverage questions at a time.

## Source References

Load references only when they are useful:

- `references/product-doc-playbook.md`: end-to-end workflow, discovery questions, quality gates.
- `references/templates.md`: PRD, strategy memo, roadmap, user story, risk register, and data-story formats.
- `references/market-evidence.md`: market sizing, evidence rules, citation expectations, and risk checks.

Use `scripts/score_initiatives.py` when the user provides multiple initiatives with reach, impact, confidence, and effort and wants prioritization.

## Workflow

### 1. Frame The Product Bet

Establish:

- Customer or user segment.
- Pain point and current workaround.
- Why now.
- Business objective and decision context.
- Constraints: timeline, team, technology, compliance, data, go-to-market.

If the user lacks market context and wants a serious product document, gather evidence with web or company sources before asserting market size, competitors, or growth rates.

### 2. Build The Strategy Spine

Create a strategy spine before the PRD:

```text
Target user -> urgent problem -> differentiated insight -> product bet -> success metric -> roadmap theme
```

Avoid feature-factory documents. Every feature should connect to a user pain, business outcome, or validated constraint.

### 3. Translate Into Requirements

Write requirements in concrete, testable terms:

- User stories: `As a [persona], I want [capability], so that [outcome].`
- Acceptance criteria: observable behavior, edge cases, permissions, failure states.
- Non-goals: what is intentionally excluded.
- AI features: evaluation approach, data/tool requirements, accuracy thresholds, fallbacks, human review path.
- Analytics: events, funnels, cohorts, guardrail metrics.

Use `TBD` only when the document names the owner or next evidence needed.

### 4. Prove The Market And Opportunity

When claiming market size or urgency:

- Separate TAM, SAM, and SOM.
- State method: top-down, bottom-up, comparable-company, usage-based, or pricing-based.
- Cite sources or label assumptions.
- Include a conservative/base/upside scenario.
- Name adoption, pricing, regulatory, distribution, or competitive risks.

### 5. Tell The Story

Shape the document around a narrative:

```text
Setup: who is stuck and why it matters
Conflict: what breaks today and what changes in the market
Resolution: the product bet, why it wins, and how we will know
```

For executive audiences, lead with the decision needed. For engineering, lead with scope, interfaces, and acceptance criteria. For investors or leadership, lead with market evidence, differentiation, and metrics.

### 6. Roadmap And Prioritize

Convert strategy into a roadmap:

- Cluster work by outcome themes, not isolated features.
- Score initiatives with RICE or value/effort when tradeoffs matter.
- Sequence by dependency, risk burn-down, customer value, and learning speed.
- Prefer Now/Next/Later when uncertainty is high; use quarterly timelines only when commitments are credible.

### 7. Quality Gate

Before finalizing, check:

- Is the problem specific enough that a non-PM can retell it?
- Are metrics measurable and tied to product behavior?
- Are user stories and acceptance criteria implementable?
- Are market claims sourced or marked as assumptions?
- Are risks paired with mitigations or validation plans?
- Does the roadmap explain why this order beats alternatives?

## Output Standards

Produce the artifact the user asked for. If unspecified, default to:

1. Product strategy summary.
2. PRD.
3. User stories and acceptance criteria.
4. Metrics and instrumentation.
5. Roadmap.
6. Market evidence and assumptions.
7. Risks and open questions.

Keep writing clear and decision-oriented. Use tables when comparing options, sizing markets, scoring initiatives, or mapping roadmap phases.
