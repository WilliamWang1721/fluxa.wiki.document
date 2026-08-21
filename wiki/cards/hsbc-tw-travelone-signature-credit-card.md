---
collection: cards
title: '汇丰旅人御玺卡'
shortName: '旅人御玺卡'
slug: hsbc-tw-travelone-signature-credit-card
country: TW
bank: hsbc-taiwan
rewardProgram: hsbc-taiwan-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: globalHsbcTwTraveloneSignatureCreditCard
  issuer: 'HSBC TW'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'HSBC'
  - 'TW'
  - '旅人御玺卡'
  - '官方产品页列出，未见停售标记'
relatedCards:
  - 'hsbc-tw-cashback-business-titanium-credit-card'
  - 'hsbc-tw-live-plus-credit-card'
  - 'hsbc-tw-travelone-credit-card'
  - 'hsbc-tw-premier-credit-card'
  - 'hsbc-tw-cashback-signature-credit-card'
sources:
  - 'hsbc-taiwan-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 汇丰旅人御玺卡

> 台湾 HSBC 官方信用卡产品。官方名称：HSBC TravelOne Signature Credit Card。状态：官方产品页列出，未见停售标记。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 汇丰旅人御玺卡 |
| 简称 | 旅人御玺卡 |
| 市场 | 台湾 |
| 发卡银行 | [[banks:hsbc-taiwan|汇丰台湾]](../banks/hsbc-taiwan.md) |
| 积分体系 | [[reward-programs:hsbc-taiwan-rewards|汇丰台湾奖赏]](../reward-programs/hsbc-taiwan-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `globalHsbcTwTraveloneSignatureCreditCard` |
| 英文官方名 | HSBC TravelOne Signature Credit Card |
| 产品状态 | 官方产品页列出，未见停售标记 |

## 概述

**汇丰旅人御玺卡** 是 [[banks:hsbc-taiwan|汇丰台湾]](../banks/hsbc-taiwan.md) 在台湾市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-taiwan|汇丰台湾]](../banks/hsbc-taiwan.md)
- 积分体系：[[reward-programs:hsbc-taiwan-rewards|汇丰台湾奖赏]](../reward-programs/hsbc-taiwan-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-taiwan-rewards|汇丰台湾奖赏]](../reward-programs/hsbc-taiwan-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `globalHsbcTwTraveloneSignatureCreditCard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:hsbc-taiwan-official-terms|汇丰台湾 官方产品 / 条款]](../sources/hsbc-taiwan-official-terms.md) — https://www.hsbc.com.tw/credit-cards/products/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-tw-cashback-business-titanium-credit-card|汇丰汇钻卡]](../cards/hsbc-tw-cashback-business-titanium-credit-card.md)
- [[cards:hsbc-tw-live-plus-credit-card|汇丰 Live+ 现金回馈卡]](../cards/hsbc-tw-live-plus-credit-card.md)
- [[cards:hsbc-tw-travelone-credit-card|汇丰旅人轻旅卡]](../cards/hsbc-tw-travelone-credit-card.md)
- [[cards:hsbc-tw-premier-credit-card|汇丰卓越理财信用卡]](../cards/hsbc-tw-premier-credit-card.md)
- [[cards:hsbc-tw-cashback-signature-credit-card|汇丰现金回馈御玺卡]](../cards/hsbc-tw-cashback-signature-credit-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-tw-travelone-signature-credit-card`
- 关系字段：`bank` → `hsbc-taiwan`；`rewardProgram` → `hsbc-taiwan-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:台湾信用卡]]
[[Category:汇丰台湾]]
[[Category:HSBC]]
[[Category:TW]]
[[Category:旅人御玺卡]]
[[Category:官方产品页列出，未见停售标记]]
