# Operator Reliability Cheat Sheet

Google's official documentation is short. Most "advanced dork" lists mix documented, undocumented, and retired operators. This repository separates them.

## Tier A — documented, most reliable

| Operator | Purpose | Example |
|---|---|---|
| `"..."` | Exact phrase | `"internal use only"` |
| `-` | Exclude a term or site | `site:TARGET -site:TARGET/blog` |
| `site:` | Restrict to a domain, subdomain, or URL prefix | `site:TARGET` |
| `filetype:` | Restrict to a file type | `site:TARGET filetype:pdf` |
| `before:` | Last updated before a date | `site:TARGET before:2025-01-01` |
| `after:` | Last updated after a date | `site:TARGET after:2024-01-01` |
| `OR` | Either term; must be uppercase | `site:TARGET login OR signin` |
| `..` | Number range from Advanced Search | `camera 2019..2023` |
| `imagesize:` | Exact image size; Google Images only | `imagesize:1200x630` |
| `src:` | Pages referencing an image URL; Google Images only | `src:example.com/logo.png` |

## Tier B — widely used, not officially documented

| Operator | Purpose | Example |
|---|---|---|
| `intitle:` | Term in page title | `site:TARGET intitle:"index of"` |
| `allintitle:` | All following terms in title | `allintitle:admin login` |
| `inurl:` | Term in URL | `site:TARGET inurl:/api/` |
| `allinurl:` | All following terms in URL | `allinurl:admin backup` |
| `intext:` | Term in visible body text | `site:TARGET intext:"Powered by"` |
| `allintext:` | All following terms in body text | `allintext:confidential internal` |
| `ext:` | Alias for `filetype:` | `site:TARGET ext:env` |
| `AROUND(n)` | Terms within n words | `site:TARGET password AROUND(3) reset` |
| `*` | Wildcard inside a phrase | `"password * reset"` |
| `()` | Grouping | `site:TARGET (login OR signin)` |

## Tier C — retired or unreliable

Avoid these in new queries:

```text
cache:
related:
link:
info:
+
~
inanchor:
allinanchor:
```

## Syntax rules

```text
site:TARGET        correct
site: TARGET       wrong
OR                 uppercase only
or                 usually treated as a normal word
```

- Multiple operators in one query are generally treated as AND.
- `allintitle:`, `allinurl:`, and `allintext:` consume the remaining terms; place them last or avoid mixing them.
- `site:` results are a sample, not a complete index.
- A result can be stale, cached, or already fixed; verify carefully and respect scope.
- Manual querying only; do not automate Google result scraping.

## Query-building pattern

```text
site:TARGET filetype:pdf intext:"internal use only" -site:TARGET/blog after:2024-01-01
```

Read it as:

1. Stay inside `TARGET`.
2. Only PDFs.
3. Body text contains `internal use only`.
4. Remove blog noise.
5. Prefer newer indexed documents.

## Reliability policy for this repo

- Every target-specific query starts with `site:TARGET`.
- Tier C operators are never used.
- Tier B operators are marked as heuristic lead generators.
- Before testing a lead, follow `workflows/methodology.md`.
