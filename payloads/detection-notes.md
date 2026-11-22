# Detection Notes

For defenders auditing owned assets.

## Signals to monitor

| Signal | Why it matters |
|---|---|
| Spike in requests for `robots.txt`, `sitemap.xml`, `.env`, `*.bak` | Common indexed-path validation. |
| Search-referrer traffic to old paths | Google-indexed or stale content may be exposed. |
| Repeated 404s on backup/config filenames | Manual path validation after dorking. |
| Requests containing `opencodetest123` or `zzBENIGNzz` | Benign recon probes from this repo. |
| Raw error pages containing stack traces | Often discoverable via index and error dorks. |
| Directory-listing titles in search results | Misconfiguration visible externally. |

## Defensive checks

```text
site:OWNED_DOMAIN intitle:"index of"
site:OWNED_DOMAIN filetype:env
site:OWNED_DOMAIN filetype:sql
site:OWNED_DOMAIN filetype:log
site:OWNED_DOMAIN "internal use only"
site:OWNED_DOMAIN "BEGIN PRIVATE KEY"
```

Replace `OWNED_DOMAIN` with your own domain.

## Response playbook

1. Confirm the asset is owned and the exposure is real.
2. Remove the public content, not just rename it.
3. Revoke any exposed credentials immediately.
4. Purge CDN/cache copies.
5. Fix the root cause: server config, CI secret handling, or access control.
6. Re-run the same query after the fix.
7. Record query, URL, fix, and verification date.

## Logging fields worth keeping

```text
timestamp
request path
query string
status code
referrer
user agent
source IP
response size
matched rule
```

## Alert idea

```text
if path matches .env|*.bak|*.sql|*.log
and status in 200,206
and referrer contains search engine
then alert
```

Tune carefully to avoid noise from legitimate files.
