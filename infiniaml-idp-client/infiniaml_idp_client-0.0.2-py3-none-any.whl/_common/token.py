from datetime import datetime, timedelta
from typing import ClassVar


class Token:

    type: ClassVar[str] = "Bearer"
    buffer: ClassVar[timedelta] = timedelta(seconds=10)

    def __init__(self, *, value: str, expires_in: int):
        self._value = value
        self._created = datetime.now()
        self._expiration_date = self._created + timedelta(seconds=expires_in)

    @property
    def is_expired(self) -> bool:
        if datetime.now() > self._expiration_date - self.buffer:
            return True
        return False

    @property
    def value(self) -> str:
        return self._value
