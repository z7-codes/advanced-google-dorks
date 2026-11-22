# Operator-Free Discovery

This guide covers discovery that does **not** start with `site:`. It is for finding candidate assets and hints, not for testing random websites.

> A search result without a scope check is still only a rumor. Never test an asset until it appears in written authorization, a program scope, or a CTF-provided domain list.

## When this is useful

- The scope names a product or brand, but not every asset is known.
- Official docs, status pages, app listings, or social profiles mention hostnames.
- Public writeups reveal an old path or parameter family.
- A CTF gives a product name instead of a direct target URL.
- You want to build a target map before writing scoped queries.

## Rule first

- **Discovery is not authorization.**
- Third-party websites are **intel only**, never testing targets.
- Browse manually. No crawlers, no mass scrapers, no automated link following.
- Do not download files, archives, dumps, or credential material from random hosts.
- If a page contains sensitive data, stop and record only a redacted description.

## Operator-free discovery patterns

Replace `Acme` with the product, brand, or program name from your written scope. These examples are fictional and are **lead generators only**.

```text
"Acme" "developer portal"
"Acme" "api documentation"
"Acme" "status page"
"Acme" "security advisory"
"Acme" "bug bounty"
"Acme" "responsible disclosure"
"Acme" "staging"
"Acme" "internal tools"
"Acme" "sitemap.xml"
"Acme" "robots.txt"
"Acme" filetype:pdf
"Acme" filetype:pdf "confidential"
"Acme" "login" "dashboard"
"Acme" "admin" "portal"
```

Useful variations:

```text
"Acme Mobile" "privacy policy"
"Acme" "developer" "subdomain"
"Acme" "API" "v1"
"Acme" "API" "v2"
"Acme" "changelog"
"Acme" "release notes"
"Acme" "support" "portal"
"Acme" "careers" "engineering"
```

These are not dorks against a target. They are questions about what the ecosystem publicly exposes.

## Manual browsing map

Start from official sources and expand one link at a time.

```text
official homepage
  -> footer links
  -> docs / developer portal
  -> status page
  -> changelog / release notes
  -> support / help center
  -> privacy policy / terms
  -> security.txt / responsible disclosure
  -> app store listing
  -> GitHub organization
  -> social profiles
  -> PDF reports and slide decks
```

For each page, record:

- URL where the hint appeared.
- Hostname or product name mentioned.
- Whether the hostname is official.
- Whether the hostname is in written scope.
- Whether the path is already in Known Issues.
- Whether it is worth converting into a scoped query.

## Convert leads into scoped queries

Only after ownership and scope are confirmed, convert the discovery into a scoped query.

```text
site:TARGET inurl:/docs
site:TARGET inurl:/api
site:TARGET inurl:/v1
site:TARGET inurl:/v2
site:TARGET inurl:/staging
site:TARGET inurl:/internal
site:TARGET inurl:/admin
site:TARGET ext:pdf
site:TARGET inurl:robots.txt
site:TARGET inurl:sitemap.xml
```

Example reasoning:

```text
Discovery: "Acme" "api documentation" points to docs.acme.example
Scope check: docs.acme.example is listed in the program scope
Convert: site:TARGET inurl:/docs
Decision: inventory only unless a live in-scope parameter is found
```

## Third-party and random websites

Third-party sites can be useful, but they carry strict limits.

| Source | Safe use | Unsafe use |
|---|---|---|
| Public writeup | Learn parameter family or root cause | Copy exploit chain and fire it at a target |
| Paste site | Note that a leak may exist | Copy, store, or share leaked values |
| GitHub repo | Identify official tooling or config patterns | Test leaked credentials or endpoints |
| Screenshot host | Understand a UI path | Treat it as proof of a live vulnerability |
| Random blog | Find a search term | Assume the target is in scope |

If a third-party site mentions an official asset, go back to the official asset and verify scope there. Do not test the third-party site.

## Lead classification

```text
lead_id | source | candidate | ownership | scope_status | action
L-001   | docs   | api.acme.example | official | in-scope | convert to scoped query
L-002   | blog   | acme-staging.example | unclear | unknown | hold, do not test
L-003   | paste  | dumps.acme.example | official | in-scope | stop, redacted report only
L-004   | forum  | fake-acme.example | third-party | out-of-scope | discard
```

## Stop conditions

- Ownership cannot be confirmed.
- Asset is not explicitly in scope.
- Search result contains real user data, secrets, or credentials.
- A third-party host is the only available copy of the content.
- The lead depends on credential stuffing, brute force, or social engineering.

## Rule

Operator-free discovery finds **candidates**. Scope checks turn candidates into **targets**. Only benign, manual validation turns targets into **findings**.
