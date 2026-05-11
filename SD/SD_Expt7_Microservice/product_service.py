from fastapi import FastAPI
import json

app = FastAPI()

DATA_FILE = "data.json"


def read_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.get("/products")
def get_products():
    data = read_data()
    return data["products"]


@app.post("/add_product")
def add_product(name: str, price: int):
    data = read_data()

    new_product = {
        "id": len(data["products"]) + 1,
        "name": name,
        "price": price
    }

    data["products"].append(new_product)
    write_data(data)

    return {"message": "Product added", "product": new_product}