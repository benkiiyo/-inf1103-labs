# order.py
# An Order is made up of OrderLine objects.
#
# COMPOSITION: the Order CREATES and OWNS its OrderLines.
# - OrderLines are only created inside add_order_line(), never outside.
# - Each OrderLine belongs to exactly one Order and is never moved to another.
#
# STRATEGY PATTERN: the Order is GIVEN a DiscountStrategy and just calls its
# apply() method. There is no if/elif about discount types in here, so new
# discounts can be added without changing this class (Open/Closed Principle).

from product import Product                       # needed for the type hints
from order_line import OrderLine                  # the "part" this Order is made of
from discount_strategy import DiscountStrategy    # the abstract discount type
from no_discount import NoDiscount                # the default discount


class Order:

    # Create an empty order with an ID and (optionally) a discount strategy
    # If no discount is given, use NoDiscount()
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []   # the Order's own lines
        # ASSOCIATION: the Order uses a discount object but doesn't own it
        if discount is None:
            discount = NoDiscount()
        self.__discount: DiscountStrategy = discount

    # Getter: return the order ID
    def get_order_id(self) -> str:
        return self.__order_id

    # Swap to a different discount strategy later on
    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    # The Order makes the OrderLine ITSELF from a product and quantity.
    # (OrderLine checks that the quantity is valid - it owns that rule)
    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)   # created HERE, inside the Order
        self.__order_lines.append(order_line)

    # Remove the line for a product, through the Order (the owner)
    # Returns True if a line was removed, False if no line had that product ID
    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id().upper() == product_id.upper():
                self.__order_lines.remove(order_line)
                return True
        return False

    # Give back a copy of the lines (read-only use, e.g. testing)
    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    # Add up every line's subtotal, then let the discount strategy adjust it
    def calculate_total(self) -> float:
        total = sum(order_line.calculate_subtotal() for order_line in self.__order_lines)
        return self.__discount.apply(total)   # the strategy decides the discount

    # Print the order: its ID, each line, and the total
    def display_information(self) -> None:
        print(f"Order {self.__order_id}")
        if len(self.__order_lines) == 0:
            print("  (no order lines)")
        for order_line in self.__order_lines:
            print("  ", end="")   # indent each line
            order_line.display_information()
        print(f"  Total (after discount): ${self.calculate_total():.2f}")
