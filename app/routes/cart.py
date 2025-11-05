from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import CartItem
from app.schemas import CartItemCreate, CartItemResponse

router = APIRouter(
    tags=["Cart"]
)

@router.get("/", response_model=List[CartItemResponse])
def get_cart_items(db: Session = Depends(get_db)):
    return db.query(CartItem).all()

@router.post("/", response_model=CartItemResponse)
def add_to_cart(item: CartItemCreate, db: Session = Depends(get_db)):
    new_item = CartItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.put("/{item_id}", response_model=CartItemResponse)
def update_cart_item(item_id: int, item: CartItemCreate, db: Session = Depends(get_db)):
    cart_item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(cart_item, key, value)
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.delete("/{item_id}")
def delete_cart_item(item_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(cart_item)
    db.commit()
    return {"detail": "Item deleted"}
