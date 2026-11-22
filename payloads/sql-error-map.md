# SQL Error Shape Map

Use this file to **classify error text**, not to extract data or prove exploitability. Error strings are triage signals; many programs list them as Known Issues.

## Family map

| Family | Indexed indicators | What it suggests | Guardrail |
|---|---|---|---|
| MySQL / MariaDB | `Warning: mysql`, `You have an error in your SQL syntax` | Query reached a MySQL-compatible parser. | Often excluded as verbose error; dedupe first. |
| MSSQL | `Microsoft OLE DB Provider`, `Unclosed quotation mark` | SQL Server error path exposed. | Do not access other databases or linked servers. |
| Oracle | `ORA-` sequence in response text | Oracle error surfaced. | Error code alone is not impact. |
| PostgreSQL | `PSQLException`, `PG::` | PostgreSQL driver/library error. | Avoid library-version rabbit holes. |
| SQLite | `SQLiteException`, `near "...": syntax error` | SQLite parser error. | Usually low impact without a data boundary. |
| Generic framework | `Stack trace`, `SQLException`, `database error` | Application leaked internal detail. | Check program policy before reporting. |

## Scoped lookup dorks

```text
site:TARGET intext:"Warning: mysql"
site:TARGET intext:"You have an error in your SQL syntax"
site:TARGET intext:"Unclosed quotation mark"
site:TARGET intext:"Microsoft OLE DB Provider"
site:TARGET intext:"ORA-"
site:TARGET intext:"PSQLException"
site:TARGET intext:"SQLiteException"
site:TARGET intext:"Stack trace" inurl:?id=
```

## Reading an error lead

1. Record the exact error family, endpoint, and parameter name.
2. Compare with a normal request to the same endpoint.
3. Check whether the text is static documentation or a live response.
4. Check Known Issues and public writeups.
5. Note whether any data, schema, or file path is exposed.
6. Stop immediately if sensitive rows or credentials appear.

## What not to store

- Database names, table names, or column names beyond what is needed for a redacted proof.
- Any real user record.
- Password hashes, tokens, keys, or connection strings.
- Full stack traces when a short redacted excerpt is enough.

## Defensive view

- Return generic error pages to users.
- Log detailed errors server-side with a correlation ID.
- Parameterize queries and allowlist identifier-like input.
- Keep DB accounts least-privileged and segmented.
- Remove debug endpoints and indexed log files.
