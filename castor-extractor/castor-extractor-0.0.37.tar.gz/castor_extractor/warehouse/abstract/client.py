from abc import ABC, abstractmethod
from typing import Iterator, Optional, cast

from sqlalchemy import text
from sqlalchemy.engine import Connection, create_engine

from .query import ExtractionQuery


class AbstractWarehouseClient(ABC):
    """interface for the client to connect to the source"""

    def __init__(self, **credentials: dict):
        """init signature can vary"""
        pass

    @abstractmethod
    def connect(self) -> Connection:
        pass

    @abstractmethod
    def close(self) -> bool:
        pass

    @abstractmethod
    def execute(self, query: ExtractionQuery) -> Iterator[dict]:
        pass


class SqlalchemyClient(AbstractWarehouseClient, ABC):
    def __init__(self, credentials: dict):
        super().__init__(**credentials)
        self._uri = self._build_uri(credentials)
        self._options = self._engine_options(credentials)
        self._engine = create_engine(self._uri, **self._options)
        self._connection: Optional[Connection] = None

    @abstractmethod
    def _build_uri(self, credentials: dict) -> str:
        pass

    @abstractmethod
    def _engine_options(self, credentials: dict) -> dict:
        pass

    def connect(self) -> Connection:
        if not self._connection or self._connection.closed:
            self._connection = self._engine.connect()
        return cast(Connection, self._connection)

    def execute(self, query: ExtractionQuery) -> Iterator[dict]:
        connection = self.connect()
        try:
            proxy = connection.execute(text(query.statement), query.params)
            results = (dict(row) for row in proxy)
            return results
        finally:
            self.close()

    def close(self) -> bool:
        if not self._connection:
            return False
        self._connection.close()
        return True
