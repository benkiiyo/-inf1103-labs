from product import Product
from supplier import Supplier


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

    def display_information(self) -> None:
        super().display_information()
        print(f"    Type: Digital | Download size: {self.__download_size:.2f} MB")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally via a download link."
