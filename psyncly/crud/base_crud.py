from typing import Any

from sqlalchemy.orm import Session


class BaseCrud:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self, skip: int = 0, limit: int = 100, filters: dict = {}):
        return self._list(skip, limit, filters)

    def get(self, id: int):
        return self._get(id)

    def create(self, obj: Any):
        return self._create(obj)

    def modify(self, id: int, obj: Any):
        return self._modify(id, obj)

    def delete(self, id: int):
        return self._delete(id)

    def _list(self, skip: int, limit: int, filters: dict):
        raise NotImplementedError()

    def _get(self, id: int):
        raise NotImplementedError()

    def _create(self, object: Any):
        raise NotImplementedError()

    def _modify(self, id: int, object: Any):
        raise NotImplementedError()

    def _delete(self, id: int):
        raise NotImplementedError()
