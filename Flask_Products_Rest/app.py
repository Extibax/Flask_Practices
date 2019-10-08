""" Imports """
from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route("/ping")
def ping():
    return jsonify({"Message": "Pong"})


@app.route("/products")
def get_products():
    return jsonify({"Products": products, "Message": "Product's List"})


@app.route("/products/<string:product_name>")
def get_product(product_name):
    product_fund = [
        product for product in products if product['name'] == product_name]
    if (len(product_fund) > 0):
        return jsonify({"Product": product_fund[0]})
    return jsonify({"Message": "Product not found"})


@app.route("/products", methods=["POST"])
def add_product():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"Message": "Product added succesfully", "Products": products})


@app.route("/products/<string:product_name>", methods=["PUT"])
def edit_product(product_name):
    product_found = [
        product for product in products if product["name"] == product_name]
    if (len(product_found) > 0):
        product_found[0]["name"] = request.json["name"]
        product_found[0]["price"] = request.json["price"]
        product_found[0]["quantity"] = request.json["quantity"]
        return jsonify({
            "Message": "Product Updated",
            "Product": product_found[0]
        })
    return jsonify({"message": "Product not found"})


@app.route("/products/<string:product_name>", methods=["DELETE"])
def delete_product(product_name):
    product_found = [
        product for product in products if product["name"] == product_name]
    if (len(product_found) > 0):
        products.remove(product_found[0])
        return jsonify({
            "Message": "Product deleted",
            "Products": products
        })
    return jsonify({"Message": "Product not found"})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
