---
collection: cards
title: '中银香港 Chill Card'
shortName: 'Chill Card'
slug: bochk-chill-card
country: HK
bank: boc-hong-kong
rewardProgram: boc-hong-kong-points
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: bochkChillCard
  issuer: 'BOC Hong Kong'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'BOCHK'
  - 'Chill'
  - '网上签账'
relatedCards:
  - 'bochk-private-card'
  - 'bochk-visa-infinite-card'
  - 'bochk-unionpay-dual-currency-diamond-card'
  - 'bochk-cheers-card'
  - 'bochk-i-card-virtual-card'
  - 'bochk-dual-currency-gba-card'
sources:
  - 'boc-hong-kong-official-terms-5'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 中银香港 Chill Card

> 中银香港 Chill Card 按网上 / 生活类别、基本奖赏与 FTF 规则收录。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 中银香港 Chill Card |
| 简称 | Chill Card |
| 市场 | 香港 |
| 发卡银行 | [[banks:boc-hong-kong|中银香港]](../banks/boc-hong-kong.md) |
| 积分体系 | [[reward-programs:boc-hong-kong-points|中银香港积分]](../reward-programs/boc-hong-kong-points.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 基本回赠 | 1 point / HK$1 = 0.4% |
| 奖赏单位 | HKD |
| 计算器插件 | `bochkChillCard` |

## 概述

**中银香港 Chill Card** 是 [[banks:boc-hong-kong|中银香港]](../banks/boc-hong-kong.md) 在香港市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:boc-hong-kong|中银香港]](../banks/boc-hong-kong.md)
- 积分体系：[[reward-programs:boc-hong-kong-points|中银香港积分]](../reward-programs/boc-hong-kong-points.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:boc-hong-kong-points|中银香港积分]](../reward-programs/boc-hong-kong-points.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 已收录回赠口径

以下规则摘自主仓库计算器数据，**不是**数据库正文，迁移后仍需对照官方条款核验。

| 项目 | 口径 |
| --- | --- |
| Gift Point 基本现金价值 | 1 point / HK$1 = 0.4% |
| 网上 / 海外额外现金回赠 | 额外 3.6% 现金回赠 |
| Chill 指定商户额外现金回赠 | 额外 7.6% 现金回赠 |

## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `bochkChillCard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:boc-hong-kong-official-terms-5|中银香港 官方产品 / 条款]](../sources/boc-hong-kong-official-terms-5.md) — https://www.bochk.com/dam/boccreditcard/chillcardmp/eng/index662.html

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:bochk-private-card|中银香港 Private Card]](../cards/bochk-private-card.md)
- [[cards:bochk-visa-infinite-card|中银香港 Visa Infinite 卡（旧称）]](../cards/bochk-visa-infinite-card.md)
- [[cards:bochk-unionpay-dual-currency-diamond-card|中银香港银联双币钻石卡]](../cards/bochk-unionpay-dual-currency-diamond-card.md)
- [[cards:bochk-cheers-card|中银香港 Cheers Card]](../cards/bochk-cheers-card.md)
- [[cards:bochk-i-card-virtual-card|中银 i-card 双币钻石虚拟卡]](../cards/bochk-i-card-virtual-card.md)
- [[cards:bochk-dual-currency-gba-card|中银双币卡]](../cards/bochk-dual-currency-gba-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`bochk-chill-card`
- 关系字段：`bank` → `boc-hong-kong`；`rewardProgram` → `boc-hong-kong-points`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:香港信用卡]]
[[Category:中银香港]]
[[Category:BOCHK]]
[[Category:Chill]]
[[Category:网上签账]]
