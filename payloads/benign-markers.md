# Benign Validation Markers

Use these for context classification only. Do not escalate to exploit-style input.

## Validation ladder

1. Plain marker: check reflection and storage.
2. HTML marker: check raw vs encoded output.
3. Attribute marker: check where the value lands.
4. Error-shape marker: check behavior difference only.
5. Stop if the result is destructive, sensitive, or out of scope.

## Reflection markers

```text
zzPROBE123
zzBENIGNzz
```

## HTML context markers

```text
<b>zzPROBE123</b>
<i>zzPROBE123</i>
```

Do not add boundary-break strings here. If a marker appears inside markup, record the context and stop.

## SQL error-shape markers

```text
'
''
zzPROBE123'
zzPROBE123"
```

Many programs treat plain verbose SQL errors as Known Issues or out of scope. Dedupe before deeper testing. Do not use boolean tradeoff strings, time-delay strings, or data-dump strings here.

## Interpretation

- Marker visible raw in HTML source -> reflection lead; check encoding/context.
- Marker visible inside an HTML tag or attribute -> potential injection lead; record and stop.
- SQL error or behavior difference -> potential injection lead; dedupe before deeper tests.
- No reflection or error -> likely not useful.

## Never use in this repo

- Cookie or session theft strings.
- Database time-delay or blind-injection payloads.
- Boolean tradeoff or mass data-dump strings.
- Template or expression evaluation probes.
- Anything touching another user's account or data.
