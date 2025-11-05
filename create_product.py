from app.database import SessionLocal
from app.models import Product

db = SessionLocal()

new_product = Product(
    name="Test Product",
    description="This is a test product",
    price=10.0,
    quantity=5,
    category_id=None
)

db.add(new_product)
db.commit()
db.refresh(new_product)
print("Product added:", new_product)
db.close()
