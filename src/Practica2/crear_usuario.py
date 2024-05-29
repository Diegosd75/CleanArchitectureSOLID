from user import User

class CrearUsuario:
    def __init__(self, usuario_repo):
        self.usuario_repo= usuario_repo


    def ejecutar(self, nombre, correo_electronico, contrasena):
        usuario = User(None, nombre, correo_electronico, contrasena)
        self.usuario_repo.guardar(usuario)
        return usuario