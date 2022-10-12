# SPDX-License-Identifier: GPL-3.0-or-later

# Base defintions for policies for altering HTTP requests.
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

from immutables import Map

from ... url_patterns import ParsedUrl
from .. import state
from .. import http_messages


class PolicyPriority(int, enum.Enum):
    """...."""
    _ONE   = 1
    _TWO   = 2
    _THREE = 3

ProducedMessage = t.Union[
    http_messages.ProducedRequest,
    http_messages.ProducedResponse
]

class Policy(ABC):
    """...."""
    _process_request:  t.ClassVar[bool] = False
    _process_response: t.ClassVar[bool] = False
    anticache:         t.ClassVar[bool] = True

    priority: t.ClassVar[PolicyPriority]

    def should_process_request(self, parsed_url: ParsedUrl) -> bool:
        return self._process_request

    def should_process_response(self, parsed_url: ParsedUrl) -> bool:
        return self._process_response

    def consume_request(self, request_info: http_messages.RequestInfo) \
        -> t.Optional[ProducedMessage]:
        raise NotImplementedError(
            'This kind of policy does not consume requests.'
        )

    def consume_response(self, response_info: http_messages.ResponseInfo) \
        -> t.Optional[http_messages.ProducedResponse]:
        raise NotImplementedError(
            'This kind of policy does not consume responses.'
        )


# mypy needs to be corrected:
# https://stackoverflow.com/questions/70999513/conflict-between-mix-ins-for-abstract-dataclasses/70999704#70999704
@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class PolicyFactory(ABC):
    """...."""
    builtin: bool

    @abstractmethod
    def make_policy(self, haketilo_state: state.HaketiloState) \
        -> t.Optional[Policy]:
        """...."""
        ...

    def __lt__(self, other: 'PolicyFactory'):
        """...."""
        return sorting_keys.get(self.__class__.__name__, 999) < \
            sorting_keys.get(other.__class__.__name__, 999)

sorting_order = (
    'PayloadResourcePolicyFactory',

    'PayloadPolicyFactory',

    'RuleBlockPolicyFactory',
    'RuleAllowPolicyFactory',

    'FallbackPolicyFactory'
)

sorting_keys = Map((cls, name) for name, cls in enumerate(sorting_order))
