/**
 * MyST plugin: {github-issues}
 *
 * Fetches open issues from a GitHub repo at build time and renders them as a
 * linked list. Results are cached in _build/cache/github-issues.json so
 * repeated builds (and local dev) don't hammer the API.
 *
 * Usage in a .md page:
 *
 *   :::{github-issues}
 *   :repo: nucleus-eng/nucleus-docs
 *   :label: roadmap
 *   :::
 *
 * Options:
 *   repo   GitHub repo in "org/name" form. Default: nucleus-eng/nucleus-docs
 *   label  Filter to issues that have this label. Omit to show all open issues.
 *
 * Auth: reads GH_TOKEN or GITHUB_TOKEN from env. Without a token the GitHub
 * API allows 60 unauthenticated requests/hour — enough for local builds.
 * In GitHub Actions, pass GITHUB_TOKEN via the workflow env block.
 */

import { execSync } from 'child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';

const CACHE_FILE = join('_build', 'cache', 'github-issues.json');
const DEFAULT_REPO = 'nucleus-eng/nucleus-docs';

// ---------------------------------------------------------------------------
// Data layer
// ---------------------------------------------------------------------------

// Fetch issues synchronously via gh CLI (uses stored credentials locally,
// GITHUB_TOKEN in CI). Falls back to [] on any error so the page still builds.
function fetchIssues(repo, label) {
  const cacheKey = `${repo}__${label || 'all'}`;

  // Return cached data if available
  let cache = {};
  if (existsSync(CACHE_FILE)) {
    try { cache = JSON.parse(readFileSync(CACHE_FILE, 'utf8')); } catch {}
    if (cache[cacheKey]) return cache[cacheKey];
  }

  let cmd = `gh issue list --repo ${repo} --state open --limit 100 --json number,title,labels,url,updatedAt`;
  if (label) cmd += ` --label "${label}"`;

  let raw;
  try {
    raw = execSync(cmd, { encoding: 'utf8', timeout: 15000 });
  } catch (e) {
    console.warn(`[github-issues] gh issue list failed: ${e.message}`);
    return [];
  }

  let issues;
  try {
    // gh CLI uses camelCase field names; normalise to match render expectations
    issues = JSON.parse(raw).map(i => ({
      number: i.number,
      title: i.title,
      html_url: i.url,
      updated_at: i.updatedAt,
      labels: i.labels || [],
    }));
  } catch (e) {
    console.warn(`[github-issues] Could not parse gh output: ${e.message}`);
    return [];
  }

  // Write cache
  cache[cacheKey] = issues;
  mkdirSync(dirname(CACHE_FILE), { recursive: true });
  writeFileSync(CACHE_FILE, JSON.stringify(cache, null, 2));

  return issues;
}

// ---------------------------------------------------------------------------
// Rendering — MyST AST nodes
// ---------------------------------------------------------------------------

function timeAgo(dateStr) {
  const days = Math.floor((Date.now() - new Date(dateStr)) / 86400000);
  if (days === 0) return 'today';
  if (days === 1) return 'yesterday';
  if (days < 30) return `${days}d ago`;
  const mo = Math.floor(days / 30);
  if (mo < 12) return `${mo}mo ago`;
  return `${Math.floor(mo / 12)}yr ago`;
}

function renderIssues(issues) {
  if (!issues.length) {
    return [{ type: 'paragraph', children: [{ type: 'text', value: 'No open issues found.' }] }];
  }

  return [{
    type: 'list',
    ordered: false,
    children: issues.map(issue => {
      const labelText = (issue.labels || []).map(l => l.name).join(', ');
      const meta = [labelText, `updated ${timeAgo(issue.updated_at)}`].filter(Boolean).join(' — ');
      return {
        type: 'listItem',
        spread: false,
        children: [{
          type: 'paragraph',
          children: [
            {
              type: 'link',
              url: issue.html_url,
              children: [{ type: 'text', value: `#${issue.number} ${issue.title}` }],
            },
            { type: 'text', value: `  ${meta}` },
          ],
        }],
      };
    }),
  }];
}

// ---------------------------------------------------------------------------
// Directive
// ---------------------------------------------------------------------------

const githubIssuesDirective = {
  name: 'github-issues',
  doc: 'Display open GitHub issues, optionally filtered by label.',
  options: {
    repo: { type: String, doc: 'GitHub repo (org/name). Default: nucleus-eng/nucleus-docs' },
    label: { type: String, doc: 'Filter to issues with this label' },
  },
  run(data) {
    const repo = data.options?.repo || DEFAULT_REPO;
    const label = data.options?.label;
    const issues = fetchIssues(repo, label);
    return renderIssues(issues);
  },
};

export default { name: 'GitHub Issues Board', directives: [githubIssuesDirective] };
