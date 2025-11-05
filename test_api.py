import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    print("Root:", r.json())

def test_create_category():
    payload = {"name": "Electronics"}
    r = requests.post(f"{BASE_URL}/categories/", json=payload)
    assert r.status_code in [200, 201]
    print("Category created:", r.json())
    return r.json()["id"]

def test_create_product(category_id):
    payload = {
        "name": "Laptop Lenovo",
        "description": "Lightweight and powerful",
        "price": 999.99,
        "quantity": 10,
        "category_id": category_id
    }
    r = requests.post(f"{BASE_URL}/products/", json=payload)
    assert r.status_code in [200, 201]
    print("Product created:", r.json())

def test_get_products():
    r = requests.get(f"{BASE_URL}/products/")
    assert r.status_code == 200
    print("Products list:", r.json())

if __name__ == "__main__":
    test_root()
    cat_id = test_create_category()
    test_create_product(cat_id)
    test_get_products()
