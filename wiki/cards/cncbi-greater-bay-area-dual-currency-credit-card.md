---
collection: cards
title: '信银香港大湾区双币信用卡'
shortName: '大湾区双币'
slug: cncbi-greater-bay-area-dual-currency-credit-card
country: HK
bank: citic-international
rewardProgram: citic-international-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: true
rebateCalculator:
  enabled: true
  calculatorId: cncbiGreaterBayAreaDualCurrency
  issuer: 'China CITIC Bank International'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'CNCBI'
  - '大湾区'
  - '双币'
relatedCards:
  - 'cncbi-purple-diamond-credit-card'
  - 'cncbi-jewel-world-credit-card'
  - 'cncbi-hong-kong-airlines-visa-signature-card'
  - 'cncbi-motion-credit-card'
  - 'cncbi-dch-living-mastercard'
sources:
  - 'citic-international-official-terms-25'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 信银香港大湾区双币信用卡

> 信银香港大湾区双币信用卡按银联 / 内地签账和 FTF 官方条款收录。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 信银香港大湾区双币信用卡 |
| 简称 | 大湾区双币 |
| 市场 | 香港 |
| 发卡银行 | [[banks:citic-international|中信银行国际]](../banks/citic-international.md) |
| 积分体系 | [[reward-programs:citic-international-rewards|中信银行国际奖赏]](../reward-programs/citic-international-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 是 |
| 基本回赠 | 0.4% |
| 奖赏单位 | HKD |
| 计算器插件 | `cncbiGreaterBayAreaDualCurrency` |

## 概述

**信银香港大湾区双币信用卡** 是 [[banks:citic-international|中信银行国际]](../banks/citic-international.md) 在香港市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:citic-international|中信银行国际]](../banks/citic-international.md)
- 积分体系：[[reward-programs:citic-international-rewards|中信银行国际奖赏]](../reward-programs/citic-international-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:citic-international-rewards|中信银行国际奖赏]](../reward-programs/citic-international-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 已收录回赠口径

以下规则摘自主仓库计算器数据，**不是**数据库正文，迁移后仍需对照官方条款核验。

| 项目 | 口径 |
| --- | --- |
| 基本现金回赠 | 0.4% |
| 人民币 / 云闪付 App 额外回赠 | 额外 3.6% |
| 单笔人民币签账额外回赠 | 额外 6% |

## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `cncbiGreaterBayAreaDualCurrency` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:citic-international-official-terms-25|中信银行国际 官方产品 / 条款]](../sources/citic-international-official-terms-25.md) — https://www.cncbinternational.com/_document/personal/credit-cards/gba_10percent_tncs_en.pdf?uuid=Ni20ltQxBdwhernZ0263

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:cncbi-purple-diamond-credit-card|信银国际 CITIC diamond 银联双币信用卡]](../cards/cncbi-purple-diamond-credit-card.md)
- [[cards:cncbi-jewel-world-credit-card|信银香港 Jewel World 信用卡]](../cards/cncbi-jewel-world-credit-card.md)
- [[cards:cncbi-hong-kong-airlines-visa-signature-card|信银国际香港航空 Mastercard]](../cards/cncbi-hong-kong-airlines-visa-signature-card.md)
- [[cards:cncbi-motion-credit-card|信银香港 Motion 信用卡]](../cards/cncbi-motion-credit-card.md)
- [[cards:cncbi-dch-living-mastercard|信银香港 DCH Living Mastercard]](../cards/cncbi-dch-living-mastercard.md)

## 迁移备注

- Payload collection：`cards`
- slug：`cncbi-greater-bay-area-dual-currency-credit-card`
- 关系字段：`bank` → `citic-international`；`rewardProgram` → `citic-international-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:香港信用卡]]
[[Category:中信银行国际]]
[[Category:银联]]
[[Category:CNCBI]]
[[Category:大湾区]]
[[Category:双币]]
