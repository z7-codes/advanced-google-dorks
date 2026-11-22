# Advanced Google Dorks — Beginner to Advanced

[![GitHub repo](https://img.shields.io/badge/GitHub-z7--codes%2Fadvanced--google--dorks-blue)](https://github.com/z7-codes/advanced-google-dorks)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Authorized testing only](https://img.shields.io/badge/scope-authorized%20only-orange)](SECURITY.md)
[![Research-backed](https://img.shields.io/badge/research-GHDB%20%2B%20CTF-purple)](research/sources.md)
[![Source notes](https://img.shields.io/badge/research-output%20context-blue)](research/external-references.md)
[![Learning path](https://img.shields.io/badge/level-beginner%20to%20advanced-blueviolet)](LEARNING_PATH.md)

A professionally curated, research-backed, scope-safe Google dork library for **authorized** bug bounty, CTF, and defensive recon.

Maintained by `z7-codes`.

> Search results are leads, not proof. Never exploit, download, or store sensitive data from public exposures. Test only assets you own or have written authorization to test. Report responsibly.

## Why this repo is different

- Root-cause guide explaining how vulnerabilities actually happen.
- Complete **beginner → intermediate → advanced** learning path.
- Built from public research: GHDB categories, Google documentation, practitioner guides, and CTF writeups.
- Operator reliability split into **documented**, **undocumented**, and **retired** tiers.
- Every target-specific query uses a `site:TARGET` placeholder.
- Full mapping of all 14 GHDB categories to safe, scoped repo sections.
- Dedicated SQLi and XSS tracks built from source reviews, reduced to methodology only.
- Template-inspired lead quality bar: IDs, layered matchers, exclusions, validation, dedupe.
- Context-aware benign payload matrix: HTML, attribute, URL, JSON, header, and error-shape probes.
- No WAF-bypass strings, exploit chains, or scanner-ready attack templates.
- Sanitized walkthroughs that show reasoning without real targets.
- Copy-ready recon tracker and report templates.
- Built-in `check_dorks.py` audit for dork, payload, example, and template files.
- Defensive exposure-audit and detection notes for blue teams.
- No credential theft, no mass scanning, no auto-exploitation.
- Local-only tooling — no network calls, no target scanning.

## Start here

New to dorking? Follow this order:

```text
README.md
  -> dorks/operators.md
  -> VULNERABILITY_FUNDAMENTALS.md
  -> dorks/beginner.md
  -> dorks/intermediate.md
  -> payloads/context-probes.md
  -> dorks/sqli.md
  -> dorks/xss.md
  -> dorks/advanced.md
  -> dorks/ctf.md
  -> workflows/quality-bar.md
  -> examples/sanitized-walkthroughs.md
  -> templates/recon-tracker.md
  -> workflows/defensive-audit.md
```

Full plan: `LEARNING_PATH.md`.

## Repo layout

```text
LEARNING_PATH.md             4-week beginner-to-advanced curriculum
VULNERABILITY_FUNDAMENTALS.md root causes behind real vulnerabilities
articles/
  medium-article.md           publish-ready write-up for z7-codes
  medium-article.html         import-friendly HTML version for Medium
research/
  sources.md                  verified public sources and conclusions
  external-references.md      source review notes and safety boundaries
dorks/
  operators.md                Tier A/B/C operator reliability
  ghdb-mapping.md             all 14 GHDB categories mapped safely
  beginner.md                 first queries, core operators, mistakes
  intermediate.md             chaining, dates, noise reducers
  advanced.md                 index fossils, differential queries, stale surfaces
  injection.md                SQLi / XSS / LFI parameter discovery
  sqli.md                     SQLi parameter, error, and false-positive families
  xss.md                      XSS input surfaces and output-context validation
  recon.md                    asset, endpoint, auth-surface, tech discovery
  exposure.md                 defensive public-exposure checks
  ctf.md                      CTF web/OSINT/post-event dorks
payloads/
  README.md                   payload index and safety ladder
  benign-markers.md           context-classification markers only
  context-probes.md           context-aware benign probes
  sql-error-map.md            database error-family classification
  detection-notes.md          blue-team detection and response notes
examples/
  sanitized-walkthroughs.md   fictional reasoning cases
templates/
  recon-tracker.md            lead and dedupe tracker
  report-template.md          report format
workflows/
  methodology.md              scope -> dork -> triage -> validate -> dedupe -> report
  quality-bar.md              lead IDs, matchers, exclusions, evidence
  nuclei-style-triage.md      template-inspired manual triage recipes
  defensive-audit.md          blue-team exposure audit
scripts/
  make_dorks.py               local-only query generator
  check_dorks.py              local repo quality audit
CHANGELOG.md                  release notes
CONTRIBUTING.md               contribution rules
SECURITY.md                   allowed use and reporting
LICENSE                       MIT license, z7-codes
```

## Categories

| Category | File | Purpose |
|---|---|---|
| Learning path | `LEARNING_PATH.md` | 4-week beginner-to-advanced plan |
| Vulnerability guide | `VULNERABILITY_FUNDAMENTALS.md` | Root causes behind real vulnerabilities |
| Article | `articles/medium-article.md` | Publish-ready write-up for z7-codes |
| Article (HTML) | `articles/medium-article.html` | Import-friendly version for Medium |
| Research | `research/sources.md` | Verified sources and key conclusions |
| External notes | `research/external-references.md` | Source review notes and safety boundaries |
| Operators | `dorks/operators.md` | Documented / unofficial / retired operators |
| GHDB map | `dorks/ghdb-mapping.md` | 14 legacy categories mapped safely |
| Beginner | `dorks/beginner.md` | Core operators and first queries |
| Intermediate | `dorks/intermediate.md` | Chaining, dates, noise reducers |
| Advanced | `dorks/advanced.md` | Index fossils and differential chains |
| Injection | `dorks/injection.md` | SQLi / XSS / LFI parameter discovery |
| SQLi | `dorks/sqli.md` | Parameter families, error families, false positives |
| XSS | `dorks/xss.md` | Input surfaces and output-context validation |
| Recon | `dorks/recon.md` | Assets, endpoints, auth surface, tech stack |
| Exposure | `dorks/exposure.md` | Defensive exposure checks |
| CTF | `dorks/ctf.md` | CTF web/OSINT/post-event learning |
| Payload index | `payloads/README.md` | Safety ladder and exclusions |
| Benign markers | `payloads/benign-markers.md` | Context-classification markers only |
| Payload matrix | `payloads/context-probes.md` | Safe context-aware probes |
| SQL errors | `payloads/sql-error-map.md` | Error-family classification only |
| Detection | `payloads/detection-notes.md` | Blue-team monitoring ideas |
| Examples | `examples/sanitized-walkthroughs.md` | Reasoning with fictional targets |
| Templates | `templates/` | Tracker and report formats |
| Workflow | `workflows/methodology.md` | End-to-end safe testing flow |
| Quality bar | `workflows/quality-bar.md` | Lead IDs, matchers, exclusions, evidence |
| Triage recipes | `workflows/nuclei-style-triage.md` | Template-inspired manual checks |
| Defense | `workflows/defensive-audit.md` | Exposure audit and remediation |
| Generator | `scripts/make_dorks.py` | Local-only query generator |
| Audit script | `scripts/check_dorks.py` | Flags unsafe patterns in dork/payload/example/template files |
| Security | `SECURITY.md` | Allowed use and reporting |
| License | `LICENSE` | MIT license, z7-codes |

## Operator policy

```text
Tier A  documented, preferred: "..."  -  site:  filetype:  before:  after:  OR  ..  imagesize:  src:
Tier B  useful but unofficial: intitle:  inurl:  intext:  allintitle:  allinurl:  allintext:  ext:  AROUND(n)  *  ()
Tier C  retired, never use: cache:  related:  link:  info:  inanchor:  allinanchor:  +  ~
```

Full details: `dorks/operators.md`.

## Quick start

Replace `TARGET` with your in-scope domain:

```text
site:TARGET inurl:?id=
site:TARGET filetype:pdf intext:"confidential"
site:TARGET intitle:"index of" "parent directory"
```

Then:

1. Open result only if it is in scope.
2. Check benign marker reflection.
3. Dedupe against program Known Issues and public writeups.
4. Validate manually with minimal harmless input.
5. Report with clear impact and reproduction steps.

## Generator

The generator is local-only. It prints queries; it does not contact Google or the target.

```bash
python scripts/make_dorks.py --list
python scripts/make_dorks.py example.com beginner
python scripts/make_dorks.py example.com intermediate
python scripts/make_dorks.py example.com advanced
python scripts/make_dorks.py example.com sqli
python scripts/make_dorks.py example.com xss recon
python scripts/make_dorks.py example.com all
python scripts/make_dorks.py example.com exposure --json
```

Categories: `beginner`, `intermediate`, `advanced`, `xss`, `sqli`, `lfi`, `recon`, `exposure`, `ctf`, `ghdb`, `all`.

## Quality checks

Run before contributing or publishing changes:

```bash
python scripts/check_dorks.py
python -m py_compile scripts/*.py
```

`check_dorks.py` flags:

- Queries containing `TARGET` without `site:TARGET`.
- Retired Tier C operators.
- Invalid `operator: value` spacing.
- Exploitable-looking strings inside code blocks.

## Rules

- Own assets, written authorization, labs, or CTFs only.
- No real user accounts or third-party data.
- No automated mass requests or search-result scraping.
- No exploitation of admin panels or credential material found via search.
- CTF dorks are for provided domains and post-event learning only.
- Payloads are benign context probes, never exploit chains.
- If sensitive data is found: stop, do not save it, report minimal redacted evidence.

## Research basis

See `research/sources.md` for the core source list, and `research/external-references.md` for the SQLi/XSS, template-structure, and output-context review notes. Exploit-DB GHDB, Google Search Help, Google Search Central, practitioner guides, CTFtime, and public CTF writeups are included.

## Contributing

Pull requests are welcome for scoped dork categories, better noise reducers, operator corrections, CTF methodology notes, examples, templates, and defensive audit patterns. See `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.
