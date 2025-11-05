# 🛍️ Mini Shop Backend (FastAPI)

This is a **FastAPI-based backend** for the Mini Shop project.

---

## 🚀 Features

- User registration & authentication (JWT)
- Product & category management
- Shopping cart system
- SQLite database (can be replaced with PostgreSQL)
- Modular structure with routers and schemas

---

## 🧱 Project Structure

backend/
│
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ ├── routes/
│ │ ├── users.py
│ │ ├── auth.py
│ │ ├── products.py
│ │ ├── categories.py
│ │ └── cart.py
│
├── venv/ # Virtual environment (ignored by .gitignore)
├── requirements.txt
├── .gitignore
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the API
bash
Copy code
uvicorn app.main:app --reload
Server runs on:
👉 http://127.0.0.1:8000

🧪 API Testing (Postman)
Endpoint	Method	Description
/users/register	POST	Register a new user
/auth/login	POST	Login and get JWT token
/products	GET	List all products
/cart/add	POST	Add product to user cart

📦 Example .env file
ini
Copy code
DATABASE_URL=sqlite:///./minishop.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
📜 License
MIT License © 2025 Sanaz Azimi