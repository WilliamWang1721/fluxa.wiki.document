# fluxa.wiki.document

[Fluxa WikiCard](https://fluxa.wiki) 的 **词条暂存仓库**。

主站 `payload-website-starter` 还在开发，卡片摘要和正文按设计存在数据库里。这个仓库用 Markdown + Wiki 语法，把词条、银行、积分体系和来源先写在 Git 里，等主站就绪再迁回 Payload。

姊妹产品：[Fluxa Map](https://github.com/WilliamWang1721/Fluxa-Map)。

---

## 你接下来最可能做的两件事

| 场景 | 怎么做 |
| --- | --- |
| **完善已有词条**（最常见：`wiki/cards/` 里已有 stub） | 打开对应 `{slug}.md`，按规则补摘要、来源和回赠口径。**不要改 slug 和文件名。** |
| **新建还不存在的词条** | 先读 [词条新建规则](wiki/meta/new-entry-rules.md)，再复制 [wiki/_templates/](wiki/_templates/) 里对应模板。 |

完整规则（按信用卡 / 银行 / 积分体系 / 来源 / 指南拆开，含回写清单）：

**[wiki/meta/new-entry-rules.md](wiki/meta/new-entry-rules.md)**

五分钟上手：

1. 在本仓搜索中文名或英文产品名，确认还没有这篇（或确认要改的就是那篇 stub）。
2. 信用卡依赖银行 → 积分体系 → 来源，缺哪个先建哪个。
3. 复制模板，文件名必须等于 YAML 里的 `slug`。
4. 链接写成 `[[banks:hsbc-hong-kong|汇丰香港]](../banks/hsbc-hong-kong.md)` 这种「Wiki 链 + GitHub 路径」。
5. 新卡要回写银行页、积分体系页、`wiki/cards/_index.md`、来源页和分类页。

---

## 词条长什么样

每一篇都是「YAML 头 + Markdown 正文」：

```yaml
---
collection: cards          # 对应将来 Payload 的 collection
title: '汇丰 Red 信用卡'
slug: hsbc-red-credit-card # 必须等于文件名
bank: hsbc-hong-kong       # 只写 slug，不写中文
sourceLevel: C             # 新建默认待复核
_status: draft
---
```

- YAML：给以后导入数据库用，关系字段全是 slug。
- 正文：给人读；信息框表格要和 YAML 一致。
- `[[collection:slug|标题]](相对路径)`：左边给百科引擎，括号给 GitHub 预览。

对照一篇已有的卡：[wiki/cards/hsbc-red-credit-card.md](wiki/cards/hsbc-red-credit-card.md)

---

## 目录（按词条类型）

```
wiki/
  Home.md                 百科首页（阅读入口）
  _Sidebar.md             侧栏
  _templates/             新建时复制的空白稿
  cards/                  信用卡          → Payload cards
  banks/                  银行（含集团 / 子行）→ banks
  reward-programs/        积分 / 礼遇     → reward-programs
  sources/                官方条款与来源  → sources
  pages/                  指南与政策      → pages
  posts/                  说明文章        → posts
  glossary/               术语
  categories/             分类页
  meta/
    new-entry-rules.md    ★ 新建 / 编辑规则（先读这个）
    syntax.md             Wiki 语法
    payload-mapping.md    字段怎样对上 Payload
    migration.md          以后怎么迁回主仓库
scripts/generate_wiki.py  一次性从主仓库卡册生成 stub（勿在手写后重跑）
```

浏览：

- 百科首页：[wiki/Home.md](wiki/Home.md)
- 信用卡索引：[wiki/cards/_index.md](wiki/cards/_index.md)
- 银行：[wiki/banks/_index.md](wiki/banks/_index.md)
- 积分体系：[wiki/reward-programs/_index.md](wiki/reward-programs/_index.md)
- 来源：[wiki/sources/_index.md](wiki/sources/_index.md)

---

## 编辑时记住的几条

1. **一个 slug 一篇文件**，文件名 `{slug}.md`。
2. **关系只写 slug**：`bank: hang-seng`，不要写 `恒生银行`。
3. **新建默认** `sourceLevel: C`、`_status: draft`。没有官方 URL 就不要写具体费率。
4. **限时活动**可以写在正文并带来源，但不要写进「默认回赠口径」表。
5. **不要运行** `python3 scripts/generate_wiki.py` 来「刷新列表」。它会清空 `cards` / `banks` / `reward-programs` / `sources` / `categories` 再生成，手写内容会丢。那只是当初从主仓库卡册做骨架用的。
6. 主站数据库里如果已经有摘要或正文，迁入时以数据库为准，见 [migration.md](wiki/meta/migration.md)。

来源等级：`S` 官方 · `A` 强来源 · `B` 交叉核验 · `C` 待复核 · `D` 低置信。说明在 [glossary/source-level.md](wiki/glossary/source-level.md)。

---

## 相关文档

| 文档 | 用途 |
| --- | --- |
| [词条新建规则](wiki/meta/new-entry-rules.md) | 各类型怎么建、回写哪些索引 |
| [模板目录](wiki/_templates/) | 复制空白稿 |
| [Wiki 语法](wiki/meta/syntax.md) | 链接、信息框、分类 |
| [字段对照](wiki/meta/payload-mapping.md) | YAML 怎样对上 Payload |
| [编写约定（短版）](wiki/pages/how-to-contribute.md) | 文风与默认等级 |
| [迁回主仓库](wiki/meta/migration.md) | 主站就绪后怎么导入 |

---

## 声明

内容仅供参考，不构成申请、投资或财务建议。实际权益、费用和活动以发卡机构最新官方条款为准。
