# Quick checks for the Lab 7 classes. Run with: py test_classes.py

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped

# --- Test 1: create one of each and display them (inheritance + overriding) ---
print("=== Test 1: display_information() ===")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5)
game = DigitalProduct("D001", "Video Game", 59.99, 100, 45000)
laptop.display_information()   # common details + weight
game.display_information()     # common details + download size

# --- Test 2: each child has its own get_fulfilment_info() ---
print("\n=== Test 2: get_fulfilment_info() ===")
print("Laptop:", laptop.get_fulfilment_info())
print("Video Game:", game.get_fulfilment_info())

# --- Test 3: shipping cost for different weights (interface) ---
print("\n=== Test 3: calculate_shipping_cost() ===")
for weight in [0.5, 2.5, 10]:
    item = PhysicalProduct("T001", "Test Box", 10.00, 1, weight)
    print(f"{weight} kg -> shipping ${item.calculate_shipping_cost():.2f}")

# --- Test 4: digital products are not shippable ---
print("\n=== Test 4: is the digital product shippable? ===")
print("Laptop can be shipped:", isinstance(laptop, CanBeShipped))       # True
print("Video Game can be shipped:", isinstance(game, CanBeShipped))     # False

# --- Test 5: try to create a plain Product (should fail - it's abstract) ---
print("\n=== Test 5: create a plain Product ===")
try:
    plain = Product("X001", "Mystery", 1.00, 1)
except TypeError as error:   # Python raises TypeError for abstract classes
    print("Could not create Product:", error)
