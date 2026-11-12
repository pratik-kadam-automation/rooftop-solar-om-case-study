import pytest

from tools import savings as sv


def test_breakeven_units():
    assert sv.breakeven_units(700000, 15) == pytest.approx(46666.67, rel=1e-4)
    assert sv.breakeven_units(700000, 17) == pytest.approx(41176.47, rel=1e-4)


def test_recovered_units_mid_case():
    # 14.5 lakh kWh a year now, PR 66% -> 87%: 1 - 0.66/0.87 = 7/29 of current generation
    assert sv.recovered_units(1450000, 0.87, 0.66) == pytest.approx(350000, rel=1e-6)


def test_no_improvement_recovers_nothing():
    assert sv.recovered_units(1000000, 0.80, 0.80) == pytest.approx(0)


def test_lakh_format():
    assert sv.lakh(700000) == "\u20b97.00 lakh"
