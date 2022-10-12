# SPDX-License-Identifier: GPL-3.0-or-later

# Classes/protocols for representing HTTP requests and responses data.
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
import sys

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

from .. import url_patterns


DefaultGetValue = t.TypeVar('DefaultGetValue', str, None)

class IHeaders(Protocol):
    """...."""
    def __getitem__(self, key: str) -> str:  ...

    def get_all(self, key: str) -> t.Iterable[str]: ...

    @t.overload
    def get(self, key: str) -> t.Optional[str]:
        ...
    @t.overload
    def get(self, key: str, default: DefaultGetValue) \
        -> t.Union[str, DefaultGetValue]:
        ...

    def items(self) -> t.Iterable[tuple[str, str]]: ...

def encode_headers_items(headers: t.Iterable[tuple[str, str]]) \
    -> t.Iterable[tuple[bytes, bytes]]:
    """...."""
    for name, value in headers:
        yield name.encode(), value.encode()

@dc.dataclass(frozen=True)
class ProducedRequest:
    """...."""
    url:         str
    method:      str
    headers:     t.Iterable[tuple[bytes, bytes]]
    body:        bytes

@dc.dataclass(frozen=True)
class RequestInfo:
    """...."""
    url:         url_patterns.ParsedUrl
    method:      str
    headers:     IHeaders
    body:        bytes

    def make_produced_request(self) -> ProducedRequest:
        """...."""
        return ProducedRequest(
            url     = self.url.orig_url,
            method  = self.method,
            headers = encode_headers_items(self.headers.items()),
            body    = self.body
        )

@dc.dataclass(frozen=True)
class ProducedResponse:
    """...."""
    status_code: int
    headers:     t.Iterable[tuple[bytes, bytes]]
    body:        bytes

@dc.dataclass(frozen=True)
class ResponseInfo:
    """...."""
    url:         url_patterns.ParsedUrl
    orig_url:    url_patterns.ParsedUrl
    status_code: int
    headers:     IHeaders
    body:        bytes

    def make_produced_response(self) -> ProducedResponse:
        """...."""
        return ProducedResponse(
            status_code = self.status_code,
            headers     = encode_headers_items(self.headers.items()),
            body        = self.body
        )
