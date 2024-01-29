from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from psyncly.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, index=True)
    playlists = relationship("Playlist", back_populates="owner")


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="playlists")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)
    isrc = Column(String, unique=True)


class PlaylistContent(Base):
    __tablename__ = "playlist_content"

    id = Column(Integer, primary_key=True)
    track_id = Column(Integer, ForeignKey("tracks.id"))
    playlist_id = Column(Integer, ForeignKey("playlists.id"))
