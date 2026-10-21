from discount import Coupon, order_total


def test_fixed_coupon_reduces_total():
    assert order_total([45.0], Coupon("TENOFF", "fixed", 10)) == 35.0


def test_fixed_coupon_does_not_go_below_zero():
    assert order_total([5.0], Coupon("TENOFF", "fixed", 10)) == 0.0
