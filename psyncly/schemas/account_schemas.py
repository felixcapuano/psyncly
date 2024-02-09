from pydantic import BaseModel, ConfigDict
from datetime import datetime
from psyncly.schemas.user_schemas import User


class Account(BaseModel):
    id: int
    account_type: str
    owner: User
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateAccount(BaseModel):
    account_type: str

    model_config = ConfigDict(from_attributes=True)


class ModifyAccount(BaseModel):
    new_account_type: str | None
    new_owner_id: int | None

    model_config = ConfigDict(from_attributes=True)
