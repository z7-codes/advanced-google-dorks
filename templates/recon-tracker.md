# Recon Tracker

Copy this table into your notes. Keep entries short and redacted.

## Lead log

| # | Date | Query | URL/Endpoint | Parameter | Observation | Scope? | Known Issue? | Next |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | yes/no | yes/no | keep/discard/validate |

## Query log

| # | Level | Query | Results count | Filters added | Reason |
|---|---|---|---|---|---|
| 1 | beginner | `site:TARGET` | | | baseline |
| 2 | intermediate | `site:TARGET filetype:pdf` | | | document sweep |

## Dedupe log

| # | Lead | Search term | Duplicate URL | Decision |
|---|---|---|---|---|
| 1 | | | | duplicate / unique / unclear |

## Probe log

| # | Lead | Context | Probe | Response snippet | Decision |
|---|---|---|---|---|---|
| 1 | | HTML body | `opencodetest123` | | reflected / encoded / none |

## Status legend

```text
keep      worth further scoped validation
discard   duplicate, out of scope, or already known
validate  needs benign probe
blocked   missing authorization or account
stop      sensitive data / destructive behavior
```
