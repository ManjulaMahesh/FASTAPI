from app.core.database import get_connection
from app.models.product_model import Product

def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Name, Price, Warranty FROM Product")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "price": r[2], "warranty": r[3]} for r in rows]

def get_product_by_id(product_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Name, Price, Warranty FROM Product WHERE ID=?", product_id)
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "name": row[1], "price": row[2], "warranty": row[3]}
    return None

def add_product(product: Product):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Product (Name, Price, Warranty) VALUES (?, ?, ?)",
        (product.name, product.price, product.warranty)
    )
    conn.commit()
    conn.close()

def update_product(product_id: int, product: Product):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Product SET Name=?, Price=?, Warranty=? WHERE ID=?",
        (product.name, product.price, product.warranty, product_id)
    )
    conn.commit()
    conn.close()

def delete_product(product_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Product WHERE ID=?", product_id)
    conn.commit()
    conn.close()
