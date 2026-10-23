"""Flag overlapping or back-to-back events in schedule.md."""
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

LINE = re.compile(r"^- (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})-(\d{2}:\d{2}) \| ([^|]+?)\s*(?:\|.*)?$")
TIGHT_GAP = timedelta(minutes=15)


def load(path):
    events = []
    for n, raw in enumerate(Path(path).read_text().splitlines(), 1):
        m = LINE.match(raw.strip())
        if not m:
            continue
        day, start, end, title = m.groups()
        s = datetime.fromisoformat(f"{day} {start}")
        e = datetime.fromisoformat(f"{day} {end}")
        if e <= s:
            e += timedelta(days=1)
        events.append((s, e, title, n))
    return sorted(events)


def main(path="schedule.md"):
    events = load(path)
    problems = 0
    for i, (s1, e1, t1, n1) in enumerate(events):
        for s2, e2, t2, n2 in events[i + 1:]:
            if s2 >= e1 + TIGHT_GAP:
                break
            kind = "CONFLICT" if s2 < e1 else "TIGHT"
            print(f"{kind}: '{t1}' ({s1:%a %m-%d %H:%M}-{e1:%H:%M}, line {n1}) "
                  f"vs '{t2}' ({s2:%H:%M}-{e2:%H:%M}, line {n2})")
            problems += 1
    print(f"{len(events)} events, {problems} issue(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
