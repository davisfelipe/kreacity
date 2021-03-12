from pydantic import BaseModel, Field


class User(BaseModel):
    names: str = Field(..., min_length = 3)
    last_names: str = Field(..., min_length = 3)
    identification_type: str = Field(..., enum = ['CC', 'CE', "TI"])
    identification_number: int = Field(...)
    rol: str = Field(...)

    class Config:
        validate_assignment = True
