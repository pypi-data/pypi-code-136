from web_foundation.kernel.channel import IChannel


class Resource:
    _channel: IChannel
    _inited: bool

    def __init__(self, *args, **kwargs):
        _inited = False

    async def init(self, channel: IChannel, *args, **kwargs):
        self._channel = channel
        self._inited = True

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
