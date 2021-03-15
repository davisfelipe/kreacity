from src.models import Client, User


class UserRepository:

    @staticmethod
    def find_one(username) -> User:
        return User.objects(username = username).first()


class ClientRepository:

    @staticmethod
    def find_one(client_id) -> Client:
        return Client.objects(identification=client_id).first()
