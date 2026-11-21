# discount_strategy.py
# STRATEGY PATTERN: DiscountStrategy is the abstract "shape" every discount must have.
# Each kind of discount is its own class with its own apply() method.
# Order only ever calls apply() - it never needs to know which discount it has.

from abc import ABC, abstractmethod   # tools for making abstract classes


class DiscountStrategy(ABC):

    # Take an order total and give back the total after the discount
    # Every discount class MUST write its own version of this
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
