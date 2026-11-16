from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):

    BASE_SHIPPING_FEE: float = 5.00
    COST_PER_KG: float = 2.00

    # Create a physical product: all the normal product details + weight
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, weight: float) -> None:
        # super() = the parent class: reuse Product's __init__ for the common details
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = float(weight)   # the extra attribute, in kilograms

    # Getter: return the weight
    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"    Type: Physical | Weight: {self.__weight:.2f} kg")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    # Rule: $5 base fee + $2 per kg
    def calculate_shipping_cost(self) -> float:
        return self.BASE_SHIPPING_FEE + self.COST_PER_KG * self.__weight
