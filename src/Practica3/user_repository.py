import mysql.connector
from abc import ABC, abstractmethod
from user_entity import UserEntity

class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id):
        pass

class MySQLUserRepository(UserRepository):
    def __init__(self, connection_params):
        self.connection_params = connection_params

    def get_user(self, user_id):
        connection = mysql.connector.connect(**self.connection_params)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, document_type, document_number, birth_date, residence_city FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return UserEntity(result['id'], result['name'], result['email'], result['document_type'], result['document_number'], result['birth_date'], result['residence_city'])
        else:
            return None
