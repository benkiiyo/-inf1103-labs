# csv_loader.py
# Reads products from a CSV file, creates each one through the ProductFactory,
# and adds it to an Inventory. Uses try / except / else / finally so that a
# missing file or a bad row never crashes the program.

import csv   # Python's built-in tool for reading CSV files

from inventory import Inventory               # where loaded products go
from supplier import Supplier                 # every loaded product gets this supplier
from product_factory import ProductFactory    # creates the right kind of product


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")   # try to open the file
    except FileNotFoundError:
        # Runs ONLY if the file doesn't exist
        print(f"Products file not found: {path}")
    else:
        # Runs ONLY if the file opened successfully
        loaded = 0
        with file:   # makes sure the file gets closed afterwards
            reader = csv.reader(file)
            next(reader)   # skip the header row (product_type,product_id,...)

            for row in reader:
                # Each row gets its OWN try, so one bad row doesn't stop the rest
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(product_type, product_id, name,
                                                    float(price), int(stock), supplier)
                    if inventory.add_product(product):   # False if the ID is already used
                        loaded += 1
                except ValueError as error:
                    # Report the bad row and carry on with the next one
                    print(f"Skipped row {row}: {error}")

        print(f"{loaded} products loaded.")
    finally:
        # Runs EVERY time, whether the file was found or not
        print("Load attempt finished.")
