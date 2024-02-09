from pydantic import BaseModel, ConfigDict
from datetime import datetime
from psyncly.schemas.user_schemas import User


class Playlist(BaseModel):
    id: int
    name: str
    # owner: User
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreatePlaylist(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)


class ModifyPlaylist(BaseModel):
    new_name: str | None
    new_owner_id: int | None

    model_config = ConfigDict(from_attributes=True)
