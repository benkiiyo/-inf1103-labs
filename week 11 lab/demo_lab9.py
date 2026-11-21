# demo_lab9.py
# Runs each "Predict first" scenario for Lab 9 so you can compare with your predictions.
# Run with: py demo_lab9.py

from supplier import Supplier
from inventory import Inventory
from order import Order
from product_factory import ProductFactory
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount
from csv_loader import load_products

supplier = Supplier("S001", "Logitech", "sales@logitech.com")

# ---------------------------------------------------------------
# Predict first (2.3): an order adding up to 250, Bulk then Percentage
# ---------------------------------------------------------------
print("=== Strategy: switching discounts on one order ===")
chair = ProductFactory.create("physical", "P010", "Office Chair", 125.00, 10, supplier,
                              weight=12.0)
order = Order("O001", BulkDiscount(200, 20))
order.add_order_line(chair, 2)   # 2 x 125 = 250
print("With BulkDiscount(200, 20):", order.calculate_total())
order.set_discount(PercentageDiscount(10))
print("After set_discount(PercentageDiscount(10)):", order.calculate_total())

# 2.4: a brand new strategy, with NO changes to Order
order.set_discount(StudentDiscount())
print("After set_discount(StudentDiscount()):", order.calculate_total())

# Predict first (2.4): can two orders share ONE discount object?
shared_discount = PercentageDiscount(10)
order_a = Order("O002", shared_discount)
order_b = Order("O003", shared_discount)
order_a.add_order_line(chair, 1)
order_b.add_order_line(chair, 2)
print("Order O002 total:", order_a.calculate_total())
print("Order O003 total:", order_b.calculate_total())
print("(both orders use the same PercentageDiscount object)")

# ---------------------------------------------------------------
# Predict first (3.2): asking the factory for an unknown type
# ---------------------------------------------------------------
print("\n=== Factory: unknown product type ===")
try:
    ProductFactory.create("service", "S001", "Installation", 30.00, 5, supplier)
except ValueError as error:
    # Without this try/except, the program would CRASH here with a traceback
    print("Caught ValueError:", error)

# ---------------------------------------------------------------
# Validation: rules each class protects
# ---------------------------------------------------------------
print("\n=== Validation ===")
try:
    ProductFactory.create("physical", "P011", "Free Thing", 0, 5, supplier)
except ValueError as error:
    print("Price 0:", error)
try:
    ProductFactory.create("digital", "D011", "Ebook", 9.99, -1, supplier)
except ValueError as error:
    print("Stock -1:", error)
try:
    order.add_order_line(chair, 0)
except ValueError as error:
    print("Order quantity 0:", error)

# ---------------------------------------------------------------
# Predict first (5.2): loading products.csv, then a missing file
# ---------------------------------------------------------------
print("\n=== Loading products.csv ===")
inventory = Inventory()
load_products("products.csv", inventory, supplier)
inventory.display_all()

print("\n=== Loading a file that doesn't exist ===")
load_products("products_renamed.csv", inventory, supplier)
