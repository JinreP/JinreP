"""Rewrites the <!--START_SECTION:activity--> block in README.md with the
latest public commits of the profile owner, formatted like a terminal log."""

import json
import os
import re
import urllib.request
from datetime import datetime, timezone

USER = "JinreP"
LIMIT = 6
README = "README.md"
START = "<!--START_SECTION:activity-->"
END = "<!--END_SECTION:activity-->"


def fetch(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-readme-bot",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def relative(ts):
    then = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - then
    s = int(delta.total_seconds())
    for unit, size in (("d", 86400), ("h", 3600), ("m", 60)):
        if s >= size:
            return f"{s // size}{unit} ago"
    return "just now"


def main():
    events = fetch(f"https://api.github.com/users/{USER}/events/public?per_page=100")
    lines = []
    for ev in events:
        if ev.get("type") != "PushEvent":
            continue
        repo = ev["repo"]["name"]
        for c in reversed(ev["payload"].get("commits", [])):
            msg = c["message"].splitlines()[0].strip()
            if len(msg) > 60:
                msg = msg[:57] + "..."
            lines.append(f"* {c['sha'][:7]}  {msg:<60}  {repo.split('/')[-1]}  ({relative(ev['created_at'])})")
            if len(lines) >= LIMIT:
                break
        if len(lines) >= LIMIT:
            break

    body = "```text\n$ git log --all --oneline -n %d\n\n%s\n```" % (
        LIMIT, "\n".join(lines) if lines else "* (no public commits in the last 90 days)")

    with open(README, encoding="utf-8") as f:
        content = f.read()
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n{body}\n{END}",
        content,
        flags=re.S,
    )
    if new != content:
        with open(README, "w", encoding="utf-8") as f:
            f.write(new)
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
