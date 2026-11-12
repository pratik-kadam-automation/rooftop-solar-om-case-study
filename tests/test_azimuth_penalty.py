import pytest

pytest.importorskip("pvlib")

from tools import azimuth_penalty as ap


def test_west_facing_gets_less_than_south_facing():
    rel = dict(ap.relative_to_south(19.0, 73.0, 15, [180, 270]))
    assert rel[180] == pytest.approx(1.0)
    assert 0.85 < rel[270] < 1.0


def test_east_and_west_are_similar():
    rel = dict(ap.relative_to_south(19.0, 73.0, 15, [90, 270]))
    assert abs(rel[90] - rel[270]) < 0.03
