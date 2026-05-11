from fastapi import FastAPI, HTTPException
from database import collection

app = FastAPI(title="Backup API (MongoDB)")

@app.get("/go/{code}")
def redirect(code: str):
    url = collection.find_one({"short_code": code})

    if not url:
        raise HTTPException(status_code=404, detail="Not found")

    return {"redirect_to": url["original_url"]}