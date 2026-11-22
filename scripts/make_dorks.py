import json
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
        "site:{target} inurl:?lang=",
        "site:{target} intext:\"search\" inurl:?q=",
        "site:{target} inurl:?s=",
        "site:{target} inurl:?text=",
        "site:{target} inurl:?redirect=",
        "site:{target} ext:php inurl:?q=",
        "site:{target} inurl:?view= intext:\"error\"",
    ],
    "sqli": [
        "site:{target} inurl:?id=",
        "site:{target} inurl:?ID=",
        "site:{target} inurl:?cat=",
        "site:{target} inurl:?category=",
        "site:{target} inurl:?page=",
        "site:{target} inurl:?product=",
        "site:{target} ext:php inurl:?id=",
        "site:{target} ext:asp inurl:?id=",
        "site:{target} inurl:?id= intext:\"SQL syntax\"",
        "site:{target} inurl:?id= intext:\"Warning: mysql\"",
        "site:{target} inurl:?pid=",
        "site:{target} inurl:?cat=",
        "site:{target} inurl:?order=",
        "site:{target} ext:aspx inurl:?id=",
        "site:{target} intext:\"Unclosed quotation mark\"",
        "site:{target} intext:\"Microsoft OLE DB Provider\"",
    ],
    "lfi": [
        "site:{target} inurl:?file=",
        "site:{target} inurl:?page=",
        "site:{target} inurl:?path=",
        "site:{target} inurl:?include=",
        "site:{target} inurl:?inc=",
        "site:{target} inurl:?lang=",
        "site:{target} inurl:?language=",
        "site:{target} inurl:?template=",
        "site:{target} inurl:?download=",
    ],
    "recon": [
        "site:{target}",
        "site:{target} -www",
        "site:{target} inurl:dev",
        "site:{target} inurl:staging",
        "site:{target} inurl:test",
        "site:{target} inurl:api",
        "site:{target} inurl:/graphql",
        "site:{target} inurl:/swagger",
        "site:{target} intitle:\"login\"",
        "site:{target} ext:json",
        "site:{target} inurl:robots.txt",
        "site:{target} filetype:pdf",
    ],
    "exposure": [
        "site:{target} intitle:\"index of\"",
        "site:{target} ext:bak",
        "site:{target} ext:old",
        "site:{target} ext:zip",
        "site:{target} ext:sql",
        "site:{target} ext:env",
        "site:{target} ext:conf",
        "site:{target} filetype:env intext:\"api_key\"",
        "site:{target} filetype:log intext:\"password\"",
        "site:{target} filetype:pdf intext:\"confidential\"",
        "site:{target} filetype:pdf \"Nessus Scan Report\"",
        "site:{target} intext:\"internal use only\"",
    ],
    "ctf": [
        "site:{target} inurl:robots.txt",
        "site:{target} inurl:sitemap.xml",
        "site:{target} inurl:/static/",
        "site:{target} inurl:/assets/",
        "site:{target} inurl:/backup",
        "site:{target} inurl:/src",
        "site:{target} inurl:/api/",
        "site:{target} intitle:\"index of\" \"parent directory\"",
        "site:{target} ext:bak OR ext:zip OR ext:tar",
        "site:{target} filetype:txt intext:\"flag\"",
    ],
    "ghdb": [
        "site:{target} intitle:\"index of\"",
        "site:{target} ext:env",
        "site:{target} ext:sql",
        "site:{target} ext:bak",
        "site:{target} intitle:\"login\"",
        "site:{target} inurl:admin",
        "site:{target} intext:\"Powered by\"",
        "site:{target} intext:\"SQL syntax\"",
        "site:{target} filetype:pdf intext:\"confidential\"",
        "site:{target} filetype:csv intext:\"username\"",
        "site:{target} inurl:/backup/",
        "site:{target} inurl:/old/",
    ],
    "beginner": [
        "site:{target}",
        "site:{target} -site:{target}/blog",
        "site:{target} filetype:pdf",
        "site:{target} inurl:robots.txt",
        "site:{target} \"confidential\"",
        "site:{target} \"internal use only\"",
        "site:{target} intitle:\"index of\"",
        "site:{target} login OR signin",
        "site:{target} filetype:pdf after:2024-01-01",
    ],
    "intermediate": [
        "site:{target} inurl:dev -site:{target}/blog -site:{target}/news",
        "site:{target} inurl:/api/ -inurl:/docs -inurl:/status",
        "site:{target} intitle:\"login\" -inurl:help -inurl:support",
        "site:{target} inurl:/v1/ OR inurl:/v2/ OR inurl:/legacy/",
        "site:{target} filetype:env intext:\"api_key\"",
        "site:{target} filetype:log intext:\"password\"",
        "site:{target} inurl:?q= -site:{target}/blog",
        "site:{target} intext:\"Powered by\" after:2024-01-01",
    ],
    "advanced": [
        "site:{target}/api/",
        "site:{target}/legacy/",
        "site:{target} inurl:/old/ OR inurl:/archive/ OR inurl:/backup/",
        "site:{target} inurl:/api/ -inurl:/docs after:2025-01-01",
        "site:{target} filetype:env intext:\"api_key\" -inurl:public",
        "site:{target} \"BEGIN PRIVATE KEY\" -inurl:docs",
        "site:{target} intext:\"Stack trace\" filetype:txt",
        "site:{target} intitle:\"dashboard\" -site:{target}/blog",
        "site:{target} inurl:/router/ OR inurl:/camera/ OR inurl:/printer/",
    ],
}


def usage():
    print("usage: python make_dorks.py TARGET CATEGORY [CATEGORY ...] [--json]")
    print("       python make_dorks.py TARGET all [--json]")
    print("       python make_dorks.py --list")
    print("categories: " + ", ".join(sorted(TEMPLATES)))


def selected_categories(names):
    if names == ["all"]:
        return sorted(TEMPLATES)
    unknown = [name for name in names if name not in TEMPLATES]
    if unknown:
        print("unknown category: " + ", ".join(unknown))
        raise SystemExit(1)
    return names


def build_rows(target, names):
    rows = []
    for name in selected_categories(names):
        rows.append(
            {
                "category": name,
                "queries": [template.format(target=target) for template in TEMPLATES[name]],
            }
        )
    return rows


def main():
    args = sys.argv[1:]

    if not args:
        usage()
        raise SystemExit(1)

    if "--help" in args or "-h" in args:
        usage()
        return

    if "--list" in args:
        for name in sorted(TEMPLATES):
            print(name + ": " + str(len(TEMPLATES[name])) + " queries")
        return

    as_json = "--json" in args
    positional = [arg for arg in args if arg != "--json"]

    if len(positional) < 2:
        usage()
        raise SystemExit(1)

    target = positional[0]
    rows = build_rows(target, positional[1:])

    if as_json:
        print(json.dumps({"target": target, "results": rows}, indent=2))
        return

    for row in rows:
        print("# " + row["category"])
        for query in row["queries"]:
            print(query)
        print()


if __name__ == "__main__":
    main()
