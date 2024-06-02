import pytest
from app.entities.product import Product
from app.services.cart_service import CartService

@pytest.fixture
def cart_service():
    return CartService()

def test_add_product(cart_service):
    product = Product(id=1, name="Product 1", price=10.0)
    cart_service.add_product(product)
    assert len(cart_service.cart.products) == 1
    assert cart_service.cart.products[0].name == "Product 1"

def test_remove_product(cart_service):
    product1 = Product(id=1, name="Product 1", price=10.0)
    product2 = Product(id=2, name="Product 2", price=20.0)
    cart_service.add_product(product1)
    cart_service.add_product(product2)
    cart_service.remove_product(product1.id)
    assert len(cart_service.cart.products) == 1
    assert cart_service.cart.products[0].name == "Product 2"

def test_get_total(cart_service):
    product1 = Product(id=1, name="Product 1", price=10.0)
    product2 = Product(id=2, name="Product 2", price=20.0)
    cart_service.add_product(product1)
    cart_service.add_product(product2)
    total = cart_service.get_total()
    assert total == 30.0

def test_add_product_with_negative_price(cart_service):
    product = Product(id=3, name="Product 3", price=-5.0)
    with pytest.raises(ValueError):
        cart_service.add_product(product)
