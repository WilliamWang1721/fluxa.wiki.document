---
collection: pages
title: 'Wiki 语法'
slug: syntax
status: published
---

# Wiki 语法

本仓库同时使用 **GitHub Flavored Markdown** 和 **Wiki 链语法**。GitHub 网页能渲染 Markdown 链接；`[[collection:slug|标题]]` 是给后续迁入 Payload / 百科引擎用的稳定标识。

## 内部链接

```md
[[banks:hsbc-hong-kong|汇丰香港]](../banks/hsbc-hong-kong.md)
```

| 部分 | 含义 |
| --- | --- |
| `banks` | Payload collection / 本仓目录名 |
| `hsbc-hong-kong` | `slug` |
| `汇丰香港` | 显示标题 |
| `(../banks/hsbc-hong-kong.md)` | GitHub 可点击的相对路径 |

简写（迁入百科引擎后即可解析，GitHub 上不会自动跳转）：

```md
[[汇丰香港]]
[[Category:香港信用卡]]
```

## 信息框

词条开头的 `{{Infobox card}}` / `{{Infobox bank}}` / `{{Infobox reward program}}` 是占位宏。真正字段在紧随其后的 Markdown 表格，以及 YAML frontmatter。迁入主站时：

- 表格里「显示在卡片信息框」的行 → Payload `compare-parameters.showInCardInfobox`
- frontmatter → collection 字段

## 分类

每个词条文末使用 MediaWiki 风格分类：

```md
[[Category:信用卡]]
[[Category:香港信用卡]]
[[Category:汇丰香港]]
```

分类页在 `wiki/categories/`。

## Frontmatter

卡片词条顶部 YAML 对齐 `payload-website-starter` 的 Cards collection，详见 [[meta:payload-mapping|字段对照]](payload-mapping.md)。

## 不要写进词条的内容

主仓库明确约定：

- 卡片摘要、正文 → 数据库，不写进前端源码
- 银行名单 → `banks` 关系，不靠标题模糊匹配
- 计算器数字规则 → 仍可留在主仓库 TypeScript；本 Wiki 只记录口径说明和来源

[[Category:元文档]]
