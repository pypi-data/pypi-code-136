# SPDX-License-Identifier: GPL-3.0-or-later

# Tools for working with Content Security Policy headers.
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

import re
import typing as t
import dataclasses as dc

from immutables import Map, MapMutation

from . import http_messages


header_names_and_dispositions = (
    ('content-security-policy',             'enforce'),
    ('content-security-policy-report-only', 'report'),
    ('x-content-security-policy',           'enforce'),
    ('x-content-security-policy',           'report'),
    ('x-webkit-csp',                        'enforce'),
    ('x-webkit-csp',                        'report')
)

enforce_header_names_set = {
    name for name, disposition in header_names_and_dispositions
    if disposition == 'enforce'
}

@dc.dataclass
class ContentSecurityPolicy:
    directives:  Map[str, t.Sequence[str]]
    header_name: str
    disposition: str

    def serialize(self) -> str:
        """...."""
        serialized_directives = []
        for name, value_list in self.directives.items():
            serialized_directives.append(f'{name} {" ".join(value_list)}')

        return ';'.join(serialized_directives)

    @staticmethod
    def deserialize(
            serialized:  str,
            header_name: str,
            disposition: str = 'enforce'
    ) -> 'ContentSecurityPolicy':
        """...."""
        # For more info, see:
        # https://www.w3.org/TR/CSP3/#parse-serialized-policy
        empty_directives: Map[str, t.Sequence[str]] = Map()

        directives = empty_directives.mutate()

        for serialized_directive in serialized.split(';'):
            if not serialized_directive.isascii():
                continue

            serialized_directive = serialized_directive.strip()
            if len(serialized_directive) == 0:
                continue

            tokens = serialized_directive.split()
            directive_name = tokens.pop(0).lower()
            directive_value = tokens

            # Specs mention giving warnings for duplicate directive names but
            # from our proxy's perspective this is not important right now.
            if directive_name in directives:
                continue

            directives[directive_name] = directive_value

        return ContentSecurityPolicy(
            directives  = directives.finish(),
            header_name = header_name,
            disposition = disposition
        )

def extract(headers: http_messages.IHeaders) \
    -> tuple[ContentSecurityPolicy, ...]:
    """...."""
    csp_policies = []

    for header_name, disposition in header_names_and_dispositions:
        for serialized_list in headers.get_all(header_name):
            for serialized in serialized_list.split(','):
                policy = ContentSecurityPolicy.deserialize(
                    serialized,
                    header_name,
                    disposition
                )

                if policy.directives != Map():
                    csp_policies.append(policy)

    return tuple(csp_policies)
