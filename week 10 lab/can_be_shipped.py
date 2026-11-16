from abc import ABC, abstractmethod


class CanBeShipped(ABC):

    # Any class that can be shipped MUST write its own version of this
    # It must give back the shipping cost as a decimal number (float)
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass