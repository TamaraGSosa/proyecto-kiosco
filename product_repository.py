import sqlite3
from product import Product 

class ProductRepository:
    def __init__(self, db="kiosco.db"):
        self.db = db

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

    def insertar_producto(self, producto: Product):
        with self.conect() as con:
            con.execute(
                "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
                (producto.name, producto.price, producto.stock)
            )

    def listar_productos(self):
        with self.conect() as con:
            # Seleccionamos: id(0), name(1), price(2), stock(3)
            cursor = con.execute("SELECT id, name, price, stock FROM products")
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

    def actualizar_stock(self, id_producto, nuevo_stock):
        with self.conect() as con:
            con.execute(
                "UPDATE products SET stock=? WHERE id=?", 
                (nuevo_stock, id_producto)
            )