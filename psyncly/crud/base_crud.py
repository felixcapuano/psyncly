from typing import Any

from sqlalchemy.orm import Session
from functools import wraps


def crudmethod(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


class BaseCrud:
    def __init__(self, db: Session) -> None:
        self.db = db
