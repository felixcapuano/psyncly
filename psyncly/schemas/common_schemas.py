from typing import Literal
from pydantic import BaseModel


class Operation(BaseModel):
    type: Literal["add", "remove"]
    resource_id: int
