---
collection: posts
title: '如何阅读一张信用卡词条'
slug: how-to-read-a-card-entry
status: published
---

# 如何阅读一张信用卡词条

以 [[cards:hsbc-red-credit-card|汇丰 Red 信用卡]](../cards/hsbc-red-credit-card.md) 为例。

1. **标题与简称**：`title` 是官方/对外名，`shortName` 是卡册和对比表用的短名。
2. **信息框表格**：银行、市场、积分体系、来源等级。主站会把 `showInCardInfobox` 的对比参数显示在页面顶部。
3. **概述**：对应 Payload `summary`。若仍是计算器一句话口径，等级就是 C。
4. **回赠口径表**：来自主仓库 TypeScript，不是数据库正文。迁移时不要把它当成已核验事实覆盖 Admin 里的内容。
5. **计算器接入**：`calculatorId` / `ruleId` 必须和主仓库插件选项一致。
6. **来源**：能点开官方条款再相信数字。
7. **相关词条**：同银行其它卡，迁入后写入 `relatedCards`。

如果你发现过期活动，主站请提交 Change Request；在本仓请开 Issue 或改 Markdown 并保持 `sourceLevel: C` 直到有人核验。

[[Category:指南]]
