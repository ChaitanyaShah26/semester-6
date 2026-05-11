def url_schema(url) -> dict:
    return {
        "id": str(url["_id"]),
        "short_code": url["short_code"],
        "original_url": url["original_url"]
    }