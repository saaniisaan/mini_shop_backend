from app.database import Base, engine
from app import models

# ایجاد جداول دیتابیس
Base.metadata.create_all(bind=engine)

print("Database created successfully!")
