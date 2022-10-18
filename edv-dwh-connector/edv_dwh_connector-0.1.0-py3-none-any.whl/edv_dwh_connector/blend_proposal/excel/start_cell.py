"""
This module defines cell where we want to start.
.. since: 0.1
"""

# -*- coding: utf-8 -*-
# Copyright (c) 2022 Endeavour Mining
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to read
# the Software only. Permissions is hereby NOT GRANTED to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from abc import ABC, abstractmethod


class StartCell(ABC):
    """
    Start cell.
    .. since: 0.1
    """

    def __init__(self):
        """
        Ctor.
        """
        self.__row = None
        self.__column = None

    def row(self) -> int:
        """
        Gets row position.
        :return: Position
        """
        if self.__row is None:
            self.__row = self._find()[0]
        return self.__row

    def column(self) -> int:
        """
        Gets column position.
        :return: Position
        """
        if self.__column is None:
            self.__column = self._find()[1]
        return self.__column

    def exist(self) -> bool:
        """
        Checks whether it exists.
        :return: Exists or not
        """
        return self.row() != -1

    @abstractmethod
    def _find(self) -> tuple:
        """
        Finds cell position.
        :return: Tuple of row and column positions
        """
