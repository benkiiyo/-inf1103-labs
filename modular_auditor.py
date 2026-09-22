def get_valid_input():
    quantity = input("Enter stock quantity (or type 'quit' to finish): ")

    if quantity == "quit":
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
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory = 0
failed_entries = 0

while True:
    quantity = get_valid_input()

    if quantity == "quit":
        break

    elif quantity is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, quantity)
    tax = calculate_tax(quantity)

generate_report(inventory, failed_entries)