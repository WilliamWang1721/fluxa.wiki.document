---
collection: cards
title: '汇丰澳门 Visa 金卡'
shortName: 'Visa 金卡'
slug: hsbc-mo-visa-gold-card
country: MO
bank: hsbc-macau
rewardProgram: hsbc-macau-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: globalHsbcMoVisaGoldCard
  issuer: 'HSBC MO'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'HSBC'
  - 'MO'
  - 'Visa 金卡'
  - '官方产品页列出，未见停售标记'
relatedCards:
  - 'hsbc-mo-pulse-unionpay-dual-currency-diamond-credit-card'
  - 'hsbc-mo-visa-classic-card'
sources:
  - 'hsbc-macau-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 汇丰澳门 Visa 金卡

> 澳门 HSBC 官方信用卡产品。官方名称：HSBC Visa Gold Card。状态：官方产品页列出，未见停售标记。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 汇丰澳门 Visa 金卡 |
| 简称 | Visa 金卡 |
| 市场 | 澳门 |
| 发卡银行 | [[banks:hsbc-macau|汇丰澳门]](../banks/hsbc-macau.md) |
| 积分体系 | [[reward-programs:hsbc-macau-rewards|汇丰澳门奖赏]](../reward-programs/hsbc-macau-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `globalHsbcMoVisaGoldCard` |
| 英文官方名 | HSBC Visa Gold Card |
| 产品状态 | 官方产品页列出，未见停售标记 |

## 概述

**汇丰澳门 Visa 金卡** 是 [[banks:hsbc-macau|汇丰澳门]](../banks/hsbc-macau.md) 在澳门市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-macau|汇丰澳门]](../banks/hsbc-macau.md)
- 积分体系：[[reward-programs:hsbc-macau-rewards|汇丰澳门奖赏]](../reward-programs/hsbc-macau-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-macau-rewards|汇丰澳门奖赏]](../reward-programs/hsbc-macau-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `globalHsbcMoVisaGoldCard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:hsbc-macau-official-terms|汇丰澳门 官方产品 / 条款]](../sources/hsbc-macau-official-terms.md) — https://www.hsbc.com.mo/credit-cards/products/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-mo-pulse-unionpay-dual-currency-diamond-credit-card|汇丰澳门 Pulse 银联双币钻石信用卡]](../cards/hsbc-mo-pulse-unionpay-dual-currency-diamond-credit-card.md)
- [[cards:hsbc-mo-visa-classic-card|汇丰澳门 Visa 经典卡]](../cards/hsbc-mo-visa-classic-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-mo-visa-gold-card`
- 关系字段：`bank` → `hsbc-macau`；`rewardProgram` → `hsbc-macau-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:澳门信用卡]]
[[Category:汇丰澳门]]
[[Category:HSBC]]
[[Category:MO]]
[[Category:Visa 金卡]]
[[Category:官方产品页列出，未见停售标记]]
