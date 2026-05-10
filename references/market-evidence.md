# Market Evidence Guide

## Evidence Ladder

Prefer stronger evidence:

1. Direct customer behavior: usage, conversion, churn, paid pilots, interviews.
2. Company-owned data: CRM, support, search logs, funnel analytics.
3. Credible market sources: filings, analyst reports, government data, industry associations.
4. Comparable products: pricing, adoption, revenue, category benchmarks.
5. Explicit assumptions: labeled, scenario-tested, and easy to revise.

## Market Sizing Methods

### Top-Down

Use category market size and narrow it to the reachable segment.

```text
TAM = total category spend
SAM = geography/segment/channel reachable by this product
SOM = realistic share over a defined time horizon
```

Best for executive framing. Risk: can feel inflated without bottom-up validation.

### Bottom-Up

Use target accounts, penetration, usage, and pricing.

```text
SOM = target accounts x expected penetration x annual contract value
```

Best for product and go-to-market planning. Risk: assumptions must be explicit.

### Usage-Based

Use frequency, active users, transactions, or workflows.

```text
Annual value = users x frequency x value per completed workflow
```

Best for AI agents, workflow tools, and productivity products.

## Scenario Table

| Scenario | Adoption | Pricing | Market Reach | Revenue/Impact | Key Assumption |
| --- | ---: | ---: | ---: | ---: | --- |
| Conservative | | | | | |
| Base | | | | | |
| Upside | | | | | |

## Citation Rules

- Include source name, date, and link when available.
- Do not blend data from different years without saying so.
- Distinguish market size from serviceable revenue.
- Mark inference clearly: "Assumption", "Estimate", or "Based on".
- Include counter-evidence when it materially changes the decision.

## China Evidence Checklist

Use China-specific evidence when the target market includes mainland China, Hong Kong, Macau, Taiwan, or Chinese-speaking users. Prefer:

- Official statistics and regulators: National Bureau of Statistics, MIIT, CAC, PBOC, CSRC, HKEX, SFC, industry regulators.
- Public company materials: annual reports, prospectuses, exchange filings, investor presentations.
- Industry bodies and credible research: CNNIC, CAICT, industry associations, reputable consulting or research firms.
- Platform evidence: app store rankings, WeChat ecosystem signals, public traffic estimates, e-commerce/category data, job postings, procurement notices.
- Customer evidence: Chinese user interviews, sales calls, support tickets, community posts, paid pilots, enterprise procurement feedback.

For China-facing claims, explicitly note:

- Whether the market is mainland China, Greater China, Chinese-speaking global users, or cross-border Chinese users.
- Whether market size is in RMB, USD, HKD, or another currency.
- Whether numbers refer to users, accounts, enterprises, transaction volume, revenue, or spend.
- Whether policy, data residency, cloud, payment, app filing, or content requirements could change adoption.

## Overseas Evidence Checklist

Use overseas-specific evidence when targeting non-China markets. Prefer:

- Government and multilateral data: census, labor, trade, health, education, financial regulators, World Bank, OECD, IMF where relevant.
- Public company filings: 10-K, 20-F, S-1/F-1, annual reports, investor decks.
- Industry and standards bodies: trade associations, standards groups, developer ecosystems.
- Market signals: competitor pricing, review sites, app marketplaces, cloud marketplaces, search trends, job postings.
- Customer evidence: interviews, paid pilots, usage logs, CRM pipeline, churn/loss notes.

For overseas claims, state:

- Region: US, North America, EU, UK, APAC, LATAM, MENA, or global.
- Currency and year.
- Whether compliance affects adoption: GDPR, CCPA/CPRA, SOC 2, HIPAA, PCI, financial regulation, export control, or local rules.
- Whether the GTM motion is PLG, sales-led, channel-led, marketplace-led, or partner-led.

## Cross-Border Market Split

When China and overseas both matter, do not collapse evidence into one global number. Use this structure:

| Market | User Segment | Evidence Source | TAM/SAM/SOM Method | Currency | Key Risk |
| --- | --- | --- | --- | --- | --- |
| China | | | | RMB | |
| Overseas | | | | USD | |
| Cross-border | | | | USD/RMB | |

## Risk Counterweight

Every market-size claim should be paired with at least one risk:

- Distribution risk: reaching the buyer is harder than the model assumes.
- Adoption risk: users do not change workflow.
- Monetization risk: willingness to pay is lower than modeled.
- Competitive risk: incumbents copy or bundle the feature.
- Regulatory risk: data, privacy, or market rules block rollout.
- Execution risk: the product cannot meet quality, latency, or cost targets.
- Localization risk: translated copy, pricing, support, or workflow assumptions do not fit local behavior.
- Compliance risk: privacy, data transfer, financial, health, education, or content rules constrain launch.
