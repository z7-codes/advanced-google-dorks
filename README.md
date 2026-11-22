# Advanced Google Dorks

[![GitHub repo](https://img.shields.io/badge/GitHub-z7--codes%2Fadvanced--google--dorks-blue)](https://github.com/z7-codes/advanced-google-dorks)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Authorized testing only](https://img.shields.io/badge/scope-authorized%20only-orange)](README.md)
[![Research-backed](https://img.shields.io/badge/research-GHDB%20%2B%20CTF-purple)](research/sources.md)

A professionally curated, research-backed, scope-safe Google dork library for **authorized** bug bounty, CTF, and defensive recon.

> Search results are leads, not proof. Never exploit, download, or store sensitive data from public exposures. Test only assets you own or have written authorization to test. Report responsibly.

## Why this repo is different

- Built from public research: GHDB categories, Google documentation, practitioner guides, and CTF writeups.
- Operator reliability split into **documented**, **undocumented**, and **retired** tiers.
- Categorized instead of one giant noisy list.
- Every target-specific query uses a `site:TARGET` placeholder.
- Full mapping of all 14 GHDB categories to safe, scoped repo sections.
- CTF section for web/OSINT learning and post-event writeups.
- Benign validation markers before any exploit-style testing.
- Defensive exposure-audit workflow for blue teams.
- No credential theft, no mass scanning, no auto-exploitation.
- Local-only generator — no network calls, no target scanning.

## Repo layout

```text
research/
  sources.md              verified public sources and conclusions
dorks/
  operators.md            Tier A/B/C operator reliability
  ghdb-mapping.md         all 14 GHDB categories mapped safely
  injection.md            SQLi / XSS / LFI parameter discovery
  recon.md                asset, endpoint, auth-surface, tech discovery
  exposure.md             defensive public-exposure checks
  ctf.md                  CTF web/OSINT/post-event dorks
payloads/
  benign-markers.md       harmless reflection/error probes
workflows/
  methodology.md          scope -> dork -> triage -> validate -> dedupe -> report
  defensive-audit.md      blue-team exposure audit
scripts/
  make_dorks.py           local-only query generator, no network calls
CHANGELOG.md
CONTRIBUTING.md
SECURITY.md
LICENSE
```

## Categories

| Category | File | Purpose |
|---|---|---|
| Research | `research/sources.md` | Verified sources and key conclusions |
| Operators | `dorks/operators.md` | Documented / unofficial / retired operators |
| GHDB map | `dorks/ghdb-mapping.md` | 14 legacy categories mapped safely |
| Injection | `dorks/injection.md` | SQLi / XSS / LFI parameter discovery |
| Recon | `dorks/recon.md` | Assets, endpoints, auth surface, tech stack |
| Exposure | `dorks/exposure.md` | Defensive exposure checks |
| CTF | `dorks/ctf.md` | CTF web/OSINT/post-event learning |
| Payloads | `payloads/benign-markers.md` | Harmless validation markers |
| Workflow | `workflows/methodology.md` | End-to-end safe testing flow |
| Defense | `workflows/defensive-audit.md` | Exposure audit and remediation |

## Operator policy

```text
Tier A  documented, preferred: "..."  -  site:  filetype:  before:  after:  OR
Tier B  useful but unofficial: intitle:  inurl:  intext:  ext:  AROUND(n)
Tier C  retired, never use: cache:  related:  link:  info:  +  ~
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
python scripts/make_dorks.py example.com sqli
python scripts/make_dorks.py example.com xss recon
python scripts/make_dorks.py example.com all
python scripts/make_dorks.py example.com exposure --json
```

Categories: `xss`, `sqli`, `lfi`, `recon`, `exposure`, `ctf`, `ghdb`, `all`.

## Rules

- Own assets, written authorization, labs, or CTFs only.
- No real user accounts or third-party data.
- No automated mass requests or search-result scraping.
- No exploitation of admin panels or credential material found via search.
- CTF dorks are for provided domains and post-event learning only.
- If sensitive data is found: stop, do not save it, report minimal redacted evidence.

## Research basis

See `research/sources.md` for the full source list, including Exploit-DB/OffSec GHDB, Google Search Help, Google Search Central, practitioner guides, CTFtime, and public CTF writeups.

## Contributing

Pull requests are welcome for scoped dork categories, better noise reducers, operator corrections, CTF methodology notes, and defensive audit patterns. See `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.
