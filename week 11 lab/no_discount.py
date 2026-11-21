# no_discount.py
# A strategy that changes nothing - the default when an order has no discount.

from discount_strategy import DiscountStrategy   # the abstract strategy


class NoDiscount(DiscountStrategy):

    # Give back the total unchanged
    def apply(self, total: float) -> float:
        return total
