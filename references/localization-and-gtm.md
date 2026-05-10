# Localization And GTM Guide

## Market Mode

Classify the product before writing the document:

| Mode | Use When | Document Implication |
| --- | --- | --- |
| China-first | Users, buyers, channels, and compliance are primarily in China | Write Chinese-first. Use China evidence and local workflow assumptions. |
| Overseas-first | The launch market is outside China | Write English-first unless the user asks otherwise. Use region-specific evidence. |
| Cross-border | Product serves China and overseas users, companies, capital, trade, travel, education, or data flows | Split assumptions by market and name cross-border dependencies. |
| Global platform | Same core product with localized GTM | Use a shared core PRD plus region-specific appendices. |

## China Product Checklist

- Identity and account: phone, WeChat, enterprise SSO, real-name needs.
- Payment and monetization: WeChat Pay, Alipay, bank transfer, invoice/fapiao, procurement cycles.
- Channels: WeChat, mini programs, app stores, Douyin/Kuaishou/Bilibili/Xiaohongshu, enterprise sales, partner ecosystems.
- Product expectations: mobile-first, dense information surfaces where appropriate, local customer support, operations workflows.
- Compliance and infrastructure: PIPL, data residency expectations, content safety, ICP/app filing, domestic cloud or CDN where applicable.
- Trust signals: case studies, local support, local billing, integration with local tools.

## Overseas Product Checklist

- Region: specify US, EU, UK, APAC, LATAM, MENA, or global.
- Buyer and motion: PLG, sales-led, channel-led, marketplace, open-source/community-led.
- Payments and tax: cards, ACH, invoices, VAT/GST, local currency.
- Compliance: GDPR, CCPA/CPRA, SOC 2, HIPAA, PCI, financial or sector-specific rules when relevant.
- Product expectations: onboarding, accessibility, transparency, terms/privacy, self-serve support, integrations.
- Trust signals: security docs, customer logos, compliance posture, public roadmap, documentation.

## Cross-Border Risk Register

| Risk | China Consideration | Overseas Consideration | Mitigation |
| --- | --- | --- | --- |
| Data transfer | Data residency, PIPL | GDPR/SCCs, regional hosting | Split storage, consent, DPA review |
| Payments | Local wallets, invoices | Cards, tax, local currency | Region-specific billing |
| Support | Chinese business hours, WeChat-style ops | Email/chat SLAs, multilingual support | Tiered support model |
| GTM | Ecosystem/community/private traffic | SEO, marketplaces, sales-led/PLG | Separate channel plans |
| Compliance | Filing/content/industry rules | Privacy/security/sector rules | Launch-gate checklist |

## Output Rule

When the user asks for a product document for both Chinese and overseas users, include:

1. A shared product thesis.
2. China-specific user, evidence, GTM, compliance, and roadmap notes.
3. Overseas-specific user, evidence, GTM, compliance, and roadmap notes.
4. A localization roadmap.
5. Risks that could make the China and overseas versions diverge.
