import sqlite3
from product import Product 

class ProductRepository:
    def __init__(self, db="kiosco.db"):
        self.db = db
        self.create_table()

    def conect(self):
        return sqlite3.connect(self.db)

    def create_table(self):
        with self.conect() as con:
            con.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL default 0
                )
            ''')

    def add_product(self, product: Product):
        with self.conect() as con:
            cursor =con.execute(
                "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
                (product.name, product.price, product.stock)
            )
            product.id_producto=cursor.lastrowid

    def get_all_products(self):
        with self.conect() as con:
            cursor = con.execute("SELECT id, name, price, stock FROM products ORDER BY name")
            rows = cursor.fetchall()
            
            # Mapeo correcto: SELECT id(0), name(1), price(2), stock(3)
            return [
                Product(
                    id_producto=row[0],
                    name=row[1],
                    price=row[2],
                    stock=row[3],
                )
                for row in rows
            ]

    def get_id_product(self, id_producto):
        with self.conect() as con:
            cursor = con.execute("SELECT id, name, price, stock FROM products WHERE id=?", (id_producto,))
            row = cursor.fetchone()
            if row:
                return Product(
                    id_producto=row[0],
                    name=row[1],
                    price=row[2],
                    stock=row[3],
                )
            else:
                return None
    def update_stock(self, id_product, new_stock):
        with self.conect() as con:
            cursor = con.execute(
                "UPDATE products SET stock=? WHERE id=?", 
                (new_stock, id_product)
            )
            return cursor.rowcount > 0
        
    def delete_product(self, id_producto):
        with self.conect() as con:
            cursor = con.execute("DELETE FROM products WHERE id=?", (id_producto,))
            return cursor.rowcount > 0