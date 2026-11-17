import pytest
from validation_lab.limits import check_temperature


def test_normal_temperature_is_ok():
    assert check_temperature(60.0) == "ok"


def test_high_temperature_fails():
    assert check_temperature(105.0) == "fail"


def test_out_of_range_reading_raises():
    with pytest.raises(ValueError):
        check_temperature(500.0)
