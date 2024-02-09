from pydantic import BaseModel, ConfigDict
from datetime import datetime
from psyncly.schemas.playlist_schemas import Playlist
from psyncly.schemas.account_schemas import Account


class ServicePlaylist(BaseModel):
    id: int
    external_id: str
    playlist: Playlist
    account: Account
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateServicePlaylist(BaseModel):
    external_id: str
    # playlist_id: int
    # account_id: int

    model_config = ConfigDict(from_attributes=True)


class ModifyServicePlaylist(BaseModel):
    external_id: str | None
    playlist_id: int | None
    account_id: int | None

    model_config = ConfigDict(from_attributes=True)
