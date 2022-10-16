import contextlib
from collections import defaultdict
from dataclasses import dataclass, replace
from typing import Any, Dict, List, Optional, Set, Tuple

from dropland.blocks.sql.base import SqlStorageType
from dropland.data.context import get_context
from .engine import EngineKey, SqlStorageEngine, SqlStorageBackend


@dataclass
class Session:
    engine: SqlStorageEngine
    connection: Any
    timeout_secs: int
    in_transaction: bool = False


class ConnectionContext:
    def __init__(self):
        self.sessions: Dict[str, Session] = dict()
        self.sessions_by_key: Dict[EngineKey, Set[str]] = defaultdict(set)


class SessionManager:
    def __init__(self, engine_factory: SqlStorageBackend):
        self._engine_factory = engine_factory

    def get_session(self, name: str) -> Optional[Session]:
        ctx = get_context()
        if '_sql_session' not in ctx:
            ctx._sql_session = ConnectionContext()
        return ctx._sql_session.sessions.get(name)

    def get_sessions_for_type(self, db_type: SqlStorageType, is_async: bool) -> List[Session]:
        ctx = get_context()
        if '_sql_session' not in ctx:
            ctx._sql_session = ConnectionContext()
        conn_names = ctx._sql_session.sessions_by_key[EngineKey(db_type=db_type, is_async=is_async)]
        return [ctx._sql_session.sessions.get(name) for name in conn_names if name in ctx._sql_session.sessions]

    def get_or_create_session(self, name: str) -> Tuple[bool, Optional[Session]]:
        if conn := self.get_session(name):
            return False, conn

        if engine := self._engine_factory.get_engine(name):
            return True, Session(
                engine=engine, connection=engine.new_connection(),
                timeout_secs=int(engine.timeout.total_seconds()))

        return False, None

    @contextlib.contextmanager
    def sync_session_context(self, name: str, begin_tx: bool = True, autocommit: bool = True):
        created, session = self.get_or_create_session(name)
        assert not session.engine.is_async, \
            f'Sql engine with name "{name}" has only async driver, ' \
            f'use async_session_context() function instead'

        if not created:
            if begin_tx and not session.in_transaction:
                with session.engine.sync_transaction_context(session.connection, autocommit):
                    yield self._add_session(name, replace(session, in_transaction=True))
                    self._add_session(name, replace(session, in_transaction=False))
            else:
                yield session
            return

        with session.connection as conn:
            assert isinstance(conn, session.engine.connection_class), \
                f'Engine with name "{name}" has only async driver, ' \
                f'use async_session_context() function instead'

            session = replace(session, connection=conn, in_transaction=begin_tx)
            if begin_tx:
                with session.engine.sync_transaction_context(session.connection, autocommit):
                    yield self._add_session(name, session)
            else:
                yield self._add_session(name, session)
            self._remove_session(name)

    @contextlib.asynccontextmanager
    async def session_context(self, name: str, begin_tx: bool = True, autocommit: bool = True):
        created, session = self.get_or_create_session(name)
        assert session.engine.is_async, \
            f'Sql engine with name "{name}" has only sync driver, ' \
            f'use session_context() function instead'

        if not created:
            if begin_tx and not session.in_transaction:
                async with session.engine.transaction_context(session.connection, autocommit):
                    yield self._add_session(name, replace(session, in_transaction=True))
                    self._add_session(name, replace(session, in_transaction=False))
            else:
                yield session
            return

        async with session.connection as conn:
            assert isinstance(conn, session.engine.connection_class), \
                f'Sql engine with name "{name}" has only sync driver, ' \
                f'use session_context() function instead'

            session = replace(session, connection=conn, in_transaction=begin_tx)
            if begin_tx:
                async with session.engine.transaction_context(session.connection, autocommit):
                    yield self._add_session(name, session)
            else:
                yield self._add_session(name, session)
            self._remove_session(name)

    @contextlib.contextmanager
    def init_sync_engines(self, names: List[str] = None):
        engines = self._engine_factory.get_engines(names or [])
        with contextlib.ExitStack() as stack:
            for name, engine in engines.items():
                if engine.is_async:
                    continue
                engine.sync_start()
                stack.callback(engine.sync_stop)
            yield

    @contextlib.asynccontextmanager
    async def init_engines(self, names: List[str] = None):
        engines = self._engine_factory.get_engines(names or [])
        async with contextlib.AsyncExitStack() as stack:
            for name, engine in engines.items():
                if engine.is_async:
                    await engine.start()
                    stack.push_async_callback(engine.stop)
                else:
                    engine.sync_start()
                    stack.callback(engine.sync_stop)
            yield

    def _add_session(self, name: str, data: Session) -> Session:
        ctx = get_context()
        if '_sql_session' not in ctx:
            ctx._sql_session = ConnectionContext()
        ctx._sql_session.sessions[name] = data
        ctx._sql_session.sessions_by_key[
            EngineKey(db_type=data.engine.db_type, is_async=data.engine.is_async)
        ].add(name)
        return data

    def _remove_session(self, name: str):
        ctx = get_context()
        if '_sql_session' in ctx:
            data = ctx._sql_session.sessions.pop(name, None)
            ctx._sql_session.sessions_by_key.pop(
                EngineKey(db_type=data.engine.db_type, is_async=data.engine.is_async), None)
