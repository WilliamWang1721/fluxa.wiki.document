#!/usr/bin/env node
/**
 * Prepare static artifact for GitHub Pages (docsify + wiki/ source).
 */

import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SITE = path.join(ROOT, '_site');

function copyRecursive(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

const nav = spawnSync(process.execPath, ['scripts/build-nav.mjs'], {
  cwd: ROOT,
  stdio: 'inherit',
});
if (nav.status !== 0) {
  process.exit(nav.status ?? 1);
}

fs.rmSync(SITE, { recursive: true, force: true });
fs.mkdirSync(SITE);

for (const file of ['index.html', '.nojekyll']) {
  fs.copyFileSync(path.join(ROOT, file), path.join(SITE, file));
}

copyRecursive(path.join(ROOT, 'wiki'), path.join(SITE, 'wiki'));

console.log('Site artifact ready at _site/');
