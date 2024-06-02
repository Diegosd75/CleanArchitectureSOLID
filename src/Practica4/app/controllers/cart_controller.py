from flask import Flask, request, jsonify
from app.entities.product import Product
from app.services.cart_service import CartService

app = Flask(__name__)
cart_service = CartService()

@app.route('/cart/add', methods=['POST'])
def add_product():
    data = request.json
    product = Product(id=data['id'], name=data['name'], price=data['price'])
    cart_service.add_product(product)
    return jsonify({"message": "Product added to cart"}), 201

@app.route('/cart/remove/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    cart_service.remove_product(product_id)
    return jsonify({"message": "Product removed from cart"}), 200

@app.route('/cart/total', methods=['GET'])
def get_total():
    total = cart_service.get_total()
    return jsonify({"total": total}), 200
