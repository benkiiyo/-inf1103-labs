inventory = 0
failed_entries = 0

while True:
    quantity = input("Enter stock quantity (or type 'quit' to finish): ")

    if quantity == "quit":
        break

    elif not quantity.isdigit():
        print("Invalid input. Please enter a number.")
        failed_entries += 1
        continue

    quantity = int(quantity)
    inventory += quantity

    if inventory > 500:
        print("OVERSTOCK ALERT: Inventory exceeds 500 units.")
        break

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)