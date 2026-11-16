from product import Product                 # the parent class
from supplier import Supplier               # needed for the supplier type hint
from can_be_shipped import CanBeShipped     # the interface


class PhysicalProduct(Product, CanBeShipped):

    BASE_SHIPPING_FEE = 5.00   # every shipment costs at least $5
    COST_PER_KG = 2.00         # plus $2 for every kilogram

    # Create a physical product: all the normal product details + weight
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, weight: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = float(weight)   # the extra attribute, in kilograms

    # Getter: return the weight
    def get_weight(self):
        return self.__weight

    # OVERRIDING: our own version of display_information()
    def display_information(self):
        super().display_information()   # parent prints the common details first
        print(f"    Type: Physical | Weight: {self.__weight:.2f} kg")   # then we add ours

    # OVERRIDING: add the type and weight to the parent's dictionary
    def to_dict(self):
        data = super().to_dict()   # start with id/name/price/stock from Product
        data["type"] = "physical"  # so loading knows which class to create
        data["weight"] = self.__weight
        return data

    # Required by Product (the abstract method)
    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    # Required by CanBeShipped (the interface)
    # Rule: $5 base fee + $2 per kg
    def calculate_shipping_cost(self):
        return self.BASE_SHIPPING_FEE + self.COST_PER_KG * self.__weight
