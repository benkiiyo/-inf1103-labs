import json
import os

FILENAME = "inventory.json"

def load_inventory():
    if not os.path.exists(FILENAME):
        print("inventory.json not found. Starting with an empty inventory.")
        return []

    print("inventory.json found.")
    with open(FILENAME, "r") as file:
        inventory = json.load(file)
    print("Inventory loaded successfully.")
    return inventory


def display_all(inventory):
    print("Current Inventory")
    print("-" * 48)
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)

inventory = load_inventory()
display_all(inventory)