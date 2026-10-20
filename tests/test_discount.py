import pytest

from discount import Coupon, apply_coupon, order_total


def test_no_coupon():
    assert apply_coupon(50.0, None) == 50.0


def test_percent_coupon():
    assert apply_coupon(80.0, Coupon("SPRING20", "percent", 20)) == 64.0


def test_percent_coupon_out_of_range():
    with pytest.raises(ValueError):
        apply_coupon(80.0, Coupon("BAD", "percent", 150))


def test_unknown_coupon_kind():
    with pytest.raises(ValueError):
        apply_coupon(80.0, Coupon("X", "bogo", 1))


def test_order_total_with_tax():
    assert order_total([10.0, 20.0], tax_rate=0.1) == 33.0


def test_order_total_with_percent_coupon_and_tax():
    assert order_total([50.0, 50.0], Coupon("HALF", "percent", 50), tax_rate=0.1) == 55.0
