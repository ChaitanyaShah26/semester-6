from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import database_sql, models_sql, schemas, crud_sql, crud_mongo
import asyncio

# SQL setup
models_sql.Base.metadata.create_all(bind=database_sql.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database_sql.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---- SQL ENDPOINTS ----
@app.post("/sql/users/")
def create_user_sql(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud_sql.create_user(db, user)

@app.get("/sql/users/")
def read_users_sql(db: Session = Depends(get_db)):
    return crud_sql.get_users(db)

@app.post("/sql/items/")
def create_item_sql(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud_sql.create_item(db, item)

@app.get("/sql/items/")
def read_items_sql(db: Session = Depends(get_db)):
    return crud_sql.get_items(db)

@app.post("/sql/cart/")
def create_cart_sql(cart: schemas.CartCreate, db: Session = Depends(get_db)):
    return crud_sql.create_cart(db, cart.user_id)

@app.post("/sql/cart/{cart_id}/add")
def add_to_cart_sql(cart_id: int, item: schemas.AddToCart, db: Session = Depends(get_db)):
    return crud_sql.add_item_to_cart(db, cart_id, item.item_id, item.quantity)

@app.get("/sql/cart/{cart_id}")
def view_cart_sql(cart_id: int, db: Session = Depends(get_db)):
    return crud_sql.view_cart(db, cart_id)

# ---- MONGO ENDPOINTS ----
@app.post("/mongo/users/")
async def create_user_mongo(user: schemas.UserCreate):
    return await crud_mongo.create_user(user.dict())

@app.get("/mongo/users/")
async def read_users_mongo():
    return await crud_mongo.get_users()

@app.post("/mongo/items/")
async def create_item_mongo(item: schemas.ItemCreate):
    return await crud_mongo.create_item(item.dict())

@app.get("/mongo/items/")
async def read_items_mongo():
    return await crud_mongo.get_items()

@app.post("/mongo/cart/")
async def create_cart_mongo(user_id: str):
    return await crud_mongo.create_cart(user_id)

@app.post("/mongo/cart/{cart_id}/add")
async def add_to_cart_mongo(cart_id: str, item_id: str, quantity: int):
    return await crud_mongo.add_item_to_cart(cart_id, item_id, quantity)

@app.get("/mongo/cart/{cart_id}")
async def view_cart_mongo(cart_id: str):
    return await crud_mongo.view_cart(cart_id)
