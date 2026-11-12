"""Measure what a cleaning actually recovered.

Compares performance ratio for a few clear days before and after each cleaning.
Rain days confound this, so only days with enough sun are used.

Daily CSV columns: date (YYYY-MM-DD), ac_kwh, poa_kwh_m2
Cleaning CSV column: date
"""
import argparse
import csv
from datetime import datetime, timedelta

from tools.pr import performance_ratio


def _d(s):
    return datetime.strptime(s.strip(), "%Y-%m-%d").date()


def daily_pr(rows, dc_kwp, min_poa=3.0):
    out = {}
    for r in rows:
        poa = float(r["poa_kwh_m2"])
        if poa >= min_poa:
            out[_d(r["date"])] = performance_ratio(float(r["ac_kwh"]), dc_kwp, poa)
    return out


def cleaning_gain(pr_by_date, cleaning_date, days=3, search=7):
    before = [pr_by_date[d] for d in (cleaning_date - timedelta(n) for n in range(1, search + 1)) if d in pr_by_date][:days]
    after = [pr_by_date[d] for d in (cleaning_date + timedelta(n) for n in range(1, search + 1)) if d in pr_by_date][:days]
    if len(before) < 2 or len(after) < 2:
        return None
    b = sum(before) / len(before)
    a = sum(after) / len(after)
    return {"date": cleaning_date, "pr_before": b, "pr_after": a, "gain_points": (a - b) * 100, "gain_relative": (a / b - 1) * 100}


def main():
    ap = argparse.ArgumentParser(description="PR before and after cleaning")
    ap.add_argument("daily_csv")
    ap.add_argument("cleaning_csv")
    ap.add_argument("--kwp", type=float, required=True)
    ap.add_argument("--min-poa", type=float, default=3.0, help="kWh/m2 a day needed to use that day")
    ap.add_argument("--days", type=int, default=3)
    a = ap.parse_args()
    with open(a.daily_csv, newline="") as f:
        pr = daily_pr(list(csv.DictReader(f)), a.kwp, a.min_poa)
    with open(a.cleaning_csv, newline="") as f:
        dates = [_d(r["date"]) for r in csv.DictReader(f)]
    print(f"{'cleaning':11} {'PR before':10} {'PR after':10} {'gain (points)':14} gain (relative)")
    for d in dates:
        g = cleaning_gain(pr, d, a.days)
        if g is None:
            print(f"{d.isoformat():11} not enough clear days around this cleaning")
        else:
            print(f"{d.isoformat():11} {g['pr_before'] * 100:8.1f} % {g['pr_after'] * 100:8.1f} % {g['gain_points']:12.2f}   {g['gain_relative']:.2f} %")


if __name__ == "__main__":
    main()
