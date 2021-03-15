from mongoengine import NotUniqueError
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)

from src.models import Client, ClientInput, ClientUpdateInput, User
from src.repository import ClientRepository
from src.utils import BaseResponse, BusinessCase
from src.utils.encoder import BsonObject
from src.utils.response import ClientMessages, UserMessages


class ClientResponse(BaseResponse):
    pass


class CreateClient(BusinessCase):

    def handle(self, client: ClientInput) -> ClientResponse:
        client = self._create_client_and_user(client)
        return client

    @classmethod
    def _create_client_and_user(cls, user: ClientInput) -> ClientResponse:
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


class FindClient(BusinessCase):
    def handle(self, client_id: int):
        client = ClientRepository.find_one(client_id)
        if not client:
            return ClientResponse(
                message = ClientMessages.NOT_FOUND,
                status_code = HTTP_404_NOT_FOUND
            )
        return ClientResponse(
            message = ClientMessages.FOUND,
            status_code = HTTP_200_OK,
            data = BsonObject.to_dict(client)
        )


class UpdateClient(BusinessCase):
    def handle(self, client_id: int, client: ClientUpdateInput):
        client_found = ClientRepository.find_one(client_id)
        if not client_found:
            return ClientResponse(
                message = ClientMessages.NOT_FOUND,
                status_code = HTTP_404_NOT_FOUND
            )
        client_found.update(**client.dict())
        client_found.reload()
        return ClientResponse(
            message = ClientMessages.UPDATED,
            status_code = HTTP_200_OK,
            data = BsonObject.to_dict(client_found)
        )
