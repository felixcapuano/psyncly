from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
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

    tracks = relationship("PlaylistTrackRelation", back_populates="playlist")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)

    title = Column(String)
    artist = Column(String)
    isrc = Column(String, unique=True)

    playlists = relationship("PlaylistTrackRelation", back_populates="track")


class PlaylistTrackRelation(Base):
    __tablename__ = "playlist_track_relation"
    __table_args__ = (
        UniqueConstraint(
            "track_id", "playlist_id", name="playlist_track_relation_constraint"
        ),
    )

    id = Column(Integer, primary_key=True)

    track_id = Column(Integer, ForeignKey("tracks.id"))
    track = relationship("Track", back_populates="")

    playlist_id = Column(Integer, ForeignKey("playlists.id"))
    playlist = relationship("Playlist", back_populates="tracks")
