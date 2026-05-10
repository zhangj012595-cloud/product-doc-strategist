# Product Doc Strategist

## 中文简介

`product-doc-strategist` 是一个面向产品经理、创业团队、AI Agent 团队和研发协作团队的 Codex skill。它帮助把一个模糊想法整理成可信、可复查、能给研发和业务团队使用的产品文档。

它特别关注中国市场、海外市场和跨境产品场景：不仅写 PRD，还会补齐产品战略、用户故事、路线图、市场规模证据、数据叙事、风险对照和本地化 GTM 假设。

## English Overview

`product-doc-strategist` is a Codex skill for product managers, founders, AI-agent builders, and product-engineering teams. It turns vague product ideas into strategy-backed product documents that are clear enough for execution and credible enough for stakeholder review.

It supports China-facing, overseas, and cross-border products by combining PRD writing, product strategy, user stories, roadmap planning, market evidence, data storytelling, localization, GTM assumptions, and risk review.

## Who It Is For

- Product managers writing PRDs, strategy memos, roadmap docs, and stakeholder narratives.
- Founders turning a product idea into an investor- or team-ready product plan.
- AI Agent teams defining task boundaries, tools, evals, safety, and rollout plans.
- China-facing teams that need Chinese-language product documents and local market assumptions.
- Global or cross-border teams that need China and overseas assumptions separated.

## What It Helps Produce

- Product strategy summary.
- PRD with user stories and acceptance criteria.
- Roadmap using Now/Next/Later or release phases.
- Market evidence with TAM/SAM/SOM and scenario assumptions.
- Data-supported executive story.
- China/overseas localization and GTM notes.
- Risk register and validation plan.
- RICE prioritization table via `scripts/score_initiatives.py`.

## Install

```bash
npx skills add zhangj012595-cloud/product-doc-strategist
```

Or install from the GitHub path with your preferred skill installer.

## Example Prompts

```text
Use $product-doc-strategist to write a Chinese PRD for our finance research agent. Include product strategy, user stories, market evidence, roadmap, and risks.
```

```text
Use $product-doc-strategist to turn this AI agent idea into a bilingual product strategy memo for China and US markets.
```

```text
Use $product-doc-strategist to prioritize these roadmap initiatives with RICE and explain the tradeoffs for leadership.
```

## Repository Structure

```text
product-doc-strategist/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── product-doc-playbook.md
│   ├── templates.md
│   ├── market-evidence.md
│   └── localization-and-gtm.md
└── scripts/
    └── score_initiatives.py
```

## What It Does Not Do

- It does not replace real customer discovery.
- It does not guarantee market-size accuracy without sources.
- It does not provide legal, financial, compliance, or investment advice.
- It does not decide product strategy alone; it structures assumptions so they can be reviewed.
