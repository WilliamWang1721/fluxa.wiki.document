---
collection: pages
title: 'Fluxa WikiCard'
slug: home
status: published
---

# Fluxa WikiCard

**卡片百科。** 用百科的方式整理卡片、银行、礼遇与地图场景。

本仓库是 [fluxa.wiki](https://fluxa.wiki) 的 **Git 暂存 Wiki**：主仓库 `payload-website-starter` 尚未完成，词条正文目前写在 Payload / Postgres 里。这里先用 Markdown + Wiki 语法把词条骨架、关系和来源立起来，等主站代码稳定后再迁回数据库。

## 从一个词条开始

- 信用卡：[[cards:_index|信用卡词条]](cards/_index.md)
- 银行：[[banks:_index|银行词条]](banks/_index.md)
- 积分体系：[[reward-programs:_index|礼遇 / 积分体系]](reward-programs/_index.md)
- 核验来源：[[sources:_index|来源]](sources/_index.md)
- 分类：[[categories:信用卡|分类：信用卡]](categories/信用卡.md)

## 站点功能对照

| 主站路径 | 本 Wiki |
| --- | --- |
| `/cards` | [[cards:_index\|信用卡]](cards/_index.md) |
| `/banks` | [[banks:_index\|银行]](banks/_index.md) |
| `/rewards` | [[reward-programs:_index\|积分体系]](reward-programs/_index.md) |
| `/compare` | 对比参数仍在数据库，本仓只保留词条关系 |
| `/rebate-calculator` | 卡片 frontmatter 的 `rebateCalculator` |
| `/conversion-calculator` | 卡片 frontmatter 的 `conversionCalculator` |
| `/privacy` | [[pages:privacy\|隐私政策]](pages/privacy.md) |
| `/terms` | [[pages:terms\|使用条款]](pages/terms.md) |

姊妹产品：[Fluxa Map](https://payments-maps.asia)（支付场景地图）。

## 编辑入口

新增或完善词条，先读这一份：

- [[meta:new-entry-rules|词条新建规则]](meta/new-entry-rules.md)（按类型：信用卡 / 银行 / 积分 / 来源）
- [空白模板](_templates/README.md)
- 仓库 README：[项目根目录 README](https://github.com/WilliamWang1721/fluxa.wiki.document/blob/main/README.md)

其它：

- [[pages:how-to-contribute|词条编写约定（短版）]](pages/how-to-contribute.md)
- [[meta:syntax|Wiki 语法]](meta/syntax.md)
- [[meta:payload-mapping|Payload 字段对照]](meta/payload-mapping.md)
- [[meta:migration|迁回主仓库]](meta/migration.md)
- [[glossary:source-level|来源等级]](glossary/source-level.md)

## 声明

内容仅供参考，不构成申请、投资或财务建议。实际权益、费用和活动以发卡机构最新官方条款为准。

[[Category:索引]]
