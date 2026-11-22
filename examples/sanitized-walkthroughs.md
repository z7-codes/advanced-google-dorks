# Sanitized Walkthroughs

All targets below are fictional. These show reasoning, not real findings.

## Case 1 — Public document

```text
Query: site:target.example filetype:pdf "internal use only"
Result: /docs/2025/vendor-pricing.pdf
```

Observation:

- PDF is indexed and publicly reachable.
- Title and first page snippet contain the phrase.
- No credentials or personal data visible in the snippet.

Decision:

- Checked Known Issues: similar exposure already listed.
- Discarded as duplicate.
- Saved query and duplicate link in tracker.

Lesson: exposure does not equal reportable if already known.

## Case 2 — Reflected search parameter

```text
Query: site:lab.example inurl:?q=
Probe: zzPROBE123
```

Observation:

- Marker reflected in HTML body.
- `<b>zzPROBE123</b>` returned escaped as `&lt;b&gt;...`.
- Attribute probes did not change context.

Decision:

- No injection lead.
- Recorded as sanitized/encoded.
- Did not escalate.

Lesson: reflection alone is not XSS.

## Case 3 — Directory listing

```text
Query: site:target.example intitle:"index of" "parent directory"
Result: /uploads/legacy/
```

Observation:

- Directory listing enabled.
- Only old public images, no sensitive files.
- Search snippet dated several years old.

Decision:

- Checked Known Issues: directory listing excluded.
- Discarded.

Lesson: many programs exclude plain directory listings.

## Case 4 — CTF robots hint

```text
Query: site:ctf.example inurl:robots.txt
Result: /robots.txt contains Disallow: /secret-panel/
```

Observation:

- Path is inside the challenge domain.
- `/secret-panel/` returns a challenge page.
- Source contains a benign encoded clue.

Decision:

- Followed challenge-provided scope.
- Documented chain: dork -> robots -> source -> clue.
- No traffic sent outside the CTF domain.

Lesson: dorks are often hint-finders, not exploit tools.

## Case 5 — Stale API path

```text
Query: site:target.example inurl:/v1/ -inurl:/docs after:2025-01-01
Result: /api/v1/legacy/search
```

Observation:

- Indexed page mentions a legacy endpoint.
- Live request returns a standard 404.
- No parameters reflected.

Decision:

- Marked as stale index fossil.
- No report.

Lesson: indexed does not mean live.
