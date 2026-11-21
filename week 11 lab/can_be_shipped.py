# can_be_shipped.py
# CanBeShipped is an INTERFACE-style abstract base class.
# It's a "contract": any class that signs it (inherits from it)
# promises to provide a calculate_shipping_cost() method.

from abc import ABC, abstractmethod   # tools for making abstract classes


class CanBeShipped(ABC):

    # Any class that can be shipped MUST write its own version of this
    # It must give back the shipping cost as a decimal number (float)
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass
