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
        filters: dict | None = None,
        skip: int = 0,
        limit: int = 100,
    ):
        select = self.db.query(self.ModelClass)
        if filters:
            select = select.filter_by(**filters)

        return select.offset(skip).limit(limit).all()

    @errorhandler
    def get_by_id(self, id: int):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)

        return select.first()

    @errorhandler
    def create(self, obj: Any):
        new_obj = self.ModelClass(**dict(obj))
        self.db.add(new_obj)
        self.db.commit()

        return new_obj

    @errorhandler
    def modify(self, id: int, obj: Any):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)
        select.update(dict(obj))
        self.db.commit()

        return select.first()

    @errorhandler
    def delete(self, filters: dict | None = None):
        select = self.db.query(self.ModelClass)
        if filters:
            select = select.filter_by(**filters)
        select.delete()
        self.db.commit()

    @errorhandler
    def delete_by_id(self, id: int):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)
        select.delete()
        self.db.commit()


class TrackCrud(ResourceCrud):
    ModelClass = models.Track


class UserCrud(ResourceCrud):
    ModelClass = models.User


class PlaylistCrud(ResourceCrud):
    ModelClass = models.Playlist
