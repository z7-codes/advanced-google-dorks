# Context Probe Matrix

Goal: learn **where** input lands. Use this for context classification only; do not escalate.

## Context map

| Context | Probe | What to observe |
|---|---|---|
| HTML body | `zzPROBE123` | Raw reflection vs encoded output. |
| HTML body | `<b>zzPROBE123</b>` | Whether tags are escaped. |
| Attribute value | `zzPROBE123` | Whether the value is encoded for attributes. |
| URL parameter | `https://example.invalid/?q=zzPROBE123` | Redirect/URL encoding behavior. |
| URL parameter | `zzPROBE123?x=1&y=2` | Query splitting and decoding. |
| JSON value | `{"probe":"zzPROBE123"}` | Escaping in JSON responses. |
| Header | `X-Probe: zzPROBE123` | Whether request headers are reflected. |
| SQL shape | `'` | Error-shape only; dedupe before reporting. |

## Interpretation

```text
raw marker in source          -> reflection lead
tag parsed as markup          -> escaping lead
attribute value encoded       -> context handled
error text appears            -> error-shape lead; often Known Issue
no visible change             -> likely not useful
```

## Decision rules

1. One probe at a time.
2. Record request, response snippet, and context.
3. Do not escalate beyond these markers.
4. Do not test another user's data.
5. Stop on sensitive output or destructive behavior.

## What not to infer

- A reflected marker is not automatically XSS.
- A SQL error is not automatically exploitable SQLi.
- A public doc is not automatically a reportable exposure.
- A search result is never proof.

Dedupe with Known Issues and public writeups before deeper testing.

## OWASP-derived output-context map

| Output context | Safe expectation | Defense |
|---|---|---|
| HTML text | Marker is displayed as text, not markup. | HTML entity encoding. |
| HTML attribute | Quote boundaries stay intact. | Attribute-aware encoding. |
| URL / redirect | Scheme and destination remain allowlisted. | URL validation and safe redirect mapping. |
| Script data | Value remains quoted data, never code. | Avoid string-built code; use safe DOM APIs. |
| Style data | Value cannot create a new rule or external URL. | Strict CSS/URL allowlisting. |
| JSON | Value remains a string field. | Serializer-based encoding. |
| Template expression | Marker is never evaluated. | No user-controlled template or expression evaluation. |

## Dangerous contexts to record, not exploit

- User input placed directly into executable script or markup.
- User input used as an attribute name or unquoted attribute value.
- User input used as a URL scheme or redirect target.
- User input used as a template, expression, or include path.
- User input used to build a database identifier or query fragment.

Record the context, encoding behavior, and impact in `templates/recon-tracker.md`. Do not add filter-evasion strings or exploit chains to this repo.

## Defensive notes

- Encoding must match the output context; one universal filter is not enough.
- Denylists and keyword removal are fragile.
- Canonicalize before validation, then validate with allowlists.
- Framework autoescaping should stay enabled.
- WAF rules are defense-in-depth, not a substitute for correct output handling.
- CSP, `HttpOnly` cookies, and safe DOM APIs reduce impact but do not fix the sink.
