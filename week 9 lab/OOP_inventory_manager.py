import json   # read and write inventory.json
import os     # check whether inventory.json exists

from physical_product import PhysicalProduct   # product that has a weight
from digital_product import DigitalProduct     # product that has a download size
from can_be_shipped import CanBeShipped        # the shipping interface
from inventory import Inventory                # manages the list of products

FILENAME = "inventory.json"   # the file we save to and load from


# =====================================================================
# File handling (load and save inventory.json)
# =====================================================================

# Read inventory.json and create the RIGHT kind of object for each product
def load_inventory(inventory):
    if not os.path.exists(FILENAME):
        print("inventory.json not found. Starting with an empty inventory.")
        return

    print("inventory.json found.")
    with open(FILENAME, "r") as file:
        data = json.load(file)   # a list of dictionaries

    for item in data:
        # Old Week 5/6 products have no "type", so treat them as physical
        product_type = item.get("type", "physical")

        # Use the type to decide which class to create
        if product_type == "digital":
            product = DigitalProduct(item["id"], item["name"], item["price"],
                                     item["stock"], item.get("download_size", 0))
        else:
            product = PhysicalProduct(item["id"], item["name"], item["price"],
                                      item["stock"], item.get("weight", 0))
        inventory.add_product(product)

    print("Inventory loaded successfully.")


# Save every product to inventory.json
def save_inventory(inventory):
    data = []
    for product in inventory.get_all_products():
        # Each product builds its own dictionary (including its type),
        # so this function doesn't need to know about weight or download size
        data.append(product.to_dict())

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


# =====================================================================
# Menu and user input
# =====================================================================

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


# Option 2: ask which type, then the details, then create the right object
def add_product_menu(inventory):
    print("Add New Product")

    # Keep asking until the user picks a valid type
    while True:
        product_type = input("Type (physical/digital): ").strip().lower()
        if product_type in ("physical", "digital"):
            break
        print("Please type 'physical' or 'digital'.")

    product_id = input("Product ID: ").strip().upper()
    name = input("Product Name: ").strip()

    try:
        # .replace("$", "") so "$30.00" works as well as "30.00"
        price = float(input("Price: ").replace("$", ""))
        stock = int(input("Stock Quantity: "))

        # Ask for the extra detail that only this type has
        if product_type == "physical":
            weight = float(input("Weight (kg): "))
            new_product = PhysicalProduct(product_id, name, price, stock, weight)
        else:
            download_size = float(input("Download Size (MB): "))
            new_product = DigitalProduct(product_id, name, price, stock, download_size)
    except ValueError:   # happens if the user types letters instead of a number
        print("Invalid number. Product not added.")
        return

    if inventory.add_product(new_product):   # Inventory stores the object
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

    if product.update_stock(new_stock):
        print("Stock updated successfully!")


# Option 4: search by ID and show everything about the product
def search_product_menu(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 48)
    product.display_information()                  # the product prints itself
    print(f"Fulfilment: {product.get_fulfilment_info()}")

    # Only products that signed the CanBeShipped contract have a shipping cost
    if isinstance(product, CanBeShipped):
        print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    print("-" * 48)


# The main loop: load the data, show the menu, and react to the user's choice
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 40)

    inventory = Inventory()     # create the one Inventory object
    load_inventory(inventory)   # fill it with product objects from inventory.json
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
