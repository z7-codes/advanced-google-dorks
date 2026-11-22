# Changelog

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
