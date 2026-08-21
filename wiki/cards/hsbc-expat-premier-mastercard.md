---
collection: cards
title: 'HSBC Expat Premier Mastercard 信用卡'
shortName: 'Premier Mastercard'
slug: hsbc-expat-premier-mastercard
country: EXPAT_JE
bank: hsbc-expat
rewardProgram: hsbc-expat-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: globalHsbcExpatPremierMastercard
  issuer: 'HSBC EXPAT_JE'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'HSBC'
  - 'EXPAT_JE'
  - 'Premier Mastercard'
  - '可申请，需 Expat Premier'
relatedCards:
  - 'hsbc-expat-premier-world-elite-mastercard'
  - 'hsbc-expat-credit-card'
sources:
  - 'hsbc-expat-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# HSBC Expat Premier Mastercard 信用卡

> HSBC Expat / 泽西离岸 HSBC 官方信用卡产品。官方名称：Premier Mastercard。状态：可申请，需 Expat Premier。

| 字段 | 值 |
| --- | --- |
| 官方名称 | HSBC Expat Premier Mastercard 信用卡 |
| 简称 | Premier Mastercard |
| 市场 | HSBC Expat / 泽西离岸 |
| 发卡银行 | [[banks:hsbc-expat|汇丰 Expat]](../banks/hsbc-expat.md) |
| 积分体系 | [[reward-programs:hsbc-expat-rewards|汇丰 Expat奖赏]](../reward-programs/hsbc-expat-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `globalHsbcExpatPremierMastercard` |
| 英文官方名 | Premier Mastercard |
| 产品状态 | 可申请，需 Expat Premier |

## 概述

**HSBC Expat Premier Mastercard 信用卡** 是 [[banks:hsbc-expat|汇丰 Expat]](../banks/hsbc-expat.md) 在HSBC Expat / 泽西离岸市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-expat|汇丰 Expat]](../banks/hsbc-expat.md)
- 积分体系：[[reward-programs:hsbc-expat-rewards|汇丰 Expat奖赏]](../reward-programs/hsbc-expat-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-expat-rewards|汇丰 Expat奖赏]](../reward-programs/hsbc-expat-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `globalHsbcExpatPremierMastercard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:hsbc-expat-official-terms|汇丰 Expat 官方产品 / 条款]](../sources/hsbc-expat-official-terms.md) — https://www.expat.hsbc.com/credit-cards/products/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-expat-premier-world-elite-mastercard|HSBC Expat Premier World Elite Mastercard 信用卡]](../cards/hsbc-expat-premier-world-elite-mastercard.md)
- [[cards:hsbc-expat-credit-card|HSBC Expat 信用卡]](../cards/hsbc-expat-credit-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-expat-premier-mastercard`
- 关系字段：`bank` → `hsbc-expat`；`rewardProgram` → `hsbc-expat-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:HSBC Expat / 泽西离岸信用卡]]
[[Category:汇丰 Expat]]
[[Category:HSBC]]
[[Category:EXPAT_JE]]
[[Category:Premier Mastercard]]
[[Category:可申请，需 Expat Premier]]
