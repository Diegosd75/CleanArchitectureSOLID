from user_repository import UserRepository
from user import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        user_entity = self.user_repository.get_user(user_id)
        if user_entity:
            return User(
                id=user_entity.id,
                name=user_entity.name,
                email=user_entity.email,
                document_type=user_entity.document_type,
                document_number=user_entity.document_number,
                birth_date=user_entity.birth_date,
                residence_city=user_entity.residence_city
            )
        else:
            return None
