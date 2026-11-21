# tests/test_factory.py
# Automated tests for the Factory pattern (ProductFactory).

import unittest

from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory


class TestProductFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.supplier = Supplier("S001", "Logitech", "sales@logitech.com")

    def test_creates_physical_product(self) -> None:
        product = ProductFactory.create("physical", "P001", "Lamp", 25.0, 10,
                                        self.supplier, weight=1.5)
        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.get_weight(), 1.5)

    def test_creates_digital_product(self) -> None:
        product = ProductFactory.create("digital", "D001", "Editor", 49.9, 100,
                                        self.supplier, download_size=800)
        self.assertIsInstance(product, DigitalProduct)
        self.assertEqual(product.get_download_size(), 800)

    def test_type_is_not_case_sensitive(self) -> None:
        product = ProductFactory.create(" Physical ", "P002", "Chair", 80.0, 3, self.supplier)
        self.assertIsInstance(product, Product)

    def test_unknown_type_raises_value_error(self) -> None:
        with self.assertRaises(ValueError) as context:
            ProductFactory.create("service", "S001", "Installation", 30.0, 5, self.supplier)
        self.assertIn("Unknown product type", str(context.exception))   # clear message


if __name__ == "__main__":
    unittest.main()
