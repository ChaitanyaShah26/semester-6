from bson import ObjectId
from .database_mongo import mongodb

# Users
async def create_user(user):
    result = await mongodb.users.insert_one(user)
    user["_id"] = str(result.inserted_id)
    return user

async def get_users():
    users = []
    async for u in mongodb.users.find():
        u["_id"] = str(u["_id"])
        users.append(u)
    return users

# Items
async def create_item(item):
    result = await mongodb.items.insert_one(item)
    item["_id"] = str(result.inserted_id)
    return item

async def get_items():
    items = []
    async for i in mongodb.items.find():
        i["_id"] = str(i["_id"])
        items.append(i)
    return items

# Cart
async def create_cart(user_id):
    cart = {"user_id": user_id, "items": [], "total_amount": 0}
    result = await mongodb.carts.insert_one(cart)
    cart["_id"] = str(result.inserted_id)
    return cart

async def add_item_to_cart(cart_id, item_id, quantity):
    item = await mongodb.items.find_one({"_id": ObjectId(item_id)})
    total_price = item["item_price"] * quantity

    await mongodb.carts.update_one(
        {"_id": ObjectId(cart_id)},
        {
            "$push": {"items": {"item_id": item_id, "quantity": quantity, "price": item["item_price"]}},
            "$inc": {"total_amount": total_price}
        }
    )
    cart = await mongodb.carts.find_one({"_id": ObjectId(cart_id)})
    cart["_id"] = str(cart["_id"])
    return cart

async def view_cart(cart_id):
    cart = await mongodb.carts.find_one({"_id": ObjectId(cart_id)})
    cart["_id"] = str(cart["_id"])
    return cart
