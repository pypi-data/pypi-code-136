from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

from atoti._local_session import LocalSession


class AzurePlugin(Plugin):
    def init_session(self, session: BaseSessionBound, /) -> None:
        if not isinstance(session, LocalSession):
            return

        session._java_api.gateway.jvm.io.atoti.loading.azure.AzurePlugin.init()  # pyright: ignore

    @property
    def jar_path(self) -> Optional[Path]:
        return Path(__file__).parent / "data" / "atoti-azure.jar"
