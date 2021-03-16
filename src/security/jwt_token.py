from typing import Tuple

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, encode
from starlette.status import HTTP_403_FORBIDDEN

from src.config import JWT
from src.models import User
from src.repository import UserRepository
from src.utils import DateTime, TokenMessages

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")


def generate_jwt(user: User):
    payload = dict(
        exp = DateTime.expiration_date(hours = 1),
        iat = DateTime.current_datetime(),
        user = str(user.username)
    )

    return encode(payload, JWT.phrase, algorithm = 'HS256')


def decode_jwt(token: str) -> Tuple[dict, bool]:
    try:
        data = decode(token, JWT.phrase, algorithms=['HS256'])
        data['exp'] = DateTime.from_timestamp(data.get('exp'))
        data['iat'] = DateTime.from_timestamp(data.get('iat'))
        return data, False
    except Exception as error:
        return dict(error=error), True


def validate_datetime(payload: dict) -> bool:
    current_date = DateTime.current_datetime()
    expiration_date = payload.get('exp')
    if current_date > expiration_date:
        return False
    return True


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload, has_decode_error = decode_jwt(token)
    if has_decode_error:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail=TokenMessages.INVALID)

    is_valid = validate_datetime(payload)
    if not is_valid:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail=TokenMessages.EXPIRED)

    user = UserRepository.find_one(payload.get('user'))
    if not user or not user.is_enabled:
        raise HTTPException(status_code = HTTP_403_FORBIDDEN, detail = TokenMessages.INVALID)
    return user
