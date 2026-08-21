---
collection: posts
title: '计算器规则和百科词条为什么要分开'
slug: calculator-vs-wiki
status: published
---

# 计算器规则和百科词条为什么要分开

主仓库把两件事拆开：

| | 计算器 | 百科词条 |
| --- | --- | --- |
| 存放 | TypeScript（`rebateRules` 等） | Payload 数据库 / 本 Wiki |
| 目的 | 可运行的估算 | 可阅读、可引用、可审核的事实 |
| 失败时 | 健康检查仍可能通过，但估算不准 | 详情页缺摘要、缺银行关系 |
| 谁改 | 开发者 | 编辑 / 读者更改申请 |

因此：

- **不要**把整份条款粘进计算器代码
- **不要**把银行列表写死在 React 页面里
- **可以**在词条里写「该卡已接入返利计算器，插件 `hsbcRed`」
- 词条迁入数据库后，计算器仍然读 `rebateCalculator.calculatorId`

相关代码：`src/collections/Cards.ts`、`src/lib/wikiQueries.ts`、`src/app/(frontend)/cards/[slug]/page.tsx`。

[[Category:指南]]
