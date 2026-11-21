# bulk_discount.py
# A strategy that takes a fixed amount off big orders,
# e.g. BulkDiscount(200, 20) takes $20 off any total of $200 or more.

from discount_strategy import DiscountStrategy   # the abstract strategy


class BulkDiscount(DiscountStrategy):

    # Remember the threshold (minimum total) and the amount to take off
    def __init__(self, threshold: float, amount: float) -> None:
        # VALIDATION: neither number can be negative
        if threshold < 0 or amount < 0:
            raise ValueError("Threshold and amount cannot be negative.")
        self.__threshold: float = float(threshold)
        self.__amount: float = float(amount)

    # Only take the amount off if the total reaches the threshold
    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return total - self.__amount
        return total
