from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    message: str = Field(...)
    status_code: int = Field(...)
    data: Any = Field(None)


@dataclass
class ClientMessages:
    CREATED: str = 'Client has been created'
    EXIST: str = 'Client Exist'
    NOT_FOUND: str = 'Client Not Found'
    FOUND: str = 'Client found'
    UPDATED: str = 'Client has been updated'


@dataclass
class UserMessages:
    EXIST: str = 'User Exist'
    NOT_FOUND: str = 'User Not Found'
    GRANTED: str = "User has been logged"
