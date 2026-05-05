from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    user_name: str
    email: str

class ItemCreate(BaseModel):
    item_name: str
    item_price: float

class CartCreate(BaseModel):
    user_id: int

class AddToCart(BaseModel):
    item_id: int
    quantity: int
