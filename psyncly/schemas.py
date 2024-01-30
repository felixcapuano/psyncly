from typing import Literal

from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class ModifyUser(BaseModel):
    username: str | None
    email: str | None

    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    username: str
    email: str

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


class Track(BaseModel):
    id: int
    title: str
    artist: str
    isrc: str

    class Config:
        from_attributes = True


class CreatePlaylist(BaseModel):
    name: str
    owner_id: int

    class Config:
        from_attributes = True


class ModifyPlaylist(BaseModel):
    name: str
    owner_id: int

    class Config:
        from_attributes = True


class Playlist(BaseModel):
    id: int
    name: str
    owner: User

    class Config:
        from_attributes = True


class Operation(BaseModel):
    type: Literal["add", "remove"]
    resource_id: int
