# Methodology

## 1. Scope

- Confirm the asset is owned/controlled by the program.
- Read the policy, Known Issues, and recent duplicates.
- Use only test accounts or accounts you are authorized to use.
- Stop if the target is not explicitly in scope.

## 2. Dork

- Start with category files in `dorks/`.
- For operator-free leads, confirm scope first with `dorks/manual-discovery.md`, then convert to a scoped query.
- Replace `TARGET` with the in-scope domain.
- Prefer Tier A operators from `dorks/operators.md`.
- Save only URL, parameter name, and observed behavior.
- Do not store sensitive content from search results.

## 3. Triage

- Is it in scope?
- Is it already in Known Issues?
- Is the parameter authenticated or public?
- Is there a public writeup with the same root cause?
- Is the finding merely a verbose error, missing header, or directory listing?

## 4. Benign validation

- Send `zzPROBE123` first.
- Observe reflection, encoding, error shape, and content-type.
- Follow the ladder in `payloads/benign-markers.md`.
- Only then consider targeted, harmless confirmation.

## 5. Dedupe

Search the program and public web. `PROGRAM` means the program handle; `VULN_CLASS` means a short issue class such as XSS or SQLi.

```text
program:PROGRAM PARAMETER
program:PROGRAM ENDPOINT impact
"VULN_CLASS" "TARGET" bug bounty
site:ctftime.org "TARGET" "VULN_CLASS"
site:github.com "TARGET" "VULN_CLASS" writeup
```

## 6. Report

Include:

- Descriptive title.
- In-scope target.
- Step-by-step reproduction.
- Minimal PoC.
- Clear impact statement.
- Known Issues check.
- Duplicate search notes.
- Timestamp and environment details.

## Evidence template

```text
Title:
Asset:
Scope source:
Query used:
URL/endpoint:
Parameter:
Observed behavior:
Minimal PoC:
Impact:
Known Issues checked:
Duplicate links:
Timestamp:
```

## Stop conditions

- Sensitive data found.
- Real user account involved.
- Rate-limit/security block appears.
- Behavior becomes destructive or unclear.
- Authorization status changes.
