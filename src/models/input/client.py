from hashlib import sha256

from pydantic import Field, validator
from pydantic.types import SecretStr

from src.models.input.base import BaseSchema


class ClientUpdate(BaseSchema):
    name: str = Field(None, min_length = 3)
    last_name: str = Field(None, min_length = 3)
    identification_type: str = Field(None, enum = ['CC', 'CE', "TI"])
    rol: str = Field(None)


class Client(ClientUpdate):
    name: str = Field(..., min_length = 3)
    last_name: str = Field(..., min_length = 3)
    identification: int = Field(...)
    identification_type: str = Field(..., enum = ['CC', 'CE', "TI"])
    password: SecretStr = Field(...)
    rol: str = Field(...)

    @validator('password', pre=True)
    def password_encrypt(cls, v):
        hash_pass = sha256()
        hash_pass.update(v.encode('utf-8'))
        return hash_pass.hexdigest()


class User(BaseSchema):
    username: int = Field(...)
    password: SecretStr = Field(...)
