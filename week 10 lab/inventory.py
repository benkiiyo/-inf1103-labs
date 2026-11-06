class Inventory:

    # __init__ runs when a new Inventory is created
    def __init__(self):
        # Private list that will hold all the product objects
        self.__products = []

    # Add a product object to the list
    # Returns True if added, False if that ID is already used
    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print(f"A product with ID {product.get_product_id()} already exists.")
            return False
        self.__products.append(product)
        return True

    # Find a product by its ID
    # Returns the product object if found, or None ("nothing") if not found
    def search_product(self, product_id):
        for product in self.__products:
            # .upper() so "p001" and "P001" count as the same ID
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    # Print every product in the inventory
    def display_all(self):
        print("Current Inventory")
        print("-" * 48)
        if len(self.__products) == 0:
            print("Inventory is empty.")
        for product in self.__products:
            # Each product runs ITS OWN display_information() so physical ones show weight and digital ones show download size
            product.display_information()
        print("-" * 48)

    # Give back a copy of the product list (used when saving to JSON)
    def get_all_products(self):
        return list(self.__products)
