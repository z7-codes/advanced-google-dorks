# Template-Inspired Triage Workflow

Scanner templates are useful as a **thinking model**: unique identity, explicit scope, layered matchers, exclusions, and repeatable validation. This file applies that model to manual dork triage without using executable attack templates.

## SQL error lead recipe

```text
id: SQLI-ERROR-SURFACE-001
name: indexed database error text on scoped parameter
scope: TARGET
discovery:
  - site:TARGET ext:php inurl:?id=
  - site:TARGET intext:"SQL syntax"
surface:
  parameter: id
  method: GET
matcher:
  primary: database error family
  secondary: response differs from baseline
  exclusion: documentation, tutorial, known issue, static sample
validation:
  input: harmless marker zzPROBE123
  observe: status, error family, content shape
  stop: sensitive rows, schema dump, write behavior
dedupe:
  - program Known Issues
  - public writeups for endpoint/parameter
report:
  require: clear impact and minimal redacted proof
```

## XSS context lead recipe

```text
id: XSS-CONTEXT-SURFACE-001
name: reflected parameter with unclear output encoding
scope: TARGET
discovery:
  - site:TARGET inurl:?q=
  - site:TARGET inurl:?search=
surface:
  parameter: q or search
  method: GET
matcher:
  primary: marker reflected in response
  secondary: landing context identified
  exclusion: static help page, public search engine, safe encoded text
validation:
  input: one benign marker at a time
  observe: raw vs encoded, attribute boundary, content-type
  stop: real user data, session material, destructive action
dedupe:
  - program Known Issues
  - public writeups for endpoint/parameter
report:
  require: context break plus clear impact
```

## Exposure lead recipe

```text
id: EXPOSED-FILE-001
name: indexed sensitive file type on scoped host
scope: TARGET
discovery:
  - site:TARGET filetype:env
  - site:TARGET intitle:"index of"
surface:
  path: indexed file or directory
matcher:
  primary: file type or listing signature
  secondary: owner/scope confirmation
  exclusion: public sample, docs, test fixture
validation:
  input: none beyond normal read
  observe: redacted description only
  stop: credentials, personal data, secrets
dedupe:
  - program Known Issues
  - prior public exposure reports
report:
  require: owner notification and redacted evidence
```

## Promotion rules

| Stage | Promote only when |
|---|---|
| Discovered | Host is in scope and query is saved. |
| Interesting | Surface and parameter are identified. |
| Matched | Indicator is observed and static samples are excluded. |
| Validated | Benign input changed something measurable. |
| Reportable | Impact is clear, evidence is redacted, and duplicates are checked. |

## Anti-patterns

- Treating a single operator match as a finding.
- Reusing someone else’s template result without rechecking scope.
- Keeping payload strings that were never needed.
- Reporting a WAF block as a vulnerability.
- Reporting a database error without checking Known Issues.
- Opening every result from a broad dork.

## Output format

Keep one row per lead in `templates/recon-tracker.md` and one section per reportable issue in `templates/report-template.md`.
