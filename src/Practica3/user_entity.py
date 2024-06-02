# user_entity.py

class UserEntity:
    def __init__(self, id, name, email, document_type, document_number, birth_date, residence_city):
        self.id = id
        self.name = name
        self.email = email
        self.document_type = document_type
        self.document_number = document_number
        self.birth_date = birth_date
        self.residence_city = residence_city

    def full_name(self):
        return f"{self.name}"

    def __str__(self):
        return f"UserEntity(id={self.id}, name={self.name}, email={self.email}, document_type={self.document_type}, document_number={self.document_number}, birth_date={self.birth_date}, residence_city={self.residence_city})"
