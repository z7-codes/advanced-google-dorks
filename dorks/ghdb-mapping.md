# GHDB Category Mapping

The Google Hacking Database (GHDB) is an Exploit-DB-maintained, categorized index of search queries for publicly indexed information. It remains the reference point for "Google dorking".

This repo does not reproduce the GHDB verbatim. It recreates the useful categories as original, scoped, defensive patterns.

## Official category map

| GHDB category | Repo location | Safe use |
|---|---|---|
| Footholds | `dorks/recon.md` | Inventory indexed entry points only. |
| Files Containing Usernames | `dorks/exposure.md` | Check redacted exposure; do not collect identities. |
| Sensitive Directories | `dorks/exposure.md` | Minimal proof, then report. |
| Web Server Detection | `dorks/recon.md` | Fingerprint indexed tech for scope planning. |
| Vulnerable Files | `dorks/injection.md`, `dorks/exposure.md` | Look for candidate legacy files; dedupe hard. |
| Vulnerable Servers | `dorks/recon.md` | Passive version/tech hints, not mass scanning. |
| Error Messages | `dorks/injection.md` | Error-shape discovery; many programs exclude plain errors. |
| Files Containing Juicy Info | `dorks/exposure.md` | Verify scope/impact with redaction only. |
| Files Containing Passwords | `dorks/exposure.md` | Highest sensitivity: stop, do not copy values. |
| Sensitive Online Shopping Info | `dorks/exposure.md` | Defensive exposure audit only. |
| Network or Vulnerability Data | `dorks/exposure.md` | Redact IPs, hosts, and internal paths. |
| Pages Containing Login Portals | `dorks/recon.md` | Authentication-surface inventory only. |
| Various Online Devices | `dorks/recon.md` | Indexed device/admin pages; never access unauthorized panels. |
| Advisories and Vulnerabilities | `research/sources.md`, `workflows/methodology.md` | Dedupe against public CVEs/writeups before testing. |

## Why the original GHDB-style lists are risky

- Many are 15–25 years old and almost always duplicated.
- They often target generic paths like `admin/login.php` with no scope.
- They can expose credentials or personal data if opened carelessly.
- Some programs treat known public-index exposure as a Known Issue.

## Safe reconstruction rules

1. Add `site:TARGET`.
2. Use current operator tiers from `dorks/operators.md`.
3. Save only URL, parameter, and observed behavior.
4. Apply benign markers from `payloads/benign-markers.md`.
5. Check Known Issues and public writeups before deeper work.
6. Stop immediately if real secrets or personal data appear.
