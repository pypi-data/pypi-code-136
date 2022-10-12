# SPDX-License-Identifier: GPL-3.0-or-later

# Policies for blocking and allowing JS in pages fetched with HTTP.
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

from ...url_patterns import ParsedPattern
from .. import csp
from .. import state
from ..import http_messages
from . import base


class AllowPolicy(base.Policy):
    """...."""
    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._TWO

class BlockPolicy(base.Policy):
    """...."""
    _process_response: t.ClassVar[bool] = True

    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._TWO

    def _modify_headers(self, response_info: http_messages.ResponseInfo) \
        -> t.Iterable[tuple[bytes, bytes]]:
        """...."""
        csp_policies = csp.extract(response_info.headers)

        for header_name, header_value in response_info.headers.items():
            if header_name.lower() not in csp.header_names_and_dispositions:
                yield header_name.encode(), header_value.encode()

        for policy in csp_policies:
            if policy.disposition != 'enforce':
                continue

            directives = policy.directives.mutate()
            directives.pop('report-to',  None)
            directives.pop('report-uri', None)

            policy = dc.replace(policy, directives=directives.finish())

            yield policy.header_name.encode(), policy.serialize().encode()

        extra_csp = ';'.join((
            "script-src 'none'",
            "script-src-elem 'none'",
            "script-src-attr 'none'"
        ))

        yield b'Content-Security-Policy', extra_csp.encode()


    def consume_response(self, response_info: http_messages.ResponseInfo) \
        -> http_messages.ProducedResponse:
        """...."""
        new_response = response_info.make_produced_response()

        new_headers = self._modify_headers(response_info)

        return dc.replace(new_response, headers=new_headers)

@dc.dataclass(frozen=True)
class RuleAllowPolicy(AllowPolicy):
    """...."""
    pattern: ParsedPattern


@dc.dataclass(frozen=True)
class RuleBlockPolicy(BlockPolicy):
    """...."""
    pattern: ParsedPattern


@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class RulePolicyFactory(base.PolicyFactory):
    """...."""
    pattern: ParsedPattern

    def __lt__(self, other: base.PolicyFactory) -> bool:
        """...."""
        if type(other) is not type(self):
            return super().__lt__(other)

        assert isinstance(other, RulePolicyFactory)

        return self.pattern < other.pattern


@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class RuleBlockPolicyFactory(RulePolicyFactory):
    """...."""
    def make_policy(self, haketilo_state: state.HaketiloState) \
        -> RuleBlockPolicy:
        """...."""
        return RuleBlockPolicy(self.pattern)


@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class RuleAllowPolicyFactory(RulePolicyFactory):
    """...."""
    def make_policy(self, haketilo_state: state.HaketiloState) \
        -> RuleAllowPolicy:
        """...."""
        return RuleAllowPolicy(self.pattern)
