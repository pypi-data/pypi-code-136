import shutil
from enum import Enum
from pathlib import Path
from typing import Type, TypeVar, Generic, Any, Generator
from aiofiles import os
from aiofiles.os import wrap
from aiofiles.threadpool import open
from aiofiles.base import AiofilesContextManager

from web_foundation.kernel.channel import IChannel
from web_foundation.resources.files.interface import FilesResource

rmtree = wrap(shutil.rmtree)


class OsFilesResource(FilesResource):

    def __init__(self, root, *args, **kwargs):
        self.root = root
        super().__init__(*args, **kwargs)

    def exists(self, path: Path) -> bool:
        return self.root.joinpath(path).exists()

    def get_full_path(self, path: Path) -> Path:
        return self.root.joinpath(path)

    async def open(self, path: Path, *args, **kwargs) -> AiofilesContextManager:
        return open(self.root.joinpath(path), *args, **kwargs)

    async def remove(self, path: Path, *args, **kwargs):
        if path.is_dir():
            await rmtree(path, *args, **kwargs)
        else:
            await os.remove(path, *args, **kwargs)

    async def list(self, path: Path, *args, **kwargs) -> Generator[Path, None, None]:
        target = self.root.joinpath(path)
        return target.iterdir()

    async def shutdown(self):
        pass

    async def init(self, channel: IChannel, *args, **kwargs):
        await super(OsFilesResource, self).init(channel, *args, **kwargs)
        if not self.root.exists():
            raise FileNotFoundError(str(self.root))
