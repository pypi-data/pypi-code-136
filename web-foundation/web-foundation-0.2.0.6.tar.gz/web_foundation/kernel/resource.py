from typing import Any

from web_foundation.config import GenericConfig
from web_foundation.kernel.channel import IChannel


class Resource:
    _communicator: Any | None
    _channel: IChannel | None
    _inited: bool
    _config: GenericConfig

    def __init__(self, *args, **kwargs):
        _inited = False

    async def init(self, config: GenericConfig, channel: IChannel | None = None, communicator: Any | None = None, *args,
                   **kwargs) -> None:
        self._config = config
        self._channel = channel
        self._inited = True
        self._communicator = communicator

    async def shutdown(self):
        raise NotImplementedError

    @property
    def ready(self):
        return self._inited

    @property
    def channel(self):
        if not self._inited:
            raise RuntimeError("Resource not inited")
        return self._channel

    @property
    def communicator(self):
        if not self._inited:
            raise RuntimeError("Resource not inited. Can't access to communicator")
        return self._communicator
