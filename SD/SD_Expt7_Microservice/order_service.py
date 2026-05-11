from fastapi import FastAPI
import requests
import json

app = FastAPI()

DATA_FILE = "data.json"

USER_SERVICE = "http://127.0.0.1:8001/users"
PRODUCT_SERVICE = "http://127.0.0.1:8002/products"


def read_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.get("/orders")
def get_orders():
    data = read_data()
    return data["orders"]


@app.post("/create_order")
def create_order(user_id: int, product_id: int):

    users = requests.get(USER_SERVICE).json()
    products = requests.get(PRODUCT_SERVICE).json()

    user = next((u for u in users if u["id"] == user_id), None)
    product = next((p for p in products if p["id"] == product_id), None)

    if not user:
        return {"error": "User not found"}

    if not product:
        return {"error": "Product not found"}

    data = read_data()

    order = {
        "id": len(data["orders"]) + 1,
        "user": user["name"],
        "product": product["name"],
        "price": product["price"]
    }

    data["orders"].append(order)
    write_data(data)

    return {"message": "Order created", "order": order}