# Product Document Playbook

## Discovery Questions

Ask only the questions needed to remove the biggest ambiguity:

- Who is the primary user, buyer, and internal stakeholder?
- Is the target market China, overseas, or cross-border?
- Which language should the final document use: Chinese, English, or bilingual?
- What painful job are they trying to complete?
- What happens today without this product or feature?
- Why does this matter now?
- What business result should change?
- What data, user feedback, or sales signal proves this problem exists?
- What constraints are fixed: deadline, team, stack, budget, compliance, channels?
- What local constraints matter: identity/login, payment, procurement, privacy, data residency, app store, cloud vendor, content moderation, or support model?
- What would make this product bet obviously fail?

## Product Strategy Spine

Use this before writing the PRD:

| Element | Question | Output |
| --- | --- | --- |
| User | Who is served first? | Narrow segment and persona |
| Market | Where will this win first? | China, overseas region, or cross-border wedge |
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

## China And Overseas Product Lens

For China-facing products, check:

- User behavior: WeChat/mini-program expectations, mobile-first flows, enterprise admin roles, offline-to-online workflows.
- Channels: private traffic, app stores, enterprise sales, ecosystem partnerships, KOL/content, community operations.
- Commercial model: subscription, usage-based, service bundle, enterprise procurement, reseller/channel partner.
- Compliance: PIPL, data residency expectations, content safety, ICP/app filing where applicable, industry-specific rules.
- Infrastructure: domestic cloud, latency, payment, SMS, identity verification, customer support hours.

For overseas products, check:

- Region priority: North America, Europe, APAC, LATAM, Middle East, or global self-serve.
- Buyer motion: PLG, sales-led, channel-led, marketplace, or partner-led.
- Compliance: GDPR, CCPA/CPRA, SOC 2, HIPAA, PCI, FINRA/SEC, or other domain-specific requirements when relevant.
- Localization: language, currency, tax, payment, support, onboarding, legal terms, cultural UX expectations.
- Competition: global incumbents, local champions, open-source alternatives, and bundled platform features.

For cross-border products, split the document into:

1. Shared product thesis.
2. China-specific assumptions.
3. Overseas-specific assumptions.
4. Cross-border risks and dependencies.
5. Localization roadmap.

## Review Loop

Run review in this order:

1. Strategy review: is the bet worth making?
2. Customer review: does the pain and workflow match reality?
3. Engineering review: is scope feasible and testable?
4. Data review: are metrics instrumentable?
5. Risk review: are assumptions and mitigations explicit?
6. Market review: are China and overseas claims separated and sourced?
