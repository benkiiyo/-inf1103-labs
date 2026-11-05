from abc import ABC, abstractmethod   # tools for making abstract classes


class CanBeShipped(ABC):

    # Any class that can be shipped MUST write its own version of this
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
