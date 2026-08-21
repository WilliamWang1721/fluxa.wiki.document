---
collection: pages
title: '词条编写约定'
slug: how-to-contribute
status: published
---

# 词条编写约定

完整、按类型拆开的规则（含依赖顺序、回写清单、提交检查）在：

**[[meta:new-entry-rules|词条新建规则]](../meta/new-entry-rules.md)**

空白稿：[`wiki/_templates/`](../_templates/)。仓库级说明见根目录 [README.md](../../README.md)。

## 先改 stub 还是新建

- `wiki/cards/{slug}.md` **已经存在**：改这一篇。不要另开同名或近名词条，也不要改 slug。
- 确认搜索后没有：按新建规则走，信用卡必须先有银行和积分体系。

## 文风（短则）

- 先写事实，再写玩法。活动数字必须带来源。
- 不要把未确认的限时倍数写进默认回赠口径。
- `title` 用对外官方名，`shortName` 用卡册简称。
- 不构成申请建议。费用、FTF、迎新以官方条款为准。
- 新建信用卡默认 `sourceLevel: C`、`_status: draft`。

## 链接

同时写 Wiki 链和 Markdown 相对路径，GitHub 预览和以后导入都能用：

```md
[[banks:hsbc-hong-kong|汇丰香港]](../banks/hsbc-hong-kong.md)
```

语法见 [[meta:syntax|Wiki 语法]](../meta/syntax.md)。

## 不要做的事

- 不要把银行名单、卡片正文写进主仓库前端源码。
- 不要在手写词条之后运行 `scripts/generate_wiki.py`（会清空已生成目录）。
- 主站就绪后，不要把本仓当成唯一真相。导入规则见 [[meta:migration|迁移说明]](../meta/migration.md)。

[[Category:指南]]
