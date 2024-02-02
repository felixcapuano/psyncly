from pydantic import BaseModel
from datetime import datetime


class Track(BaseModel):
    id: int
    title: str
    artist: str
    isrc: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreateTrack(BaseModel):
    title: str
    artist: str
    isrc: str

    class Config:
        from_attributes = True


class ModifyTrack(BaseModel):
    title: str | None
    artist: str | None
    isrc: str | None

    class Config:
        from_attributes = True
