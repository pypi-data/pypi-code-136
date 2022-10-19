#!/usr/bin/env python3
"""downsampling_buffer

Contains: 
- DownsamplingBuffer: buffer object that downsamples by factor 2 when full
"""


import numpy as np
from typing import Union, List, Dict
from numpy_array_buffer.abstract_buffer import AbstractBuffer


class DownsamplingBuffer(AbstractBuffer):
    def __init__(
        self,
        buffer_length: int,
        width: int,
        dtype=float,
        column_names: Union[None, List[str]] = None,
    ):
        """Fixed length buffer that downsamples its buffer when full.

        Args:
            buffer_length (int)
            width (int): length of single buffer row
            dtype (_type_, optional): type of buffer elements. Defaults to float.
            column_names (Union[None, List[str]], optional): Name of columns,
                can be used to access columns and add dictionary to buffer. Defaults to None.
        """

        if buffer_length % 2 != 0:
            raise Exception(f"array_len needs to be even")
        self.buffer_length = buffer_length

        if column_names is None:
            self.column_names = [f"col_{i}" for i in range(width)]

        elif len(column_names) != width:
            raise Exception(f"Length of column names does not match width")
        else:
            self.column_names = column_names

        # self.array_len = array_len
        self.width = width
        # if self.
        # self.data_matrix = np.zeros((self.buffer_length, width), dtype=dtype)
        if width == 1:
            self.data_matrix = np.zeros([self.buffer_length], dtype=dtype)
        else:
            self.data_matrix = np.zeros([self.buffer_length, width], dtype=dtype)

        self.first_empty_row_index: int = 0
        self.downsampling_rate: int = 1
        self.downsampling_counter: int = 0

    def clear(self):
        self.first_empty_row_index: int = 0
        self.downsampling_rate: int = 1
        self.downsampling_counter: int = 0
        self.data_matrix[:] = 0

    def append(self, data_row: Union[List, np.ndarray, tuple]) -> None:
        """Add data row to buffer

        Args:
            data_array (Union[List, np.ndarray, tuple]): _description_
        """

        if self.width > 1 and len(data_row) != self.width:
            raise Exception(f"wrong data format")

        # either add or skip a sample
        if (self.downsampling_counter + 1) >= self.downsampling_rate:

            # length is reached, need to downsample
            if self.buffer_length == self.first_empty_row_index:
                self.downsample_buffer()

            # add data row
            if self.width == 1:
                self.data_matrix[self.first_empty_row_index] = data_row
            else:
                self.data_matrix[self.first_empty_row_index, :] = data_row

            self.first_empty_row_index += 1
            self.downsampling_counter = 0
        else:
            self.downsampling_counter += 1

    def downsample_buffer(self):
        self.first_empty_row_index = self.buffer_length // 2
        if self.width == 1:
            self.data_matrix[: self.first_empty_row_index] = self.data_matrix[::2]
        else:
            self.data_matrix[: self.first_empty_row_index, :] = self.data_matrix[::2, :]

        self.downsampling_rate *= 2

    def get_array(self) -> np.ndarray:
        """return full buffer"""
        if self.width > 1:
            return self.data_matrix[: self.first_empty_row_index, :]
        else:
            return self.data_matrix[: self.first_empty_row_index]

    def __repr__(self):
        return f"{self.get_array()}"

    def __str__(self):
        return f"Downsampling buffer of buffer length: 4, rowlength: 3"

    def __len__(self):
        return self.first_empty_row_index
