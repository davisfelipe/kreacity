from dataclasses import dataclass

from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    message: str = Field(...)
    status_code: int = Field(...)
    data: dict = Field(None)


@dataclass
class ClientMessages:
    CREATED: str = 'Client has been created'
    EXIST: str = 'Client Exist'
    NOT_FOUND: str = 'Client Not Found'


@dataclass
class UserMessages:
    EXIST: str = 'User Exist'
    NOT_FOUND: str = 'User Not Found'
