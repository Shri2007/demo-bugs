"""Order total calculation with coupons."""

from dataclasses import dataclass


@dataclass
class Coupon:
    code: str
    kind: str  # "percent" or "fixed"
    value: float


def apply_coupon(subtotal: float, coupon: Coupon | None) -> float:
    """Return the subtotal after applying `coupon`. Never goes below zero."""
    if coupon is None:
        return round(subtotal, 2)
    if coupon.kind == "percent":
        if not 0 <= coupon.value <= 100:
            raise ValueError("percent coupon must be between 0 and 100")
        return round(subtotal * (1 - coupon.value / 100), 2)
    if coupon.kind == "fixed":
        return round(max(0.0, subtotal - coupon.value), 2)
    raise ValueError(f"unknown coupon kind: {coupon.kind}")


def order_total(prices: list[float], coupon: Coupon | None = None, tax_rate: float = 0.0) -> float:
    subtotal = sum(prices)
    discounted = apply_coupon(subtotal, coupon)
    return round(discounted * (1 + tax_rate), 2)
