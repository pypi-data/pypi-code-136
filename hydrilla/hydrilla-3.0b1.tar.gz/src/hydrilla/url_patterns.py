# SPDX-License-Identifier: GPL-3.0-or-later

# Data structure for querying URL patterns.
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
This module contains functions for deconstruction and construction of URLs and
Haketilo URL patterns.

Data structures for querying data using URL patterns are also defined there.
"""

import re
import urllib.parse as up
import typing as t
import dataclasses as dc

from immutables import Map

from .translations import smart_gettext as _
from .exceptions import HaketiloException

default_ports: t.Mapping[str, int] = Map(http=80, https=443, ftp=21)

ParsedUrlType = t.TypeVar('ParsedUrlType', bound='ParsedUrl')

@dc.dataclass(frozen=True, unsafe_hash=True, order=True)
class ParsedUrl:
    """...."""
    orig_url:           str               # used in __hash__() and __lt__()
    scheme:             str               = dc.field(hash=False, compare=False)
    domain_labels:      t.Tuple[str, ...] = dc.field(hash=False, compare=False)
    path_segments:      t.Tuple[str, ...] = dc.field(hash=False, compare=False)
    query:              str               = dc.field(hash=False, compare=False)
    has_trailing_slash: bool              = dc.field(hash=False, compare=False)
    port:               t.Optional[int]   = dc.field(hash=False, compare=False)

    @property
    def url_without_path(self) -> str:
        """...."""
        scheme = self.scheme

        netloc = '.'.join(reversed(self.domain_labels))

        if self.port is not None and \
           default_ports.get(scheme) != self.port:
            netloc += f':{self.port}'

        return f'{scheme}://{netloc}'

    def reconstruct_url(self) -> str:
        """...."""
        path = '/'.join(('', *self.path_segments))
        if self.has_trailing_slash:
            path += '/'

        return self.url_without_path + path

    def path_append(self: ParsedUrlType, *new_segments: str) -> ParsedUrlType:
        """...."""
        new_url = self.reconstruct_url()
        if not self.has_trailing_slash:
            new_url += '/'

        new_url += '/'.join(new_segments)

        return dc.replace(
            self,
            orig_url           = new_url,
            path_segments      = tuple((*self.path_segments, *new_segments)),
            has_trailing_slash = False
        )

ParsedPattern = t.NewType('ParsedPattern', ParsedUrl)

# # We sometimes need a dummy pattern that means "match everything".
# catchall_pattern = ParsedPattern(
#     ParsedUrl(
#         orig_url           = '<dummy_catchall_url_pattern>'
#         scheme             = '<dummy_all-scheme>'
#         domain_labels      = ('***',)
#         path_segments      = ('***',)
#         has_trailing_slash = False
#         port               = 0
#     )
# )


# URLs with those schemes will be recognized but not all of them have to be
# actually supported by Hydrilla server and Haketilo proxy.
supported_schemes = 'http', 'https', 'ftp', 'file'

def _parse_pattern_or_url(
        url:               str,
        orig_url:          str,
        is_pattern:        bool = False
) -> ParsedUrl:
    """...."""
    if not is_pattern:
        assert orig_url == url

    parse_result = up.urlparse(url)

    # Verify the parsed URL is valid
    has_hostname = parse_result.hostname is not None
    if not parse_result.scheme or \
       (parse_result.scheme == 'file' and parse_result.port is not None) or \
       (parse_result.scheme == 'file' and has_hostname) or \
       (parse_result.scheme != 'file' and not has_hostname):
        if is_pattern:
            msg = _('err.url_pattern_{}.bad').format(orig_url)
            raise HaketiloException(msg)
        else:
            raise HaketiloException(_('err.url_{}.bad') .format(url))

    # Verify the URL uses a known scheme and extract it.
    scheme = parse_result.scheme

    if parse_result.scheme not in supported_schemes:
        if is_pattern:
            msg = _('err.url_pattern_{}.bad_scheme').format(orig_url)
            raise HaketiloException(msg)
        else:
            raise HaketiloException(_('err.url_{}.bad_scheme').format(url))

    # Extract and keep information about special pattern schemas used.
    if is_pattern and orig_url.startswith('http*:'):
        if parse_result.port:
            fmt = _('err.url_pattern_{}.special_scheme_port')
            raise HaketiloException(fmt.format(orig_url))

    # Extract URL's explicit port or deduce the port based on URL's protocol.
    try:
        explicit_port = parse_result.port
        port_out_of_range = explicit_port == 0
    except ValueError:
        port_out_of_range = True

    if port_out_of_range:
        if is_pattern:
            msg = _('err.url_pattern_{}.bad_port').format(orig_url)
            raise HaketiloException(msg)
        else:
            raise HaketiloException(_('err.url_{}.bad_port').format(url))

    port = explicit_port or default_ports.get(parse_result.scheme)

    # Make URL's hostname into a list of labels in reverse order. E.g.
    #     'https://a.bc..de.fg.com/h/i/' -> ['com', 'fg', 'de', 'bc', 'a']
    hostname = parse_result.hostname or ''
    domain_labels_with_empty = reversed(hostname.split('.'))
    domain_labels = tuple(lbl for lbl in domain_labels_with_empty if lbl)

    # Make URL's path into a list of segments. E.g.
    #     'https://ab.cd/e//f/g/' -> ['e', 'f', 'g']
    path_segments_with_empty = parse_result.path.split('/')
    path_segments = tuple(sgmt for sgmt in path_segments_with_empty if sgmt)

    # Record whether a trailing '/' is present in the URL.
    has_trailing_slash = parse_result.path.endswith('/')

    # Perform some additional sanity checks and return the result.
    if is_pattern:
        if parse_result.query:
            msg = _('err.url_pattern_{}.has_query').format(orig_url)
            raise HaketiloException(msg)

        if parse_result.fragment:
            msg = _('err.url_pattern_{}.has_frag').format(orig_url)
            raise HaketiloException(msg)

    query = parse_result.query

    return ParsedUrl(
        orig_url           = orig_url,
        scheme             = scheme,
        port               = port,
        domain_labels      = domain_labels,
        path_segments      = path_segments,
        query              = query,
        has_trailing_slash = has_trailing_slash
    )

replace_scheme_regex = re.compile(r'^[^:]*')

def parse_pattern(url_pattern: str) -> t.Iterator[ParsedPattern]:
    """...."""
    if url_pattern.startswith('http*:'):
        patterns = [
            replace_scheme_regex.sub('http', url_pattern),
            replace_scheme_regex.sub('https', url_pattern)
        ]
    else:
        patterns = [url_pattern]

    for pat in patterns:
        yield ParsedPattern(
            _parse_pattern_or_url(pat, url_pattern, True)
        )

def parse_url(url: str) -> ParsedUrl:
    """...."""
    return _parse_pattern_or_url(url, url)


def normalize_pattern(url_pattern: str) -> str:
    parsed = next(parse_pattern(url_pattern))

    reconstructed = parsed.reconstruct_url()

    if url_pattern.startswith('http*'):
        reconstructed = replace_scheme_regex.sub('http*', reconstructed)

    return reconstructed
