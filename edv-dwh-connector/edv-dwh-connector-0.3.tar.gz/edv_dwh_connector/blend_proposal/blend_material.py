"""
This module defines a Blend material.
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


# pylint: disable=duplicate-code
class BlendMaterial(ABC):
    """
    Blend Material.
    .. since: 0.1
    """

    @abstractmethod
    def machine_type(self) -> str:
        """
        Gets machine type.
        :return: Name
        """

    @abstractmethod
    def pit(self) -> str:
        """
        Gets a PIT.
        :return: PIT name
        """

    @abstractmethod
    def name(self) -> str:
        """
        Gets material name.
        :return: Material name
        """

    @abstractmethod
    def au_grade(self) -> float:
        """
        Gets Au grade.
        :return: Au grade
        """

    @abstractmethod
    def sol_cu(self) -> float:
        """
        Gets Sol cu.
        :return: Sol cu
        """

    @abstractmethod
    def as_ppm(self) -> float:
        """
        Gets As
        :return: As in ppm
        """

    @abstractmethod
    def moisture(self) -> float:
        """
        Gets Moisture.
        :return: Moisture
        """

    @abstractmethod
    def indicative_rec(self) -> float:
        """
        Get Indicative rec.
        :return: Indicative rec
        """

    @abstractmethod
    def bucket(self) -> float:
        """
        Gets bucket.
        :return: Bucket
        """

    @abstractmethod
    def available_tons(self) -> float:
        """
        Gets available tons.
        :return: Available tons
        """

    @abstractmethod
    def prop(self) -> float:
        """
        Gets prop.
        :return: Prop
        """
