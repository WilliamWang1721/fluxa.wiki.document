---
collection: cards
title: '东亚银行香港马主协会 World Mastercard 卡'
shortName: '马主协会 World'
slug: bea-hk-racehorse-owners-world-mastercard
country: HK
bank: bank-of-east-asia
rewardProgram: bea-rewards
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: beaHkRacehorseOwnersWorldMastercard
  issuer: 'Bank of East Asia'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'BEA'
  - 'World Mastercard'
  - '联营卡'
relatedCards:
  - 'bea-aia-credit-card'
  - 'bea-centennial-world-elite-mastercard'
  - 'bea-corporate-credit-card'
  - 'bea-cpa-australia-credit-card'
  - 'bea-ctf-life-credit-card'
  - 'bea-eduhk-student-visa-card'
  - 'bea-goal-credit-card'
  - 'bea-hku-space-mastercard'
sources:
  - 'bank-of-east-asia-official-terms-9'
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 东亚银行香港马主协会 World Mastercard 卡

> 东亚银行香港马主协会 World Mastercard 按基本奖赏与 FTF 规则收录。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 东亚银行香港马主协会 World Mastercard 卡 |
| 简称 | 马主协会 World |
| 市场 | 香港 |
| 发卡银行 | [[banks:bank-of-east-asia|东亚银行]](../banks/bank-of-east-asia.md) |
| 积分体系 | [[reward-programs:bea-rewards|东亚银行奖赏]](../reward-programs/bea-rewards.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 基本回赠 | 1 point / HK$1 = 0.4% |
| 奖赏单位 | HKD |
| 计算器插件 | `beaHkRacehorseOwnersWorldMastercard` |

## 概述

**东亚银行香港马主协会 World Mastercard 卡** 是 [[banks:bank-of-east-asia|东亚银行]](../banks/bank-of-east-asia.md) 在香港市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:bank-of-east-asia|东亚银行]](../banks/bank-of-east-asia.md)
- 积分体系：[[reward-programs:bea-rewards|东亚银行奖赏]](../reward-programs/bea-rewards.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:bea-rewards|东亚银行奖赏]](../reward-programs/bea-rewards.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 已收录回赠口径

以下规则摘自主仓库计算器数据，**不是**数据库正文，迁移后仍需对照官方条款核验。

| 项目 | 口径 |
| --- | --- |
| 基本积分现金价值 | 1 point / HK$1 = 0.4% |

## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `beaHkRacehorseOwnersWorldMastercard` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

- [[sources:bank-of-east-asia-official-terms-9|东亚银行 官方产品 / 条款]](../sources/bank-of-east-asia-official-terms-9.md) — https://www.hkbea.com/pdf/en/credit-card/master-reward-tnc_en.pdf

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:bea-aia-credit-card|东亚银行 AIA 信用卡]](../cards/bea-aia-credit-card.md)
- [[cards:bea-centennial-world-elite-mastercard|东亚银行 CENTENNIAL World Elite Mastercard 卡]](../cards/bea-centennial-world-elite-mastercard.md)
- [[cards:bea-corporate-credit-card|东亚银行公司卡]](../cards/bea-corporate-credit-card.md)
- [[cards:bea-cpa-australia-credit-card|东亚银行澳洲会计师公会信用卡]](../cards/bea-cpa-australia-credit-card.md)
- [[cards:bea-ctf-life-credit-card|东亚银行周大福人寿信用卡]](../cards/bea-ctf-life-credit-card.md)
- [[cards:bea-eduhk-student-visa-card|东亚银行香港教育大学 Visa 卡（学生专用）]](../cards/bea-eduhk-student-visa-card.md)
- [[cards:bea-goal-credit-card|东亚银行 BEA GOAL 信用卡]](../cards/bea-goal-credit-card.md)
- [[cards:bea-hku-space-mastercard|东亚银行香港大学专业进修学院 Mastercard 卡]](../cards/bea-hku-space-mastercard.md)

## 迁移备注

- Payload collection：`cards`
- slug：`bea-hk-racehorse-owners-world-mastercard`
- 关系字段：`bank` → `bank-of-east-asia`；`rewardProgram` → `bea-rewards`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:香港信用卡]]
[[Category:东亚银行]]
[[Category:BEA]]
[[Category:World Mastercard]]
[[Category:联营卡]]
