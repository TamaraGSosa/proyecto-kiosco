import sqlite3

from item import Item
from product import Product


class SellItemRepository:

    def __init__(self, db="kiosco.db"):

        self.db = db
        self.create_table()

    def conect(self):
        return sqlite3.connect(self.db)

    def create_table(self):

        with self.conect() as con:

            con.execute("""
                CREATE TABLE IF NOT EXISTS sell_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_sell INTEGER NOT NULL,
                    id_product INTEGER NOT NULL,
                    product_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price REAL NOT NULL
                )
            """)

    def add_sell_item(self, item: Item, sell_id):

        with self.conect() as con:

            cursor = con.execute("""
                INSERT INTO sell_items
                (
                    id_sell,
                    id_product,
                    product_name,
                    quantity,
                    unit_price
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                sell_id,
                item.product.id_producto,
                item.product.name,
                item.quantity,
                item.product.price
            ))

            return cursor.lastrowid

    def get_by_sell(self, sell_id):

        with self.conect() as con:

            cursor = con.execute("""
                SELECT
                    id_product,
                    product_name,
                    quantity,
                    unit_price
                FROM sell_items
                WHERE id_sell = ?
            """, (sell_id,))

            rows = cursor.fetchall()

            items = []

            for row in rows:

                product = Product(
                    id_producto=row[0],
                    name=row[1],
                    price=row[3],
                    stock=999999
                )

                item = Item(
                    product=product,
                    quantity=row[2]
                )

                items.append(item)

            return items