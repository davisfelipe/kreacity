from src.models import Client, User


class UserRepository:

    @staticmethod
    def find_one(username: int) -> User:
        query_params = dict(
            username=username,
            is_enabled=True
        )
        return User.objects(**query_params).first()


class ClientRepository:

    @staticmethod
    def find_one(client_id: int) -> Client:
        query_params = dict(
            is_deleted=False,
            identification=client_id
        )
        return Client.objects(**query_params).first()
