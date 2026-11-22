# Benign Validation Markers

Use these before any exploit-style input. Goal: see where input lands and whether it is encoded, escaped, reflected, or rejected.

## Validation ladder

1. Plain marker: check reflection and storage.
2. HTML marker: check raw vs encoded output.
3. Attribute/context marker: check where the value lands.
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
"><b>zzPROBE123</b>
'"><b>zzPROBE123</b>
```

## Template / expression markers

```text
{{zzPROBE123}}
${zzPROBE123}
#{zzPROBE123}
```

## SQL error-shape markers

```text
'
''
zzPROBE123'
zzPROBE123"
1' AND '1'='1
1' AND '1'='2
```

Many programs treat plain verbose SQL errors as Known Issues or out of scope. Dedupe before deeper testing.

## Interpretation

- Marker visible raw in HTML source -> reflection lead; check encoding/context.
- Marker visible inside an HTML tag/attribute -> potential injection lead.
- SQL error or behavior difference -> potential injection lead; dedupe before deeper tests.
- No reflection/error -> likely not useful.

## Never start with

- Cookie-stealing JavaScript.
- Database time-delay or heavy blind-injection payloads.
- Mass data-dump tautologies.
- Anything touching another user's account or data.
