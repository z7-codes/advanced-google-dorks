# Context Probe Matrix

Goal: learn **where** input lands before trying anything stronger. Replace values with your own benign marker.

## Context map

| Context | Probe | What to observe |
|---|---|---|
| HTML body | `zzPROBE123` | Raw reflection vs encoded output. |
| HTML body | `<b>zzPROBE123</b>` | Whether tags are escaped. |
| Attribute value | `zzPROBE123" y="zzBENIGNzz` | Quote escaping and extra attributes. |
| Attribute value | `zzPROBE123' y='zzBENIGNzz` | Single-quote escaping. |
| Attribute break | `"><b>zzPROBE123</b>` | Whether the attribute boundary is escaped. |
| Attribute break | `'"><b>zzPROBE123</b>` | Whether both quote styles are handled. |
| URL parameter | `https://example.invalid/?q=zzPROBE123` | Redirect/URL encoding behavior. |
| URL parameter | `zzPROBE123?x=1&y=2` | Query splitting and decoding. |
| JSON value | `{"probe":"zzPROBE123"}` | Escaping in JSON responses. |
| Header | `X-Probe: zzPROBE123` | Whether request headers are reflected. |
| Template | `{{zzPROBE123}}` | Server-side template evaluation. |
| Template | `${zzPROBE123}` | Expression evaluation. |
| SQL shape | `'` | Error-shape only; dedupe before reporting. |
| SQL shape | `1' AND '1'='1` | Boolean behavior difference; do not dump data. |

## Interpretation

```text
raw marker in source          -> reflection lead
tag parsed as markup          -> escaping lead
attribute boundary changed    -> context break lead
error text appears            -> error-shape lead; often Known Issue
template expression evaluated -> lead; verify carefully in scope
no visible change             -> likely not useful
```

## Decision rules

1. One probe at a time.
2. Record request, response snippet, and context.
3. Do not combine with exploit payloads.
4. Do not test another user's data.
5. Stop on sensitive output or destructive behavior.

## What not to infer

- A reflected marker is not automatically XSS.
- A SQL error is not automatically exploitable SQLi.
- A public doc is not automatically a reportable exposure.
- A search result is never proof.

Dedupe with Known Issues and public writeups before deeper testing.
