from pydantic import Field
from pydantic.types import SecretStr

from src.models.input.base import BaseSchema


class ClientUpdate(BaseSchema):
    name: str = Field(..., min_length = 3)
    last_name: str = Field(..., min_length = 3)
    identification_type: str = Field(..., enum = ['CC', 'CE', "TI"])
    rol: str = Field(...)


class Client(ClientUpdate):
    identification: int = Field(...)
    password: SecretStr = Field(...)


class User(BaseSchema):
    username: int = Field(...)
    password: SecretStr = Field(...)
