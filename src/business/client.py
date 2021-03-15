from mongoengine import NotUniqueError
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from src.models import Client, User, UserInput
from src.utils import BaseResponse, BusinessCase
from src.utils.response import ClientMessages, UserMessages


class ClientResponse(BaseResponse):
    pass


class CreateClient(BusinessCase):

    def handle(self, user: UserInput) -> ClientResponse:
        client = self._create_client_and_user(user)
        return client

    def _create_client_and_user(self, user: UserInput) -> (ClientResponse, bool):
        new_client = Client.from_json(user.json())
        new_user = User(
            username=user.identification,
            password=user.password.get_secret_value()
        )
        try:
            new_user.save()
        except NotUniqueError:
            response = ClientResponse(
                message = ClientMessages.EXIST,
                status_code = HTTP_400_BAD_REQUEST
            )
            return response

        try:
            new_client.save()
        except NotUniqueError:
            response = ClientResponse(
                message = UserMessages.EXIST,
                status_code = HTTP_400_BAD_REQUEST
            )
            return response
        return ClientResponse(
            message = ClientMessages.CREATED,
            status_code = HTTP_201_CREATED
        )
