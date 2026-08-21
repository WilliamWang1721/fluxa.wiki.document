---
collection: cards
title: '建行亚洲白金信用卡'
shortName: '白金卡'
slug: ccb-asia-platinum-credit-card
country: HK
bank: ccb-asia
rewardProgram: ccb-asia-points
sourceLevel: C
status: stub
_status: draft
lastVerifiedAt: null
unionPay: false
rebateCalculator:
  enabled: true
  calculatorId: ccbAsiaPlatinum
  issuer: 'CCB (Asia)'
conversionCalculator:
  enabled: false
  ruleId: null
tags:
  - 'CCB Asia'
  - 'Platinum'
relatedCards:
  - 'ccb-asia-aia-visa-credit-card'
  - 'ccb-asia-eye-credit-card'
  - 'ccb-asia-gba-virtual-unionpay-credit-card'
  - 'ccb-asia-industry-unionpay-dual-currency-credit-card'
  - 'ccb-asia-octopus-motorist-unionpay-diamond-credit-card'
  - 'ccb-asia-octopus-unionpay-dual-currency-credit-card'
  - 'ccb-asia-pui-ching-unionpay-dual-currency-credit-card'
  - 'ccb-asia-travo-mastercard'
sources: []
origin: payload-website-starter
generatedAt: 2026-08-21
---
{{Infobox card}}

# 建行亚洲白金信用卡

> 白金信用卡按建行亚洲基本奖赏现金价值计算。

| 字段 | 值 |
| --- | --- |
| 官方名称 | 建行亚洲白金信用卡 |
| 简称 | 白金卡 |
| 市场 | 香港 |
| 发卡银行 | [[banks:ccb-asia|建行亚洲]](../banks/ccb-asia.md) |
| 积分体系 | [[reward-programs:ccb-asia-points|建行亚洲积分]](../reward-programs/ccb-asia-points.md) |
| 来源等级 | [[glossary:source-level|C · 待复核]](../glossary/source-level.md) |
| 词条状态 | Stub / 待迁入 Payload |
| 银联双币 | 否 |
| 计算器插件 | `ccbAsiaPlatinum` |

## 概述

**建行亚洲白金信用卡** 是 [[banks:ccb-asia|建行亚洲]](../banks/ccb-asia.md) 在香港市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：[[banks:ccb-asia|建行亚洲]](../banks/ccb-asia.md)
- 积分体系：[[reward-programs:ccb-asia-points|建行亚洲积分]](../reward-programs/ccb-asia-points.md)
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 [[reward-programs:ccb-asia-points|建行亚洲积分]](../reward-programs/ccb-asia-points.md)。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。


## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `ccbAsiaPlatinum` |
| 兑换计算器 | 否 | `—` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

尚未挂接核验来源。

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

- [[cards:ccb-asia-aia-visa-credit-card|建行亚洲 AIA Visa 信用卡]](../cards/ccb-asia-aia-visa-credit-card.md)
- [[cards:ccb-asia-eye-credit-card|建行亚洲 eye 信用卡]](../cards/ccb-asia-eye-credit-card.md)
- [[cards:ccb-asia-gba-virtual-unionpay-credit-card|建行亚洲大湾区虚拟银联信用卡]](../cards/ccb-asia-gba-virtual-unionpay-credit-card.md)
- [[cards:ccb-asia-industry-unionpay-dual-currency-credit-card|建行亚洲建造业银联双币信用卡]](../cards/ccb-asia-industry-unionpay-dual-currency-credit-card.md)
- [[cards:ccb-asia-octopus-motorist-unionpay-diamond-credit-card|八达通车生活银联钻石信用卡]](../cards/ccb-asia-octopus-motorist-unionpay-diamond-credit-card.md)
- [[cards:ccb-asia-octopus-unionpay-dual-currency-credit-card|建行亚洲八达通银联双币信用卡]](../cards/ccb-asia-octopus-unionpay-dual-currency-credit-card.md)
- [[cards:ccb-asia-pui-ching-unionpay-dual-currency-credit-card|建行亚洲培正银联双币信用卡]](../cards/ccb-asia-pui-ching-unionpay-dual-currency-credit-card.md)
- [[cards:ccb-asia-travo-mastercard|建行亚洲 TRAVO Mastercard]](../cards/ccb-asia-travo-mastercard.md)

## 迁移备注

- Payload collection：`cards`
- slug：`ccb-asia-platinum-credit-card`
- 关系字段：`bank` → `ccb-asia`；`rewardProgram` → `ccb-asia-points`
- `_status` 建议先以 `draft` 导入，核验后再 publish

[[Category:信用卡]]
[[Category:香港信用卡]]
[[Category:建行亚洲]]
[[Category:CCB Asia]]
[[Category:Platinum]]
