from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    email: str
    username: str

    class Config:
        from_attributes = True


class ModifyUser(BaseModel):
    username: str | None
    email: str | None

    class Config:
        from_attributes = True
