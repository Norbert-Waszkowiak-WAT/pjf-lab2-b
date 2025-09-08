import unittest
from solution import Shop, Supplier, Bread, Notebook

class TestNoDuplicates(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()
        self.supplier = Supplier(self.shop)
        self.bread = Bread()
        self.notebook = Notebook()

    def test_no_duplicate_food_products(self):
        self.supplier.deliver_product(self.bread)
        self.supplier.deliver_product(self.bread)
        self.assertEqual(self.shop.food_products.count(self.bread), 1)

    def test_no_duplicate_paper_products(self):
        self.supplier.deliver_product(self.notebook)
        self.supplier.deliver_product(self.notebook)
        self.assertEqual(self.shop.paper_products.count(self.notebook), 1)

if __name__ == '__main__':
    unittest.main()