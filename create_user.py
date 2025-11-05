from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.utils import get_password_hash

db: Session = SessionLocal()

# اطلاعات یوزر اولیه
email = "admin@example.com"
full_name = "Admin User"
password = "123456"

existing_user = db.query(User).filter(User.email == email).first()
if existing_user:
    print("User already exists!")
else:
    new_user = User(
        full_name=full_name,
        email=email,
        hashed_password=get_password_hash(password),
        role="admin"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(f"User created successfully! ID: {new_user.id}")

db.close()
