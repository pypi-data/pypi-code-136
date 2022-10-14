from types import TracebackType
from typing import (
    Any,
    AsyncContextManager,
    List,
    Mapping,
    NewType,
    Optional,
    Type,
)

from sqlalchemy.sql import ClauseElement

Record = NewType("Record", Mapping)


class Connection:
    async def fetch_all(
        self, query: ClauseElement, values: dict = None
    ) -> List[Record]:
        ...

    async def fetch_one(
        self, query: ClauseElement, values: dict = None
    ) -> Optional[Record]:
        ...

    async def execute(self, query: ClauseElement, values: dict = None) -> Any:
        ...

    def transaction(self) -> AsyncContextManager["Connection"]:
        ...


class Database(Connection):
    async def connect(self) -> None:
        ...

    async def disconnect(self) -> None:
        ...

    async def __aenter__(self) -> "Database":
        await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> None:
        await self.disconnect()
