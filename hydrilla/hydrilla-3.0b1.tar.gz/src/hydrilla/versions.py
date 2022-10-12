# SPDX-License-Identifier: GPL-3.0-or-later

# Functions to operate on version numbers.
#
# This file is part of Hydrilla&Haketilo.
#
# Copyright (C) 2021, 2022 Wojtek Kosior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
# I, Wojtek Kosior, thereby promise not to sue for violation of this
# file's license. Although I request that you do not make use of this
# code in a proprietary program, I am not going to enforce this in
# court.

"""
This module contains functions for deconstruction and construction of version
strings and version tuples.
"""

import typing as t

from itertools import takewhile

from . import _version


VerTuple = t.NewType('VerTuple', 't.Tuple[int, ...]')

def normalize(ver: t.Sequence[int]) -> VerTuple:
    """Strip rightmost zeroes from 'ver'."""
    new_len = 0
    for i, num in enumerate(ver):
        if num != 0:
            new_len = i + 1

    return VerTuple(tuple(ver[:new_len]))

def parse(ver_str: str) -> t.Tuple[int, ...]:
    """
    Convert 'ver_str' into an array representation, e.g. for ver_str="4.6.13.0"
    return [4, 6, 13, 0].
    """
    return tuple(int(num) for num in ver_str.split('.'))

def parse_normalize(ver_str: str) -> VerTuple:
    """
    Convert 'ver_str' into a VerTuple representation, e.g. for
    ver_str="4.6.13.0" return (4, 6, 13).
    """
    return normalize(parse(ver_str))

def version_string(ver: VerTuple, rev: t.Optional[int] = None) -> str:
    """
    Produce version's string representation (optionally with revision), like:
        1.2.3-5
    """
    return '.'.join(str(n) for n in ver) + ('' if rev is None else f'-{rev}')

haketilo_version = normalize(tuple(takewhile(
    lambda i: isinstance(i, int),
    _version.version_tuple # type: ignore
)))

int_ver_min = normalize([1])
int_ver_max = normalize([65536])
