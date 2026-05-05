from decimal import Decimal
from sqlalchemy.orm import Session
from . import models_sql

# Users
def create_user(db: Session, user):
    db_user = models_sql.User(user_name=user.user_name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models_sql.User).all()

# Items
def create_item(db: Session, item):
    db_item = models_sql.Item(item_name=item.item_name, item_price=item.item_price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session):
    return db.query(models_sql.Item).all()

# Cart
def create_cart(db: Session, user_id: int):
    cart = models_sql.Cart(user_id=user_id, total_amount=0)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return cart

def add_item_to_cart(db: Session, cart_id: int, item_id: int, quantity: int):
    item = db.query(models_sql.Item).filter(models_sql.Item.item_id==item_id).first()
    cart_item = models_sql.CartItem(cart_id=cart_id, item_id=item_id, quantity=quantity)
    db.add(cart_item)

    cart = db.query(models_sql.Cart).filter(models_sql.Cart.cart_id==cart_id).first()
    cart.total_amount += Decimal(item.item_price) * Decimal(quantity)
    db.commit()
    db.refresh(cart)
    return cart

def view_cart(db: Session, cart_id: int):
    cart = db.query(models_sql.Cart).filter(models_sql.Cart.cart_id==cart_id).first()
    items = db.query(models_sql.CartItem).filter(models_sql.CartItem.cart_id==cart_id).all()
    return {
        "cart_id": cart.cart_id,
        "user_id": cart.user_id,
        "total_amount": cart.total_amount,
        "items": [{"item_id": i.item_id, "quantity": i.quantity} for i in items]
    }
