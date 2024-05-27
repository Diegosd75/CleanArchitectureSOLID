from base_datos import BaseDatos

class ManejadorDatos:
    def procesar(self, base_datos: 'BaseDatos', data):
        base_datos.guardar(data)
        return base_datos.leer()
