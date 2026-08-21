---
collection: cards
title: '汇丰美国 Premier World Mastercard 信用卡'
shortName: 'Premier World'
slug: hsbc-us-premier-world-mastercard
country: US
bank: hsbc-united-states
rewardProgram: hsbc-united-states-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: globalHsbcUsPremierWorldMastercard
  issuer: 'HSBC US'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'HSBC'
  - 'US'
  - 'Premier World'
  - '可申请，有 Premier checking 关系要求'
relatedCards:
  - 'hsbc-us-elite-world-elite-mastercard'
sources:
  - 'hsbc-united-states-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 汇丰美国 Premier World Mastercard 信用卡

> 美国 HSBC 官方信用卡产品。官方名称：HSBC Premier credit card / HSBC Premier World Mastercard。状态：可申请，有 Premier checking 关系要求。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 汇丰美国 Premier World Mastercard 信用卡 |
| 简称 | Premier World |
| 市场 | 美国 |
| 发卡银行 | [[banks:hsbc-united-states|汇丰美国]](../banks/hsbc-united-states.md) |
| 积分体系 | [[reward-programs:hsbc-united-states-rewards|汇丰美国奖赏]](../reward-programs/hsbc-united-states-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `globalHsbcUsPremierWorldMastercard` |
| 英文官方名 | HSBC Premier credit card / HSBC Premier World Mastercard |
| 产品状态 | 可申请，有 Premier checking 关系要求 |

## 概述

**汇丰美国 Premier World Mastercard 信用卡** 是 [[banks:hsbc-united-states|汇丰美国]](../banks/hsbc-united-states.md) 在美国市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-united-states|汇丰美国]](../banks/hsbc-united-states.md)
- 积分体系：[[reward-programs:hsbc-united-states-rewards|汇丰美国奖赏]](../reward-programs/hsbc-united-states-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-united-states-rewards|汇丰美国奖赏]](../reward-programs/hsbc-united-states-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `globalHsbcUsPremierWorldMastercard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:hsbc-united-states-official-terms|汇丰美国 官方产品 / 条款]](../sources/hsbc-united-states-official-terms.md) — https://www.us.hsbc.com/credit-cards/products/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-us-elite-world-elite-mastercard|汇丰美国 Elite World Elite Mastercard 信用卡]](../cards/hsbc-us-elite-world-elite-mastercard.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-us-premier-world-mastercard`
- 关系字段：`bank` → `hsbc-united-states`；`rewardProgram` → `hsbc-united-states-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:美国信用卡]]
[[Category:汇丰美国]]
[[Category:HSBC]]
[[Category:US]]
[[Category:Premier World]]
[[Category:可申请，有 Premier checking 关系要求]]
