# main.py
from user_repository import MySQLUserRepository
from user_services import UserService

def main():
    connection_params = {
        'host': 'localhost',
        'user': 'admin',
        'password': 'admin',
        'database': 'personas'
    }

    user_repository = MySQLUserRepository(connection_params)
    user_service = UserService(user_repository)
    user = user_service.get_user_details(1)  # Cambia el ID por el ID del usuario que quieres obtener

    if user:
        print(user)
    else:
        print("Usuario no encontrado")

if __name__ == "__main__":
    main()
