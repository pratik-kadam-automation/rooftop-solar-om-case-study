"""Rank inverters by how many string faults have been left unresolved.

At the plant in this case study, inverters that later failed had a history of
several string faults that were never cleared. This is a simple heuristic from one
plant, not a validated failure model. Tune the thresholds to your site.

Input CSV columns: opened (YYYY-MM-DD), closed (YYYY-MM-DD or blank), inverter, string, fault
"""
import argparse
import csv
from collections import defaultdict
from datetime import date, datetime


def _d(s):
    s = (s or "").strip()
    return datetime.strptime(s, "%Y-%m-%d").date() if s else None


def assess(rows, as_of, open_high=3, age_high=60, window_days=180, repeat_medium=2):
    per = defaultdict(list)
    for r in rows:
        per[r["inverter"]].append((_d(r["opened"]), _d(r["closed"])))
    result = []
    for inv, faults in per.items():
        open_faults = [(o, c) for o, c in faults if o <= as_of and (c is None or c > as_of)]
        oldest = max(((as_of - o).days for o, _ in open_faults), default=0)
        recent = [o for o, _ in faults if 0 <= (as_of - o).days <= window_days]
        if len(open_faults) >= open_high or oldest >= age_high:
            level = "HIGH"
        elif len(open_faults) >= 1 and (len(recent) >= repeat_medium or len(open_faults) >= 2):
            level = "MEDIUM"
        else:
            level = "LOW"
        result.append({"inverter": inv, "level": level, "open_faults": len(open_faults),
                       "oldest_open_days": oldest, "faults_in_window": len(recent)})
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    result.sort(key=lambda r: (order[r["level"]], -r["open_faults"], -r["oldest_open_days"]))
    return result


def main():
    ap = argparse.ArgumentParser(description="Inverter risk from open string faults")
    ap.add_argument("csv")
    ap.add_argument("--as-of", default=date.today().isoformat(), help="YYYY-MM-DD")
    ap.add_argument("--open-high", type=int, default=3)
    ap.add_argument("--age-high", type=int, default=60)
    ap.add_argument("--window-days", type=int, default=180)
    ap.add_argument("--repeat-medium", type=int, default=2)
    a = ap.parse_args()
    with open(a.csv, newline="") as f:
        rows = list(csv.DictReader(f))
    res = assess(rows, _d(a.as_of), a.open_high, a.age_high, a.window_days, a.repeat_medium)
    print(f"{'inverter':9} {'risk':7} {'open':5} {'oldest open (days)':19} faults in last {a.window_days} d")
    for r in res:
        print(f"{r['inverter']:9} {r['level']:7} {r['open_faults']:<5} {r['oldest_open_days']:<19} {r['faults_in_window']}")


if __name__ == "__main__":
    main()
