# SQL Injection Discovery Dorks

SQLi dorks find **indexed URL shapes and error text**. They do not prove SQL injection. Every result is a lead that needs in-scope review, Known Issues dedupe, and minimal harmless validation.

## 1. Numeric identifier parameters

```text
site:TARGET inurl:?id=
site:TARGET inurl:?ID=
site:TARGET inurl:?pid=
site:TARGET inurl:?uid=
site:TARGET inurl:?nid=
site:TARGET inurl:?rec=
site:TARGET inurl:?num=
site:TARGET inurl:?no=
```

Why these matter: numeric IDs often map directly to database rows. A raw numeric value is normal; the risk appears only when input changes query structure or behavior.

## 2. Category and listing parameters

```text
site:TARGET inurl:?cat=
site:TARGET inurl:?category=
site:TARGET inurl:?type=
site:TARGET inurl:?group=
site:TARGET inurl:?section=
site:TARGET inurl:?topic=
site:TARGET inurl:?tag=
site:TARGET inurl:?view=
```

## 3. Commerce and search parameters

```text
site:TARGET inurl:?product=
site:TARGET inurl:?item=
site:TARGET inurl:?order=
site:TARGET inurl:?cart=
site:TARGET inurl:?checkout=
site:TARGET inurl:?search=
site:TARGET inurl:?filter=
site:TARGET inurl:?sort=
```

`order` and `sort` deserve extra care: they often feed column names or direction keywords. Treat them as allowlist candidates, not as places for crafty input.

## 4. Legacy file extensions

```text
site:TARGET ext:php inurl:?id=
site:TARGET ext:asp inurl:?id=
site:TARGET ext:aspx inurl:?id=
site:TARGET ext:jsp inurl:?id=
site:TARGET ext:cgi inurl:?id=
site:TARGET ext:pl inurl:?id=
site:TARGET ext:cfm inurl:?id=
```

Older applications are more likely to expose raw database errors. An error is still only a triage signal.

## 5. Error-text fingerprints

```text
site:TARGET inurl:?id= intext:"SQL syntax"
site:TARGET intext:"Warning: mysql"
site:TARGET intext:"You have an error in your SQL syntax"
site:TARGET intext:"Unclosed quotation mark"
site:TARGET intext:"Microsoft OLE DB Provider"
site:TARGET intext:"ORA-"
site:TARGET intext:"PSQLException"
site:TARGET intext:"PG::"
```

Full classification: `payloads/sql-error-map.md`.

## 6. Noise reducers

- Exclude documentation, blog, changelog, and support paths.
- Prefer one extension and one parameter family per query.
- Ignore results that are clearly old CMS/index fossils.
- Ignore pages where the error text is part of a tutorial, sample, or public report.
- Keep only URL, parameter name, response shape, and date observed.

## 7. Triage ladder

1. Confirm the exact host and path are in scope.
2. Record the discovery query and the parameter name only.
3. Open the result and note the baseline response.
4. Send a harmless marker such as `zzPROBE123`.
5. Compare error shape, status, and content-length.
6. Check Known Issues and public writeups for the same endpoint or root cause.
7. Stop on sensitive data, write behavior, or out-of-scope redirect.
8. Report only with clear impact and minimal redacted evidence.

## 8. Common false positives

| Lead | Why it is often noise |
|---|---|
| Verbose SQL error | Many programs treat this as a Known Issue or excluded issue. |
| `Powered by` CMS signature | Identifies technology, not a vulnerability. |
| Old indexed vulnerable URL | Page may be gone, patched, or belonging to another host now. |
| Public writeup result | Likely already reported; use it for dedupe, not as proof. |
| Error on a logged-out page | May be intentionally generic or part of a beta/debug surface. |

## 9. Defensive fix

- Use parameterized queries/prepared statements everywhere.
- Allowlist column names, sort directions, and enum-like values.
- Avoid exposing raw database errors to users.
- Run application DB accounts with least privilege.
- Log and alert on repeated malformed parameter shapes.
- Remove stale indexed backups, logs, and debug pages.
