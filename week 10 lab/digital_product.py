from product import Product   # the parent class
from supplier import Supplier   # needed for the supplier type hint


class DigitalProduct(Product):

    # Create a digital product: all the normal product details + download size
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float) -> None:
        # Reuse Product's __init__ for ID/name/price/stock
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = float(download_size)   # the extra attribute, in MB

    # Getter: return the download size
    def get_download_size(self):
        return self.__download_size

    # OVERRIDING: our own version of display_information()
    def display_information(self):
        super().display_information()   # parent prints the common details first
        print(f"    Type: Digital | Download size: {self.__download_size:.2f} MB")

    # OVERRIDING: add the type and download size to the parent's dictionary
    def to_dict(self):
        data = super().to_dict()   # start with id/name/price/stock from Product so loading knows which class to create
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    # Required by Product (the abstract method)
    def get_fulfilment_info(self):
        return "This product is delivered digitally via a download link."
