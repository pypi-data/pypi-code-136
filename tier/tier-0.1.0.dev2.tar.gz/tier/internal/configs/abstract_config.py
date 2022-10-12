# std
from __future__ import annotations
import os
from abc import abstractmethod
from typing import Generic, List, Optional as Opt, TypeVar, Union

# internal
from tier.internal.types import AtomicData, DictData, ListData, Data
from tier.internal import dict_utils

# types
T = TypeVar('T', AtomicData, DictData, ListData, Data)


class AbstractConfig:

    def __init__(self, filepath: str, data: Opt[DictData] = None, auto_write: bool = False):
        self.data: DictData = data or {}
        self.filepath: str = filepath
        self.auto_write: bool = auto_write

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}<{self.filepath}>'

    def __getitem__(self, key: Union[str, List[str]]):
        return self.get(key)

    def __setitem__(self, key: Union[str, List[str]], value: Data):
        self.set(key, value)

    def get(self, key: Union[str, List[str]], default: Data = None) -> Data:
        return dict_utils.safeget(self.data, key, default)

    def set(self, key: Union[str, List[str]], value: Data):
        dict_utils.safeset(self.data, key, value)
        if self.auto_write:
            self.write()

    def exists(self) -> bool:
        return os.path.isfile(self.filepath)

    def sub(self, prefix: Opt[Union[str, List[str]]] = None) -> SubConfig:
        return SubConfig(self, prefix)

    def write(self):
        self.dump(self.data, self.filepath)

    @classmethod
    def new(cls, filepath: str, data: Opt[DictData] = None, **kwargs) -> AbstractConfig:
        config = cls(filepath, data or {}, **kwargs)
        if config.auto_write:
            config.write()
        return config

    @classmethod
    def read(cls, filepath: str, **kwargs) -> AbstractConfig:
        return cls(filepath, cls.load(filepath), **kwargs)

    @classmethod
    def read_or_new(cls, filepath: str, data: Opt[DictData] = None, **kwargs) -> AbstractConfig:
        if os.path.isfile(filepath):
            return cls.read(filepath, **kwargs)
        else:
            return cls.new(filepath, data, **kwargs)

    @classmethod
    @abstractmethod
    def load(cls, filepath: str) -> DictData:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def dump(cls, data: DictData, filepath: str):
        raise NotImplementedError


class SubConfig(Generic[T]):

    def __init__(self, parent: AbstractConfig, prefix: Opt[Union[str, List[str]]] = None):
        self.parent: AbstractConfig = parent
        self.prefix: List[str] = dict_utils.normalize_keys(prefix)

    def __repr__(self) -> str:
        return repr(self.parent)

    def __getitem__(self, key: Union[str, List[str]]):
        return self.get(key)

    def __setitem__(self, key: Union[str, List[str]], value: T):
        self.set(key, value)

    def get(self, key: Opt[Union[str, List[str]]] = None, default: T = None) -> T:
        full_keys = self.prefix + dict_utils.normalize_keys(key)
        return self.parent.get(full_keys, default)

    def set(self, key: Opt[Union[str, List[str]]] = None, value: T = None):
        full_keys = self.prefix + dict_utils.normalize_keys(key)
        self.parent.set(full_keys, value)
