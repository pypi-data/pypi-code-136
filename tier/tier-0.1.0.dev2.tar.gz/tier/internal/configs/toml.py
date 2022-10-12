# std
from __future__ import annotations

# external
import toml as _toml

# internal
from tier.internal.types import DictData
from tier.internal.configs.abstract_config import AbstractConfig


class Toml(AbstractConfig):

    @classmethod
    def dump(cls, data: DictData, filepath: str):
        with open(filepath, 'w') as fh:
            _toml.dump(data, fh)

    @classmethod
    def load(cls, filepath: str) -> DictData:
        with open(filepath, 'r') as fh:
            return _toml.load(fh)
