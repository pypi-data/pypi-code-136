#!/usr/bin/env python3

"""ring_buffer

Contains: 
- RingBuffer: buffer that, when full, overwrites it's oldest row. Cheaply returns full buffer as numpy array.
"""
import numpy as np
from typing import Union, List, Dict, Optional
from collections.abc import Sequence

from numpy_array_buffer.abstract_buffer import AbstractBuffer


class RingBuffer(Sequence, AbstractBuffer):
    def __init__(
        self,
        buffer_length: int,
        width: int,
        dtype=float,
        column_names: Union[List[str], None] = None,
        initial_data: Union[List, np.ndarray, tuple, None] = None,
    ) -> None:
        """Ringbuffer that overwrites it's oldest row.

        Args:
            buffer_length (int)
            width (int): length of single buffer row
            dtype (_type_, optional): type of buffer elements. Defaults to float.
            column_names (Union[None, List[str]], optional): Name of columns,
                can be used to access columns and add dictionary to buffer.
                Defaults to None.
            initial_data Union[List, np.ndarray, tuple, None]: Optional initial
                data to start RingBuffer. Defaults to None,
        """

        if column_names is None:
            self.column_names: List[str] = [f"col_{i}" for i in range(width)]
        elif len(column_names) != width:
            raise Exception(f"Length of column names does not match width")
        else:
            self.column_names = column_names

        self.buffer_length = buffer_length
        self.width = width
        self.dtype = dtype

        if width == 1:
            self.data_matrix = np.zeros([self.buffer_length * 2], dtype=dtype)
        else:
            self.data_matrix = np.zeros([self.buffer_length * 2, width], dtype=dtype)
        self.curr_idx: int = 0
        self.buffer_full: bool = False

        if initial_data is not None:
            for row in initial_data:
                self.append(row)

    def clear(self):
        self.curr_idx = 0
        self.buffer_full = False
        self.data_matrix[:] = 0

    def append(self, data_array: Union[List, np.ndarray, tuple]) -> None:
        """Add data row to buffer

        Args:
            data_array (Union[List, np.ndarray, tuple]): _description_
        """
        if self.width > 1 and len(data_array) != self.width:
            raise Exception(f"wrong data format")

        if self.curr_idx == self.buffer_length:
            self.buffer_full = True

        self.curr_idx %= self.buffer_length

        if self.width == 1:
            self.data_matrix[self.curr_idx] = data_array
            self.data_matrix[self.curr_idx + self.buffer_length] = data_array
        else:
            self.data_matrix[self.curr_idx, :] = np.array(data_array)
            self.data_matrix[self.curr_idx + self.buffer_length, :] = np.array(
                data_array
            )

        self.curr_idx += 1

    def get_array(self) -> np.ndarray:
        """return full buffer"""

        if self.width == 1:
            if self.buffer_full:
                return self.data_matrix[
                    self.curr_idx : (self.curr_idx + self.buffer_length)
                ]
            else:
                return self.data_matrix[0 : self.curr_idx]

        else:
            if self.buffer_full:
                return self.data_matrix[
                    self.curr_idx : (self.curr_idx + self.buffer_length), :
                ]
            else:
                return self.data_matrix[0 : self.curr_idx, :]

    def __getitem__(self, ranges):
        return self.get_array()[ranges]

    def __len__(self):
        if self.buffer_full:
            return self.buffer_length
        else:
            return self.curr_idx

    def __repr__(self):
        return (
            f"RingBuffer(buffer_length={self.buffer_length}, width={self.width}, "
            f"dtype={self.dtype}, column_names={self.column_names}, "
            f"initial_data=np.array({self.get_array()})"
        )

    def __str__(self):
        return f"RingBuffer of dim: {self.buffer_length}x{self.width}, curr_idx: {self.curr_idx}"
