# physical_product.py
# A PhysicalProduct "is-a" Product that also has a weight.
# It inherits from Product (its parent class) and also signs the
# CanBeShipped contract (interface), because physical items get shipped.

from product import Product                 # the parent class
from supplier import Supplier               # needed for the supplier type hint
from can_be_shipped import CanBeShipped     # the interface


class PhysicalProduct(Product, CanBeShipped):

    BASE_SHIPPING_FEE: float = 5.00   # every shipment costs at least $5
    COST_PER_KG: float = 2.00         # plus $2 for every kilogram

    # Create a physical product: all the normal product details + weight
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, weight: float) -> None:
        # super() = the parent class: reuse Product's __init__ for the common details
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = float(weight)   # the extra attribute, in kilograms

    # Getter: return the weight
    def get_weight(self) -> float:
        return self.__weight

    # OVERRIDING: parent prints the common details, then we add the weight
    def display_information(self) -> None:
        super().display_information()
        print(f"    Type: Physical | Weight: {self.__weight:.2f} kg")

    # OVERRIDING: add the type and weight to the parent's dictionary
    def to_dict(self) -> dict:
        data = super().to_dict()   # start with the common details from Product
        data["type"] = "physical"  # so loading knows which class to create
        data["weight"] = self.__weight
        return data

    # Required by Product (the abstract method)
    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    # Required by CanBeShipped (the interface)
    # Rule: $5 base fee + $2 per kg
    def calculate_shipping_cost(self) -> float:
        return self.BASE_SHIPPING_FEE + self.COST_PER_KG * self.__weight
