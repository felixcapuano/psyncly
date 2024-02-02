from pydantic import BaseModel
from datetime import datetime
from psyncly.schemas.user_schemas import User


class ServiceAccount(BaseModel):
    id: int
    service_type: str
    owner: User
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreateServiceAccount(BaseModel):
    service_type: str
    owner_id: int

    class Config:
        from_attributes = True


class ModifyServiceAccount(BaseModel):
    service_type: str | None
    owner_id: int | None

    class Config:
        from_attributes = True
