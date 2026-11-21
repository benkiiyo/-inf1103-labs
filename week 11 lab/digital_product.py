# digital_product.py
# A DigitalProduct "is-a" Product that has a download size instead of a weight.
# It does NOT sign CanBeShipped, because digital products aren't shipped.

from product import Product     # the parent class
from supplier import Supplier   # needed for the supplier type hint


class DigitalProduct(Product):

    # Create a digital product: all the normal product details + download size
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float) -> None:
        # Reuse Product's __init__ for the common details
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = float(download_size)   # in megabytes

    # Getter: return the download size
    def get_download_size(self) -> float:
        return self.__download_size

    # OVERRIDING: parent prints the common details, then we add the download size
    def display_information(self) -> None:
        super().display_information()
        print(f"    Type: Digital | Download size: {self.__download_size:.2f} MB")

    # OVERRIDING: add the type and download size to the parent's dictionary
    def to_dict(self) -> dict:
        data = super().to_dict()   # start with the common details from Product
        data["type"] = "digital"   # so loading knows which class to create
        data["download_size"] = self.__download_size
        return data

    # Required by Product (the abstract method)
    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally via a download link."
