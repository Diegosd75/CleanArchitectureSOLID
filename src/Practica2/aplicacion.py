from flask import Flask, request, jsonify
from crear_usuario import CrearUsuario
from adaptador import SqliteUsuarioRepo

app = Flask(__name__)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    correo_electronico = request.form['correo_electronico']
    contrasena = request.form['contrasena']
    caso_de_uso=CrearUsuario(SqliteUsuarioRepo())
    usuario = caso_de_uso.ejecutar(nombre, correo_electronico, contrasena)
    return jsonify({'id':usuario.id,'nombre':usuario.nombre,'correo_electronico':usuario.correo_electronico,'contrasena':usuario.contrasena})

