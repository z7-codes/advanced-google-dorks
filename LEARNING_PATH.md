# Learning Path — Beginner to Advanced

Goal: go from "I know a few dorks" to "I can build a repeatable, scoped, deduped recon workflow".

## 4-week path

| Level | Days | Focus | Files | Checkpoint |
|---|---|---|---|---|
| Beginner | 1–3 | Operators, scope, root causes, safe searches | `dorks/operators.md`, `VULNERABILITY_FUNDAMENTALS.md`, `dorks/beginner.md` | Build 20 scoped queries and explain one vulnerability root cause. |
| Intermediate | 4–7 | Chaining, noise reduction, date windows, operator-free discovery | `dorks/intermediate.md`, `dorks/manual-discovery.md` | Produce a recon tracker with 30 leads and dedupe notes. |
| Validation | 8–10 | Benign probes, context mapping, stop rules | `payloads/context-probes.md`, `workflows/methodology.md` | Explain why a lead is or is not worth reporting. |
| CTF bridge | 11–14 | Web/OSINT challenge chains | `dorks/ctf.md`, `examples/sanitized-walkthroughs.md` | Solve one practice challenge and write a sanitized walkthrough. |
| Advanced | 15–21 | Index fossils, differential queries, stale surfaces | `dorks/advanced.md` | Build 5 multi-step query chains with documented reasoning. |
| Defensive | 22–28 | Blue-team audit and remediation | `workflows/defensive-audit.md`, `payloads/detection-notes.md` | Run an owned-asset audit and write a remediation checklist. |

## Daily loop

```text
1. Pick one scoped target.
2. Write 5 queries using only Tier A/B operators.
3. Save URL + query + observation in templates/recon-tracker.md.
4. Dedupe with Known Issues and public search.
5. Validate only with benign probes.
6. Write one paragraph: keep, discard, or need more context.
```

## Skill gates

### Gate 1 — Beginner

- No space after operator colon.
- Every target query starts with `site:TARGET`.
- Can explain `site:`, `filetype:`, quotes, `-`, and `OR`.
- Can describe the four-part vulnerability model: input, assumption, sink, control.

### Gate 2 — Intermediate

- Can combine 3–4 operators without over-filtering.
- Can use `after:` / `before:` for stale vs recent indexed pages.
- Can remove blog/news/support noise.
- Can verify scope before converting an operator-free lead into a `site:TARGET` query.

### Gate 3 — Validation

- Starts with `zzPROBE123`, not exploit payloads.
- Understands HTML body, attribute, URL, JSON, and error-shape contexts.
- Stops on sensitive data, real user data, or unclear authorization.

### Gate 4 — Advanced

- Builds query chains, not memorized one-liners.
- Uses differential queries to compare surfaces.
- Treats search output as leads and verifies manually.
- Documents dedupe before deeper testing.

### Gate 5 — Defensive

- Can turn a finding into a fix and recheck.
- Redacts sensitive evidence.
- Knows when a result is a Known Issue, not a bounty.

## Recommended order

```text
README.md
  -> dorks/operators.md
  -> VULNERABILITY_FUNDAMENTALS.md
  -> dorks/beginner.md
  -> dorks/intermediate.md
  -> dorks/manual-discovery.md
  -> payloads/context-probes.md
  -> dorks/sqli.md
  -> dorks/xss.md
  -> dorks/advanced.md
  -> dorks/ctf.md
  -> workflows/quality-bar.md
  -> examples/sanitized-walkthroughs.md
  -> templates/recon-tracker.md
  -> workflows/defensive-audit.md
```

## Companion tool

After Gate 2, use [ScopeForge](https://github.com/z7-codes/scopeforge) to practice the same workflow as a local CLI: validate scope, generate scoped plans, record leads, analyze evidence, and draft redacted reports.

```bash
python -m pip install git+https://github.com/z7-codes/scopeforge.git
scopeforge lab localhost
scopeforge plan main --category recon --limit 20
```

## Rule

Advanced means **more precise and better documented**, not more harmful. Keep every query scoped, manual, and reversible.
