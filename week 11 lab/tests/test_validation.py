# tests/test_validation.py
# Automated tests for validation rules in Product and OrderLine.

import unittest

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


class TestValidation(unittest.TestCase):

    def setUp(self) -> None:
        self.supplier = Supplier("S001", "Logitech", "sales@logitech.com")

    def test_price_of_zero_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            PhysicalProduct("P001", "Lamp", 0, 10, self.supplier, 1.0)

    def test_negative_price_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            DigitalProduct("D001", "Editor", -5, 10, self.supplier, 100)

    def test_text_price_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            PhysicalProduct("P001", "Lamp", "abc", 10, self.supplier, 1.0)

    def test_negative_stock_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            PhysicalProduct("P001", "Lamp", 25.0, -1, self.supplier, 1.0)

    def test_update_stock_rejects_negative_for_both_types(self) -> None:
        # LSP: both subclasses keep Product's stock rule
        lamp = PhysicalProduct("P001", "Lamp", 25.0, 10, self.supplier, 1.0)
        editor = DigitalProduct("D001", "Editor", 49.9, 10, self.supplier, 100)
        for product in (lamp, editor):
            with self.assertRaises(ValueError):
                product.update_stock(-1)

    def test_valid_stock_update_works(self) -> None:
        lamp = PhysicalProduct("P001", "Lamp", 25.0, 10, self.supplier, 1.0)
        lamp.update_stock(0)
        self.assertEqual(lamp.get_stock(), 0)

    def test_order_quantity_of_zero_is_rejected(self) -> None:
        lamp = PhysicalProduct("P001", "Lamp", 25.0, 10, self.supplier, 1.0)
        order = Order("O001")
        with self.assertRaises(ValueError):
            order.add_order_line(lamp, 0)


if __name__ == "__main__":
    unittest.main()
