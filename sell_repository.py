import sqlite3

class SellRepository:
    def __init__(self, db="kiosco.db"):
        self.db = db   

    def conect(self):
        return sqlite3.connect(self.db)

    def create_table(self):
        with self.conect() as con:
            con.execute(
                '''
                CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    total REAL NOT NULL
                )
                '''
            )
