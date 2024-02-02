from pydantic import BaseModel
from datetime import datetime
from psyncly.schemas.user_schemas import User


class Playlist(BaseModel):
    id: int
    name: str
    # owner: User
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreatePlaylist(BaseModel):
    name: str

    class Config:
        from_attributes = True


class ModifyPlaylist(BaseModel):
    new_name: str | None
    new_owner_id: int | None

    class Config:
        from_attributes = True
