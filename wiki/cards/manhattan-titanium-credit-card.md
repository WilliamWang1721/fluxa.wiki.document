---
collection: cards
title: 'MANHATTAN Titanium 信用卡'
shortName: 'MANHATTAN Titanium'
slug: manhattan-titanium-credit-card
country: HK
bank: standard-chartered-hong-kong
rewardProgram: standard-chartered-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: manhattanTitaniumCreditCard
  issuer: 'Standard Chartered Hong Kong'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'MANHATTAN'
  - 'Titanium'
relatedCards:
  - 'standard-chartered-cathay-mastercard'
  - 'standard-chartered-smart-credit-card'
  - 'standard-chartered-simply-cash-visa-card'
  - 'standard-chartered-a-point-card'
  - 'standard-chartered-visa-infinite-credit-card'
  - 'standard-chartered-unionpay-dual-currency-platinum-credit-card'
  - 'standard-chartered-platinum-cashback-credit-card'
  - 'standard-chartered-cashback-credit-card'
sources:
  - 'standard-chartered-hong-kong-official-terms-16'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# MANHATTAN Titanium 信用卡

> MANHATTAN Titanium 信用卡按娱乐 / 生活类别、基本奖赏与 FTF 规则收录。

| 字段 | 值 |
| --- | --- |
| 官方名称 | MANHATTAN Titanium 信用卡 |
| 简称 | MANHATTAN Titanium |
| 市场 | 香港 |
| 发卡银行 | [[banks:standard-chartered-hong-kong|渣打香港]](../banks/standard-chartered-hong-kong.md) |
| 积分体系 | [[reward-programs:standard-chartered-rewards|渣打奖励]](../reward-programs/standard-chartered-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 基本回赠 | 1 point / HK$1 |
| 奖赏单位 | 360 Rewards Points |
| 计算器插件 | `manhattanTitaniumCreditCard` |

## 概述

**MANHATTAN Titanium 信用卡** 是 [[banks:standard-chartered-hong-kong|渣打香港]](../banks/standard-chartered-hong-kong.md) 在香港市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:standard-chartered-hong-kong|渣打香港]](../banks/standard-chartered-hong-kong.md)
- 积分体系：[[reward-programs:standard-chartered-rewards|渣打奖励]](../reward-programs/standard-chartered-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:standard-chartered-rewards|渣打奖励]](../reward-programs/standard-chartered-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 已收录回赠口径

以下规则摘自主仓库计算器数据，**不是**数据库正文，迁移后仍需对照官方条款核验。

| 项目 | 口径 |
| --- | --- |
| 基本积分 | 1 point / HK$1 |

## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `manhattanTitaniumCreditCard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:standard-chartered-hong-kong-official-terms-16|渣打香港 官方产品 / 条款]](../sources/standard-chartered-hong-kong-official-terms-16.md) — https://www.sc.com/hk/credit-cards/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:standard-chartered-cathay-mastercard|渣打国泰 Mastercard]](../cards/standard-chartered-cathay-mastercard.md)
- [[cards:standard-chartered-smart-credit-card|渣打 Smart 信用卡]](../cards/standard-chartered-smart-credit-card.md)
- [[cards:standard-chartered-simply-cash-visa-card|渣打 Simply Cash Visa 卡]](../cards/standard-chartered-simply-cash-visa-card.md)
- [[cards:standard-chartered-a-point-card|渣打 A.Point Card]](../cards/standard-chartered-a-point-card.md)
- [[cards:standard-chartered-visa-infinite-credit-card|渣打 Visa Infinite 信用卡]](../cards/standard-chartered-visa-infinite-credit-card.md)
- [[cards:standard-chartered-unionpay-dual-currency-platinum-credit-card|渣打银联双币白金信用卡]](../cards/standard-chartered-unionpay-dual-currency-platinum-credit-card.md)
- [[cards:standard-chartered-platinum-cashback-credit-card|渣打倍多纷白金信用卡]](../cards/standard-chartered-platinum-cashback-credit-card.md)
- [[cards:standard-chartered-cashback-credit-card|渣打倍多纷信用卡]](../cards/standard-chartered-cashback-credit-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`manhattan-titanium-credit-card`
- 关系字段：`bank` → `standard-chartered-hong-kong`；`rewardProgram` → `standard-chartered-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:香港信用卡]]
[[Category:渣打香港]]
[[Category:MANHATTAN]]
[[Category:Titanium]]
