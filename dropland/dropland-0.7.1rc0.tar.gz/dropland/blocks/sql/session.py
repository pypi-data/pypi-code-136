import contextlib
from collections import defaultdict
from dataclasses import dataclass, replace
from typing import Any, Dict, List, Mapping, Optional, Sequence, Set, Tuple

from contextvars import ContextVar

from dropland.blocks.sql.base import SqlStorageType
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
        self._ctx: ContextVar[ConnectionContext] = ContextVar('_ctx', default=ConnectionContext())
        self._engine_factory = engine_factory

    def get_session(self, name: str) -> Optional[Session]:
        return self._ctx.get().sessions.get(name)

    def get_sessions_for_type(self, db_type: SqlStorageType, is_async: bool) -> List[Session]:
        ctx = self._ctx.get()
        conn_names = ctx.sessions_by_key[EngineKey(db_type=db_type, is_async=is_async)]
        return [ctx.sessions.get(name) for name in conn_names if name in ctx.sessions]

    def get_or_create_session(self, name: str) -> Tuple[bool, Optional[Session]]:
        if conn := self.get_session(name):
            return False, conn

        if engine := self._engine_factory.get_engine(name):
            return True, Session(
                engine=engine, connection=engine.new_connection(),
                timeout_secs=int(engine.timeout.total_seconds()))

        return False, None

    @contextlib.contextmanager
    def session_context(self, name: str, begin_tx: bool = True, autocommit: bool = True):
        created, session = self.get_or_create_session(name)
        assert not session.engine.is_async, \
            f'Sql engine with name "{name}" has only async driver, ' \
            f'use async_session_context() function instead'

        if not created:
            if begin_tx and not session.in_transaction:
                with session.engine.transaction_context(session.connection, autocommit):
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
                with session.engine.transaction_context(session.connection, autocommit):
                    yield self._add_session(name, session)
            else:
                yield self._add_session(name, session)
            self._remove_session(name)

    @contextlib.asynccontextmanager
    async def async_session_context(self, name: str, begin_tx: bool = True, autocommit: bool = True):
        created, session = self.get_or_create_session(name)
        assert session.engine.is_async, \
            f'Sql engine with name "{name}" has only sync driver, ' \
            f'use session_context() function instead'

        if not created:
            if begin_tx and not session.in_transaction:
                async with session.engine.async_transaction_context(session.connection, autocommit):
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
                async with session.engine.async_transaction_context(session.connection, autocommit):
                    yield self._add_session(name, session)
            else:
                yield self._add_session(name, session)
            self._remove_session(name)

    @contextlib.contextmanager
    def init_engines(self, engines: Mapping[str, Sequence[SqlStorageEngine]] = None,
                     begin_tx: bool = True, autocommit: bool = True):
        engines = self._engine_factory.get_engines(engines or [])
        with contextlib.ExitStack() as stack:
            for name, engine in engines.items():
                if engine.is_async:
                    continue
                engine.start()
                stack.callback(engine.stop)
                # stack.enter_context(self.session_context(name, begin_tx, autocommit))

            yield self._ctx.get()

    @contextlib.asynccontextmanager
    async def init_async_engines(self, engines: Mapping[str, Sequence[SqlStorageEngine]] = None,
                                 begin_tx: bool = True, autocommit: bool = True):
        engines = self._engine_factory.get_engines(engines or [])
        async with contextlib.AsyncExitStack() as stack:
            for name, engine in engines.items():
                if engine.is_async:
                    await engine.async_start()
                    stack.push_async_callback(engine.async_stop)
                    # await stack.enter_async_context(
                    #     self.async_session_context(name, begin_tx, autocommit)
                    # )
                else:
                    engine.start()
                    stack.callback(engine.stop)
                    # stack.enter_context(self.session_context(name, begin_tx, autocommit))

            yield self._ctx.get()

    def _add_session(self, name: str, data: Session) -> Session:
        ctx = self._ctx.get()
        ctx.sessions[name] = data
        ctx.sessions_by_key[EngineKey(db_type=data.engine.db_type, is_async=data.engine.is_async)].add(name)
        return data

    def _remove_session(self, name: str):
        ctx = self._ctx.get()
        data = ctx.sessions.pop(name, None)
        ctx.sessions_by_key.pop(EngineKey(db_type=data.engine.db_type, is_async=data.engine.is_async), None)
