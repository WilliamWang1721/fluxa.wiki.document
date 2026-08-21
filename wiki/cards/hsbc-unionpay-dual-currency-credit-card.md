---
collection: cards
title: '汇丰银联双币信用卡'
shortName: '银联双币'
slug: hsbc-unionpay-dual-currency-credit-card
country: HK
bank: hsbc-hong-kong
rewardProgram: hsbc-rewardcash
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: true
rebateCalculator:
  enabled: true
  calculatorId: hsbcUnionPayDualCurrency
  issuer: 'HSBC Hong Kong'
conversionCalculator:
  enabled: true
  ruleId: unionPayDualCurrency
tags:
  - 'RC'
  - '银联双币'
  - 'CNY/HKD'
relatedCards:
  - 'hsbc-advance-visa-platinum-card'
  - 'hsbc-easy-credit-card-visa-platinum-card'
  - 'hsbc-everymile-credit-card'
  - 'hsbc-premier-mastercard'
  - 'hsbc-pulse-unionpay-dual-currency-diamond-credit-card'
  - 'hsbc-red-credit-card'
  - 'hsbc-visa-gold-card'
  - 'hsbc-visa-gold-card-for-students'
sources: []
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 汇丰银联双币信用卡

> 基础 RewardCash、银联双币外币/内地场景与 FTF 计算。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 汇丰银联双币信用卡 |
| 简称 | 银联双币 |
| 市场 | 香港 |
| 发卡银行 | [[banks:hsbc-hong-kong|汇丰香港]](../banks/hsbc-hong-kong.md) |
| 积分体系 | [[reward-programs:hsbc-rewardcash|汇丰 RewardCash]](../reward-programs/hsbc-rewardcash.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 是 |
| 计算器插件 | `hsbcUnionPayDualCurrency` |
| 兑换规则 | `unionPayDualCurrency` |

## 概述

**汇丰银联双币信用卡** 是 [[banks:hsbc-hong-kong|汇丰香港]](../banks/hsbc-hong-kong.md) 在香港市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-hong-kong|汇丰香港]](../banks/hsbc-hong-kong.md)
- 积分体系：[[reward-programs:hsbc-rewardcash|汇丰 RewardCash]](../reward-programs/hsbc-rewardcash.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-rewardcash|汇丰 RewardCash]](../reward-programs/hsbc-rewardcash.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `hsbcUnionPayDualCurrency` |
| 兑换计算器 | 是 | `unionPayDualCurrency` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

尚未挂接核验来源。

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-advance-visa-platinum-card|汇丰 Advance Visa 白金卡]](../cards/hsbc-advance-visa-platinum-card.md)
- [[cards:hsbc-easy-credit-card-visa-platinum-card|汇丰 easy 信用卡 / 汇丰 Visa 白金卡]](../cards/hsbc-easy-credit-card-visa-platinum-card.md)
- [[cards:hsbc-everymile-credit-card|汇丰 EveryMile 信用卡]](../cards/hsbc-everymile-credit-card.md)
- [[cards:hsbc-premier-mastercard|汇丰卓越理财 Mastercard]](../cards/hsbc-premier-mastercard.md)
- [[cards:hsbc-pulse-unionpay-dual-currency-diamond-credit-card|汇丰 Pulse 银联双币钻石信用卡]](../cards/hsbc-pulse-unionpay-dual-currency-diamond-credit-card.md)
- [[cards:hsbc-red-credit-card|汇丰 Red 信用卡]](../cards/hsbc-red-credit-card.md)
- [[cards:hsbc-visa-gold-card|汇丰 Visa 金卡]](../cards/hsbc-visa-gold-card.md)
- [[cards:hsbc-visa-gold-card-for-students|汇丰学生 Visa 金卡]](../cards/hsbc-visa-gold-card-for-students.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-unionpay-dual-currency-credit-card`
- 关系字段：`bank` → `hsbc-hong-kong`；`rewardProgram` → `hsbc-rewardcash`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:香港信用卡]]
[[Category:汇丰香港]]
[[Category:银联]]
[[Category:RC]]
[[Category:银联双币]]
[[Category:CNY/HKD]]
