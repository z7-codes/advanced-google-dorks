# Injection Dorks

Prefix every query with `site:TARGET` and replace `TARGET` with an in-scope domain.

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
```

## SQL error indicators
```text
site:TARGET inurl:?id= intext:"SQL syntax"
site:TARGET inurl:?id= intext:"mysql_fetch_assoc"
site:TARGET inurl:?id= intext:"mysql_fetch_array"
site:TARGET inurl:?id= intext:"mysql_num_rows"
site:TARGET inurl:?id= intext:"Warning: mysql"
site:TARGET inurl:?id= intext:"ODBC SQL Server Driver"
site:TARGET inurl:?id= intext:"supplied argument is not a valid MySQL result resource"
```

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
These appear in old dork lists. They are useful for learning dork syntax but usually produce already-known targets:
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

## Rule
A dork only finds a **candidate**. Confirm with benign markers first: `payloads/benign-markers.md`.
