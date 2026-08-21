---
collection: cards
title: '汇丰越南卓越理财信用卡'
shortName: 'Premier'
slug: hsbc-vn-premier-credit-card
country: VN
bank: hsbc-vietnam
rewardProgram: hsbc-vietnam-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: globalHsbcVnPremierCreditCard
  issuer: 'HSBC VN'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'HSBC'
  - 'VN'
  - 'Premier'
  - '官方产品页列出，未见停售标记'
relatedCards:
  - 'hsbc-vn-live-plus-credit-card'
  - 'hsbc-vn-cash-back-credit-card'
  - 'hsbc-vn-livefree-credit-card'
  - 'hsbc-vn-travelone-credit-card'
sources:
  - 'hsbc-vietnam-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 汇丰越南卓越理财信用卡

> 越南 HSBC 官方信用卡产品。官方名称：HSBC Premier Credit Card。状态：官方产品页列出，未见停售标记。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 汇丰越南卓越理财信用卡 |
| 简称 | Premier |
| 市场 | 越南 |
| 发卡银行 | [[banks:hsbc-vietnam|汇丰越南]](../banks/hsbc-vietnam.md) |
| 积分体系 | [[reward-programs:hsbc-vietnam-rewards|汇丰越南奖赏]](../reward-programs/hsbc-vietnam-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `globalHsbcVnPremierCreditCard` |
| 英文官方名 | HSBC Premier Credit Card |
| 产品状态 | 官方产品页列出，未见停售标记 |

## 概述

**汇丰越南卓越理财信用卡** 是 [[banks:hsbc-vietnam|汇丰越南]](../banks/hsbc-vietnam.md) 在越南市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:hsbc-vietnam|汇丰越南]](../banks/hsbc-vietnam.md)
- 积分体系：[[reward-programs:hsbc-vietnam-rewards|汇丰越南奖赏]](../reward-programs/hsbc-vietnam-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:hsbc-vietnam-rewards|汇丰越南奖赏]](../reward-programs/hsbc-vietnam-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `globalHsbcVnPremierCreditCard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:hsbc-vietnam-official-terms|汇丰越南 官方产品 / 条款]](../sources/hsbc-vietnam-official-terms.md) — https://www.hsbc.com.vn/credit-cards/products/

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:hsbc-vn-live-plus-credit-card|汇丰越南 Live+ 信用卡]](../cards/hsbc-vn-live-plus-credit-card.md)
- [[cards:hsbc-vn-cash-back-credit-card|汇丰越南 Cash Back 信用卡]](../cards/hsbc-vn-cash-back-credit-card.md)
- [[cards:hsbc-vn-livefree-credit-card|汇丰越南 LiveFree 信用卡]](../cards/hsbc-vn-livefree-credit-card.md)
- [[cards:hsbc-vn-travelone-credit-card|汇丰越南 TravelOne 信用卡]](../cards/hsbc-vn-travelone-credit-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`hsbc-vn-premier-credit-card`
- 关系字段：`bank` → `hsbc-vietnam`；`rewardProgram` → `hsbc-vietnam-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:越南信用卡]]
[[Category:汇丰越南]]
[[Category:HSBC]]
[[Category:VN]]
[[Category:Premier]]
[[Category:官方产品页列出，未见停售标记]]
