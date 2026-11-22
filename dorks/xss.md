# Cross-Site Scripting Discovery Dorks

XSS dorks find **input surfaces**, not XSS. The useful question is always: where does the value land, and how is it encoded on the way back?

## 1. Search and query parameters

```text
site:TARGET inurl:?q=
site:TARGET inurl:?query=
site:TARGET inurl:?search=
site:TARGET inurl:?keyword=
site:TARGET inurl:?term=
site:TARGET inurl:?s=
site:TARGET inurl:?text=
site:TARGET inurl:?value=
```

## 2. URL and redirect parameters

```text
site:TARGET inurl:?url=
site:TARGET inurl:?redirect=
site:TARGET inurl:?next=
site:TARGET inurl:?return=
site:TARGET inurl:?target=
site:TARGET inurl:?r=
site:TARGET inurl:?u=
site:TARGET inurl:?goto=
```

These often feed a navigation decision. Read the redirect behavior before deciding whether the parameter reflects into HTML.

## 3. Localization, view, and template parameters

```text
site:TARGET inurl:?lang=
site:TARGET inurl:?language=
site:TARGET inurl:?locale=
site:TARGET inurl:?view=
site:TARGET inurl:?template=
site:TARGET inurl:?theme=
site:TARGET inurl:?mode=
site:TARGET inurl:?page=
```

A value used to choose a file or template is a different risk class from reflected text. Do not assume XSS from reflection alone.

## 4. Legacy and error surfaces

```text
site:TARGET ext:php inurl:?q=
site:TARGET ext:asp inurl:?q=
site:TARGET ext:aspx inurl:?search=
site:TARGET ext:jsp inurl:?keyword=
site:TARGET inurl:?q= intext:"error"
site:TARGET intext:"Stack trace" inurl:?page=
```

## 5. Context-first validation

| Landing context | Question to answer | Safe observation | Expected defense |
|---|---|---|---|
| HTML text | Is the marker raw or encoded? | Source/view shows text vs entity form. | Contextual output encoding. |
| Attribute value | Are quote boundaries preserved? | Extra attributes do not appear. | Attribute-aware encoding. |
| URL value | Is the scheme controlled? | No unexpected scheme change. | Allowlisted schemes and safe redirects. |
| Script string | Is the value data or code? | Value stays inside a quoted data value. | Safe DOM APIs, no string-built code. |
| Style value | Is the value confined? | No new style rule appears. | CSS/URL allowlisting. |
| JSON response | Is escaping consistent? | String remains a string field. | Serializer-based encoding. |
| Template expression | Is evaluation absent? | Marker is displayed literally. | No server-side expression evaluation. |

Full probe matrix: `payloads/context-probes.md`.

## 6. OWASP-derived rules

- XSS is an **output-context** problem, not a “bad word” problem.
- Do not rely on denylists, regexes, or keyword removal.
- Validate with allowlists where input has a known shape.
- Prefer framework autoescaping and safe DOM APIs.
- Avoid dangerous sinks that turn strings into code.
- Treat WAF rules as defense-in-depth, never as the fix.
- Test encoded and malformed markup carefully, but record only context and behavior here.

## 7. Triage ladder

1. Confirm scope and Known Issues.
2. Record query, URL, parameter, and landing context.
3. Send one harmless marker at a time.
4. Observe reflection, encoding, content-type, and storage behavior.
5. Distinguish reflected, stored, and DOM-shaped behavior.
6. Stop if real user data, sessions, or destructive actions appear.
7. Report only with a minimal, non-destructive proof and clear impact.

## 8. Common false positives

| Lead | Why it is often noise |
|---|---|
| Marker reflected as text | Normal behavior; encoding is doing its job. |
| Search term shown in a results heading | Usually safely escaped by the framework. |
| Error page echo | Often generic or already known. |
| Public demo/search engine result | Not application behavior. |
| Self-only change with no persistence | May be low impact unless it crosses a trust boundary. |
| WAF block page | Shows a filter exists, not that XSS exists. |

## 9. Defensive fix

- Use contextual output encoding for HTML, attribute, script, style, and URL contexts.
- Keep framework autoescaping enabled.
- Use safe DOM APIs instead of string-to-code sinks.
- Sanitize only when rich HTML is genuinely required, with a strict allowlist.
- Set `HttpOnly` on session cookies and use a restrictive CSP as hardening.
- Add regression tests for each output context instead of blocking individual words.
