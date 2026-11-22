# External Reference Notes

Research date: `2026-11-21`.

These notes were added after a second source review requested for this repo. The aim was to extract method, not to copy material. Public dork lists, slide decks, scanner template repos, and WAF-evasion material are full of fragile strings; this repo keeps only the parts that improve scoping, triage, and defense.

| # | Source | Access during review | Extracted value | Applied in | Boundary |
|---|---|---|---|---|---|
| 1 | PDFCoffee — SQL Injection Dorks | Direct fetch blocked with `403 GET`; indexed mirrors and related lists were available | Parameter-first dorking (`id`, `cat`, `category`, `product`, `page`, `num`, `file`) and database error-string classification | `dorks/sqli.md`, `payloads/sql-error-map.md`, `scripts/make_dorks.py` | No exploit chains, no union/data-dump strings, no copied list verbatim. |
| 2 | SlideShare — XSS Attacks: Defense | Direct fetch blocked by `Client Challenge`; indexed catalog outlines were available | Discovery → theory → attack methods → advanced vectors → prevention structure; context-first defense | `dorks/xss.md`, `payloads/context-probes.md` | No exploit frameworks, worms, malware, or live payload strings. |
| 3 | projectdiscovery/nuclei-templates | Repository fetched; creation guide was navigation-heavy/truncated | Unique IDs, precise metadata, references, tags, layered matchers, false-positive discipline, template review habits | `workflows/quality-bar.md`, `workflows/nuclei-style-triage.md` | Structure and QA only; no executable vulnerability template copied. |
| 4 | OWASP XSS Filter Evasion Cheat Sheet | Fetched successfully | Testing categories: baseline locators, malformed markup, encoding/obfuscation, active elements, event handlers, CSS, URL/request surfaces, WAF-focused material. Defensive lesson: output context decides encoding; denylists and keyword filters fail. | `dorks/xss.md`, `payloads/context-probes.md` | Only category names and defensive lessons; no literal evasion strings. |
| 5 | Secondary indexed SQL dork collections | Found while checking the PDF | Common mitigations: allowlist untrusted data, parameterize statements, least-privilege DB accounts | `dorks/sqli.md`, `workflows/defensive-audit.md` | Used as a sanity check, not as a source to copy. |

## What changed in the repo

- SQLi section now separates **parameter families**, **error families**, and **false-positive families**.
- XSS section now starts from **where input lands** instead of starting from payloads.
- Added `payloads/sql-error-map.md` for reading error text without treating it as proof.
- Added a nuclei-inspired **quality bar** for every lead: ID, scope, discovery, discriminator, exclusion, validation, stop rule, evidence.
- `check_dorks.py` now also blocks exploitable-looking strings inside code blocks.

## What this repo deliberately excludes

- WAF bypass strings and filter-evasion payloads.
- SQL union/data-dump, time-delay, or blind-extraction payloads.
- Script tags, event-handler payloads, JavaScript URI payloads, cookie theft, or DOM sink payloads.
- Scanner-ready exploit templates or automated attack chains.
- Copied database dumps, leaked credential lists, or sensitive search results.

## Rule of thumb

If a source teaches **how to find and understand a risky input surface**, it belongs here.

If it teaches **how to break through a control, extract data, or evade detection**, it stays out.
