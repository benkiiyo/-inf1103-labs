from product import Product
from order_line import OrderLine


class Order:

    # Create an empty order with an ID
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []   # the Order's own lines

    # Getter: return the order ID
    def get_order_id(self) -> str:
        return self.__order_id

    # The Order makes the OrderLine ITSELF from a product and quantity.
    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)   # created HERE, inside the Order
        self.__order_lines.append(order_line)

    # Remove the line for a product, through the Order (the owner)
    # Returns True if a line was removed, False if no line had that product ID
    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id().upper() == product_id.upper():
                self.__order_lines.remove(order_line)   # the line is gone for good
                return True
        return False

    # Give back a copy of the lines (read-only use, e.g. testing)
    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    # Total = add up every line's subtotal (each line calculates its own)
    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()
        return total

    # Print the order: its ID, each line, and the total
    def display_information(self) -> None:
        print(f"Order {self.__order_id}")
        if len(self.__order_lines) == 0:
            print("  (no order lines)")
        for order_line in self.__order_lines:
            print("  ", end="")
            order_line.display_information()
        print(f"  Total: ${self.calculate_total():.2f}")
