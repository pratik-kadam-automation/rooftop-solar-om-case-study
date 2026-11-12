from datetime import date, timedelta

import pytest

from tools import cleaning_gain as cg


def _rows(prs, start=date(2025, 5, 1), kwp=100.0, poa=5.0):
    return [{"date": (start + timedelta(i)).isoformat(), "ac_kwh": kwp * poa * p, "poa_kwh_m2": poa} for i, p in enumerate(prs)]


def test_gain_is_measured():
    prs = [0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.84, 0.84, 0.84, 0.84]
    pr = cg.daily_pr(_rows(prs), 100.0)
    g = cg.cleaning_gain(pr, date(2025, 5, 7), days=3)  # cleaning on day index 6
    assert g["gain_points"] == pytest.approx(6.0, abs=0.01)


def test_cloudy_days_are_ignored():
    rows = _rows([0.8] * 10)
    rows[3]["poa_kwh_m2"] = 1.0
    assert date(2025, 5, 4) not in cg.daily_pr(rows, 100.0)


def test_not_enough_days_returns_none():
    pr = cg.daily_pr(_rows([0.8, 0.8]), 100.0)
    assert cg.cleaning_gain(pr, date(2025, 5, 2)) is None
