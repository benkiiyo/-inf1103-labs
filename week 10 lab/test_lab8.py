from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


# Test 1: ASSOCIATION between Supplier and Product
print("=== Test 1: Association (Supplier and Product) ===")

# Create the Supplier FIRST, on its own
supplier = Supplier("S001", "Logitech", "sales@logitech.com")

# Give the SAME supplier object to two different products
mouse = PhysicalProduct("P002", "Mouse", 25.50, 50, supplier, 0.2)
app = DigitalProduct("D003", "Logi Options+", 19.99, 999, supplier, 500)

# Each product can reach its supplier through the reference it stores
print("Mouse's supplier:")
mouse.get_supplier().display_information()
print("App's supplier:")
app.get_supplier().display_information()

# "is" checks whether two name tags point at the SAME object
print("Both products point to the same Supplier object:",
      mouse.get_supplier() is app.get_supplier())

del supplier

print("\nAfter 'del supplier':")
mouse.display_information()
app.display_information()


# Test 2: AGGREGATION between Inventory and Product
from inventory import Inventory

print("\n=== Test 2: Aggregation (Inventory and Product) ===")

# Step 1: create the Product BEFORE any Inventory exists
supplier2 = Supplier("S002", "Dell", "orders@dell.com")
monitor = PhysicalProduct("P004", "Monitor", 299.99, 10, supplier2, 5.0)

# Step 2: create two inventories and add the monitor to Inventory A
inventory_a = Inventory()
inventory_b = Inventory()
inventory_a.add_product(monitor)
print("Inventory A:")
inventory_a.display_all()

removed = inventory_a.remove_product("P004")
print("\nAfter removing P004 from Inventory A:")
inventory_a.display_all()

print("Is the monitor still usable?")
monitor.display_information()
print("Shipping cost:", f"${monitor.calculate_shipping_cost():.2f}")
print("Removed object is the same monitor:", removed is monitor)

# Step 4: add the SAME monitor object to Inventory B (a transfer)
inventory_b.add_product(monitor)
print("\nInventory B after the transfer:")
inventory_b.display_all()


# Test 3: COMPOSITION between Order and OrderLine
from order import Order

print("\n=== Test 3: Composition (Order and OrderLine) ===")

keyboard = PhysicalProduct("P003", "Keyboard", 45.00, 25, supplier2, 0.8)

# The Order creates its own OrderLines from a product + quantity
order_1 = Order("O001")
order_1.add_order_line(mouse, 2)
order_1.add_order_line(keyboard, 1)
order_1.add_order_line(app, 1)
order_1.display_information()

order_2 = Order("O002")
order_2.add_order_line(mouse, 5)
order_2.display_information()

line_in_order_1 = order_1.get_order_lines()[0]   # the mouse line in order 1
line_in_order_2 = order_2.get_order_lines()[0]   # the mouse line in order 2
print("Same OrderLine object in both orders:", line_in_order_1 is line_in_order_2)
print("Same Product object in both lines:",
      line_in_order_1.get_product() is line_in_order_2.get_product())
print("id() of the two OrderLines:", id(line_in_order_1), id(line_in_order_2))
print("id() of the mouse in each :", id(line_in_order_1.get_product()),
      id(line_in_order_2.get_product()))

# Remove a line THROUGH the Order (the owner), not on its own
order_1.remove_order_line("P003")
print("\nOrder O001 after removing the keyboard line:")
order_1.display_information()

# Remove the whole order: its lines go with it, but the mouse product remains
del order_2
print("After deleting order O002, the mouse product still exists:")
mouse.display_information()


# Test 4: LISKOV SUBSTITUTION - any Product works where a Product is expected
from product import Product

print("\n=== Test 4: Liskov Substitution ===")


# This function only knows about Product - not Physical or Digital
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


show_product_details(monitor)
show_product_details(app)

print("Update monitor stock to 7:", monitor.update_stock(7))
print("Update app stock to 7:", app.update_stock(7))
print("Update app stock to -1:", app.update_stock(-1))


# Test 5: POLYMORPHISM - one loop, every Product behaves its own way
print("\n=== Test 5: Polymorphism ===")

store = Inventory()
store.add_product(monitor)
store.add_product(keyboard)
store.add_product(app)

for product in store.get_all_products():
    product.display_information()
    print("  ->", product.get_fulfilment_info())
