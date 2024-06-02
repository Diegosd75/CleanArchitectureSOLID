# user_controller.py

class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def get_user(self, user_id):
        user = self.user_service.get_user(user_id)
        if user:
            return f"User: {user.name}, Email: {user.email}"
        else:
            return "User not found"
