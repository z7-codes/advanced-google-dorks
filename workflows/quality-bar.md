# Lead Quality Bar

This repo borrows the discipline of template-driven scanners, not their exploit payloads. Every saved lead should be readable, reproducible, and safe to hand to another researcher.

## Required fields

```text
id: FAMILY-0001
name: short descriptive lead name
scope: exact in-scope host or wildcard
discovery: saved query that found the surface
indicator: what made it interesting
exclusion: why similar results are not this lead
context: where input lands
validation: benign marker + baseline comparison
stop_rule: condition that ends testing
evidence: redacted request/response snippet
impact: clear statement of what changes for an attacker
dedupe: Known Issues and public writeup notes
references: source or observation link
```

## Quality rules

1. One lead per file or tracker row.
2. Use a stable ID so follow-up notes stay attached.
3. Name the exact host, path, and parameter family.
4. Include at least one discriminator beyond “looks interesting”.
5. Include at least one explicit exclusion for common noise.
6. Record the landing context before choosing a probe.
7. Validate with one benign marker at a time.
8. Keep a baseline response for comparison.
9. Dedupe before deeper testing.
10. Stop on sensitive data, write behavior, real users, or scope changes.

## Matcher discipline

A good lead has layers:

```text
layer 1  discovery: scoped search query
layer 2  surface: endpoint + parameter family
layer 3  indicator: error text, reflection context, or behavior change
layer 4  exclusion: docs, blog, known issue, static sample
layer 5  validation: benign marker + baseline diff
layer 6  evidence: minimal redacted proof
```

Do not promote a lead on layer 1 alone. Search results are leads, never proof.

## Review checklist

- Is the target explicitly in scope?
- Is the query reproducible without hidden automation?
- Is the exclusion list honest?
- Was only harmless input used?
- Is the impact specific, not “possible vulnerability”?
- Is the evidence redacted?
- Are Known Issues checked?
- Would a triager understand this without asking basic questions?

## Reject if

- The only finding is a missing header, verbose error, banner, or technology signature.
- The report depends on scanning noise or a copied public list.
- The proof exposes real user data.
- The lead needs exploitation beyond written authorization.
- The impact cannot be stated in one clear sentence.
