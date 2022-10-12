from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

from atoti._local_session import LocalSession


class AWSPlugin(Plugin):
    def init_session(self, session: BaseSessionBound, /) -> None:
        if not isinstance(session, LocalSession):
            return

        session._java_api.gateway.jvm.io.atoti.loading.s3.AwsPlugin.init()  # pyright: ignore

    @property
    def jar_path(self) -> Optional[Path]:
        return Path(__file__).parent / "data" / "atoti-aws.jar"
