from pydantic import BaseModel
from typing import Literal


class WriteUser(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class ReadUser(WriteUser):
    id: int


class WriteTrack(BaseModel):
    title: str
    artist: str
    isrc: str

    class Config:
        from_attributes = True


class ReadTrack(WriteTrack):
    id: int


class WritePlaylist(BaseModel):
    name: str
    owner_id: int

    class Config:
        from_attributes = True


class ReadPlaylist(WritePlaylist):
    id: int
    owner: ReadUser


class Operation(BaseModel):
    operation: Literal["add", "remove"]
    resource_id: int


class BulkOperation(BaseModel):
    operations: list[Operation]
