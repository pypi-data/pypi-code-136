# SPDX-License-Identifier: GPL-3.0-or-later

# Miscellaneous policies.
#
# This file is part of Hydrilla&Haketilo.
#
# Copyright (C) 2022 Wojtek Kosior
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
.....
"""

import dataclasses as dc
import typing as t
import enum

from abc import ABC, abstractmethod

from .. import state
from .. import http_messages
from . import base
from .rule import AllowPolicy, BlockPolicy


class FallbackAllowPolicy(AllowPolicy):
    """....."""
    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._ONE


class FallbackBlockPolicy(BlockPolicy):
    """...."""
    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._ONE


@dc.dataclass(frozen=True)
class ErrorBlockPolicy(BlockPolicy):
    """...."""
    error: Exception

    builtin: bool = True

class DoNothingPolicy(base.Policy):
    """
    A special policy class for handling of the magical mitm.it domain. It causes
    request and response not to be modified in any way, and also (unlike
    FallbackAllowPolicy) prevents them from being streamed.
    """
    _process_request:  t.ClassVar[bool] = True
    _process_response: t.ClassVar[bool] = True
    anticache:         t.ClassVar[bool] = False

    def consume_request(self, request_info: http_messages.RequestInfo) -> None:
        return None

    def consume_response(self, response_info: http_messages.ResponseInfo) \
        -> None:
        return None

    builtin: bool = True
