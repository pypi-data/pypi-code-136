import contextlib
from dataclasses import dataclass, replace
from typing import Dict, List, Optional, Tuple

from aio_pika import RobustConnection as RmqConnection

from dropland.data.context import get_context
from .engine import RmqStorageBackend, RmqStorageEngine


@dataclass
class Session:
    engine: RmqStorageEngine
    connection: RmqConnection


class ConnectionContext:
    def __init__(self):
        self.sessions: Dict[str, Session] = dict()


class SessionManager:
    def __init__(self, engine_factory: RmqStorageBackend):
        self._engine_factory = engine_factory

    def get_session(self, name: str) -> Optional[Session]:
        ctx = get_context()
        if '_rmq_session' not in ctx:
            ctx._rmq_session = ConnectionContext()
        return ctx._rmq_session.sessions.get(name)

    def get_or_create_session(self, name: str) -> Tuple[bool, Optional[Session]]:
        if session := self.get_session(name):
            return False, session

        if engine := self._engine_factory.get_engine(name):
            return True, Session(
                engine=engine,
                connection=engine.new_connection())

        return False, None

    @contextlib.asynccontextmanager
    async def session_context(self, name: str):
        created, session = self.get_or_create_session(name)

        if not created:
            yield session
            return

        async with session.connection as conn:
            session = replace(session, connection=conn)
            yield self._add_session(name, session)
            self._remove_session(name)

    @contextlib.asynccontextmanager
    async def init_engines(self, names: List[str] = None):
        engines = self._engine_factory.get_engines(names or [])
        async with contextlib.AsyncExitStack() as stack:
            for name, engine in engines.items():
                assert engine is self._engine_factory.get_engine(name)
                if engine.is_async:
                    await engine.async_start()
                    stack.push_async_callback(engine.async_stop)
                else:
                    engine.start()
                    stack.callback(engine.stop)
            yield

    def _add_session(self, name: str, data: Session) -> Session:
        ctx = get_context()
        if '_rmq_session' not in ctx:
            ctx._rmq_session = ConnectionContext()
        ctx._rmq_session.sessions[name] = data
        return data

    def _remove_session(self, name: str):
        ctx = get_context()
        if '_rmq_session' in ctx:
            ctx._rmq_session.sessions.pop(name)
