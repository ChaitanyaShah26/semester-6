from fastapi import FastAPI, HTTPException
from database import collection
from utils import generate_short_code

app = FastAPI(title="Main API (MongoDB)")

@app.post("/shorten")
def shorten_url(data: dict):
    short_code = generate_short_code()

    document = {
        "short_code": short_code,
        "original_url": data["url"]
    }

    collection.insert_one(document)

    return {
        "short_url": f"http://localhost:5000/go/{short_code}"
    }

@app.get("/go/{code}")
def redirect(code: str):
    url = collection.find_one({"short_code": code})

    if not url:
        raise HTTPException(status_code=404, detail="Not found")

    return {"redirect_to": url["original_url"]}