---
collection: pages
title: 'Verified wiki queue'
slug: verified-wiki-queue
status: published
---

# Verified wiki queue

主站首页把「Verified wiki queue」作为已核验词条队列。本仓对应规则：

| 来源等级 | 是否进入核验队列 |
| --- | --- |
| S 官方来源 | 是 |
| A 强来源 | 是 |
| B 已交叉核验 | 是 |
| C 待复核 | 否（默认，当前几乎全部 stub） |
| D 低置信 | 否 |

升级等级前必须：

1. 挂上 `sourceType: official` 或 `terms` 的来源
2. 填写 `lastVerifiedAt`
3. 确认 `bank` 关系不是靠标题猜的

相关：[[glossary:source-level|来源等级]](../glossary/source-level.md)

[[Category:指南]]
