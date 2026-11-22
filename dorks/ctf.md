# CTF Dorks

Use these only for:

- A CTF-provided challenge domain.
- Your own practice challenges.
- Public writeups and challenge archives **after** the event.

Do not use search to short-circuit a live CTF or retrieve another team's flag.

## CTF categories first

| Category | Typical clue | First tool |
|---|---|---|
| Web | A URL, param, or challenge box | Browser + `robots.txt`, source, dorks |
| OSINT / SOCMINT | Name, username, email, profile | Manual search chains |
| GEOINT | Photo, map, skyline, sign | Reverse image search, maps |
| IMINT | Provided image/file | `exiftool`, `strings`, `binwalk` |
| Threat intel | Domain, IP, certificate, IOC | CT logs, passive DNS, writeups |
| Forensics | Archive, disk, memory, logs | File carving and timeline tools |

Dorks are mainly useful for Web, OSINT, and post-event learning.

## Web challenge surface

```text
site:TARGET inurl:robots.txt
site:TARGET inurl:sitemap.xml
site:TARGET inurl:/static/
site:TARGET inurl:/assets/
site:TARGET inurl:/backup
site:TARGET inurl:/src
site:TARGET inurl:/api/
site:TARGET inurl:/admin
site:TARGET intitle:"index of" "parent directory"
site:TARGET ext:bak OR ext:zip OR ext:tar OR ext:gz
```

Common challenge patterns from public writeups include `robots.txt` hints, exposed source archives, and stale paths left in indexed results.

## OSINT challenge chains

Replace `HANDLE` with a challenge-provided identifier. Elsewhere, `CHALLENGE_DOMAIN` means the domain supplied by the challenge:

```text
"HANDLE" site:github.com
"HANDLE" site:twitter.com OR site:x.com
"HANDLE" site:reddit.com
"HANDLE" site:linkedin.com
"HANDLE" site:pastebin.com
"HANDLE" filetype:pdf
"HANDLE" intitle:"index of"
"HANDLE" intext:"contact"
```

For a challenge-provided exact phrase:

```text
site:TARGET "PHRASE FROM CHALLENGE"
site:TARGET intext:"PHRASE FROM CHALLENGE"
site:TARGET filetype:txt "PHRASE FROM CHALLENGE"
```

## Wayback / stale-content leads

Google is weaker here than the Wayback Machine, but these can still reveal indexed copies:

```text
site:web.archive.org "CHALLENGE_DOMAIN"
site:TARGET "old version"
site:TARGET inurl:/old/
site:TARGET inurl:/v1/
site:TARGET inurl:/archive/
```

Then verify with the Wayback CDX API if the challenge rules allow it.

## Post-event writeup learning

```text
site:ctftime.org/writeup "robots.txt" CTF
site:ctftime.org/writeup "osint" CTF
site:ctftime.org/writeup "google dork" CTF
site:ctftime.org/writeup "flag{" CTF
site:github.com/google/google-ctf "flag"
site:github.com "CTF{" "writeup"
```

Use these to learn methodology, not to copy flags into a live scoreboard.

## Challenge triage checklist

1. Identify category before choosing a tool.
2. Add only 2–4 operators; more usually over-filters.
3. Record URL, phrase, and why it matched.
4. Check whether the path is still live.
5. Do not brute-force all paths.
6. If a hint is found, pivot manually to the next clue.
7. For writeups, cite the source URL in your notes.

## Sources

- `https://ctftime.org/writeups`
- `https://github.com/google/google-ctf`
- `https://hackerdna.com/blog/google-dorking`
- `https://ctftime.org/writeup/29295`
