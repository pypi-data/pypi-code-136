from typing import Union, Iterable
from shlex import quote
from pathlib import Path
from asyncio.subprocess import Process

from .shell import Shell


class Repo(Shell):
    pwd: Path

    def __init__(self, path: Union[str, Path]):
        super().__init__()

        self.cd(path)

    @property
    def initialized(self) -> bool:
        return (self.pwd / '.git').exists()

    async def cmd(self, args, **kwargs) -> Process:
        params = self._kwargs_to_params(**kwargs)

        return await self.run(('git', *args, *params))

    async def init(self) -> Process:
        if self.initialized:
            raise ValueError(
                f'There is already a git repository at {self.pwd}'
            )

        return await self.cmd(('init',))

    async def add(self, files: Iterable[str], **kwargs) -> Process:
        args = ('add', *map(quote, files))

        return await self.cmd(args, **kwargs)

    async def commit(self, message: str, **kwargs) -> Process:
        args = ('commit', '-m', quote(message))

        return await self.cmd(args, **kwargs)
