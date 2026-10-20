# "$10 off" coupon makes my order MORE expensive

I applied the coupon `TENOFF` (a fixed $10-off coupon) at checkout on a $45
order and my total went up to $55 instead of down to $35.

Percentage coupons like SPRING20 seem to work fine. It's only the flat-amount
ones.

Repro:

```python
from discount import Coupon, order_total

order_total([45.0], Coupon("TENOFF", "fixed", 10))
# got 55.0, expected 35.0
```

Customers have noticed this and it's pretty embarrassing.
