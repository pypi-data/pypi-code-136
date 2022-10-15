# Copyright (c) 2022 Mario S. Könz; License: MIT
import typing as tp

T = tp.TypeVar("T")  # pylint: disable=invalid-name


class StoreProtocol(tp.Protocol):
    def dump(self, obj: T) -> tp.Any:
        pass  # pragma: no cover

    def load(self, dataclass: type[T], **filter_kwgs: tp.Any) -> T:
        pass  # pragma: no cover
