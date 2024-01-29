from functools import wraps
from typing import Any

from sqlalchemy.orm import Session


def crudmethod(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


class BaseCrud:
    def __init__(self, db: Session) -> None:
        self.db = db
