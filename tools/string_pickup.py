"""Find strings that start late in the morning.

This automates the daily dashboard check: compare when each string first carries
current against the other strings on the same inverter. A string that keeps starting
late is usually wet or damaged insulation, water near a connector, or a loose joint.

Input CSV columns: timestamp (ISO 8601), inverter, string, current_a
"""
import argparse
import csv
import statistics
from collections import defaultdict
from datetime import datetime


def first_pickups(rows, min_current=1.0):
    """Return {(date, inverter, string): first datetime with current >= min_current, or None}."""
    seen = {}
    keys = set()
    for r in rows:
        ts = datetime.fromisoformat(r["timestamp"])
        key = (ts.date(), r["inverter"], r["string"])
        keys.add(key)
        if float(r["current_a"]) >= min_current:
            if key not in seen or ts < seen[key]:
                seen[key] = ts
    return {k: seen.get(k) for k in keys}


def _minutes(t):
    return t.hour * 60 + t.minute + t.second / 60.0


def delays(pickups):
    """Minutes behind the median pickup of the other strings, per inverter and day.

    None means the string never picked up that day.
    """
    groups = defaultdict(dict)
    for (d, inv, s), t in pickups.items():
        groups[(d, inv)][s] = t
    out = {}
    for (d, inv), strs in groups.items():
        times = [t for t in strs.values() if t is not None]
        if not times:
            continue
        med = statistics.median(_minutes(t) for t in times)
        for s, t in strs.items():
            out[(d, inv, s)] = None if t is None else _minutes(t) - med
    return out


def flag_strings(delay_map, late_min=20.0, min_days=3, window_days=5):
    """Flag strings that were late (or never started) on at least min_days of the last window_days."""
    per = defaultdict(list)
    for (d, inv, s), v in delay_map.items():
        per[(inv, s)].append((d, v))
    flagged = []
    for (inv, s), items in per.items():
        items.sort(key=lambda x: x[0])
        recent = items[-window_days:]
        late = [v for _, v in recent if v is None or v >= late_min]
        if len(late) >= min_days:
            never = sum(1 for _, v in recent if v is None)
            vals = [v for _, v in recent if v is not None and v >= late_min]
            flagged.append({
                "inverter": inv, "string": s,
                "late_days": len(late), "window": len(recent),
                "never_started_days": never,
                "avg_delay_min": (sum(vals) / len(vals)) if vals else None,
                "last_date": recent[-1][0].isoformat(),
            })
    flagged.sort(key=lambda f: (-f["never_started_days"], -(f["avg_delay_min"] or 0), -f["late_days"]))
    return flagged


def main():
    ap = argparse.ArgumentParser(description="Flag strings with late morning pickup")
    ap.add_argument("csv")
    ap.add_argument("--min-current", type=float, default=1.0, help="amps that count as picked up")
    ap.add_argument("--late-min", type=float, default=20.0, help="minutes behind peers that counts as late")
    ap.add_argument("--min-days", type=int, default=3, help="late days needed inside the window")
    ap.add_argument("--window", type=int, default=5, help="most recent days to look at")
    a = ap.parse_args()
    with open(a.csv, newline="") as f:
        rows = list(csv.DictReader(f))
    flagged = flag_strings(delays(first_pickups(rows, a.min_current)), a.late_min, a.min_days, a.window)
    if not flagged:
        print("No strings flagged.")
        return
    print(f"{'inverter':9} {'string':7} {'late days':10} {'never started':14} {'avg delay (min)':16} last date")
    for f_ in flagged:
        avg = "-" if f_["avg_delay_min"] is None else f"{f_['avg_delay_min']:.0f}"
        print(f"{f_['inverter']:9} {f_['string']:7} {f_['late_days']}/{f_['window']:<8} {f_['never_started_days']:<14} {avg:16} {f_['last_date']}")
    print("\nNext step: inspect the connector and gland for water or looseness, and test insulation")
    print("resistance once the string is safely isolated, following your site procedure.")


if __name__ == "__main__":
    main()
