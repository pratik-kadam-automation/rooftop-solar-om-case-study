import os
import subprocess
import sys
from datetime import datetime, timedelta

from tools import string_pickup as sp


def _rows(day, start_by_string):
    rows = []
    for s, start in start_by_string.items():
        t = datetime(2025, 6, day, 6, 0)
        while t.hour < 10:
            cur = 5.0 if t >= start.replace(day=day) else 0.0
            rows.append({"timestamp": t.isoformat(), "inverter": "INV-1", "string": s, "current_a": cur})
            t += timedelta(minutes=10)
    return rows


def test_late_string_is_flagged():
    rows = []
    for day in range(1, 6):
        rows += _rows(day, {"S01": datetime(2025, 6, 1, 6, 40), "S02": datetime(2025, 6, 1, 6, 40),
                            "S03": datetime(2025, 6, 1, 6, 40), "S04": datetime(2025, 6, 1, 7, 30)})
    flagged = sp.flag_strings(sp.delays(sp.first_pickups(rows)))
    assert [f["string"] for f in flagged] == ["S04"]
    assert flagged[0]["late_days"] == 5
    assert round(flagged[0]["avg_delay_min"]) == 50


def test_string_that_never_starts_is_flagged():
    rows = []
    for day in range(1, 6):
        rows += _rows(day, {"S01": datetime(2025, 6, 1, 6, 40), "S02": datetime(2025, 6, 1, 6, 40),
                            "S03": datetime(2025, 6, 1, 6, 40), "S04": datetime(2030, 6, 1, 23, 0)})
    flagged = sp.flag_strings(sp.delays(sp.first_pickups(rows)))
    assert flagged[0]["string"] == "S04"
    assert flagged[0]["never_started_days"] == 5


def test_normal_strings_not_flagged():
    rows = []
    for day in range(1, 6):
        rows += _rows(day, {"S01": datetime(2025, 6, 1, 6, 40), "S02": datetime(2025, 6, 1, 6, 50)})
    assert sp.flag_strings(sp.delays(sp.first_pickups(rows))) == []


def test_sample_data_end_to_end(tmp_path):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    subprocess.run([sys.executable, "-m", "tools.make_sample_data"], cwd=root, check=True, capture_output=True)
    import csv
    with open(os.path.join(root, "data", "sample", "string_currents.csv"), newline="") as f:
        rows = list(csv.DictReader(f))
    flagged = sp.flag_strings(sp.delays(sp.first_pickups(rows)))
    names = [(f["inverter"], f["string"]) for f in flagged]
    assert ("INV-1", "S05") in names
    assert ("INV-2", "S07") in names
