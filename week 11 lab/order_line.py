# order_line.py
# An OrderLine is ONE line of an order: a product and how many were ordered.
# OrderLines are only ever created by an Order (composition) - see order.py.
# An OrderLine REFERS to a Product, but doesn't own it (association):
# the Product still exists on its own and can also be in an Inventory.

from product import Product   # needed for the type hints


class OrderLine:

    # Create one order line from a product and a quantity
    def __init__(self, product: Product, quantity: int) -> None:
        # VALIDATION: the OrderLine protects its own quantity
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.__product: Product = product      # a reference to an existing Product
        self.__quantity: int = int(quantity)   # how many of it were ordered

    # Getter: return the Product this line is for
    def get_product(self) -> Product:
        return self.__product

    # Getter: return the quantity ordered
    def get_quantity(self) -> int:
        return self.__quantity

    # Price of this line = product price x quantity
    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    # Print this line, e.g. "2 x Mouse @ $25.50 = $51.00"
    def display_information(self) -> None:
        print(f"{self.__quantity} x {self.__product.get_name()} "
              f"@ ${self.__product.get_price():.2f} = ${self.calculate_subtotal():.2f}")
