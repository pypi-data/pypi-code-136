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

    async def exists(self, path: Path) -> bool: # Todo async
        return self.root.joinpath(path).exists()

    async def get_full_path(self, path: Path) -> Path: # Todo async
        return self.root.joinpath(path)

    async def open(self, path: Path, *args, **kwargs) -> AiofilesContextManager:
        return open(self.root.joinpath(path), *args, **kwargs)

    async def remove(self, path: Path, recursive: bool = False, *args, **kwargs):
        if recursive and path.is_dir():
            await rmtree(path, *args, **kwargs)
        else:
            await os.remove(path, *args, **kwargs)

    async def replace(self, path: Path, new_path: Path, *args, **kwargs):
        await os.replace(path, new_path, *args, **kwargs)

    async def mkdir(self, path: Path, *args, **kwargs):
        await os.mkdir(path, *args, **kwargs)

    async def makedirs(self, path: Path, *args, **kwargs):
        await os.makedirs(path, exist_ok=True)

    async def rename(self, path: Path, new_name: str, *args, **kwargs):
        await os.rename(path, path.parent.joinpath(new_name))

    async def list(self, path: Path, *args, **kwargs) -> Generator[Path, None, None]:
        target = self.root.joinpath(path)
        return target.iterdir()

    async def shutdown(self):
        pass

    async def init(self, channel: IChannel, *args, **kwargs):
        await super(OsFilesResource, self).init(channel, *args, **kwargs)
        if not self.root.exists():
            raise FileNotFoundError(str(self.root))
