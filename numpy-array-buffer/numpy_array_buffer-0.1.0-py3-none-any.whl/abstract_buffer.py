#!/usr/bin/env python3
"""downsampling_buffer

Contains: 
- DownsamplingBuffer: buffer object that downsamples by factor 2 when full
"""


from abc import ABC, abstractmethod
import numpy as np
from typing import Union, List, Dict
from numbers import Number

HANDLED_FUNCTIONS = {}


def implements(np_function):
    "Register an __array_function__ implementation for DiagonalArray objects."

    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class AbstractBuffer(ABC):
    def __init__(
        self,
        buffer_length: int,
        width: int,
        dtype=float,
        column_names: Union[None, List[str]] = None,
    ):
        self.buffer_length = buffer_length

        if column_names is None:
            self.column_names = [f"col_{i}" for i in range(width)]

        elif len(column_names) != width:
            raise Exception(f"Length of column names does not match width")
        else:
            self.column_names = column_names

        self.width = width

    def add_dict(self, data_dict: Dict) -> None:
        """add row to buffer, matching dictionary entries to column names

        Args:
            data_dict (Dict)
        """
        keys, values = zip(*data_dict.items())
        if keys == tuple(self.column_names):
            self.append(values)
        else:
            try:
                data = [data_dict[key] for key in self.column_names]
                self.append(data)

            except:
                raise Exception(f"Could not parse data dict")

    def __getitem__(self, ranges):
        return self.get_array()[ranges]

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method == "__call__":
            N = None
            scalars = []
            for input in inputs:
                if isinstance(input, Number):
                    scalars.append(input)
                elif isinstance(input, self.__class__):
                    scalars.append(input._i)
                    if N is not None:
                        if N != self._N:
                            raise TypeError("inconsistent sizes")
                    else:
                        N = self._N
                else:
                    return NotImplemented
            return self.__class__(N, ufunc(*scalars, **kwargs))
        else:
            return NotImplemented

    def get_col(self, col_name: str) -> np.ndarray:
        """return single buffer column

        Args:
            col_name (str): name of single column

        Returns:
            np.ndarray: single buffer column
        """
        try:
            col_idx = self.column_names.index(col_name)
        except:
            raise Exception("Invalid column name")

        if self.width == 1:
            return self.get_array()[:]
        else:
            return self.get_array()[:, col_idx]

    @abstractmethod
    def __repr__(self):
        pass
        # return "[1,2,3..]"

    @abstractmethod
    def __str__(self):
        return "Buffer description"

    @abstractmethod
    def __len__(self):
        pass

    @implements(np.mean)
    def mean(self, **kwargs):
        return np.mean(self.get_array(), axis=0)

    @implements(np.max)
    def max(self, **kwargs):
        return np.max(self.get_array(), axis=0)

    @implements(np.sum)
    def sum(self, **kwargs):
        return np.sum(self.get_array(), axis=0)

    @implements(np.std)
    def std(self, **kwargs):
        return np.std(self.get_array(), axis=0)

    @implements(np.median)
    def median(self, **kwargs):
        return np.median(self.get_array(), axis=0)

    @abstractmethod
    def get_array(self) -> np.ndarray:
        pass

    @abstractmethod
    def append(self, data_array: Union[List, np.ndarray, tuple]) -> None:
        pass

    # def __array__(self):
    #     print(f"{type(self.get_array())}")
    #     print(f"--------array---")
    #     return self.get_array()

    # def __iter__(self):

    #     # print(f"Here")

    #     if self.width == 1:
    #         for item in self.get_array():
    #             yield item
    #     else:
    #         for item in self.get_array():
    #             yield list(item)
