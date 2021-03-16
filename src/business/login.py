from starlette.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from src.models import UserAuth
from src.repository import UserRepository
from src.security.jwt_token import generate_jwt
from src.utils import BaseResponse, BusinessCase
from src.utils.response import UserMessages


class UserResponse(BaseResponse):
    pass


class LoginUser(BusinessCase):

    def handle(self, user: UserAuth) -> UserResponse:
        user_found = UserRepository.find_one(user.username)
        response = UserResponse(
            message = UserMessages.DENIED,
            status_code = HTTP_403_FORBIDDEN
        )
        if not user_found:
            return response

        if user.password != user_found.password:
            return response

        data = dict(
            token=generate_jwt(user_found),
            user=user_found.username
        )
        return UserResponse(
            message = UserMessages.GRANTED,
            status_code = HTTP_200_OK,
            data = data
        )
