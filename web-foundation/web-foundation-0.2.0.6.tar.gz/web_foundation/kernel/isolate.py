import asyncio
from abc import ABCMeta
from typing import Dict

from web_foundation.kernel.channel import IChannel


class Isolate(metaclass=ABCMeta):
    name: str
    channel: IChannel
    init_kwargs: Dict

    def __init__(self, name: str, **kwargs):
        self.name = name
        self.channel = IChannel(f"Channel_{name}")
        self.init_kwargs = kwargs

    async def work(self, **kwargs) -> None:
        raise NotImplementedError

    def run_forked(self) -> None:
        async def call():
            nonlocal self
            asyncio.create_task(self.channel.listen_consume())
            await self.work(**self.init_kwargs)

        try:
            asyncio.run(call())
        except KeyboardInterrupt:
            print("done")
            self.close()

    def close(self):
        pass
