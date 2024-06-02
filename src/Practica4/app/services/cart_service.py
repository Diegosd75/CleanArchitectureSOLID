from app.entities.cart import Cart

class CartService:
    def __init__(self):
        self.cart = Cart()

    def add_product(self, product):
        self.cart.add_product(product)

    def remove_product(self, product_id):
        self.cart.remove_product(product_id)

    def get_total(self):
        return self.cart.get_total()
