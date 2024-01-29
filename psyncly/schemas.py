from typing import Literal

from pydantic import BaseModel


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


class WritePlaylistTrackRelation(BaseModel):
    track: ReadTrack

    class Config:
        from_attributes = True


class ReadPlaylistTrackRelation(WritePlaylistTrackRelation):
    id: int


class Operation(BaseModel):
    type: Literal["add", "remove"]
    resource_id: int


class WritePlaylist(BaseModel):
    name: str

    class Config:
        from_attributes = True


class ReadPlaylist(WritePlaylist):
    id: int
    owner: ReadUser
