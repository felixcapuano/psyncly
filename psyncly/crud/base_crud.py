from sqlalchemy.orm import Session
from typing import Any


class BaseCrud:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get(self, skip: int, limit: int, filters: dict | None = None):
        raise NotImplementedError()

    def get_by_id(self, id: int):
        raise NotImplementedError()

    def create(self, obj: Any):
        raise NotImplementedError()

    def modify(self, id: int, obj: Any):
        raise NotImplementedError()

    def delete(self, filters: dict | None = None):
        raise NotImplementedError()

    def delete_by_id(self, id: int):
        raise NotImplementedError()
