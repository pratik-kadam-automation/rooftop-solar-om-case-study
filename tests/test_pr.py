import pytest
from tools import pr


def test_performance_ratio_known_values():
    # 930 kWp, 100,000 kWh, 150 kWh/m2 POA -> final yield 107.53 h, PR 71.7 %
    assert pr.final_yield(100000, 930) == pytest.approx(107.527, rel=1e-4)
    assert pr.performance_ratio(100000, 930, 150) == pytest.approx(0.7168, rel=1e-3)


def test_expected_energy_matches_pr():
    exp = pr.expected_energy(930, 150, 0.85)
    assert exp == pytest.approx(930 * 150 * 0.85)
    assert pr.performance_ratio(exp, 930, 150) == pytest.approx(0.85)


def test_structural_loss_ceiling():
    assert pr.ceiling_with_structural_loss(0.95, 0.10) == pytest.approx(0.855)


def test_zero_poa_rejected():
    with pytest.raises(ValueError):
        pr.performance_ratio(100, 10, 0)
