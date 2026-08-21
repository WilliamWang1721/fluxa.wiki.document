---
collection: cards
title: '汇丰卡塔尔 Advance Platinum 信用卡'
shortName: 'Advance Platinum'
slug: hsbc-qa-advance-platinum-credit-card
country: QA
bank: hsbc-qatar
rewardProgram: hsbc-qatar-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: globalHsbcQaAdvancePlatinumCreditCard
  issuer: 'HSBC QA'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'HSBC'
  - 'QA'
  - 'Advance Platinum'
  - 'Advance 客户产品'
relatedCards:
  - 'hsbc-qa-premier-credit-card'
  - 'hsbc-qa-visa-platinum-credit-card'
  - 'hsbc-qa-cashback-credit-card'
sources:
  - 'hsbc-qatar-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 汇丰卡塔尔 Advance Platinum 信用卡

> 卡塔尔 HSBC 官方信用卡产品。官方名称：HSBC Advance Platinum Credit Card。状态：Advance 客户产品。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 汇丰卡塔尔 Advance Platinum 信用卡 |
| 简称 | Advance Platinum |
| 市场 | 卡塔尔 |
| 发卡银行 | [[banks:hsbc-qatar|汇丰卡塔尔]](../banks/hsbc-qatar.md) |
| 积分体系 | [[reward-programs:hsbc-qatar-rewards|汇丰卡塔尔奖赏]](../reward-programs/hsbc-qatar-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `globalHsbcQaAdvancePlatinumCreditCard` |
| 英文官方名 | HSBC Advance Platinum Credit Card |
| 产品状态 | Advance 客户产品 |

## 概述

**汇丰卡塔尔 Advance Platinum 信用卡** 是 [[banks:hsbc-qatar|汇丰卡塔尔]](../banks/hsbc-qatar.md) 在卡塔尔市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-qatar|汇丰卡塔尔]](../banks/hsbc-qatar.md)
- 积分体系：[[reward-programs:hsbc-qatar-rewards|汇丰卡塔尔奖赏]](../reward-programs/hsbc-qatar-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-qatar-rewards|汇丰卡塔尔奖赏]](../reward-programs/hsbc-qatar-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `globalHsbcQaAdvancePlatinumCreditCard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:hsbc-qatar-official-terms|汇丰卡塔尔 官方产品 / 条款]](../sources/hsbc-qatar-official-terms.md) — https://www.hsbc.com.qa/credit-cards/products/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-qa-premier-credit-card|汇丰卡塔尔 Premier 信用卡]](../cards/hsbc-qa-premier-credit-card.md)
- [[cards:hsbc-qa-visa-platinum-credit-card|汇丰卡塔尔 Visa Platinum 信用卡]](../cards/hsbc-qa-visa-platinum-credit-card.md)
- [[cards:hsbc-qa-cashback-credit-card|汇丰卡塔尔 Cashback 信用卡]](../cards/hsbc-qa-cashback-credit-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-qa-advance-platinum-credit-card`
- 关系字段：`bank` → `hsbc-qatar`；`rewardProgram` → `hsbc-qatar-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:卡塔尔信用卡]]
[[Category:汇丰卡塔尔]]
[[Category:HSBC]]
[[Category:QA]]
[[Category:Advance Platinum]]
[[Category:Advance 客户产品]]
