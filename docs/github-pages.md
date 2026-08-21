# GitHub Pages 部署说明

本仓库用 [Docsify](https://docsify.js.org/) 在浏览器端渲染 `wiki/` 里的 Markdown，不复制词条正文。推送 `main` 后由 GitHub Actions 自动构建并发布。

## 预计站点地址

https://williamwang1721.github.io/fluxa.wiki.document/

（首次启用 Pages 后可能需要等待 1–3 分钟生效。）

## 仓库管理员需要做的设置（一次性）

Pages Source 已设为 **GitHub Actions**（2026-08-21）。若部署仍失败，再检 **Settings → Actions → General** 的 Workflow permissions 是否为 Read and write。

若 Actions 部署失败并提示缺少 Pages 权限，请在 GitHub 仓库里完成以下步骤：

1. 打开 **Settings → Pages**。
2. **Build and deployment → Source** 选择 **GitHub Actions**（不要选 “Deploy from a branch”）〃
3. 打开 **Settings → Actions → General**：
   - **Workflow permissions** 选 **Read and write permissions**（或至少允许 `pages: write` 与 `id-token: write`）。
   - 若组织策略限制了 Actions，需组织管理员放行 `actions/deploy-pages` 与 `actions/upload-pages-artifact`。
4. 回到 **Actions**，手动运行一次 **Deploy GitHub Pages**（`workflow_dispatch`），或向 `main` 推送任意 commit 触发。

### 常见卡点

| 现象 | 处理 |
| --- | --- |
| Workflow 报 `Resource not accessible by integration` | Settings → Actions → General 里把 Workflow permissions 改为 Read and write |
| Pages 环境不存在 / 无法创建 `github-pages` environment | 先在 Settings → Pages 里选 GitHub Actions 作为 Source |
| 站点 404 | 确认最新 workflow 已成功；URL 需带仓库名 `/fluxa.wiki.document/` |
| 侧栏为空 | 检查 `wiki/_Sidebar.generated.md` 是否由 CI 生成（本地可运行 `node scripts/build-nav.mjs`） |

## 内容如何随 commit 更新

1. 编辑 `wiki/` 下任意 `.md` 并 push 到 `main`。
2. **Deploy GitHub Pages** workflow 运行 `scripts/build-site.mjs`：
   - `scripts/build-nav.mjs` 扫描 `wiki/` 目录树，生成 `wiki/_Sidebar.generated.md`（按文件夹折叠导航；有 `_index.md` 的目录用其 `title` 作索引入口）。
   - 将 `index.html`、`.nojekyll` 与整个 `wiki/` 复制到 `_site/`。
3. `actions/deploy-pages` 发布 `_site/`。无需手动发版。

**不要运行** `scripts/generate_wiki.py`——它会清空手写词条。

## 本地预览

```bash
node scripts/build-site.mjs
npx --yes serve _site -p 3000
```

浏览器打开 `http://localhost:3000/#/wiki/Home`（Docsify 使用 hash 路由）。

## 导航规则

- 侧栏顶层：**Home**，以及 `wiki/` 下各内容目录（`banks`、`cards`、`glossary`、`sources`、`meta`、`categories`、`posts`、`pages`、`reward-programs` 等）。
- 每个目录内：若有 `_index.md`，排在最前作为目录封面；其余 `.md` 按文件名排序，显示 YAML 里的 `title`。
- `_templates/`、`_Footer.md`、`_Sidebar.md` 等维护文件不出现在导航中。
- 正文中的 YAML frontmatter 与 `{{Infobox …}}` 占位符在展示时隐藏；`[[collection:slug|标题]](相对路径)` 转为可点击 Markdown 链接。
