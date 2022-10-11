from dataclasses import dataclass, field
from typing import Any, Optional

__all__ = ["Watermark"]

from .watermark_store import WatermarkStore


@dataclass
class Watermark:

    key: str
    value: Any
    store: WatermarkStore

    _watermark: Any = field(init=False, repr=False, default=None)

    def __post_init__(self):
        self.update()

    @property
    def watermark(self) -> Any:
        return self._watermark

    @watermark.setter
    def watermark(self, watermark: Any):
        self.set_watermark(watermark, persist=True)

    def set_watermark(self, watermark: Any, persist: bool = True):

        self._watermark = watermark
        if persist:
            self.persist()

    def get_watermark(self, default=None) -> Any:
        return self.watermark or default

    def persist(self):
        self.store.set(self.key, self._watermark)

    def update(self):
        self._watermark = self.store.get(self.key)

    def create_instance_watermark(
        self, key: str, value: Any = None, store: Optional[WatermarkStore] = None
    ) -> "Watermark":
        return Watermark(
            key=f"{self.key}:{key}", value=value, store=store or self.store
        )
