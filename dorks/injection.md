# Injection Dorks

Prefix every query with `site:TARGET` and replace `TARGET` with an in-scope domain.

These queries find **candidates**, not confirmed vulnerabilities.

## Operator policy

- Prefer Tier A: `site:`, `filetype:`, quotes, `-`, `after:`, `before:`.
- Tier B such as `inurl:` and `intext:` is useful but unofficial.
- Never use retired Tier C operators. See `dorks/operators.md`.

## XSS / reflection parameter discovery

```text
site:TARGET inurl:?q=
site:TARGET inurl:?query=
site:TARGET inurl:?search=
site:TARGET inurl:?keyword=
site:TARGET inurl:?term=
site:TARGET inurl:?s=
site:TARGET inurl:?name=
site:TARGET inurl:?message=
site:TARGET inurl:?url=
site:TARGET inurl:?redirect=
site:TARGET inurl:?next=
site:TARGET inurl:?lang=
```

## SQLi parameter discovery

```text
site:TARGET inurl:?id=
site:TARGET inurl:?ID=
site:TARGET inurl:?cat=
site:TARGET inurl:?category=
site:TARGET inurl:?page=
site:TARGET inurl:?product=
site:TARGET inurl:?item=
site:TARGET inurl:?num=
site:TARGET inurl:?newsid=
site:TARGET inurl:?user=
site:TARGET ext:php inurl:?id=
site:TARGET ext:asp inurl:?id=
```

## Error-message indicators

GHDB category: **Error Messages**.

```text
site:TARGET inurl:?id= intext:"SQL syntax"
site:TARGET inurl:?id= intext:"mysql_fetch_assoc"
site:TARGET inurl:?id= intext:"mysql_fetch_array"
site:TARGET inurl:?id= intext:"mysql_num_rows"
site:TARGET inurl:?id= intext:"Warning: mysql"
site:TARGET inurl:?id= intext:"ODBC SQL Server Driver"
site:TARGET inurl:?id= intext:"supplied argument is not a valid MySQL result resource"
```

Many programs exclude plain verbose errors. Check Known Issues before reporting.

## LFI-style parameter discovery

```text
site:TARGET inurl:?file=
site:TARGET inurl:?page=
site:TARGET inurl:?path=
site:TARGET inurl:?include=
site:TARGET inurl:?inc=
site:TARGET inurl:?lang=
site:TARGET inurl:?language=
site:TARGET inurl:?template=
site:TARGET inurl:?view=
site:TARGET inurl:?doc=
site:TARGET inurl:?download=
```

## Duplicate-heavy legacy names

These are useful for learning dork syntax but usually produce already-known targets:

```text
trainers.php?id=
buy.php?category=
article.php?id=
news.php?id=
product.php?id=
gallery.php?id=
view_product.php?id=
detail.php?ID=
readnews.php?id=
event.php?id=
```

## Validation sequence

1. Send `opencodetest123`; observe reflection.
2. Try context markers from `payloads/benign-markers.md`.
3. Check encoding, escaping, content type, and error shape.
4. Dedupe against program Known Issues and public writeups.
5. Only then consider minimal, harmless confirmation inside scope.

## Rule

A dork only finds a candidate. Never turn discovery into unauthorized access.
