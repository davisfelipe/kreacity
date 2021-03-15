from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import encode

from src.config import JWT
from src.models import User
from src.utils import DateTime

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")


def generate_jwt(user: User):
    payload = dict(
        exp = DateTime.expiration_date(hours = 1).isoformat(),
        iat = DateTime.current_datetime().isoformat(),
        user = str(user.username)
    )

    return encode(payload, JWT.phrase, algorithm = 'HS256')
