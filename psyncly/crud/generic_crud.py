from typing import Any

from sqlalchemy.orm import Session

from psyncly import models, schemas
from psyncly.crud.base_crud import BaseCrud
from psyncly.database import Base


class GenericCrud(BaseCrud):
    db: Session
    ModelClass: Base = None

    def __init__(self, db: Session) -> None:
        if not self.ModelClass:
            raise ValueError("ModelClass propertry must be overwrite")

        super().__init__(db)

    def _list(self, skip: int = 0, limit: int = 100, _: dict = {}):
        select = self.db.query(self.ModelClass).offset(skip).limit(limit)

        return select.all()

    def _get(self, id: int):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)

        return select.first()

    def _create(self, obj: Any):
        new_obj = self.ModelClass(**dict(obj))
        self.db.add(new_obj)
        self.db.commit()
        self.db.refresh(new_obj)

        return new_obj

        # except exc.SQLAlchemyError as e:
        #     self.db.rollback()
        #     raise e

    def _modify(self, id: int, obj: Any):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)
        select.update(dict(obj))
        self.db.commit()

        return select.first()

    def _delete(self, id: int):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)
        select.delete()
        self.db.commit()
