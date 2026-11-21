# product.py
# Product is the ABSTRACT parent class for every product in the store.
# "Abstract" means you can't create a plain Product - only a PhysicalProduct
# or a DigitalProduct (the child classes), which fill in the missing method.
# Each Product is ASSOCIATED with one Supplier (it keeps a reference to it).

from abc import ABC, abstractmethod   # tools for making abstract classes
from supplier import Supplier         # needed for the supplier type hint


class Product(ABC):   # inheriting from ABC makes Product an abstract class

    # __init__ runs when a new product is created
    # (the child classes call this using super().__init__)
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier) -> None:
        # Double underscore (__) = private: outside code uses the methods below
        # float() and int() raise a ValueError by themselves if given text like "abc"
        price = float(price)
        stock = int(stock)

        # VALIDATION: Product owns the rules about price and stock,
        # so it checks them here, once, for every kind of product
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if stock < 0:
            raise ValueError("Stock quantity cannot be negative.")

        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price   # price is a decimal number
        self.__stock: int = stock     # stock is a whole number
        # ASSOCIATION: we store a reference to a Supplier object that was
        # created somewhere else. The Product doesn't create or own it.
        self.__supplier: Supplier = supplier

    # Getter: return the product ID
    def get_product_id(self) -> str:
        return self.__product_id

    # Getter: return the product name
    def get_name(self) -> str:
        return self.__name

    # Getter: return the price
    def get_price(self) -> float:
        return self.__price

    # Getter: return the stock amount
    def get_stock(self) -> int:
        return self.__stock

    # Getter: return the Supplier object this product is linked to
    def get_supplier(self) -> Supplier:
        return self.__supplier

    # Change the stock - the Product checks the value first (encapsulation)
    # VALIDATION: raises a ValueError if the new stock is negative
    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.__stock = quantity

    # Print the details EVERY product has
    # The child classes add their own extra details on top of this (overriding)
    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock} | "
              f"Supplier: {self.__supplier.get_name()}")

    # Turn the common details into a dictionary, ready to save to JSON
    # The child classes add their type and extra attribute on top of this
    def to_dict(self) -> dict:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            # Save the supplier's details too, so it can be rebuilt when loading
            "supplier": {
                "id": self.__supplier.get_supplier_id(),
                "name": self.__supplier.get_name(),
                "email": self.__supplier.get_contact_email()
            }
        }

    # ABSTRACT method: no code here on purpose.
    # Every child class MUST write its own version.
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
