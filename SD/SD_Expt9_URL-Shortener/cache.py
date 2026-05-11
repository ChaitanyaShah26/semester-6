cache = {}

def get_from_cache(code):
    return cache.get(code)

def set_cache(code, long_url):
    cache[code] = long_url