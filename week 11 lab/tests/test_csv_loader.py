# tests/test_csv_loader.py
# Automated tests for load_products(): bad rows are skipped, a missing file doesn't crash.

import os
import tempfile
import unittest

from supplier import Supplier
from inventory import Inventory
from csv_loader import load_products

# The same rows as products.csv: 3 good rows, 1 unknown type, 1 bad price
CSV_TEXT = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


class TestLoadProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.supplier = Supplier("S001", "Logitech", "sales@logitech.com")
        self.inventory = Inventory()
        # Write a temporary CSV file for the test to read
        self.temp_file = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                                     newline="")
        self.temp_file.write(CSV_TEXT)
        self.temp_file.close()

    # tearDown runs after EVERY test: delete the temporary file
    def tearDown(self) -> None:
        os.remove(self.temp_file.name)

    def test_valid_rows_load_and_bad_rows_are_skipped(self) -> None:
        load_products(self.temp_file.name, self.inventory, self.supplier)
        ids = [p.get_product_id() for p in self.inventory.get_all_products()]
        self.assertEqual(ids, ["P001", "D001", "P003"])

    def test_missing_file_does_not_crash(self) -> None:
        load_products("this_file_does_not_exist.csv", self.inventory, self.supplier)
        self.assertEqual(len(self.inventory.get_all_products()), 0)


if __name__ == "__main__":
    unittest.main()
