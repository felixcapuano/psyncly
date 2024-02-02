from pydantic import BaseModel
from datetime import datetime
from psyncly.schemas.playlist_schemas import Playlist
from psyncly.schemas.service_account_schemas import ServiceAccount


class ServicePlaylist(BaseModel):
    id: int
    external_id: str
    playlist: Playlist
    service_account: ServiceAccount
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreateServicePlaylist(BaseModel):
    external_id: str
    playlist_id: int
    service_account_id: int

    class Config:
        from_attributes = True


class ModifyServicePlaylist(BaseModel):
    external_id: str | None
    playlist_id: int | None
    service_account_id: int | None

    class Config:
        from_attributes = True
