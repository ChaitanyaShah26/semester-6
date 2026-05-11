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


@app.get("/users")
def get_users():
    data = read_data()
    return data["users"]


@app.post("/add_user")
def add_user(name: str):
    data = read_data()

    new_user = {
        "id": len(data["users"]) + 1,
        "name": name
    }

    data["users"].append(new_user)
    write_data(data)

    return {"message": "User added", "user": new_user}