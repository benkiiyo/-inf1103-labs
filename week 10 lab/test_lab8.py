from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


# Test 1: ASSOCIATION between Supplier and Product
print("=== Test 1: Association (Supplier and Product) ===")

# Create the Supplier FIRST, on its own
supplier = Supplier("S001", "Logitech", "sales@logitech.com")

# Give the SAME supplier object to two different products
mouse = PhysicalProduct("P002", "Mouse", 25.50, 50, supplier, 0.2)
app = DigitalProduct("D003", "Logi Options+", 0.00, 999, supplier, 500)

# Each product can reach its supplier through the reference it stores
print("Mouse's supplier:")
mouse.get_supplier().display_information()
print("App's supplier:")
app.get_supplier().display_information()

# "is" checks whether two name tags point at the SAME object
print("Both products point to the same Supplier object:",
      mouse.get_supplier() is app.get_supplier())

# PREDICT FIRST: what happens to the products' supplier after this line?
del supplier

print("\nAfter 'del supplier':")
mouse.display_information()
app.display_information()
