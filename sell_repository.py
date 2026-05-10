import sqlite3
from datetime import datetime

from sell import Sell


class SellRepository:

    def __init__(self, db="kiosco.db"):

        self.db = db
        self.create_table()

    def conect(self):
        return sqlite3.connect(self.db)

    def create_table(self):

        with self.conect() as con:

            con.execute('''
                CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    total REAL NOT NULL
                )
            ''')

    def add_sale(self, sale: Sell):

        with self.conect() as con:

            cursor = con.execute(
                "INSERT INTO sales (date, total) VALUES (?, ?)",
                (sale.date, sale.total)
            )

            sale.sell_id = cursor.lastrowid

    def update_sale(self, sale: Sell):

        with self.conect() as con:

            cursor = con.execute(
                "UPDATE sales SET total = ? WHERE id = ?",
                (sale.total, sale.sell_id)
            )

            return cursor.rowcount > 0

    def sales_of_day(self, date=None):

        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        with self.conect() as con:

            cursor = con.execute(
                "SELECT * FROM sales WHERE date(date) = date(?)",
                (date,)
            )

            return cursor.fetchall()

    def total_revenue_today(self):

        today = datetime.now().strftime("%Y-%m-%d")

        with self.conect() as con:

            cursor = con.execute(
                "SELECT SUM(total) FROM sales WHERE date(date) = date(?)",
                (today,)
            )

            result = cursor.fetchone()[0]

            return result if result else 0