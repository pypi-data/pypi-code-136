from abc import ABC, abstractmethod
import importlib
from os import getenv
import json

from typing import *


DEFAULT_WATERMARK_STORE = "odp.compute.flow_state.store.WatermarkInmemoryStore"


class WatermarkStore(ABC):
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        pass

    @abstractmethod
    def set(self, key: str, value: Any):
        pass

    @abstractmethod
    def list_keys(self, pattern: str) -> List[str]:
        pass

    @classmethod
    def from_file(cls, fname: str, open_mode: str = "r"):
        with open(fname, open_mode) as fd:
            return cls(**json.load(fd))


def get_watermark_store() -> WatermarkStore:

    try:
        store_packagename = getenv("ODP__WATERMARK_STORE_CLS", DEFAULT_WATERMARK_STORE)
        store_args = [
            x.strip() for x in getenv("ODP__WATERMARK_STORE_ARGS", "").split(",")
        ]
        store_args = [x for x in store_args if x]

        parts = store_packagename.split(".")

        if parts[-1][0].islower():
            store_packagename, store_clsname = ".".join(parts[:-2]), parts[-2]
            store_funcname = parts[-1]
        else:
            store_packagename, store_clsname = ".".join(parts[:-1]), parts[-1]
            store_funcname = None

        store_module = importlib.import_module(store_packagename)
        store_cls = getattr(store_module, store_clsname)

        if store_funcname:
            return getattr(store_cls, store_funcname)(*store_args)
        else:
            return store_cls(*store_args)
    except KeyError:
        from odp.compute.flow_state.store.watermark_inmemory_store import (
            WatermarkInmemoryStore,
        )

        return WatermarkInmemoryStore()
