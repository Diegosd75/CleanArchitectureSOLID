import unittest
from app.entities.product import Product
from app.services.cart_service import CartService

class TestCartService(unittest.TestCase):
    def setUp(self):
        self.cart_service = CartService()
        self.product1 = Product(id=1, name="Product 1", price=10.0)
        self.product2 = Product(id=2, name="Product 2", price=20.0)

    def test_add_product(self):
        self.cart_service.add_product(self.product1)
        self.assertEqual(len(self.cart_service.cart.products), 1)
        self.assertEqual(self.cart_service.cart.products[0].name, "Product 1")

    def test_remove_product(self):
        self.cart_service.add_product(self.product1)
        self.cart_service.add_product(self.product2)
        self.cart_service.remove_product(self.product1.id)
        self.assertEqual(len(self.cart_service.cart.products), 1)
        self.assertEqual(self.cart_service.cart.products[0].name, "Product 2")

    def test_get_total(self):
        self.cart_service.add_product(self.product1)
        self.cart_service.add_product(self.product2)
        total = self.cart_service.get_total()
        self.assertEqual(total, 30.0)

if __name__ == "__main__":
    unittest.main()
