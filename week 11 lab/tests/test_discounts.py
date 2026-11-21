# tests/test_discounts.py
# Automated tests for the Strategy pattern (discounts and Order).
# Run all tests from the lab folder with: py -m unittest discover tests

import unittest   # Python's built-in testing tool

from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


class TestDiscounts(unittest.TestCase):

    # setUp runs before EVERY test, so each test starts with a fresh order of $250
    def setUp(self) -> None:
        supplier = Supplier("S001", "Logitech", "sales@logitech.com")
        chair = PhysicalProduct("P010", "Office Chair", 125.00, 10, supplier, 12.0)
        self.order = Order("O001")   # no discount given -> NoDiscount
        self.order.add_order_line(chair, 2)   # 2 x 125 = 250

    # Each strategy on its own
    def test_no_discount_returns_total_unchanged(self) -> None:
        self.assertEqual(NoDiscount().apply(100.0), 100.0)

    def test_percentage_discount_takes_percentage_off(self) -> None:
        self.assertAlmostEqual(PercentageDiscount(10).apply(250.0), 225.0)

    def test_bulk_discount_applies_at_threshold(self) -> None:
        self.assertEqual(BulkDiscount(200, 20).apply(200.0), 180.0)

    def test_bulk_discount_not_applied_below_threshold(self) -> None:
        self.assertEqual(BulkDiscount(200, 20).apply(199.0), 199.0)

    def test_student_discount_takes_five_percent_off(self) -> None:
        self.assertAlmostEqual(StudentDiscount().apply(100.0), 95.0)

    def test_invalid_percentage_is_rejected(self) -> None:
        with self.assertRaises(ValueError):   # passes only if ValueError is raised
            PercentageDiscount(150)

    # Order using strategies
    def test_order_defaults_to_no_discount(self) -> None:
        self.assertEqual(self.order.calculate_total(), 250.0)

    def test_order_with_bulk_discount(self) -> None:
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 230.0)

    def test_set_discount_changes_strategy(self) -> None:
        self.order.set_discount(BulkDiscount(200, 20))
        self.order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(self.order.calculate_total(), 225.0)


if __name__ == "__main__":
    unittest.main()
