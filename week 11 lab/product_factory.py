# product_factory.py
# FACTORY PATTERN: ProductFactory is the ONE place that decides which
# product class to create. The rest of the program just asks the factory
# for a Product, so it doesn't need to know about PhysicalProduct or DigitalProduct.

from product import Product                    # what the factory gives back
from physical_product import PhysicalProduct   # product that has a weight
from digital_product import DigitalProduct     # product that has a download size
from supplier import Supplier                  # needed for the type hint


class ProductFactory:

    # @staticmethod = you call it on the class itself: ProductFactory.create(...)
    # No ProductFactory object is needed, because the factory stores nothing.
    # weight and download_size are optional (default 0.0), since only one applies.
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, supplier: Supplier,
               weight: float = 0.0, download_size: float = 0.0) -> Product:
        product_type = product_type.strip().lower()   # " Physical " -> "physical"

        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier, weight)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, supplier,
                                  download_size)
        else:
            # Unknown type: raise an exception with a clear message
            raise ValueError(f"Unknown product type: {product_type}")
