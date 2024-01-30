from typing import Any

from sqlalchemy.orm import Session

from psyncly.crud.base_crud import BaseCrud, crudmethod
from psyncly.database import Base


class GenericCrud(BaseCrud):
    db: Session
    ModelClass: Base = None

    def __init__(self, db: Session) -> None:
        if not self.ModelClass:
            raise ValueError("ModelClass propertry must be overwrite")

        super().__init__(db)

    @crudmethod
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

    @crudmethod
    def get_by_id(self, id: int):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)

        return select.first()

    @crudmethod
    def create(self, obj: Any):
        new_obj = self.ModelClass(**dict(obj))
        self.db.add(new_obj)
        self.db.commit()
        self.db.refresh(new_obj)

        return new_obj

    @crudmethod
    def modify(self, id: int, obj: Any):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)
        select.update(dict(obj))
        self.db.commit()

        return select.first()

    @crudmethod
    def delete(self, filters: dict | None = None):
        select = self.db.query(self.ModelClass)

        if filters:
            select = select.filter_by(**filters)

        select.delete()
        self.db.commit()

    @crudmethod
    def delete_by_id(self, id: int):
        select = self.db.query(self.ModelClass).filter(self.ModelClass.id == id)
        select.delete()
        self.db.commit()
