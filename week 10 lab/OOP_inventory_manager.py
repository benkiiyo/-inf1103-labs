# OOP_inventory_manager.py
# INF1103 Lab 8 - main program (menu, user input, and saving/loading)
# Each class lives in its own file (one class per file).

import json   # read and write inventory.json
import os     # check whether inventory.json exists

from supplier import Supplier                  # who supplies each product
from product import Product                    # the abstract parent (for type hints)
from physical_product import PhysicalProduct   # product that has a weight
from digital_product import DigitalProduct     # product that has a download size
from can_be_shipped import CanBeShipped        # the shipping interface
from inventory import Inventory                # manages the list of products

FILENAME: str = "inventory.json"   # the file we save to and load from


# =====================================================================
# Supplier helper
# =====================================================================

# Reuse a Supplier we already have, or create a new one.
# This way two products from the same supplier share ONE Supplier object.
def get_or_create_supplier(suppliers: dict[str, Supplier], supplier_id: str,
                           name: str, email: str) -> Supplier:
    if supplier_id in suppliers:              # already known: reuse it
        return suppliers[supplier_id]
    supplier = Supplier(supplier_id, name, email)
    suppliers[supplier_id] = supplier         # remember it for next time
    return supplier


# =====================================================================
# File handling (load and save inventory.json)
# =====================================================================

# Read inventory.json and create the RIGHT kind of object for each product
def load_inventory(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    if not os.path.exists(FILENAME):
        print("inventory.json not found. Starting with an empty inventory.")
        return

    print("inventory.json found.")
    with open(FILENAME, "r") as file:
        data = json.load(file)   # a list of dictionaries

    for item in data:
        # Rebuild the Supplier (older files without one get "Unknown Supplier")
        supplier_data = item.get("supplier", {"id": "S000", "name": "Unknown Supplier",
                                              "email": "n/a"})
        supplier = get_or_create_supplier(suppliers, supplier_data["id"],
                                          supplier_data["name"], supplier_data["email"])

        # Use the saved type to decide which class to create
        if item.get("type", "physical") == "digital":
            product = DigitalProduct(item["id"], item["name"], item["price"],
                                     item["stock"], supplier, item.get("download_size", 0))
        else:
            product = PhysicalProduct(item["id"], item["name"], item["price"],
                                      item["stock"], supplier, item.get("weight", 0))
        inventory.add_product(product)

    print("Inventory loaded successfully.")


# Save every product to inventory.json
def save_inventory(inventory: Inventory) -> None:
    data = []
    for product in inventory.get_all_products():
        # Each product builds its own dictionary (type, extra attribute, supplier)
        data.append(product.to_dict())

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


# =====================================================================
# Menu and user input
# =====================================================================

# Print the menu options
def show_menu() -> None:
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# Ask for a supplier ID; reuse a known supplier or ask for the new one's details
def ask_for_supplier(suppliers: dict[str, Supplier]) -> Supplier:
    supplier_id = input("Supplier ID: ").strip().upper()
    if supplier_id in suppliers:
        supplier = suppliers[supplier_id]
        print(f"Using existing supplier: {supplier.get_name()}")
        return supplier
    name = input("New Supplier Name: ").strip()
    email = input("New Supplier Email: ").strip()
    return get_or_create_supplier(suppliers, supplier_id, name, email)


# Option 2: ask which type, then the details, then create the right object
def add_product_menu(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
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
            extra = float(input("Weight (kg): "))
        else:
            extra = float(input("Download Size (MB): "))
    except ValueError:   # happens if the user types letters instead of a number
        print("Invalid number. Product not added.")
        return

    supplier = ask_for_supplier(suppliers)   # the Supplier exists BEFORE the product

    if product_type == "physical":
        new_product: Product = PhysicalProduct(product_id, name, price, stock, supplier, extra)
    else:
        new_product = DigitalProduct(product_id, name, price, stock, supplier, extra)

    if inventory.add_product(new_product):   # Inventory stores the object
        print("Product added successfully!")


# Option 3: find the product, then let the PRODUCT update its own stock
def update_stock_menu(inventory: Inventory) -> None:
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.find_product(product_id)

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
def search_product_menu(inventory: Inventory) -> None:
    print("Search Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 48)
    product.display_information()                  # the product prints itself
    print(f"Fulfilment: {product.get_fulfilment_info()}")
    print("Supplier details:")
    product.get_supplier().display_information()   # reach the Supplier through the Product

    # Only products that signed the CanBeShipped contract have a shipping cost
    if isinstance(product, CanBeShipped):
        print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    print("-" * 48)


# The main loop: load the data, show the menu, and react to the user's choice
def main() -> None:
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 40)

    inventory = Inventory()                  # the one Inventory object
    suppliers: dict[str, Supplier] = {}      # known suppliers, looked up by ID
    load_inventory(inventory, suppliers)     # fill both from inventory.json
    show_menu()

    while True:
        choice = input("Enter option: ").strip()
        print()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_menu(inventory, suppliers)
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
