from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Track(BaseModel):
    id: int
    title: str
    artist: str
    isrc: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateTrack(BaseModel):
    title: str
    artist: str
    isrc: str

    model_config = ConfigDict(from_attributes=True)


class ModifyTrack(BaseModel):
    title: str | None
    artist: str | None
    isrc: str | None

    model_config = ConfigDict(from_attributes=True)
