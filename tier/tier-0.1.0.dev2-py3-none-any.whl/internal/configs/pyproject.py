# std
from __future__ import annotations
import os
from typing import List, Optional as Opt, TYPE_CHECKING

# internal
from tier.internal.build_systems import build_system
from tier.internal.configs.toml import Toml

if TYPE_CHECKING:
    from tier.internal.build_systems.abstract_build_system import AbstractBuildSystem


class PyProject(Toml):

    FILENAME = 'pyproject.toml'

    @property
    def dirpath(self) -> str:
        return os.path.dirname(self.filepath)

    def get_build_system(self) -> 'AbstractBuildSystem':
        return build_system.get(self.sub())

    @classmethod
    def from_dirpath(cls, dirpath: Opt[str] = None, **kwargs) -> PyProject:
        filepath = os.path.join(dirpath or os.getcwd(), cls.FILENAME)
        return cls.read_or_new(filepath, **kwargs)

    @classmethod
    def find_recursively(cls, dirpath: Opt[str] = None) -> List[PyProject]:
        dirpath = dirpath or os.getcwd()
        result = []
        for dirpath, dirnames, filenames in os.walk(dirpath):
            if cls.FILENAME in filenames:
                result.append(PyProject.from_dirpath(dirpath, auto_write=True))
        return result
