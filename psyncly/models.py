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
from uuid import uuid4

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
    provider_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    created_on = Column(DateTime(), default=datetime.now, nullable=False)
    update_on = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    owner = relationship("User", back_populates="playlists")
    tracks = relationship(
        "Track",
        secondary="track_playlist_associations",
        back_populates="playlists",
    )
    consumers = relationship(
        "Service",
        secondary="consumers_associations",
        back_populates="playlists_as_consumer",
    )
    provider = relationship("Service", back_populates="playlists_as_provider")


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
        secondary="track_playlist_associations",
        back_populates="tracks",
        viewonly=True,
    )


class CronTasks(Base):
    __tablename__ = "cron_tasks"

    id = Column(Integer, primary_key=True)
    cron_id = Column(String, default=uuid4)
    # provider
    # consumers


class Sevice(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)

    playlist_as_consumer = relationship(
        "Playlist",
        secondary="consumers_associations",
        back_populates="consumers",
    )
    playlist_as_provider = relationship("Playlist", back_populates="provider")


class ConsumersAssociation(Base):
    __tablename__ = "consumers_associations"

    playlist_id = Column(Integer, ForeignKey("playlists.id"), primary_key=True)
    service_id = Column(Integer, ForeignKey("services.id"), primary_key=True)


class TrackPlaylistAssociation(Base):
    __tablename__ = "track_playlist_associations"

    track_id = Column(Integer, ForeignKey("tracks.id"), primary_key=True)
    playlist_id = Column(Integer, ForeignKey("playlists.id"), primary_key=True)
