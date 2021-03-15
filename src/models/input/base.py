from pydantic import BaseModel


class BaseSchema(BaseModel):

    class Config:
        validate_assignment = True
