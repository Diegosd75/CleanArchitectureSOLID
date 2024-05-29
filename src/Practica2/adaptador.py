import sqlite3
from user import User

class SqliteUsuarioRepo:
    def __init__(self):
        self.conexion = sqlite3.connect('usuarios.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, correo TEXT, contrasena TEXT)')

    def guardar (self,usuario):
        self.cursor.execute('INSERT INTO usuarios VALUES (?, ?, ?, ?)', (usuario.user_id, usuario.nombre, usuario.correo_electronico, usuario.contrasena))
        self.conexion.commit()

    def obtener_por_correo(self, correo):
        self.cursor.execute('SELECT * FROM usuarios WHERE correo = ?', (correo))
        fila = self.cursor.fetchone()
        if fila:
            return User(fila[0],fila[1],fila[2],fila[3])
        else:
            return None