"""Write small synthetic datasets to data/sample/. These are made up, not from a real plant."""
import csv
import math
import os
import random
from datetime import date, datetime, timedelta

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "sample")


def string_currents(rng):
    rows = []
    start = date(2025, 6, 1)
    inverters = {"INV-1": 8, "INV-2": 8}
    for day in range(10):
        d = start + timedelta(days=day)
        for inv, n in inverters.items():
            for k in range(1, n + 1):
                s = f"S{k:02d}"
                delay = 0
                never = False
                if inv == "INV-1" and s == "S05":
                    delay = 45                 # wet connector, late every day
                if inv == "INV-2" and s == "S03" and day in (1, 3, 4, 8):
                    delay = 30                 # intermittent
                if inv == "INV-2" and s == "S07" and day >= 6:
                    never = True               # open string for the last four days
                jitter = rng.randint(-4, 4)
                peak = 8.6 + rng.random() * 0.8
                rise, sets = 6.5 * 60, 18.75 * 60
                t = datetime(d.year, d.month, d.day, 6, 0)
                while t.hour < 19:
                    m = t.hour * 60 + t.minute
                    x = (m - (rise + delay + jitter)) / (sets - (rise + delay + jitter))
                    cur = 0.0 if (never or x <= 0 or x >= 1) else peak * math.sin(math.pi * x) ** 1.2
                    rows.append({"timestamp": t.isoformat(), "inverter": inv, "string": s, "current_a": round(cur, 2)})
                    t += timedelta(minutes=10)
    return rows


def fault_log():
    return [
        {"opened": "2025-02-10", "closed": "", "inverter": "INV-1", "string": "S02", "fault": "string fault"},
        {"opened": "2025-03-18", "closed": "", "inverter": "INV-1", "string": "S05", "fault": "string fault"},
        {"opened": "2025-04-02", "closed": "", "inverter": "INV-1", "string": "S06", "fault": "connector heating"},
        {"opened": "2025-05-05", "closed": "2025-05-09", "inverter": "INV-2", "string": "S03", "fault": "string fault"},
        {"opened": "2025-05-20", "closed": "2025-05-22", "inverter": "INV-2", "string": "S07", "fault": "string fault"},
        {"opened": "2025-06-04", "closed": "", "inverter": "INV-2", "string": "S03", "fault": "late pickup"},
        {"opened": "2025-01-12", "closed": "2025-01-14", "inverter": "INV-3", "string": "S01", "fault": "string fault"},
    ]


def daily_energy(rng, kwp=930.0):
    rows = []
    start = date(2025, 5, 2)
    cleanings = {date(2025, 5, 16), date(2025, 5, 31)}
    pr = 0.80
    for day in range(40):
        d = start + timedelta(days=day)
        if d in cleanings:
            pr = 0.81
        pr -= 0.0012                      # soiling builds up
        poa = 1.4 + rng.random() * 0.8 if rng.random() < 0.1 else 5.0 + rng.random() * 1.4
        ac = kwp * poa * (pr + rng.uniform(-0.004, 0.004))
        rows.append({"date": d.isoformat(), "ac_kwh": round(ac, 1), "poa_kwh_m2": round(poa, 2)})
    return rows, sorted(cleanings)


def _write(name, rows, fields):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    rng = random.Random(42)
    _write("string_currents.csv", string_currents(rng), ["timestamp", "inverter", "string", "current_a"])
    _write("fault_log.csv", fault_log(), ["opened", "closed", "inverter", "string", "fault"])
    rows, cleanings = daily_energy(rng)
    _write("daily_energy.csv", rows, ["date", "ac_kwh", "poa_kwh_m2"])
    _write("cleaning_dates.csv", [{"date": c.isoformat()} for c in cleanings], ["date"])
    print("wrote sample data to", OUT)


if __name__ == "__main__":
    main()
