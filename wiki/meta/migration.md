---
collection: pages
title: '迁回主仓库'
slug: migration
status: published
---

# 迁回主仓库

当 `payload-website-starter` 的 Wiki 读写路径稳定后，把本仓库当作内容源，而不是长期双写。

## 现在为什么单独建仓

- 主仓库代码还在改 collections、关系和计算器接入
- 词条正文按设计写在数据库，不进 Git
- 需要先有一份可 diff、可审阅的词条清单和交叉链接

## 建议迁移步骤

1. 在 Payload Admin 确认 `banks` / `reward-programs` / `cards` / `sources` 字段与 [[meta:payload-mapping|对照表]](payload-mapping.md) 一致。
2. 用 frontmatter 的 `slug` 做幂等键：已存在则更新关系，不存在则创建 `draft`。
3. 把 Markdown 正文（去掉 infobox 表格与 Category 行）转成 Lexical `content`；把 `>` 首段写入 `summary`。
4. 把 `[[collection:slug|title]]` 转成 Payload relationship 或内部链接节点。
5. 来源等级仍为 `C` 的词条不要直接 publish；走 Change Request 或编辑核验。
6. 数据库已有、本仓没有的摘要/对比参数值：**以数据库为准**，不要用 stub 覆盖。
7. 迁移完成后，本仓改为只读镜像或改为从 Payload 导出。

## 不要覆盖的数据

主站数据库里可能已经有编辑写过的 `summary`、`content`、`card-parameter-values`、`lastVerifiedAt`。导入脚本必须：

- 默认 `--dry-run`
- 对已有 `content` 非空的文档跳过正文
- 只补空的 `bank` / `rewardProgram` / `sources` 关系

## 生成脚本

```sh
python3 scripts/generate_wiki.py
```

脚本读取本地 `/tmp/payload-website-starter`（或之后改成相对路径）里的卡册 TypeScript，**不会**连接 Postgres。

[[Category:元文档]]
