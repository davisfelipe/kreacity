from src.models import User


class UserRepository:

    @staticmethod
    def find_one(username) -> User:
        return User.objects(username = username).first()
