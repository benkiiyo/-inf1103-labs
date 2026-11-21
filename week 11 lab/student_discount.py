# student_discount.py
# The 4th strategy: a fixed 5% student discount.
# Adding this needed NO changes to Order - that's the Open/Closed Principle.

from discount_strategy import DiscountStrategy   # the abstract strategy


class StudentDiscount(DiscountStrategy):

    STUDENT_PERCENTAGE: float = 5.0   # students always get 5% off

    # e.g. 5% off 100 -> 95
    def apply(self, total: float) -> float:
        return total * (1 - self.STUDENT_PERCENTAGE / 100)
