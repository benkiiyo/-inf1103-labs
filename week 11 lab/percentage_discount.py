# percentage_discount.py
# A strategy that takes a percentage off, e.g. PercentageDiscount(10) = 10% off.

from discount_strategy import DiscountStrategy   # the abstract strategy


class PercentageDiscount(DiscountStrategy):

    # Remember the percentage to take off (must be between 0 and 100)
    def __init__(self, percentage: float) -> None:
        # VALIDATION: this class owns the rule about what a valid percentage is
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.__percentage: float = float(percentage)

    # e.g. 10% off 250 -> 250 * (1 - 10/100) = 225
    def apply(self, total: float) -> float:
        return total * (1 - self.__percentage / 100)
