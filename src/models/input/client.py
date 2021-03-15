from pydantic import BaseModel, Field
from pydantic.types import SecretStr


class Client(BaseModel):
    name: str = Field(..., min_length = 3)
    last_name: str = Field(..., min_length = 3)
    identification_type: str = Field(..., enum = ['CC', 'CE', "TI"])
    identification: int = Field(...)
    password: SecretStr = Field(...)
    rol: str = Field(...)

    class Config:
        validate_assignment = True


class User(BaseModel):
    username: int = Field(...)
    password: SecretStr = Field(...)

    class Config:
        validate_assignment = True
