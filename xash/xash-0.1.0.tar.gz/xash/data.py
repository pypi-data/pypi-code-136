"""Data Analysis and Data Science common system definitions.

`DataClient` instances are wrappers on `pandas` datasets.

Data clients use selectors (`SelectorKey` instances) to retrieve data.  Xash
selectors are similar to the keys of `iloc` and `loc` pandas methods.

"""

from dataclasses import KW_ONLY, dataclass
from enum import Enum
from typing import Callable, Iterable, Union

import numpy as np

from pandas.core.frame import DataFrame, Series


Dataset = DataFrame | Series

DataGetter = Callable[[Dataset], Dataset]

BaseKey = (
    int
    | str
    | tuple[int | str | bool]
    | list[int | str | bool]
    | slice
    | np.ndarray
    | Series
)

LocatorKey = BaseKey | Callable[[Dataset], BaseKey]

# Error using new style unions: ``BaseKey | 'il' | 'll' | DataGetter``
SelectorKey = Union[BaseKey, 'il', 'll', DataGetter]


def is_integer(obj: object) -> bool:
    """Return whether obj is an integer, not including booleans."""
    from numbers import Integral

    return not isinstance(obj, bool) and isinstance(obj, Integral)


def normalize_key(key: LocatorKey) -> LocatorKey:
    """Normalize a key converting not structured values to lists."""
    if isinstance(key, (list, np.ndarray, Series, slice, Callable)):
        return key
    elif isinstance(key, Iterable) and not isinstance(key, str):
        return list(key)
    else:
        return [key]


@dataclass(init=False)
class locator:
    """Base class for non-implicit locators (see `il` and `ll`)."""

    selector: LocatorKey = None

    def __class_getitem__(cls, key: LocatorKey) -> SelectorKey:
        """Create the slice."""
        key = normalize_key(key)
        if cls is locator:
            return key if il.is_implicit(key) else ll(key)
        else:
            return cls(key)


@dataclass
class il(locator):
    """Explicit selector based on integer positions."""

    @staticmethod
    def is_implicit(key: BaseKey) -> bool:
        """Return whether key is a valid implicit positional key."""
        from numbers import Integral

        if isinstance(key, list):
            return len(key) > 0 and isinstance(key[0], Integral)
        elif isinstance(key, np.ndarray):
            return issubclass(key.dtype.type, (Integral, np.bool8, np.bool_))
        elif isinstance(key, Series):
            return issubclass(key.dtype.type, Integral)
        elif isinstance(key, slice):
            triplet = (key.start, key.stop, key.step)
            return sum(v is None or is_integer(v) for v in triplet) == 3
        else:
            return False


@dataclass
class ll(locator):
    """Explicit selector based on labels."""


class DataClientKind(Enum):
    """How `DataClient` will access the data."""

    COLUMNS = 0
    ROWS = 1
    DEFAULT = COLUMNS


@dataclass
class DataClient:
    """Base class for data clients.

    :param data: The source dataset.

    :param data_client_kind: The indexer method for data retrieving, default
           is column-centric.

    """

    data: Dataset
    _: KW_ONLY
    data_client_kind: DataClientKind = DataClientKind.DEFAULT

    def __getitem__(self, key: SelectorKey) -> Dataset:
        """Get a dataset from a key."""
        if res := self.get_by_locator(key):
            return res
        elif isinstance(key, Callable):
            res = key(self.data)
            if isinstance(res, Series) and not res.name:
                res.name = res.__name__
            return res
        else:
            key = locator[key]
            if res := self.get_by_locator(key):
                return res
            else:
                return self.get_by_position(key)

    def get_by_locator(self, key: SelectorKey) -> Dataset | None:
        """Try to get using a locator."""
        if isinstance(key, il):
            return self.get_by_position(key.selector)
        elif isinstance(key, ll):
            return self.get_by_label(key.selector)
        else:
            return None

    def get_by_position(self, key: SelectorKey) -> Dataset:
        """Get result data by using standard `iloc` method."""
        if self.data_client_kind == DataClientKind.COLUMNS:
            return self.data.iloc[:, key]
        else:
            return self.data.iloc[key]

    def get_by_label(self, key: SelectorKey) -> Dataset:
        """Get result data by using standard `loc` method."""
        if self.data_client_kind == DataClientKind.COLUMNS:
            return self.data.loc[:, key]
        else:
            return self.data.loc[key]
