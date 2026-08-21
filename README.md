# fluxa.wiki.document

[Fluxa WikiCard](https://fluxa.wiki) 的 **词条暂存仓库**。

主仓库 `payload-website-starter` 还在开发，卡片摘要和正文按设计存在 Postgres 里，而不是 GitHub。这个仓库用 Markdown + Wiki 语法先把词条、银行、积分体系和来源立起来，等主站就绪后再迁回 Payload collections。

## 从这里读

- 百科首页：[wiki/Home.md](wiki/Home.md)
- 信用卡：[wiki/cards/_index.md](wiki/cards/_index.md)
- 银行：[wiki/banks/_index.md](wiki/banks/_index.md)
- 积分体系：[wiki/reward-programs/_index.md](wiki/reward-programs/_index.md)
- 语法与迁移：[wiki/meta/syntax.md](wiki/meta/syntax.md)

姊妹产品：[Fluxa Map](https://github.com/WilliamWang1721/Fluxa-Map)。

## 目录

```
wiki/
  Home.md                 百科首页
  _Sidebar.md             Wiki 侧栏
  cards/                  信用卡词条（Payload: cards）
  banks/                  银行词条
  reward-programs/        积分体系
  sources/                核验来源
  pages/                  指南与政策
  posts/                  说明文章
  glossary/               术语
  categories/             分类页
  meta/                   语法、字段对照、迁移
scripts/generate_wiki.py  从主仓库卡册 TypeScript 生成 stub
```

## 重新生成 stub

需要一份 `payload-website-starter` 检出，默认路径 `/tmp/payload-website-starter`：

```sh
python3 scripts/generate_wiki.py
```

脚本不会连接数据库，也**不会**覆盖 `wiki/pages`、`wiki/posts`、`wiki/glossary`、`wiki/meta` 这些手写文档。

## 声明

内容仅供参考，不构成财务建议。回赠数字默认来源等级为 C（待复核）。
