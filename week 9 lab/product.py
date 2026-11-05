from abc import ABC, abstractmethod   # tools for making abstract classes


class Product(ABC):   # inheriting from ABC makes Product an abstract class

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)   # price is a decimal number
        self.__stock = int(stock)     # stock is a whole number

    # Getter: return the product ID
    def get_product_id(self):
        return self.__product_id

    # Getter: return the product name
    def get_name(self):
        return self.__name

    # Getter: return the price
    def get_price(self):
        return self.__price

    # Getter: return the stock amount
    def get_stock(self):
        return self.__stock

    # Change the stock - the Product checks the value first (encapsulation)
    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative. No change made.")
            return False   # update failed
        self.__stock = quantity
        return True        # update worked

    # Print the details EVERY product has
    # The child classes add their own extra details on top of this (overriding)
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")

    # Turn the common details into a dictionary, ready to save to JSON
    # The child classes add their type and extra attribute on top of this
    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    # Every child class MUST write its own version, or Python won't let you create objects of that child class.
    @abstractmethod
    def get_fulfilment_info(self):
        pass
