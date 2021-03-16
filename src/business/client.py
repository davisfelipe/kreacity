from mongoengine import NotUniqueError
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

from src.models import Client, ClientInput, ClientUpdateInput, User
from src.repository import ClientRepository, UserRepository
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
                message = UserMessages.EXIST,
                status_code = HTTP_400_BAD_REQUEST
            )
            return response

        try:
            new_client.save()
        except NotUniqueError:
            response = ClientResponse(
                message = ClientMessages.EXIST,
                status_code = HTTP_400_BAD_REQUEST
            )
            return response
        return ClientResponse(
            message = ClientMessages.CREATED,
            status_code = HTTP_201_CREATED
        )


class FindClient(BusinessCase):
    def handle(self, client_id: int) -> ClientResponse:
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
    def handle(self, client_id: int, client: ClientUpdateInput) -> ClientResponse:
        client_found = ClientRepository.find_one(client_id)
        if not client_found:
            return ClientResponse(
                message = ClientMessages.NOT_FOUND,
                status_code = HTTP_404_NOT_FOUND
            )
        client_found.update(**client.dict(exclude_none=True))
        client_found.reload()
        return ClientResponse(
            message = ClientMessages.UPDATED,
            status_code = HTTP_200_OK,
            data = BsonObject.to_dict(client_found)
        )


class DeleteClient(BusinessCase):
    def handle(self, client_id: int) -> ClientResponse:
        client_found = ClientRepository.find_one(client_id)
        if not client_found:
            return ClientResponse(
                message = ClientMessages.NOT_FOUND,
                status_code = HTTP_404_NOT_FOUND
            )

        user_found = UserRepository.find_one(client_id)
        if not user_found:
            return ClientResponse(
                message=UserMessages.NOT_FOUND,
                status_code=HTTP_404_NOT_FOUND
            )
        try:
            client_found.is_deleted = True
            user_found.is_enabled = False

            client_found.save().reload()
            user_found.save().reload()
        except Exception as error:
            return ClientResponse(
                message=str(error),
                status_code=HTTP_500_INTERNAL_SERVER_ERROR
            )

        return ClientResponse(
            message=ClientMessages.DELETED,
            status_code=HTTP_200_OK
        )
