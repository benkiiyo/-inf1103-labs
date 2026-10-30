import json   # read and write the inventory.json file
import os     # check whether inventory.json exists
 
FILENAME = "inventory.json"

 
class Product:
 
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
 
    def __init__(self):
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
        print("Current Inventory")
        print("-" * 48)
        if len(self.__products) == 0:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()   # each Product prints itself
        print("-" * 48)
 
    # Give back a copy of the product list
    def get_all_products(self):
        return list(self.__products)
 
 
# Read inventory.json and turn each saved product into a Product object
def load_inventory(inventory):
    # If the file doesn't exist yet, start with an empty inventory
    if not os.path.exists(FILENAME):
        print("inventory.json not found. Starting with an empty inventory.")
        return
 
    print("inventory.json found.")
    with open(FILENAME, "r") as file:
        data = json.load(file)   # a list of dictionaries, like in Week 5
 
    # Each dictionary looks like {"id": "P001", "name": "Laptop", "price": 1200.0, "stock": 15}
    for item in data:
        product = Product(item["id"], item["name"], item["price"], item["stock"])
        inventory.add_product(product)
 
    print("Inventory loaded successfully.")
 
 
# Turn every Product object back into a dictionary and write them to inventory.json
def save_inventory(inventory):
    data = []   # list that will hold one dictionary per product
    for product in inventory.get_all_products():
        # Use the getters to read each product's private values
        data.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })
 
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
 
# Print the menu options
def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
 
 
# Option 2: ask the user for details, create a Product object, give it to the Inventory
def add_product_menu(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    name = input("Product Name: ").strip()
 
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:   # happens if the user types letters instead of a number
        print("Invalid number. Product not added.")
        return
 
    new_product = Product(product_id, name, price, stock)   # create the object
    if inventory.add_product(new_product):                 # Inventory stores it
        print("Product added successfully!")
 
 
# Option 3: find the product, then let the PRODUCT update its own stock
def update_stock_menu(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)
 
    if product is None:
        print("Product not found.")
        return
 
    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
 
    try:
        new_stock = int(input("New Stock Quantity: "))
    except ValueError:
        print("Invalid number. Stock not updated.")
        return
 
    # We don't change the stock ourselves - we ask the Product to do it
    if product.update_stock(new_stock):
        print("Stock updated successfully!")
 
 
# Option 4: search by ID and show the product's details
def search_product_menu(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)
 
    if product is None:
        print("Product not found.")
        return
 
    print("Product Found")
    print("-" * 48)
    print(f"ID: {product.get_product_id()}")
    print(f"Name: {product.get_name()}")
    print(f"Price: ${product.get_price():.2f}")
    print(f"Stock: {product.get_stock()}")
    print("-" * 48)
 
 
# The main loop: load the data, show the menu, and react to the user's choice
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 40)
 
    inventory = Inventory()     # create the one Inventory object
    load_inventory(inventory)   # fill it with Product objects from inventory.json
    show_menu()
 
    while True:
        choice = input("Enter option: ").strip()
        print()
 
        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_menu(inventory)
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")
 
        print()
 
 
# Only run the program when this file is run directly
if __name__ == "__main__":
    main()