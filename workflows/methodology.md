# Methodology

## 1. Scope
- Confirm the asset is owned/controlled by the program.
- Read Known Issues and duplicates before testing.
- Use only test accounts or accounts you are authorized to use.

## 2. Dork
- Start with category files in `dorks/`.
- Replace `TARGET` with the in-scope domain.
- Save only URL, parameter name, and observed behavior.

## 3. Triage
- Is it in scope?
- Is it already in Known Issues?
- Is the parameter authenticated or public?
- Is there a public writeup with the same root cause?

## 4. Benign validation
- Send `opencodetest123` first.
- Observe reflection, encoding, error shape, and content-type.
- Only then consider targeted, harmless confirmation.

## 5. Dedupe
Search the program and public web:
```text
program:PROGRAM PARAMETER
program:PROGRAM ENDPOINT impact
"VULN_CLASS" "TARGET" bug bounty
```

## 6. Report
Include:
- Descriptive title.
- In-scope target.
- Step-by-step reproduction.
- Minimal PoC.
- Impact statement.
- Known Issues check.
- Duplicate search notes.

## Stop conditions
- Sensitive data found.
- Real user account involved.
- Rate-limit/security block appears.
- Behavior becomes destructive or unclear.
