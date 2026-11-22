# Advanced Dorks

Advanced means precision, chaining, and documentation — not harmful payloads.

## URL-prefix scoping

Use only if the subdomain or path is explicitly in scope.

```text
site:https://TARGET/api/
site:TARGET/api/
site:dev.TARGET
site:TARGET/v1/
site:TARGET/legacy/
```

## Index fossils

Find pages Google indexed but the site may have forgotten.

```text
site:TARGET inurl:/old/
site:TARGET inurl:/legacy/
site:TARGET inurl:/archive/
site:TARGET inurl:/backup/
site:TARGET inurl:/tmp/
site:TARGET "deprecated" filetype:pdf
```

## Differential queries

Compare two surfaces and inspect the delta.

```text
site:TARGET inurl:?q= -inurl:?search=
site:TARGET intitle:"login" -inurl:admin
site:TARGET filetype:pdf -site:TARGET/legal
site:TARGET inurl:/api/ -inurl:/docs -inurl:/v1/
site:TARGET "confidential" after:2025-01-01 -"annual report"
```

## High-signal exposure

```text
site:TARGET filetype:env intext:"api_key" -inurl:public
site:TARGET filetype:log intext:"token" -inurl:sample
site:TARGET filetype:sql intext:"INSERT INTO" -inurl:demo
site:TARGET "BEGIN PRIVATE KEY" -inurl:docs
site:TARGET intitle:"index of" inurl:backup
```

## Error-surface discovery

```text
site:TARGET intext:"SQL syntax" -inurl:blog
site:TARGET intext:"Warning: mysql" -site:TARGET/forum
site:TARGET intext:"Stack trace" filetype:txt
site:TARGET intext:"Fatal error" after:2025-01-01
```

Many programs exclude verbose errors. Dedupe before reporting.

## Auth and device surfaces

```text
site:TARGET intitle:"login" inurl:admin -inurl:docs
site:TARGET intitle:"dashboard" -site:TARGET/blog
site:TARGET inurl:/router/ OR inurl:/camera/ OR inurl:/printer/
site:TARGET inurl:/actuator -inurl:docs
```

Inventory only. Never access unauthorized panels.

## All-prefix caution

`allintitle:`, `allinurl:`, and `allintext:` consume the remaining terms and can break chaining. Prefer the single-term versions with quotes:

```text
site:TARGET intitle:"index of" inurl:backup
site:TARGET inurl:admin intitle:"login"
site:TARGET intext:"Powered by" filetype:html
```

## Time-based pivots

```text
site:TARGET inurl:/api/ after:2026-01-01
site:TARGET filetype:pdf after:2025-01-01 before:2026-01-01
site:TARGET inurl:/legacy/ before:2024-01-01
```

## Query chains

Example chain:

```text
site:TARGET inurl:/api/
site:TARGET inurl:/api/ -inurl:/docs
site:TARGET inurl:/api/ -inurl:/docs after:2025-01-01
site:TARGET inurl:/api/ -inurl:/docs intext:"token"
```

Then:

1. Save only URL + query + observed text.
2. Check scope and Known Issues.
3. Validate with benign markers.
4. Stop if sensitive data appears.

## Advanced checklist

- Wrote at least one differential query.
- Used URL-prefix scoping only where authorized.
- Checked for stale/index-fossil surfaces.
- Documented why each filter was added.
- Treated every result as a lead, not proof.

## Next

Use `scripts/make_dorks.py TARGET advanced --json` to generate a local batch.
