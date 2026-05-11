from fastapi import FastAPI
import requests

app = FastAPI()

USER_SERVICE = "http://127.0.0.1:8001"
PRODUCT_SERVICE = "http://127.0.0.1:8002"
ORDER_SERVICE = "http://127.0.0.1:8003"


@app.get("/")
def home():
    return {"message": "API Gateway for Online Shopping"}


@app.get("/users")
def users():
    return requests.get(f"{USER_SERVICE}/users").json()


@app.get("/products")
def products():
    return requests.get(f"{PRODUCT_SERVICE}/products").json()


@app.get("/orders")
def orders():
    return requests.get(f"{ORDER_SERVICE}/orders").json()