from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

from atoti._local_session import LocalSession


class GCPPlugin(Plugin):
    def init_session(self, session: BaseSessionBound, /) -> None:
        if not isinstance(session, LocalSession):
            return

        session._java_api.gateway.jvm.io.atoti.loading.gcp.GcpPlugin.init()  # pyright: ignore

    @property
    def jar_path(self) -> Optional[Path]:
        return Path(__file__).parent / "data" / "atoti-gcp.jar"
