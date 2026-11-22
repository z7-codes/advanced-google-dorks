# Contributing

Maintained by `z7-codes`. Pull requests are welcome.

## Good contributions

- New scoped query categories.
- Better beginner/intermediate/advanced exercises.
- Better noise reducers using documented operators.
- Corrections to operator reliability status.
- Context-aware benign payload probes.
- Sanitized examples and reusable templates.
- CTF methodology notes that are useful after an event.
- Defensive exposure-audit patterns.
- Generator templates that stay local-only.

## Requirements

- Every target-specific query must use `site:TARGET`.
- Do not add retired Tier C operators.
- Do not add exploit chains, credential attacks, or mass-scanning guidance.
- Do not include real secrets, real user data, or URLs from unauthorized tests.
- Prefer "lead" language over "vulnerability confirmed".
- Add a source URL when the pattern comes from public research.
- Run `python scripts/check_dorks.py` before opening a PR.
- Run `python -m py_compile scripts/*.py` when changing Python files.

## Suggested PR description

```text
Category:
What changed:
Source URL:
Why it is scoped and safe:
Checks run:
```

Keep contributions legal, non-destructive, and beginner-reviewable.
