# Payload Index

This folder contains **benign validation probes**, not exploit chains.

Use them only on:

- Assets you own.
- Written-authorized targets.
- Labs and CTFs.

## Files

| File | Purpose |
|---|---|
| `benign-markers.md` | Basic reflection and error-shape markers. |
| `context-probes.md` | Context-aware probes for HTML, attribute, URL, JSON, and header contexts. |
| `detection-notes.md` | Blue-team notes for spotting dork-driven exposure probes. |

## Safety ladder

```text
plain marker -> HTML marker -> attribute marker -> error-shape marker -> stop
```

## Never included here

- Cookie/session-stealing JavaScript.
- SQL data-dump payloads.
- Time-based blind injection payloads.
- SSRF/XXE/RCE chains.
- Credential attacks or real-user data.
- Payloads that exfiltrate or destroy anything.

## Rule

If a probe causes sensitive output, an account change, or any destructive behavior: stop immediately and report through the official channel.
