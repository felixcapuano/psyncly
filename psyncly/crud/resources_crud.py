from psyncly import models
from typing import Any

from sqlalchemy.orm import Session

from psyncly.crud.base_crud import BaseCrud
from psyncly.database import Base
from functools import wraps
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError


def errorhandler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=str(e.args))

    return wrapper


class ResourceCrud(BaseCrud):
    db: Session
    ModelClass: Base = None

    def __init__(self, db: Session) -> None:
        if not self.ModelClass:
            raise ValueError("ModelClass propertry must be overwrite")

        super().__init__(db)

    @errorhandler
    def get(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: tuple | None = None,
    ):
        select = self.db.query(self.ModelClass)
        if filters:
            select = select.filter(*filters)

        return select.offset(skip).limit(limit).all()

    @errorhandler
    def get_by_id(self, id: int, filters: tuple | None = None):
        select = self.db.query(self.ModelClass)
        if filters:
            select = select.filter(self.ModelClass.id == id, *filters)
        else:
            select = select.filter_by(id=id)

        return select.first()

    @errorhandler
    def create(self, obj: dict):
        new_obj = self.ModelClass(**obj)
        self.db.add(new_obj)
        self.db.commit()

        return new_obj

    @errorhandler
    def modify(self, id: int, obj: dict):
        select = self.db.query(self.ModelClass).filter_by(id=id)
        select.update(obj)
        self.db.commit()

    @errorhandler
    def delete(self, filters: tuple | None = None):
        select = self.db.query(self.ModelClass)
        if filters:
            select = select.filter(*filters)
        select.delete()
        self.db.commit()

    @errorhandler
    def delete_by_id(self, id: int, filters: dict | None = None):
        select = self.db.query(self.ModelClass)
        if filters:
            select = select.filter_by(self.ModelClass.id == id, *filters)
        else:
            select = select.filter_by(id=id)
        select.delete()
        self.db.commit()


class TrackCrud(ResourceCrud):
    ModelClass = models.Track


class UserCrud(ResourceCrud):
    ModelClass = models.User


class PlaylistCrud(ResourceCrud):
    ModelClass = models.Playlist


class ServicePlaylistCrud(ResourceCrud):
    ModelClass = models.ServicePlaylist


class ServiceAccountCrud(ResourceCrud):
    ModelClass = models.ServiceAccount


class WorkerCrud(ResourceCrud):
    ModelClass = models.Worker
