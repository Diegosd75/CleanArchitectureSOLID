import mysql.connector
from base_datos import BaseDatos

class MySQL(BaseDatos):
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='test_db'
        )
        self.cursor = self.conn.cursor()

    def guardar(self, data):
        self.cursor.execute("INSERT INTO test_table (data) VALUES (%s)", (data,))
        self.conn.commit()

    def leer(self):
        self.cursor.execute("SELECT data FROM test_table")
        result = self.cursor.fetchall()
        return result
