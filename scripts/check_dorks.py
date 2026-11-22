import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
check_dirs = ["dorks", "payloads", "examples", "templates"]
skip_files = {"dorks/operators.md", "payloads/README.md"}
retired = re.compile(r"\b(?:cache|related|link|info|inanchor|allinanchor):", re.I)
space_after_colon = re.compile(r"\b(?:site|filetype|ext|intitle|inurl|intext|allintitle|allinurl|allintext):\s+", re.I)
scoped = re.compile(r"site:(?:https?://)?(?:[a-z0-9-]+\.)*TARGET(?=/|\s|$)", re.I)
block_re = re.compile(r"```text\n(.*?)```", re.S)
blocked = re.compile(
    r"(?:<\s*script\b|on(?:error|load|click|mouseover)\s*=|javascript:|"
    r"document\s*\.\s*cookie|window\s*\.\s*location|union\s+select|"
    r"sleep\s*\(|benchmark\s*\(|pg_sleep\s*\(|waitfor\s+delay|"
    r"information_schema|into\s+outfile|load_file\s*\()",
    re.I,
)
issues = []
files = []

for name in check_dirs:
    for path in sorted((root / name).rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel in skip_files:
            continue
        files.append(rel)
        text = path.read_text(errors="ignore")
        for block in block_re.findall(text):
            for raw in block.splitlines():
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if "TARGET" in line and not scoped.search(line):
                    issues.append((rel, "missing site:TARGET", line))
                if retired.search(line):
                    issues.append((rel, "retired operator", line))
                if space_after_colon.search(line):
                    issues.append((rel, "space after colon", line))
                if blocked.search(line):
                    issues.append((rel, "blocked payload-like string", line))

print("checked_files=" + str(len(files)))
print("issues=" + str(len(issues)))
for rel, kind, line in issues:
    print(rel + " :: " + kind + " :: " + line)
raise SystemExit(1 if issues else 0)
