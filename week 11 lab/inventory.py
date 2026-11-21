# inventory.py
# Inventory manages a COLLECTION of Product objects (physical or digital).
# Single responsibility: store, add, remove, find and display products.
#
# AGGREGATION: an Inventory is a "whole" made of Product "parts", but it
# does NOT own them. Products are created outside the Inventory, can be
# removed or moved to another Inventory, and keep existing when removed.

from product import Product   # needed for the type hints


class Inventory:

    # __init__ runs when a new Inventory is created
    def __init__(self) -> None:
        # Private list of Product references.
        # list[Product] (not list[PhysicalProduct]) so it can hold ANY kind of Product
        self.__products: list[Product] = []

    # Add an EXISTING Product object to the inventory
    # (the Inventory never creates products itself - that's aggregation)
    # Returns True if added, False if that ID is already used
    def add_product(self, product: Product) -> bool:
        if self.find_product(product.get_product_id()) is not None:
            print(f"A product with ID {product.get_product_id()} already exists.")
            return False
        self.__products.append(product)
        return True

    # Remove a product's reference from this inventory
    # The Product object itself is NOT destroyed - we hand it back
    # so it can be used elsewhere (e.g. added to another inventory)
    # Returns the removed Product, or None if the ID wasn't found
    def remove_product(self, product_id: str) -> Product | None:
        product = self.find_product(product_id)
        if product is None:
            return None
        self.__products.remove(product)   # take its name tag out of OUR list only
        return product

    # Find a product by its ID
    # Returns the Product object if found, or None ("nothing") if not found
    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            # .upper() so "p001" and "P001" count as the same ID
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    # Print every product in the inventory
    def display_all(self) -> None:
        print("Current Inventory")
        print("-" * 48)
        if len(self.__products) == 0:
            print("Inventory is empty.")
        for product in self.__products:
            # Each product runs ITS OWN display_information()
            product.display_information()
        print("-" * 48)

    # Give back a copy of the product list (used when saving and looping)
    def get_all_products(self) -> list[Product]:
        return list(self.__products)
