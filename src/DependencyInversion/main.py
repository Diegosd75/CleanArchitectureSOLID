from manejador_datos import ManejadorDatos
from mysql_db import MySQL
from mongodb_db import MongoDB

def main():
    manejador = ManejadorDatos()

    # Probar con MySQL
    mysql_db = MySQL()
    print("Resultados MySQL:", manejador.procesar(mysql_db, 'Dato en MySQL'))

    # Probar con MongoDB
    mongo_db = MongoDB()
    print("Resultados MongoDB:", manejador.procesar(mongo_db, 'Dato en MongoDB'))

if __name__ == "__main__":
    main()
