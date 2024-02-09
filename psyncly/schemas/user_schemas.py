from datetime import datetime
from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateUser(BaseModel):
    email: str
    username: str

    model_config = ConfigDict(from_attributes=True)


class ModifyUser(BaseModel):
    username: str | None
    email: str | None

    model_config = ConfigDict(from_attributes=True)
