from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel


class Level(str, Enum):
    success = "success"
    error = "error"
    warning = "warning"


class ResponseApi(BaseModel):
    ok: bool
    message: Optional[str]
    data: Optional[Any]
    level: Level

    def __init__(self, message: str, level: Level, data: Optional[Any] = None):
        super().__init__(
            ok=level == Level.success,
            message=message,
            data=data,
            level=level
        )


class ResponseException(Exception):
    def __init__(self, name: str):
        self.name = name
