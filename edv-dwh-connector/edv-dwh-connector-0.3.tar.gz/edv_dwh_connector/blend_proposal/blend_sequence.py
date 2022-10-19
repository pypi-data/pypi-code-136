"""
This module defines Blend sequence.
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


class BlendSequence(ABC):
    """
    Blend sequence.
    .. since: 0.1
    """

    @abstractmethod
    def name(self) -> str:
        """
        Gets name.
        :return: Name
        """

    @abstractmethod
    def average_grade(self) -> float:
        """
        Gets average grade.
        :return: Average grade
        """

    @abstractmethod
    def soluble_copper(self) -> float:
        """
        Gets soluble copper.
        :return: Soluble copper
        """

    @abstractmethod
    def as_ppm(self) -> float:
        """
        Gets As.
        :return: As
        """

    @abstractmethod
    def moisture_estimated(self) -> float:
        """
        Gets moisture estimated.
        :return: Moisture
        """

    @abstractmethod
    def oxide_transition(self) -> float:
        """
        Gets Oxide or Transition.
        :return: Oxide or Transition
        """

    @abstractmethod
    def fresh(self) -> float:
        """
        Gets fresh.
        :return: Fresh
        """

    @abstractmethod
    def recovery_blend_estimated(self) -> float:
        """
        Gets recovery blend estimated.
        :return: Recovery blend estimated
        """

    @abstractmethod
    def materials(self) -> list:
        """
        Get list of materials.
        :return: List of materials
        """
