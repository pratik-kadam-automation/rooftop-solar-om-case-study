from datetime import date

from tools import inverter_risk as ir


def _row(opened, closed, inv, s="S01"):
    return {"opened": opened, "closed": closed, "inverter": inv, "string": s, "fault": "string fault"}


def test_levels():
    rows = [
        _row("2025-02-01", "", "A", "S01"), _row("2025-03-01", "", "A", "S02"), _row("2025-04-01", "", "A", "S03"),
        _row("2025-05-01", "2025-05-03", "B", "S01"), _row("2025-05-20", "", "B", "S02"), _row("2025-06-01", "", "B", "S03"),
        _row("2025-01-01", "2025-01-02", "C", "S01"),
    ]
    res = {r["inverter"]: r for r in ir.assess(rows, date(2025, 6, 10))}
    assert res["A"]["level"] == "HIGH"
    assert res["B"]["level"] == "MEDIUM"
    assert res["C"]["level"] == "LOW"


def test_old_single_fault_is_high():
    res = ir.assess([_row("2025-01-01", "", "A")], date(2025, 6, 10))
    assert res[0]["level"] == "HIGH"
    assert res[0]["oldest_open_days"] == 160


def test_closed_faults_do_not_count_as_open():
    res = ir.assess([_row("2025-05-01", "2025-05-05", "A")], date(2025, 6, 10))
    assert res[0]["open_faults"] == 0
