import sqlite3

class sell_repository:
    
    def __init__(self, db="kiosco.db"):
        self.bd=db

    def conect():
        return   sqlite3.connect(self.db)
    
    def create_table(self):
        with self.conect() as con:
            con.execute (
            '''
                CREATE TABLE IF NOT EXISTS sell(
                id INTEGER PRIMARY KEY INCREMENT
                date TEXT NOT NULL
                total REAL NOT NULL
                
                ) 
            ''' )
    
    