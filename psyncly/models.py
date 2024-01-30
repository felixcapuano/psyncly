"""
doc: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#combining-association-object-with-many-to-many-access-patterns
"""
from typing import List
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    DateTime,
)
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime

from psyncly.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, index=True)
    created_on = Column(DateTime(), default=datetime.now, nullable=False)
    update_on = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    playlists = relationship("Playlist", back_populates="owner")


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_on = Column(DateTime(), default=datetime.now, nullable=False)
    update_on = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    owner = relationship("User", back_populates="playlists")

    tracks = relationship(
        "Track",
        secondary="track_playlist_association",
        back_populates="playlists",
    )
    # track_associations = relationship(
    #     "TrackPlaylistAssociation",
    #     back_populates="playlist",
    # )


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    isrc = Column(String, unique=True, nullable=False)
    created_on = Column(DateTime(), default=datetime.now, nullable=False)
    update_on = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    playlists = relationship(
        "Playlist",
        secondary="track_playlist_association",
        back_populates="tracks",
        viewonly=True,
    )
    # playlist_associations = relationship(
    #     "TrackPlaylistAssociation",
    #     back_populates="track",
    # )


class TrackPlaylistAssociation(Base):
    __tablename__ = "track_playlist_association"

    track_id = Column(Integer, ForeignKey("tracks.id"), primary_key=True)
    playlist_id = Column(Integer, ForeignKey("playlists.id"), primary_key=True)

    # playlist = relationship("Playlist", back_populates="track_associations")
    # track = relationship("Track", back_populates="playlist_associations")


# class PlaylistTrackRelation(Base):
#     __tablename__ = "playlist_track_relation"
#     __table_args__ = (
#         UniqueConstraint(
#             "track_id", "playlist_id", name="playlist_track_relation_constraint"
#         ),
#     )

#     id = Column(Integer, primary_key=True)
#     track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False)
#     playlist_id = Column(Integer, ForeignKey("playlists.id"), nullable=False)
#     created_on = Column(DateTime(), default=datetime.now, nullable=False)

#     track = relationship("Track", back_populates="playlists")
#     playlist = relationship("Playlist", back_populates="tracks")
