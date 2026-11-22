import sys

TEMPLATES = {
    "xss": [
        "site:{target} inurl:?q=",
        "site:{target} inurl:?query=",
        "site:{target} inurl:?search=",
        "site:{target} inurl:?keyword=",
        "site:{target} inurl:?term=",
        "site:{target} inurl:?url=",
        "site:{target} inurl:?redirect=",
        "site:{target} inurl:?next=",
    ],
    "sqli": [
        "site:{target} inurl:?id=",
        "site:{target} inurl:?ID=",
        "site:{target} inurl:?cat=",
        "site:{target} inurl:?category=",
        "site:{target} inurl:?page=",
        "site:{target} ext:php inurl:?id=",
        "site:{target} inurl:?id= intext:\"SQL syntax\"",
        "site:{target} inurl:?id= intext:\"Warning: mysql\"",
    ],
    "lfi": [
        "site:{target} inurl:?file=",
        "site:{target} inurl:?page=",
        "site:{target} inurl:?path=",
        "site:{target} inurl:?include=",
        "site:{target} inurl:?lang=",
        "site:{target} inurl:?template=",
        "site:{target} inurl:?view=",
    ],
    "recon": [
        "site:{target} inurl:dev",
        "site:{target} inurl:staging",
        "site:{target} inurl:api",
        "site:{target} inurl:/graphql",
        "site:{target} inurl:/swagger",
        "site:{target} ext:json",
        "site:{target} inurl:robots.txt",
    ],
}

if len(sys.argv) != 3:
    print("usage: python make_dorks.py TARGET CATEGORY")
    print("categories: " + ", ".join(sorted(TEMPLATES)))
    raise SystemExit(1)

target = sys.argv[1]
category = sys.argv[2].lower()

if category not in TEMPLATES:
    print("unknown category: " + category)
    raise SystemExit(1)

for template in TEMPLATES[category]:
    print(template.format(target=target))
