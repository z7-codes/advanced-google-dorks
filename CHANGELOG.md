# Changelog

## 1.4.3 — 2026-11-22

- Added companion tool intro and badge for `z7-codes/scopeforge`.
- Linked ScopeForge from README, learning path, and category navigation.
- Documented local install and safety boundary for the companion CLI.

## 1.4.2 — 2026-11-22

- Added `dorks/manual-discovery.md` for operator-free discovery, manual browsing, third-party lead handling, and scope conversion.
- Linked the new guide from README, learning path, methodology, and release notes.
- Reinforced that third-party websites are intel only and never testing targets.

## 1.4.1 — 2026-11-21

- Added `articles/medium-article.html`, a clean import-friendly version of the Medium draft.
- Listed the HTML article in README navigation and categories.

## 1.4.0 — 2026-11-21

- Added `VULNERABILITY_FUNDAMENTALS.md` explaining root causes, exposure vs vulnerability, severity factors, and defensive fixes.
- Added `articles/medium-article.md`, a publish-ready long-form write-up branded to z7-codes.
- Aligned `LICENSE`, README, CONTRIBUTING, and release notes to a single z7-codes identity.
- Fixed retired-operator policy mismatch across README, operator notes, and `check_dorks.py`.
- Removed boundary-break, boolean-tradeoff, and expression-evaluation strings from the benign probe files.
- Removed the SQL dump-content dork from the advanced exposure section.
- Fixed `TARGET.com` noise reducers and tightened the scoped-query regex.
- Corrected CTF wording, placeholder definitions, source credits, and defensive phrasing.
- Expanded README navigation, categories, layout descriptions, and learning-order consistency.

## 1.3.0 — 2026-11-21

- Added `research/external-references.md` with SQLi, XSS, nuclei-templates, and OWASP source review notes.
- Added `dorks/sqli.md` with parameter families, error families, noise reducers, and defensive fixes.
- Added `dorks/xss.md` with input surfaces, output-context mapping, and OWASP-derived rules.
- Added `payloads/sql-error-map.md` for redacted error-family classification.
- Added `workflows/quality-bar.md` and `workflows/nuclei-style-triage.md` for template-inspired manual QA.
- Expanded `payloads/context-probes.md` with output-context and dangerous-context notes.
- Hardened `scripts/check_dorks.py` to block exploitable-looking strings in code blocks.
- Expanded SQLi and XSS generator categories and refreshed README navigation.

## 1.2.0 — 2026-11-21

- Added `LEARNING_PATH.md` with a 4-week beginner-to-advanced curriculum.
- Added `dorks/beginner.md`, `dorks/intermediate.md`, and `dorks/advanced.md`.
- Added `payloads/README.md`, `payloads/context-probes.md`, and `payloads/detection-notes.md`.
- Added `examples/sanitized-walkthroughs.md` with five fictional reasoning cases.
- Added `templates/recon-tracker.md` and `templates/report-template.md`.
- Added `scripts/check_dorks.py` to audit unscoped queries, retired operators, and spacing.
- Expanded `scripts/make_dorks.py` with `beginner`, `intermediate`, and `advanced` categories.
- Documented quality-check commands in README and contribution requirements.

## 1.1.0 — 2026-11-21

- Added `research/sources.md` with verified source list and conclusions.
- Added `dorks/operators.md` with Tier A/B/C operator reliability.
- Added `dorks/ghdb-mapping.md` mapping all 14 GHDB categories to scoped repo sections.
- Added `dorks/ctf.md` for CTF web/OSINT/post-event learning.
- Added `workflows/defensive-audit.md` for blue-team exposure audits.
- Expanded `scripts/make_dorks.py` with `all`, `--list`, and `--json`.
- Polished README, contribution rules, and repo structure.

## 1.0.0 — 2026-11-20

- Initial public release.
- Added scoped injection, recon, and exposure dorks.
- Added benign validation markers.
- Added local-only query generator.
- Published `z7-codes/advanced-google-dorks`.
