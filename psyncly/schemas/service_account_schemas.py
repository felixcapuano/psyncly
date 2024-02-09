from pydantic import BaseModel, ConfigDict
from datetime import datetime
from psyncly.schemas.user_schemas import User


class ServiceAccount(BaseModel):
    id: int
    service_type: str
    owner: User
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateServiceAccount(BaseModel):
    service_type: str

    model_config = ConfigDict(from_attributes=True)


class ModifyServiceAccount(BaseModel):
    new_service_type: str | None
    new_owner_id: int | None

    model_config = ConfigDict(from_attributes=True)
