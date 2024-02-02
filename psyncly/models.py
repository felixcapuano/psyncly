"""
doc: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#combining-association-object-with-many-to-many-access-patterns
"""

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
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    playlists = relationship("Playlist", back_populates="owner")
    service_accounts = relationship("ServiceAccount", back_populates="owner")


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    owner = relationship("User", back_populates="playlists")
    workers = relationship("Worker", back_populates="playlist")
    tracks = relationship(
        "Track",
        secondary="track_associations",
        back_populates="playlists",
    )
    service_playlists = relationship("ServicePlaylist", back_populates="playlist")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    isrc = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    playlists = relationship(
        "Playlist",
        secondary="track_associations",
        back_populates="tracks",
        viewonly=True,
    )


class ServicePlaylist(Base):
    __tablename__ = "service_playlists"

    id = Column(Integer, primary_key=True)
    external_id = Column(String, nullable=False)
    playlist_id = Column(Integer, ForeignKey("playlists.id"), nullable=False)
    service_account_id = Column(
        Integer, ForeignKey("service_accounts.id"), nullable=False
    )
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    service_account = relationship("ServiceAccount", back_populates="service_playlists")
    playlist = relationship("Playlist", back_populates="service_playlists")


class ServiceAccount(Base):
    __tablename__ = "service_accounts"

    id = Column(Integer, primary_key=True)
    service_type = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    service_playlists = relationship(
        "ServicePlaylist", back_populates="service_account"
    )
    owner = relationship("User", back_populates="service_accounts")


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)
    worker_id = Column(String, default=uuid4, nullable=False)
    worker_type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    playlist_id = Column(Integer, ForeignKey("playlists.id"), nullable=False)
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )

    playlist = relationship("Playlist", back_populates="workers")


class TrackPlaylistAssociation(Base):
    __tablename__ = "track_associations"

    track_id = Column(Integer, ForeignKey("tracks.id"), primary_key=True)
    playlist_id = Column(Integer, ForeignKey("playlists.id"), primary_key=True)
