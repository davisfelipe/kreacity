from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from src.models import UserInput
from src.repository import UserRepository
from src.security.jwt_token import generate_jwt
from src.utils import BaseResponse, BusinessCase
from src.utils.response import UserMessages


class UserResponse(BaseResponse):
    pass


class LoginUser(BusinessCase):

    def handle(self, user: UserInput) -> UserResponse:
        user_found = UserRepository.find_one(user.username)
        if not user_found:
            response = UserResponse(
                message = UserMessages.NOT_FOUND,
                status_code = HTTP_404_NOT_FOUND
            )
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
