import product 
import sqlite3
class ProductRepository:
    def __init__(self , db="kiosco.db"):
        self.db = db

    def conect(self):
        return sqlite3.connect(self.db)

    def create_table(self):
        with self.conect() as con:
            con.execute(
                '''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL default 0
                )
            ''')
            
