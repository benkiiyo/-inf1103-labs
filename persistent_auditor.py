FILENAME = "inventory.txt"
FIRST_ORDER_ID = 1001
OVERSTOCK_LIMIT = 500

def load_inventory():
    try:
        with open(FILENAME, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return 0, []

    if not lines:
        return 0, []

    try:
        inventory = int(lines[0])
        orders = []
        for line in lines[1:]:
            order_id, name, quantity = [part.strip() for part in line.split(",")]
            orders.append((int(order_id), name, int(quantity)))
        return inventory, orders
    except ValueError:
        print("Warning: inventory.txt is corrupted. Starting with an empty inventory.")
        return 0, []

def display_orders(orders):
    print("Current Orders:")
    if not orders:
        print("  (No previous orders found)")
    else:
        for order_id, name, quantity in orders:
            print(f"{order_id}, {name}, {quantity}")
    print("-" * 33)

def save_inventory(inventory, transaction_history):
    with open("inventory.txt", "w") as file:
        file.write(str(inventory) + "\n")

        for transaction in transaction_history:
            file.write(str(transaction) + "\n")

def get_valid_input():
    product_name = input("Enter Product Name (or 'quit' to exit): ").strip()

    if product_name.lower() == "quit":
        return "quit"

    if product_name == "" or "," in product_name:
        print("Invalid product name.")
        return None

    quantity = input("Enter Quantity: ").strip()

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid input. Please enter a positive whole number.")
        return None

    return product_name, int(quantity)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_transactions, total_units, failed_attempts):
    print("=== Audit Report ===")
    print("Total Transactions Recorded:", total_transactions)
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory, orders = load_inventory()
display_orders(orders)

failed_entries = 0
transactions = 0
units_processed = 0

while True:
    result = get_valid_input()

    if result == "quit":
        break

    if result is None:
        failed_entries += 1
        print()
        continue

    product_name, quantity = result
    order_id = FIRST_ORDER_ID + len(orders)
    orders.append((order_id, product_name, quantity))
    inventory = process_delivery(inventory, quantity)
    tax = calculate_tax(quantity)
    transactions += 1
    units_processed += quantity

    print()
    print("New Order Added:")
    print(f"{order_id}, {product_name}, {quantity}")
    print(f"Tax: ${tax:.2f} | Total Inventory: {inventory}")
    print()

    if inventory > OVERSTOCK_LIMIT:
        print("OVERSTOCK ALERT: Inventory exceeds 500 units.")
        break

print()
generate_report(transactions, units_processed, failed_entries)