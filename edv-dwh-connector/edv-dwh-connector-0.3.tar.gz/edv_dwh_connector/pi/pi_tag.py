"""
This module defines PI tag API.
.. since: 0.2
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


class PITag(ABC):
    """
    PI tag.
    .. since: 0.2
    """

    @abstractmethod
    def uid(self) -> int:
        """
        Gets Unique Identifier.
        :return: UID
        """

    @abstractmethod
    def code(self) -> str:
        """
        Gets code.
        :return: Code
        """

    @abstractmethod
    def name(self) -> str:
        """
        Gets name.
        :return: Name
        """

    @abstractmethod
    def uom(self) -> str:
        """
        Gets Unit of measure.
        :return: Unit
        """


class PITags(ABC):
    """
    List of PI tags.
    .. since: 0.2
    """

    @abstractmethod
    def get(self, code: str) -> PITag:
        """
        Gets tag by code
        :param code: Code
        :return: Tag
        :raises NotFoundError: If not found
        """

    @abstractmethod
    def items(self) -> list:
        """
        Gets all tags
        :return: List of tags
        """

    @abstractmethod
    def add(self, code: str, name: str, uom: str) -> PITag:
        """
        Adds a tag.
        :param code: Code
        :param name: Name
        :param uom: Unit of measure
        :return: PITag registered
        :raises AlreadyExistsError: If a tag with same code already exists
        """
