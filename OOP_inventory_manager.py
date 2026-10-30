class Product:
 
    # __init__ runs automatically when a new Product is created
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
 
    # Print this product's details on one line
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")

class Inventory:
 
    # __init__ runs when a new Inventory is created
    def __init__(self):
        # Private list that will hold all the Product objects
        self.__products = []
 
    # Add a Product object to the list
    # Returns True if added, False if that ID is already used
    def add_product(self, product):
        # Don't allow two products with the same ID
        if self.search_product(product.get_product_id()) is not None:
            print(f"A product with ID {product.get_product_id()} already exists.")
            return False
        self.__products.append(product)
        return True
 
    # Find a product by its ID
    # Returns the Product object if found, or None ("nothing") if not found
    def search_product(self, product_id):
        for product in self.__products:
            # .upper() so "p001" and "P001" count as the same ID
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None
 
    # Print every product in the inventory
    def display_all(self):
        if len(self.__products) == 0:
            print("Inventory is empty.")
            return
        print("\n--- Current Inventory ---")
        for product in self.__products:
            product.display_information()   # each Product prints itself
 
    # Give back a copy of the product list (used later when saving to JSON)
    # A copy means outside code can't accidentally mess up our real list
    def get_all_products(self):
        return list(self.__products)
 
 
# test
if __name__ == "__main__":
    inventory = Inventory()                                        # empty inventory
    inventory.add_product(Product("P001", "Laptop", 1200.00, 15))  # add a laptop
    inventory.add_product(Product("P002", "Mouse", 25.50, 40))     # add a mouse
    inventory.add_product(Product("P001", "Duplicate", 1.00, 1))   # should be refused
    inventory.display_all()                                        # shows 2 products
 
    found = inventory.search_product("p002")   # search using lowercase on purpose
    if found is not None:
        print("\nSearch result:")
        found.display_information()            # should show the Mouse
 
    print(inventory.search_product("P999"))    # not in inventory -> prints None
 
 