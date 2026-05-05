from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .database_sql import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100))
    email = Column(String(100), unique=True)
    carts = relationship("Cart", back_populates="user")

class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(100))
    item_price = Column(DECIMAL(10,2))

class Cart(Base):
    __tablename__ = "carts"
    cart_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    total_amount = Column(DECIMAL(10,2), default=0)
    user = relationship("User", back_populates="carts")
    items = relationship("CartItem", back_populates="cart")

class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("carts.cart_id"))
    item_id = Column(Integer, ForeignKey("items.item_id"))
    quantity = Column(Integer)
    cart = relationship("Cart", back_populates="items")
