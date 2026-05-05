from .config import mongo_client

def insert_nosql(db_name, data):
    try:
        # MongoDB creates the DB and Collection automatically on the first insert
        db = mongo_client[db_name]
        collection = db["users"]
        collection.insert_one(data.copy())
    except Exception as e:
        print(f"❌ NoSQL Insert Error in {db_name}: {e}")

def fetch_nosql(db_name):
    try:
        db = mongo_client[db_name]
        collection = db["users"]
        # Convert cursor to list and remove the MongoDB '_id' field for JSON compatibility
        return list(collection.find({}, {'_id': 0}))
    except Exception as e:
        print(f"❌ NoSQL Fetch Error in {db_name}: {e}")
        return []

def search_nosql_user(db_name, uid):
    try:
        db = mongo_client[db_name]
        collection = db["users"]
        return collection.find_one({"id": uid}, {'_id': 0})
    except Exception as e:
        print(f"❌ NoSQL Search Error: {e}")
        return None

def delete_nosql(db_name, uid):
    try:
        db = mongo_client[db_name]
        collection = db["users"]
        collection.delete_one({"id": uid})
    except Exception as e:
        print(f"❌ NoSQL Delete Error: {e}")