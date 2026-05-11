from database import urls_collection

def insert_url(code, long_url):
    urls_collection.insert_one({
        "code": code,
        "long_url": long_url
    })

def get_url(code):
    result = urls_collection.find_one({"code": code})
    return result["long_url"] if result else None