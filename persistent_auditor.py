def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory = int(file.readline())

            transaction_history = []

            for line in file:
                transaction_history.append(int(line.strip()))

            return inventory, transaction_history

    except FileNotFoundError:
        return 0, []

def save_inventory(inventory, transaction_history):
    with open("inventory.txt", "w") as file:
        file.write(str(inventory) + "\n")

        for transaction in transaction_history:
            file.write(str(transaction) + "\n")

def get_valid_input():
    product_name = input("Enter Product Name (or type 'quit' to finish): ")

    if product_name == "quit":
        return "quit"

    elif not quantity.isdigit():
        print("Invalid input. Please enter a number.")
        return None

    return int(quantity)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory, transaction_history = load_inventory()
failed_entries = 0
deliveries_processed = 0

while True:
    quantity = get_valid_input()

    if quantity == "quit":
        save_inventory(inventory, transaction_history)
        break

    elif quantity is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, quantity)
    transaction_history.append(quantity)
    tax = calculate_tax(quantity)
    deliveries_processed += 1

    if inventory > 500:
        print("OVERSTOCK ALERT: Inventory exceeds 500 units.")
        break

generate_report(deliveries_processed, failed_entries)