from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from models import insert_url, get_url
from cache import get_from_cache, set_cache
from utils import generate_code

app = FastAPI()

# Request body model
class URLRequest(BaseModel):
    url: str


# -----------------------------
# /shorten
# -----------------------------
@app.post("/shorten")
def shorten_url(request: URLRequest):

    long_url = request.url

    # Generate unique code
    while True:
        code = generate_code()
        if not get_url(code):
            break

    try:
        insert_url(code, long_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Cache it
    set_cache(code, long_url)

    return {
        "short_url": f"http://localhost:8000/go/{code}"
    }


# -----------------------------
# /go/{code}
# -----------------------------
@app.get("/go/{code}")
def redirect_url(code: str):

    # 1. Cache check
    cached = get_from_cache(code)
    if cached:
        print("Cache HIT")
        return RedirectResponse(url=cached)

    print("Cache MISS")

    # 2. DB lookup
    long_url = get_url(code)

    if long_url:
        set_cache(code, long_url)
        return RedirectResponse(url=long_url)

    raise HTTPException(status_code=404, detail="URL not found")