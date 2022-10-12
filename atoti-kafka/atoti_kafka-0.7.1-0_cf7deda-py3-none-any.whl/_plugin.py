from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

import atoti as tt
from atoti._local_session import LocalSession

from ._source import load_kafka


class KafkaPlugin(Plugin):
    def activate(self) -> None:
        # See https://github.com/python/mypy/issues/2427.
        tt.Table.load_kafka = load_kafka  # type: ignore[assignment]

    @property
    def jar_path(self) -> Optional[Path]:
        return Path(__file__).parent / "data" / "atoti-kafka.jar"

    def init_session(self, session: BaseSessionBound, /) -> None:
        if not isinstance(session, LocalSession):
            return

        session._java_api.gateway.jvm.io.atoti.loading.kafka.KafkaPlugin.init()  # pyright: ignore
