---
collection: pages
title: '关于 Fluxa WikiCard'
slug: about
status: published
---

# 关于 Fluxa WikiCard

Fluxa WikiCard 是 Fluxa Map 的姊妹产品，用来做**信用卡知识百科**：卡片、银行、积分体系、核验来源，以及读者提交的更改申请。

主站：[https://fluxa.wiki](https://fluxa.wiki)

技术栈（主仓库）：Payload CMS + Next.js + Postgres。本仓库只存 Markdown 词条，方便在主站代码未完成时先把百科结构搭起来。

## 产品原则

1. **词条进数据库**：卡片摘要和正文不写进前端源码。
2. **关系进 collection**：卡片必须挂到银行词条，不靠标题模糊匹配。
3. **来源可核验**：事实尽量挂 `sources`，并标注来源等级。
4. **计算器分开**：返利 / 兑换规则可以留在代码里，词条页只解释口径和限制。
5. **读者可纠错**：主站有 Change Request；本仓用 Git 和 Issue 暂代。

## 系列产品

- WikiCard：卡片百科（本仓 / fluxa.wiki）
- [Fluxa Map](https://payments-maps.asia)：支付方式与场景地图

联系：[hello@fluxa.app](mailto:hello@fluxa.app)

[[Category:指南]]
