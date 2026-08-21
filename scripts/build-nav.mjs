#!/usr/bin/env node
/**
 * Scan wiki/ and emit docsify sidebar with folder hierarchy.
 * Does NOT touch entry bodies or run generate_wiki.py.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const WIKI = path.join(ROOT, 'wiki');
const OUT = path.join(WIKI, '_Sidebar.generated.md');

const SKIP_DIRS = new Set(['_templates']);
const SKIP_FILES = new Set([
  '_Footer.md',
  '_Sidebar.md',
  '_Sidebar.generated.md',
  '_generated-stats.md',
]);

const FOLDER_LABELS = {
  banks: '银行',
  cards: '信用卡',
  categories: '分类',
  glossary: '术语',
  meta: '元文档',
  pages: '页面',
  posts: '文章',
  products: '产品',
  'reward-programs': '积分体系',
  sources: '来源',
};

function parseFrontmatter(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) {
    return { title: null, kind: null, parent: null, bank: null, content };
  }
  const fm = match[1];
  const titleMatch = fm.match(/^title:\s*(['"]?)(.+?)\1\s*$/m);
  const kindMatch = fm.match(/^kind:\s*(\S+)\s*$/m);
  const parentMatch = fm.match(/^parent:\s*(\S+)\s*$/m);
  const bankMatch = fm.match(/^bank:\s*(\S+)\s*$/m);
  return {
    title: titleMatch ? titleMatch[2] : null,
    kind: kindMatch ? kindMatch[1] : null,
    parent: parentMatch ? parentMatch[1] : null,
    bank: bankMatch ? bankMatch[1] : null,
    content,
  };
}

function pageLabel(filePath, fallback) {
  try {
    const { title } = parseFrontmatter(filePath);
    return title || fallback;
  } catch {
    return fallback;
  }
}

function toDocsifyPath(relativePath) {
  return '/wiki/' + relativePath.split(path.sep).join('/');
}

function folderHeaderLine(dir, prefix, folderName) {
  const rel = prefix + '_index.md';
  const indexPath = path.join(dir, '_index.md');
  const label = FOLDER_LABELS[folderName] || pageLabel(indexPath, folderName);
  return '- [' + label + '](' + toDocsifyPath(rel) + ')';
}

function ensureTopLevelIndex(folderName) {
  const dir = path.join(WIKI, folderName);
  const indexPath = path.join(dir, '_index.md');
  if (fs.existsSync(indexPath)) {
    return;
  }
  const label = FOLDER_LABELS[folderName] || folderName;
  const content = '---\ntitle: \'' + label + '\'\n---\n\n# ' + label + '\n';
  fs.writeFileSync(indexPath, content, 'utf8');
  console.log('Created ' + path.relative(ROOT, indexPath));
}

function sortByLabel(a, b) {
  return a.label.localeCompare(b.label, 'zh-Hans');
}

function sidebarLink(label, rel, indent = 0) {
  const pad = '  '.repeat(indent);
  return pad + '- [' + label + '](' + toDocsifyPath(rel) + ')';
}

function listHierarchicalMarkdownFiles(dir, prefix, childKind) {
  const entries = fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) =>
    a.name.localeCompare(b.name, 'zh-Hans')
  );

  const groups = [];
  const childrenByParent = new Map();
  const independent = [];

  for (const entry of entries) {
    if (!entry.isFile() || !entry.name.endsWith('.md')) {
      continue;
    }
    if (entry.name === '_index.md' || SKIP_FILES.has(entry.name)) {
      continue;
    }

    const filePath = path.join(dir, entry.name);
    const { title, kind, parent } = parseFrontmatter(filePath);
    const slug = entry.name.replace(/\.md$/, '');
    const item = {
      slug,
      label: title || slug,
      rel: prefix + entry.name,
    };

    if (kind === 'group') {
      groups.push(item);
    } else if (kind === childKind && parent) {
      if (!childrenByParent.has(parent)) {
        childrenByParent.set(parent, []);
      }
      childrenByParent.get(parent).push(item);
    } else {
      independent.push(item);
    }
  }

  for (const children of childrenByParent.values()) {
    children.sort(sortByLabel);
  }

  const lines = [];
  const topLevel = [...groups, ...independent].sort(sortByLabel);

  for (const item of topLevel) {
    lines.push(sidebarLink(item.label, item.rel));
    const children = childrenByParent.get(item.slug);
    if (children) {
      for (const child of children) {
        lines.push(sidebarLink(child.label, child.rel, 1));
      }
    }
  }

  return lines;
}

function loadBankRegistry() {
  const banksDir = path.join(WIKI, 'banks');
  const registry = new Map();

  for (const entry of fs.readdirSync(banksDir, { withFileTypes: true })) {
    if (!entry.isFile() || !entry.name.endsWith('.md') || entry.name === '_index.md') {
      continue;
    }
    const slug = entry.name.replace(/\.md$/, '');
    const filePath = path.join(banksDir, entry.name);
    const { title, kind, parent } = parseFrontmatter(filePath);
    registry.set(slug, {
      slug,
      label: title || slug,
      kind: kind || null,
      parent: parent || null,
    });
  }

  return registry;
}

function listCardMarkdownFiles(dir, prefix) {
  const bankRegistry = loadBankRegistry();
  const cardsByBank = new Map();
  const unlinked = [];

  const entries = fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) =>
    a.name.localeCompare(b.name, 'zh-Hans')
  );

  for (const entry of entries) {
    if (!entry.isFile() || !entry.name.endsWith('.md')) {
      continue;
    }
    if (entry.name === '_index.md' || SKIP_FILES.has(entry.name)) {
      continue;
    }

    const filePath = path.join(dir, entry.name);
    const { title, bank } = parseFrontmatter(filePath);
    const slug = entry.name.replace(/\.md$/, '');
    const card = {
      slug,
      label: title || slug,
      rel: prefix + entry.name,
    };

    if (!bank || !bankRegistry.has(bank)) {
      unlinked.push(card);
      continue;
    }

    if (!cardsByBank.has(bank)) {
      cardsByBank.set(bank, []);
    }
    cardsByBank.get(bank).push(card);
  }

  for (const cards of cardsByBank.values()) {
    cards.sort(sortByLabel);
  }
  unlinked.sort(sortByLabel);

  const lines = [];

  const independentBanks = [...bankRegistry.values()]
    .filter((bank) => bank.kind !== 'group' && bank.kind !== 'subsidiary')
    .filter((bank) => cardsByBank.has(bank.slug))
    .sort(sortByLabel);

  for (const bank of independentBanks) {
    lines.push(sidebarLink(bank.label, 'banks/' + bank.slug + '.md'));
    for (const card of cardsByBank.get(bank.slug)) {
      lines.push(sidebarLink(card.label, card.rel, 1));
    }
  }

  const groups = [...bankRegistry.values()]
    .filter((bank) => bank.kind === 'group')
    .sort(sortByLabel);

  for (const group of groups) {
    const subsidiaries = [...bankRegistry.values()]
      .filter((bank) => bank.parent === group.slug && cardsByBank.has(bank.slug))
      .sort(sortByLabel);

    if (subsidiaries.length === 0) {
      continue;
    }

    lines.push(sidebarLink(group.label, 'banks/' + group.slug + '.md'));
    for (const subsidiary of subsidiaries) {
      lines.push(sidebarLink(subsidiary.label, 'banks/' + subsidiary.slug + '.md', 1));
      for (const card of cardsByBank.get(subsidiary.slug)) {
        lines.push(sidebarLink(card.label, card.rel, 2));
      }
    }
  }

  if (unlinked.length > 0) {
    lines.push('- 未挂银行');
    for (const card of unlinked) {
      lines.push(sidebarLink(card.label, card.rel, 1));
    }
  }

  return lines;
}

function listMarkdownFiles(dir, prefix = '') {
  if (prefix === 'reward-programs' + path.sep) {
    return listHierarchicalMarkdownFiles(dir, prefix, 'regional');
  }
  if (prefix === 'banks' + path.sep) {
    return listHierarchicalMarkdownFiles(dir, prefix, 'subsidiary');
  }
  if (prefix === 'cards' + path.sep) {
    return listCardMarkdownFiles(dir, prefix);
  }

  const entries = fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) =>
    a.name.localeCompare(b.name, 'zh-Hans')
  );

  const lines = [];

  for (const entry of entries) {
    if (entry.isDirectory()) {
      if (SKIP_DIRS.has(entry.name) || entry.name.startsWith('.')) {
        continue;
      }
      const subDir = path.join(dir, entry.name);
      const subPrefix = prefix + entry.name + path.sep;
      lines.push(folderHeaderLine(subDir, subPrefix, entry.name));
      for (const subLine of listMarkdownFiles(subDir, subPrefix)) {
        lines.push('  ' + subLine);
      }
      continue;
    }

    if (!entry.isFile() || !entry.name.endsWith('.md')) {
      continue;
    }
    if (entry.name === '_index.md' || SKIP_FILES.has(entry.name)) {
      continue;
    }

    const rel = prefix + entry.name;
    const fallback = entry.name.replace(/\.md$/, '');
    const label = pageLabel(path.join(dir, entry.name), fallback);
    lines.push('- [' + label + '](' + toDocsifyPath(rel) + ')');
  }

  return lines;
}

function buildSidebar() {
  const homeLabel = pageLabel(path.join(WIKI, 'Home.md'), '首页');
  const lines = [
    '<!-- Auto-generated by scripts/build-nav.mjs; do not edit -->',
    '',
    '- [' + homeLabel + '](/wiki/Home.md)',
    '',
  ];

  const topEntries = fs.readdirSync(WIKI, { withFileTypes: true }).sort((a, b) =>
    a.name.localeCompare(b.name, 'zh-Hans')
  );

  for (const entry of topEntries) {
    if (!entry.isDirectory()) {
      continue;
    }
    if (SKIP_DIRS.has(entry.name) || entry.name.startsWith('.')) {
      continue;
    }

    ensureTopLevelIndex(entry.name);
    lines.push(folderHeaderLine(path.join(WIKI, entry.name), entry.name + path.sep, entry.name));
    for (const subLine of listMarkdownFiles(path.join(WIKI, entry.name), entry.name + path.sep)) {
      lines.push('  ' + subLine);
    }
    lines.push('');
  }

  return lines.join('\n').trimEnd() + '\n';
}

const sidebar = buildSidebar();
fs.writeFileSync(OUT, sidebar, 'utf8');
console.log('Wrote ' + path.relative(ROOT, OUT));
