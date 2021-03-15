from jwt import encode

from src.config import JWT
from src.models import User
from src.utils import DateTime


def validate_jwt(func):
    def execution(*args, **kwargs):
        return func(*args, **kwargs)

    return execution


def generate_jwt(user: User):
    payload = dict(
        exp = DateTime.expiration_date(hours = 1).isoformat(),
        iat = DateTime.current_datetime().isoformat(),
        user = str(user.username)
    )

    return encode(payload, JWT.phrase, algorithm = 'HS256')
