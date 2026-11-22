# Research Sources

Research date: `2026-11-21`.

This repo does not copy any database verbatim. It uses public research to structure original, scoped, defensive query patterns.

| # | Source | URL | Used for | Notes |
|---|---|---|---|---|
| 1 | Exploit-DB About | `https://www.exploit-db.com/about` | GHDB definition, maintenance, categories | GHDB is an OffSec-maintained, categorized index of search queries; popularized by Johnny Long. |
| 2 | Exploit-DB GHDB | `https://www.exploit-db.com/google-hacking-database` | Category names and concept | Direct fetch timed out during research; category names were confirmed from indexed snippets and secondary sources. |
| 3 | Google Search Help — Refine Google searches | `https://support.google.com/websearch/answer/2466433?hl=en` | Officially documented operators | Documents quotes, `-`, `site:`, `filetype:`, `before:`, `after:`. Explicitly says no space after the colon. |
| 4 | Google Search Central — site: operator | `https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site` | `site:` limitations | A `site:` result set is not exhaustive; use Search Console for accurate index counts. |
| 5 | Google Search Central — operator overview | `https://developers.google.com/search/docs/monitor-debug/search-operators` | Documented search/debug operators | Also documents image-only `imagesize:` and `src:`. |
| 6 | InfosecMonkey practitioner guide | `https://infosecmonkey.com/google-dorking-a-practitioners-guide-to-advanced-search-reconnaissance` | Practical recon categories | Confirms `site:`, `filetype:`, `intitle:`, `allintitle:`, `inurl:`, `allinurl:`, `intext:`; notes multiple operators act as AND and `all...` consumes other terms. |
| 7 | Heystacks operator reference | `https://heystacks.com/doc/487/google-advanced-search-operators` | `allintext:` / `allintitle:` behavior | Useful secondary reference for all-prefixed operators. |
| 8 | Ahrefs complete operator list | `https://ahrefs.com/blog/google-advanced-search-operators` | Working / unreliable / retired classification | Separates working, unreliable, and officially deprecated operators. |
| 9 | Rheinwunder operator list | `https://rheinwunder.com/en/knowledge/google-search-operators` | Active vs discontinued operators | States Google help covers only a short list; other operators can change without notice. |
| 10 | HackerDNA Google dorking guide | `https://hackerdna.com/blog/google-dorking` | CTF + bug bounty recon workflow | Confirms dorking is passive recon; lists OSINT and web-challenge use cases. |
| 11 | CTFtime writeups | `https://ctftime.org/writeups` | CTF learning sources | Use after events for learning, not to shortcut live challenges. |
| 12 | Google CTF public archive | `https://github.com/google/google-ctf` | Public challenge sources | Use for post-event study and challenge design patterns. |
| 13 | scriptCTF 2026 writeup | `https://cyb3r-bo1.github.io/posts/scriptCTF_2026_writeup` | Web/OSINT challenge patterns | Example: `robots.txt` enumeration and Geo-OSINT chaining. |
| 14 | Maltego Community OSINT CTF 2026 writeup | `https://medium.com/@Fr1cTioN/maltego-community-osint-ctf-2026-writeup-osint-using-news-and-reverse-image-search-google-lens-e9688ab13426` | OSINT category mapping | Shows GEOINT, IMINT, SOMINT, and cyber-threat-intel chains. |
| 15 | CTFtime — I Love Google writeup | `https://ctftime.org/writeup/29295` | Classic Google/OSINT challenge | Demonstrates search-chain thinking rather than memorized dorks. |
| 16 | External reference notes | `research/external-references.md` | SQLi/XSS source review, nuclei structure, OWASP context rules | Second-pass review; direct PDF/deck fetches were blocked, so only indexed outlines and safe defensive lessons were used. |

## Key conclusions

- Keep `site:TARGET` on every target-specific query.
- Prefer Tier A operators when precision matters.
- Treat Tier B operators as useful but unstable.
- Avoid retired operators entirely.
- Search results are leads, never proof of a vulnerability.
- Source material is reduced to method, context, and defense — never copied payloads or exploit chains.
- Google sees only indexed content; absence from search does not mean absence from the target.
- Automated bulk querying can violate Google rules; keep this repo manual and local-only.
