---
collection: cards
title: '富邦银行 Titanium 卡'
shortName: 'Titanium'
slug: fubon-titanium-card
country: HK
bank: fubon
rewardProgram: fubon-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: fubonTitaniumCard
  issuer: 'Fubon Bank Hong Kong'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'Fubon Bank'
  - 'Titanium'
  - 'Bonus Points'
  - '待确认当前申请状态'
relatedCards:
  - 'fubon-visa-platinum-card'
  - 'fubon-unionpay-dual-currency-platinum-card'
  - 'fubon-yata-credit-card'
sources:
  - 'fubon-official-terms'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 富邦银行 Titanium 卡

> 富邦银行 Titanium 卡按基本奖赏、生活类别和 FTF 官方条款收录。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 富邦银行 Titanium 卡 |
| 简称 | Titanium |
| 市场 | 香港 |
| 发卡银行 | [[banks:fubon|富邦银行]](../banks/fubon.md) |
| 积分体系 | [[reward-programs:fubon-rewards|富邦银行奖赏]](../reward-programs/fubon-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 基本回赠 | 1 point / HK$1 |
| 奖赏单位 | Bonus Points |
| 计算器插件 | `fubonTitaniumCard` |

## 概述

**富邦银行 Titanium 卡** 是 [[banks:fubon|富邦银行]](../banks/fubon.md) 在香港市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:fubon|富邦银行]](../banks/fubon.md)
- 积分体系：[[reward-programs:fubon-rewards|富邦银行奖赏]](../reward-programs/fubon-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:fubon-rewards|富邦银行奖赏]](../reward-programs/fubon-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 已收录回赠口径

以下规则摘自主仓库计算器数据，**不是**数据库正文，迁移后仍需对照官方条款核验。

| 项目 | 口径 |
| --- | --- |
| 本地基本积分 | 1 point / HK$1 |
| 非港币签账积分 | 5 points / HK$1 |
| 周末本地额外积分 | 额外 1 point / HK$1 |

## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `fubonTitaniumCard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:fubon-official-terms|富邦银行 官方产品 / 条款]](../sources/fubon-official-terms.md) — https://www.fubonbank.com.hk/en/cards/credit-card-products/fubon-credit-card.html

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:fubon-visa-platinum-card|富邦银行 Visa 白金卡]](../cards/fubon-visa-platinum-card.md)
- [[cards:fubon-unionpay-dual-currency-platinum-card|富邦银行银联双币白金卡]](../cards/fubon-unionpay-dual-currency-platinum-card.md)
- [[cards:fubon-yata-credit-card|富邦银行 YATA 信用卡]](../cards/fubon-yata-credit-card.md)

## 迁移备注

- Payload collection：`cards`
- slug：`fubon-titanium-card`
- 关系字段：`bank` → `fubon`；`rewardProgram` → `fubon-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:香港信用卡]]
[[Category:富邦银行]]
[[Category:Fubon Bank]]
[[Category:Titanium]]
[[Category:Bonus Points]]
[[Category:待确认当前申请状态]]
