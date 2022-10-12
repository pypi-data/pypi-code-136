from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

import atoti as tt
from atoti._local_session import LocalSession

from ._source import load_sql, read_sql


class SQLPlugin(Plugin):
    def activate(self) -> None:
        # See https://github.com/python/mypy/issues/2427.
        tt.Table.load_sql = load_sql  # type: ignore[assignment]
        # See https://github.com/python/mypy/issues/2427.
        tt.Session.read_sql = read_sql  # type: ignore[assignment]

    def init_session(self, session: BaseSessionBound, /) -> None:
        if not isinstance(session, LocalSession):
            return

        session._java_api.gateway.jvm.io.atoti.loading.sql.SqlPlugin.init()  # pyright: ignore

    @property
    def jar_path(self) -> Optional[Path]:
        return Path(__file__).parent / "data" / "atoti-sql.jar"
