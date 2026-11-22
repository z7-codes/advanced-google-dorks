# Defensive Exposure Audit

Use this when auditing assets you own or are explicitly authorized to audit.

## 1. Inventory

```text
site:TARGET
site:TARGET -www
site:TARGET inurl:dev OR inurl:staging OR inurl:test
site:TARGET inurl:/api/
site:TARGET inurl:/admin
site:TARGET inurl:/docs OR inurl:/swagger
```

Save only:

- URL
- Asset owner if known
- Discovery query
- Date observed

## 2. Exposure sweep

```text
site:TARGET intitle:"index of"
site:TARGET filetype:env
site:TARGET filetype:sql
site:TARGET filetype:log
site:TARGET filetype:bak OR filetype:old
site:TARGET filetype:pdf intext:"confidential"
site:TARGET intext:"BEGIN PRIVATE KEY"
```

For real secrets or personal data:

1. Stop opening further results.
2. Do not copy values.
3. Record only redacted proof.
4. Notify the owner through the official channel.
5. Fix, re-index check, and document.

## 3. Duplicate control

```text
"TARGET" "filetype:env" exposure
"TARGET" "index of" bug bounty
"TARGET" "Nessus Scan Report"
"TARGET" "BEGIN PRIVATE KEY"
```

Public known exposure may already be a Known Issue; confirm before treating it as new.

## 4. Remediation

- Remove the public file, do not merely rename it.
- Revoke exposed credentials immediately.
- Add cache purging/CDN invalidation where relevant.
- Block directory listing at the server.
- Add CI secret scanning to prevent recurrence.
- Re-run the same saved query after the fix.

## 5. Evidence template

```text
Title: Publicly indexed [file type] on [asset]
Asset: [in-scope domain]
Query: [scoped query]
URL: [redacted if sensitive]
Observed: [redacted description]
Risk: [what an unauthorized party could infer/access]
Known Issues checked: yes/no
Fix verified: yes/no
```
