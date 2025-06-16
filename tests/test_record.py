import unittest
import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.record import Record

class TestRecord(unittest.TestCase):
    def test_record_initialization(self):
        rec = Record("TestRegion", "Func", "Origin", "Product", "Date",
                     "Type", "Component", "Result", "Unit", "Plan")
        # Verifies region attribute
        self.assertEqual(rec.region, "TestRegion")
        self.assertEqual(rec.plan_code, "Plan")

if __name__ == '__main__':
    unittest.main()
