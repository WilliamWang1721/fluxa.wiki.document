---
collection: pages
title: '词条编写约定'
slug: how-to-contribute
status: published
---

# 词条编写约定

## 新增信用卡

1. 复制 `wiki/cards/` 下同银行的一篇作为模板。
2. `slug` 使用小写短横线，与主站 URL 一致，例如 `hsbc-red-credit-card`。
3. `bank`、`rewardProgram` 必须指向已存在词条。
4. 摘要写在引用块 `>` 里，对应 Payload `summary`。
5. 官方条款放进 `wiki/sources/`，并在 frontmatter `sources` 列出 slug。
6. 来源等级默认 `C`；只有对照官方条款核验后才升到 `A` 或 `S`。
7. 文末加上 `[[Category:...]]`。

## 文风

- 先写事实，再写玩法。活动数字必须带来源。
- 不要把未确认的限时倍数写进默认回赠口径。
- 中英官方名都保留：`title` 用对外显示名，`shortName` 用卡册简称。
- 不构成申请建议。费用、外币手续费、迎新以官方条款为准。

## Wiki 语法

见 [[meta:syntax|Wiki 语法]](../meta/syntax.md)。链接同时写 `[[collection:slug|标题]]` 和 Markdown 相对路径，这样 GitHub 预览和日后导入都能用。

## 主站就绪之后

不要在本仓继续作为唯一真相。把变更做成可导入的 Markdown，或直接在 Payload Admin 编辑，再按 [[meta:migration|迁移说明]](../meta/migration.md) 处理。

[[Category:指南]]
