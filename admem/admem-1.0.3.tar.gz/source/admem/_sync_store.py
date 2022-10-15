# Copyright (c) 2022 Mario S. Könz; License: MIT
import typing as tp

from ._protocols import StoreProtocol
from ._protocols import T
from ._store_setup import ACTIVE_STORES

__all__ = ["store"]


class SyncStore:
    @property
    def get_first_active(self) -> StoreProtocol:
        return next(iter(ACTIVE_STORES.values()))

    def dump(self, obj: tp.Any) -> None:
        self.get_first_active.dump(obj)

    def load(self, dataclass: type[T], **filter_kwgs: tp.Any) -> T:
        return self.get_first_active.load(dataclass, **filter_kwgs)


store = SyncStore()
