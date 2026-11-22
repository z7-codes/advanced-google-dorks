# Benign Validation Markers

Use these before any exploit-style input. Goal: see where input lands and whether it is encoded, escaped, reflected, or rejected.

## Reflection markers
```text
opencodetest123
zzBENIGNzz
```

## HTML context markers
```text
<b>opencodetest123</b>
<i>opencodetest123</i>
"><b>opencodetest123</b>
'"><b>opencodetest123</b>
```

## Template / expression markers
```text
{{opencodetest123}}
${opencodetest123}
#{opencodetest123}
```

## SQL error-shape markers
```text
'
''
opencodetest123'
opencodetest123"
1' AND '1'='1
1' AND '1'='2
```

## Interpretation
- Marker visible raw in HTML source -> reflection lead; check encoding/context.
- Marker visible inside an HTML tag/attribute -> potential injection lead.
- SQL error or behavior difference -> potential injection lead; dedupe before deeper tests.
- No reflection/error -> likely not useful.

## Never start with
- Cookie-stealing JavaScript.
- `SLEEP()` / heavy time-based payloads.
- Mass data-dump tautologies.
- Anything touching another user's account or data.
