---
collection: cards
title: '汇丰中国信用卡'
shortName: '中国信用卡'
slug: hsbc-cn-credit-card
country: CN
bank: hsbc-china
rewardProgram: hsbc-china-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: globalHsbcCnCreditCard
  issuer: 'HSBC CN'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'HSBC'
  - 'CN'
  - '中国信用卡'
  - '仅限卓越理财客户申请'
relatedCards:
  - 'hsbc-cn-sports-vip-credit-card'
  - 'hsbc-cn-choice-credit-card'
sources:
  - 'hsbc-china-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 汇丰中国信用卡

> 中国内地 HSBC 官方信用卡产品。官方名称：HSBC China Credit Card。状态：仅限卓越理财客户申请。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 汇丰中国信用卡 |
| 简称 | 中国信用卡 |
| 市场 | 中国内地 |
| 发卡银行 | [[banks:hsbc-china|汇丰中国]](../banks/hsbc-china.md) |
| 积分体系 | [[reward-programs:hsbc-china-rewards|汇丰中国奖赏]](../reward-programs/hsbc-china-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `globalHsbcCnCreditCard` |
| 英文官方名 | HSBC China Credit Card |
| 产品状态 | 仅限卓越理财客户申请 |

## 概述

**汇丰中国信用卡** 是 [[banks:hsbc-china|汇丰中国]](../banks/hsbc-china.md) 在中国内地市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-china|汇丰中国]](../banks/hsbc-china.md)
- 积分体系：[[reward-programs:hsbc-china-rewards|汇丰中国奖赏]](../reward-programs/hsbc-china-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-china-rewards|汇丰中国奖赏]](../reward-programs/hsbc-china-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `globalHsbcCnCreditCard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:hsbc-china-official-terms|汇丰中国 官方产品 / 条款]](../sources/hsbc-china-official-terms.md) — https://www.hsbc.com.cn/credit-cards/products/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-cn-sports-vip-credit-card|汇丰运动信用卡尊享版]](../cards/hsbc-cn-sports-vip-credit-card.md)
- [[cards:hsbc-cn-choice-credit-card|汇丰生活信用卡]](../cards/hsbc-cn-choice-credit-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-cn-credit-card`
- 关系字段：`bank` → `hsbc-china`；`rewardProgram` → `hsbc-china-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:中国内地信用卡]]
[[Category:汇丰中国]]
[[Category:HSBC]]
[[Category:CN]]
[[Category:中国信用卡]]
[[Category:仅限卓越理财客户申请]]
