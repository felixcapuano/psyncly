from pydantic import BaseModel, ConfigDict
from datetime import datetime
from psyncly.schemas.playlist_schemas import Playlist


class Worker(BaseModel):
    id: int
    worker_id: str
    worker_type: str
    status: str
    playlist: Playlist
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateWorker(BaseModel):
    worker_id: str
    worker_type: str
    status: str
    playlist_id: int

    model_config = ConfigDict(from_attributes=True)


class ModifyWorker(BaseModel):
    worker_id: str | None
    worker_type: str | None
    status: str | None
    playlist_id: int | None

    model_config = ConfigDict(from_attributes=True)
