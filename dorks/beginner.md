# Beginner Dorks

Start here. Replace `TARGET` with an in-scope domain.

## Five operators to know

| Operator | Meaning | Example |
|---|---|---|
| `site:` | Results from one domain/prefix | `site:TARGET` |
| `"..."` | Exact phrase | `"internal use only"` |
| `filetype:` | Specific file type | `site:TARGET filetype:pdf` |
| `-` | Exclude | `site:TARGET -site:TARGET/blog` |
| `OR` | Either term, uppercase | `site:TARGET login OR signin` |

## Level 1 — scope and inventory

```text
site:TARGET
site:TARGET -www
site:TARGET filetype:pdf
site:TARGET inurl:robots.txt
site:TARGET inurl:sitemap.xml
```

## Level 2 — exact phrases

```text
site:TARGET "confidential"
site:TARGET "internal use only"
site:TARGET "admin login"
site:TARGET "Powered by"
site:TARGET "index of"
```

## Level 3 — file types

```text
site:TARGET filetype:pdf
site:TARGET filetype:docx
site:TARGET filetype:xlsx
site:TARGET filetype:txt
site:TARGET filetype:json
```

## Level 4 — exclusions

```text
site:TARGET -site:TARGET/blog
site:TARGET -site:TARGET/news
site:TARGET -site:TARGET/careers
site:TARGET -site:TARGET/support
site:TARGET filetype:pdf -inurl:marketing
```

## Level 5 — first chains

```text
site:TARGET filetype:pdf "confidential"
site:TARGET intitle:"index of" "parent directory"
site:TARGET intitle:"login" inurl:admin
site:TARGET inurl:?q= -site:TARGET/blog
site:TARGET filetype:pdf after:2024-01-01
```

## Mini exercises

1. Write 5 queries that only search inside `TARGET`.
2. Write 3 queries that exclude `/blog`, `/news`, and `/support`.
3. Write 2 queries using `filetype:` and an exact phrase.
4. Write 1 query with `OR`.
5. Explain why `site: TARGET` is wrong.

## Beginner mistakes

- Space after the colon: `site: TARGET`.
- Lowercase `or` instead of uppercase `OR`.
- Copying old dorks without `site:TARGET`.
- Reporting a search result as a vulnerability.
- Opening exposed files and copying sensitive values.

## Next

Go to `dorks/intermediate.md`.
