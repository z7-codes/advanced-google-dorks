# Advanced Google Dorks

[![GitHub repo](https://img.shields.io/badge/GitHub-z7--codes%2Fadvanced--google--dorks-blue)](https://github.com/z7-codes/advanced-google-dorks)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Authorized testing only](https://img.shields.io/badge/scope-authorized%20only-orange)](README.md)

A professionally curated, scope-safe Google dork library for **authorized** bug bounty reconnaissance.

> Search results are leads, not proof. Never exploit, download, or store sensitive data from public exposures. Test only assets you own or have written authorization to test. Report responsibly.

## Why this repo is different
- Categorized instead of one giant noisy list.
- Every dork uses a `site:TARGET` placeholder so it stays scoped.
- Benign validation markers included before any exploit-style testing.
- Clear legal/responsible-use boundaries.
- No credential theft, no mass scanning, no auto-exploitation.
- Local-only query generator — no network calls, no target scanning.

## Repo layout
```text
dorks/
  injection.md      SQLi / XSS / LFI parameter discovery
  recon.md          asset, endpoint, tech-stack discovery
  exposure.md       accidental public exposure checks (defensive)
payloads/
  benign-markers.md harmless reflection/error probes
workflows/
  methodology.md    scope -> dork -> triage -> validate -> dedupe -> report
scripts/
  make_dorks.py     local-only query generator, no network calls
```

## Categories
| Category | File | Purpose |
|---|---|---|
| Injection | `dorks/injection.md` | SQLi / XSS / LFI parameter discovery |
| Recon | `dorks/recon.md` | Assets, endpoints, tech stack |
| Exposure | `dorks/exposure.md` | Defensive exposure checks |
| Payloads | `payloads/benign-markers.md` | Harmless validation markers |
| Workflow | `workflows/methodology.md` | End-to-end safe testing flow |

## Quick start
Replace `TARGET` with your in-scope domain:
```text
site:TARGET inurl:?id=
site:TARGET inurl:?q=
```

Then:
1. Open result only if it is in scope.
2. Check benign marker reflection.
3. Dedupe against program Known Issues and public writeups.
4. Validate manually with minimal harmless input.
5. Report with clear impact and reproduction steps.

Generate scoped queries locally:
```bash
python scripts/make_dorks.py example.com sqli
python scripts/make_dorks.py example.com xss
python scripts/make_dorks.py example.com recon
```

## Rules
- Own assets or written authorization only.
- No real user accounts or third-party data.
- No automated mass requests.
- No exploitation of admin panels or credential material found via search.
- If sensitive data is found: stop, do not save it, report minimal redacted evidence.

## Contributing
Pull requests are welcome for:
- New scoped dork categories.
- Better noise reducers.
- Benign validation markers.
- Duplicate-check workflows.

Please keep every contribution legal, scoped, and non-destructive.
