#!/usr/bin/env python3
import os, sys, requests
from datetime import date, datetime, timedelta

GQL = "https://api.github.com/graphql"
QUERY = """
query($login:String!, $from:DateTime!, $to:DateTime!){
  user(login:$login){
    contributionsCollection(from:$from, to:$to){
      contributionCalendar{
        weeks{ contributionDays{ date contributionCount } }
      }
    }
  }
}
"""

def fetch_calendar(token, login, since_iso, until_iso):
    r = requests.post(
        GQL,
        headers={"Authorization": f"Bearer {token}"},
        json={"query": QUERY, "variables":{"login": login, "from": since_iso, "to": until_iso}},
        timeout=30
    )
    r.raise_for_status()
    j = r.json()
    if "errors" in j:
        raise RuntimeError(j["errors"])
    weeks = j["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = []
    for w in weeks:
        for d in w["contributionDays"]:
            days.append((d["date"], int(d["contributionCount"])))
    days.sort(key=lambda x: x[0])
    return {d:c for d,c in days}

def current_streak(day_map):
    all_days = sorted(day_map.keys())
    if not all_days:
        return 0, None, None
    end = all_days[-1]
    streak = 0
    cur = datetime.fromisoformat(end).date()
    start = None
    while True:
        ds = cur.isoformat()
        if ds in day_map and day_map[ds] > 0:
            streak += 1
            start = cur
            cur = cur - timedelta(days=1)
        else:
            break
    return streak, start, datetime.fromisoformat(end).date()

def render_svg(streak, start, end, username):
    start_s = start.isoformat() if start else "—"
    end_s = end.isoformat() if end else "—"
    title = f"All contributions streak"
    subtitle = f"{streak} days  •  {start_s} – {end_s}"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="720" height="120" role="img" aria-label="{title}">
  <defs>
    <style><![CDATA[
      .card {{ fill: #0d1117; }}
      .border {{ stroke: #30363d; stroke-width: 1; fill: none; }}
      .title {{ fill: #e6edf3; font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial; font-size: 20px; font-weight: 600; }}
      .subtitle {{ fill: #7d8590; font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial; font-size: 16px; }}
      .pill {{ fill: #161b22; stroke: #30363d; stroke-width: 1; rx: 8; }}
      .pilltxt {{ fill: #e6edf3; font-family: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas; font-size: 14px; }}
    ]]></style>
  </defs>
  <rect class="card" x="0.5" y="0.5" width="719" height="119" rx="12"/>
  <rect class="border" x="0.5" y="0.5" width="719" height="119" rx="12"/>
  <text class="title" x="24" y="44">{title} — @{username}</text>
  <text class="subtitle" x="24" y="76">{subtitle}</text>
  <rect class="pill" x="24" y="86" width="140" height="24" rx="8"/>
  <text class="pilltxt" x="36" y="103">private included</text>
</svg>"""

def main():
    token = (os.environ.get("GH_STREAK_TOKEN") or "").strip()
    user = os.environ.get("STREAK_USER")
    out_env = os.environ.get("STREAK_OUT", "streak.svg")
    out = os.path.join(os.getcwd(), out_env)  # always save in repo root

    if not token or not user:
        print("Missing GH_STREAK_TOKEN or STREAK_USER env", file=sys.stderr)
        sys.exit(1)

    today = date.today()
    since = today - timedelta(days=365)  # GitHub GraphQL limit: ≤ 1 year

    try:
        day_map = fetch_calendar(
            token, user,
            since.isoformat() + "T00:00:00Z",
            today.isoformat() + "T23:59:59Z"
        )
    except Exception as e:
        print(f"ERROR fetching calendar: {e}", file=sys.stderr)
        sys.exit(1)

    streak, start, end = current_streak(day_map)
    svg = render_svg(streak, start, end, user)

    print(f"Writing streak.svg to {out}")
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)

    if not os.path.exists(out):
        print("❌ streak.svg failed to save", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"✅ streak.svg successfully saved at {out}")
        print(f"Streak: {streak}, from {start} to {end}")



