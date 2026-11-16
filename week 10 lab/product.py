from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):

   
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier) -> None:
        # Double underscore (__) = private: outside code uses the methods below
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = float(price)   # price is a decimal number
        self.__stock: int = int(stock)       # stock is a whole number
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
    # Returns True if it worked, False if it was refused
    def update_stock(self, quantity: int) -> bool:
        if quantity < 0:
            print("Stock cannot be negative. No change made.")
            return False   # update failed
        self.__stock = quantity
        return True        # update worked

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
            "stock": self.__stock
        }

    # Every child class MUST write its own version.
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass