from product import Product


class OrderLine:

    # Create one order line from a product and a quantity
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product      # a reference to an existing Product
        self.__quantity: int = int(quantity)   # how many of it were ordered

    # Getter: return the Product this line is for
    def get_product(self) -> Product:
        return self.__product

    # Getter: return the quantity ordered
    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(f"{self.__quantity} x {self.__product.get_name()} "
              f"@ ${self.__product.get_price():.2f} = ${self.calculate_subtotal():.2f}")
