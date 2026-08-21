---
collection: cards
title: '汇丰马耳他 Premier Credit Mastercard 信用卡'
shortName: 'Premier Mastercard'
slug: hsbc-mt-premier-credit-mastercard
country: MT
bank: hsbc-malta
rewardProgram: hsbc-malta-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: globalHsbcMtPremierCreditMastercard
  issuer: 'HSBC MT'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'HSBC'
  - 'MT'
  - 'Premier Mastercard'
  - 'Premier 客户产品'
relatedCards:
  - 'hsbc-mt-advance-credit-card'
  - 'hsbc-mt-mastercard-credit-card'
  - 'hsbc-mt-visa-credit-card'
sources:
  - 'hsbc-malta-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 汇丰马耳他 Premier Credit Mastercard 信用卡

> 马耳他 HSBC 官方信用卡产品。官方名称：Premier Credit Card / Premier Credit Mastercard。状态：Premier 客户产品。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 汇丰马耳他 Premier Credit Mastercard 信用卡 |
| 简称 | Premier Mastercard |
| 市场 | 马耳他 |
| 发卡银行 | [[banks:hsbc-malta|汇丰马耳他]](../banks/hsbc-malta.md) |
| 积分体系 | [[reward-programs:hsbc-malta-rewards|汇丰马耳他奖赏]](../reward-programs/hsbc-malta-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `globalHsbcMtPremierCreditMastercard` |
| 英文官方名 | Premier Credit Card / Premier Credit Mastercard |
| 产品状态 | Premier 客户产品 |

## 概述

**汇丰马耳他 Premier Credit Mastercard 信用卡** 是 [[banks:hsbc-malta|汇丰马耳他]](../banks/hsbc-malta.md) 在马耳他市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-malta|汇丰马耳他]](../banks/hsbc-malta.md)
- 积分体系：[[reward-programs:hsbc-malta-rewards|汇丰马耳他奖赏]](../reward-programs/hsbc-malta-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-malta-rewards|汇丰马耳他奖赏]](../reward-programs/hsbc-malta-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `globalHsbcMtPremierCreditMastercard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:hsbc-malta-official-terms|汇丰马耳他 官方产品 / 条款]](../sources/hsbc-malta-official-terms.md) — https://www.hsbc.com.mt/credit-cards/products/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-mt-advance-credit-card|汇丰马耳他 Advance 信用卡]](../cards/hsbc-mt-advance-credit-card.md)
- [[cards:hsbc-mt-mastercard-credit-card|汇丰马耳他 Mastercard 信用卡]](../cards/hsbc-mt-mastercard-credit-card.md)
- [[cards:hsbc-mt-visa-credit-card|汇丰马耳他 Visa 信用卡]](../cards/hsbc-mt-visa-credit-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-mt-premier-credit-mastercard`
- 关系字段：`bank` → `hsbc-malta`；`rewardProgram` → `hsbc-malta-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:马耳他信用卡]]
[[Category:汇丰马耳他]]
[[Category:HSBC]]
[[Category:MT]]
[[Category:Premier Mastercard]]
[[Category:Premier 客户产品]]
