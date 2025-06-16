import unittest
from app.models.record import Record

class TestTemp(unittest.TestCase):
    def test_init(self):
        r = Record("region", "func", "origin", "product", "date", "test", "comp", "res", "unit", "plan")
        self.assertEqual(r.region, "region")

if __name__ == "__main__":
    unittest.main()
