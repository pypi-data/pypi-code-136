# SPDX-License-Identifier: GPL-3.0-or-later

# Policies for resolving HTTP requests with local resources.
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

We make file resources available to HTTP clients by mapping them
at:
    http(s)://<pattern-matching_origin>/<pattern_path>/<token>/
where <token> is a per-session secret unique for every mapping.
For example, a payload with pattern like the following:
    http*://***.example.com/a/b/**
Could cause resources to be mapped (among others) at each of:
    https://example.com/a/b/**/Da2uiF2UGfg/
    https://www.example.com/a/b/**/Da2uiF2UGfg/
    http://gnome.vs.kde.example.com/a/b/**/Da2uiF2UGfg/

Unauthorized web pages running in the user's browser are exected to be
unable to guess the secret. This way we stop them from spying on the
user and from interfering with Haketilo's normal operation.

This is only a soft prevention method. With some mechanisms
(e.g. service workers), under certain scenarios, it might be possible
to bypass it. Thus, to make the risk slightly smaller, we also block
the unauthorized accesses that we can detect.

Since a web page authorized to access the resources may only be served
when the corresponding mapping is enabled (or AUTO mode is on), we
consider accesses to non-enabled mappings' resources a security breach
and block them by responding with 403 Not Found.
"""

import dataclasses as dc
import typing as t
import json

from threading import Lock
from base64 import b64encode
from urllib.parse import quote, parse_qs, urlparse, urlencode, urljoin

import jinja2

from ...translations import smart_gettext as _
from ...url_patterns import ParsedUrl
from ...versions import haketilo_version
from .. import state
from .. import http_messages
from . import base
from .payload import PayloadAwarePolicy, PayloadAwarePolicyFactory


loader = jinja2.PackageLoader(__package__, package_path='js_templates')
jinja_env = jinja2.Environment(
    loader        = loader,
    lstrip_blocks = True,
    autoescape    = False
)
jinja_lock = Lock()


def encode_string_for_js(string: str) -> str:
    return b64encode(quote(string).encode()).decode()


AnyValue = t.TypeVar('AnyValue', bound=object)

def header_keys(headers: t.Iterable[tuple[str, AnyValue]]) -> frozenset[str]:
    return frozenset(header.lower() for header, _ in headers)

def _merge_headers(
        standard_headers:         t.Iterable[tuple[str, t.Optional[str]]],
        overridable_headers_keys: frozenset[str],
        native_headers:           http_messages.IHeaders,
        extra_headers:            t.Iterable[tuple[str, str]]
) -> t.Iterable[tuple[str, str]]:
    standard_keys     = header_keys(standard_headers)
    standard_iterator = iter(standard_headers)
    native_keys       = header_keys(native_headers.items())

    selected_base: list[tuple[str, str]] = []
    processed:     set[str]              = set()

    for header, _ in native_headers.items():
        header_l = header.lower()

        if header_l in processed or header_l not in standard_keys:
            continue

        for standard_header_l, chosen_value in standard_iterator:
            if standard_header_l not in native_keys:
                if chosen_value is not None:
                    selected_base.append((standard_header_l, chosen_value))
            elif standard_header_l == header_l:
                processed.add(header_l)

                if header_l in overridable_headers_keys:
                    chosen_value = native_headers.get(header_l, chosen_value)

                if chosen_value is not None:
                    selected_base.append((header, chosen_value))

                break

    for standard_header_l, standard_value in standard_iterator:
        if standard_value is not None:
            selected_base.append((standard_header_l, standard_value))

    extra_keys     = header_keys(extra_headers)
    extra_iterator = iter(extra_headers)

    result:   list[tuple[str, str]] = []
    processed                       = set()

    for header, value in selected_base:
        header_l = header.lower()

        if header_l in processed:
            continue

        if header_l in extra_keys:
            for extra_header, extra_value in extra_iterator:
                extra_header_l = extra_header.lower()

                processed.add(extra_header_l)

                result.append((extra_header, extra_value))

                if extra_header_l == header_l:
                    break
        else:
            result.append((header, value))

    result.extend(extra_iterator)

    return result

request_standard_headers: t.Iterable[tuple[str, t.Optional[str]]] = (
    ('user-agent',      None),
    ('accept',          'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'),
    ('accept-language', 'en-US,en;q=0.5'),
    ('accept-encoding', None),
    ('dnt',             '1'),
    ('connection',      None),
    ('upgrade-insecure-requests', '1'),
    ('sec-fetch-dest',  'document'),
    ('sec-fetch-mode',  'navigate'),
    ('sec-fetch-site',  'none'),
    ('sec-fetch-user',  '?1'),
    ('te',              'trailers')
)

auto_overridable_request_headers = frozenset((
    'user-agent',
    'accept-language',
    'accept-encoding',
    'dnt'
))

def merge_request_headers(
        native_headers:   http_messages.IHeaders,
        extra_headers:    t.Iterable[tuple[str, str]]
) -> t.Iterable[tuple[str, str]]:
    return _merge_headers(
        standard_headers         = request_standard_headers,
        overridable_headers_keys = auto_overridable_request_headers,
        native_headers           = native_headers,
        extra_headers            = extra_headers
    )

response_standard_headers: t.Iterable[tuple[str, t.Optional[str]]] = (
    ('cache-control',  'max-age=0, private, must-revalidate'),
    ('connection',     None),
    ('content-length', None),
    ('content-type',   None),
    ('date',           None),
    ('keep-alive',     None),
    ('server',         None)
)

auto_overridable_response_headers = frozenset(
    header.lower()
    for header, value in response_standard_headers
    if value is None
)

def merge_response_headers(
        native_headers: http_messages.IHeaders,
        extra_headers:  t.Iterable[tuple[str, str]]
) -> t.Iterable[tuple[str, str]]:
    return _merge_headers(
        standard_headers         = response_standard_headers,
        overridable_headers_keys = auto_overridable_response_headers,
        native_headers           = native_headers,
        extra_headers            = extra_headers
    )


ProducedAny = t.Union[
    http_messages.ProducedResponse,
    http_messages.ProducedRequest
]

@dc.dataclass(frozen=True)
class PayloadResourcePolicy(PayloadAwarePolicy):
    """...."""
    _process_request: t.ClassVar[bool] = True

    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._THREE

    def extract_resource_path(self, request_url: ParsedUrl) -> tuple[str, ...]:
        # Payload resource pattern has path of the form:
        #    "/some/arbitrary/segments/<per-session_token>/***"
        #
        # Corresponding requests shall have path of the form:
        #    "/some/arbitrary/segments/<per-session_token>/actual/resource/path"
        #
        # Here we need to extract the "/actual/resource/path" part.
        segments_to_drop = len(self.payload_data.pattern_path_segments) + 1
        return request_url.path_segments[segments_to_drop:]

    def should_process_response(self, request_url: ParsedUrl) -> bool:
        return self.extract_resource_path(request_url) \
            == ('api', 'unrestricted_http')

    def _make_file_resource_response(self, path: tuple[str, ...]) \
        -> http_messages.ProducedResponse:
        """...."""
        try:
            file_data = self.payload_data.ref.get_file_data(path)
        except state.MissingItemError:
            return resource_blocked_response

        if file_data is None:
            return http_messages.ProducedResponse(
                404,
                [(b'Content-Type', b'text/plain; charset=utf-8')],
                _('api.file_not_found').encode()
            )

        return http_messages.ProducedResponse(
            200,
            ((b'Content-Type', file_data.mime_type.encode()),),
            file_data.contents
        )

    def _make_api_response(
            self,
            path:         tuple[str, ...],
            request_info: http_messages.RequestInfo
    ) -> ProducedAny:
        if path[0] == 'page_init_script.js':
            with jinja_lock:
                template = jinja_env.get_template('page_init_script.js.jinja')
                token = self.payload_data.unique_token
                base_url = self.assets_base_url(request_info.url)
                ver_str = json.dumps(haketilo_version)
                js = template.render(
                    unique_token_encoded    = encode_string_for_js(token),
                    assets_base_url_encoded = encode_string_for_js(base_url),
                    haketilo_version        = encode_string_for_js(ver_str)
                )

            return http_messages.ProducedResponse(
                200,
                ((b'Content-Type', b'application/javascript'),),
                js.encode()
            )

        if path[0] == 'unrestricted_http':
            try:
                assert self.payload_data.cors_bypass_allowed

                params = parse_qs(request_info.url.query)
                target_url,        = params['target_url']
                extra_headers_str, = params['extra_headers']

                assert urlparse(target_url).scheme in ('http', 'https')

                extra_headers = json.loads(extra_headers_str)
                assert isinstance(extra_headers, list)
                for header, value in extra_headers:
                    assert isinstance(header, str)
                    assert isinstance(value, str)

                result_headers = merge_request_headers(
                    native_headers = request_info.headers,
                    extra_headers  = extra_headers
                )

                result_headers_bytes = \
                    [(h.encode(), v.encode()) for h, v in result_headers]

                return http_messages.ProducedRequest(
                    url     = target_url,
                    method  = request_info.method,
                    headers = result_headers_bytes,
                    body    = request_info.body
                )
            except:
                return resource_blocked_response
        else:
            return resource_blocked_response

    def consume_request(self, request_info: http_messages.RequestInfo) \
        -> ProducedAny:
        resource_path = self.extract_resource_path(request_info.url)

        if resource_path == ():
            return resource_blocked_response
        elif resource_path[0] == 'static':
            return self._make_file_resource_response(resource_path[1:])
        elif resource_path[0] == 'api':
            return self._make_api_response(resource_path[1:], request_info)
        else:
            return resource_blocked_response

    def consume_response(self, response_info: http_messages.ResponseInfo) \
        -> http_messages.ProducedResponse:
        """
        This method shall only be called for responses to unrestricted HTTP API
        requests. Its purpose is to sanitize response headers and smuggle their
        original data using an additional header.
        """
        serialized = json.dumps([*response_info.headers.items()])
        extra_headers = [('X-Haketilo-True-Headers', quote(serialized)),]

        if (300 <= response_info.status_code < 400):
            location = response_info.headers.get('location')
            if location is not None:
                orig_params = parse_qs(response_info.orig_url.query)
                orig_extra_headers_str, = orig_params['extra_headers']

                new_query = urlencode({
                    'target_url':    location,
                    'extra_headers': orig_extra_headers_str
                })

                new_url = urljoin(
                    response_info.orig_url.orig_url,
                    '?' + new_query
                )

                extra_headers.append(('location', new_url))

        merged_headers = merge_response_headers(
            native_headers = response_info.headers,
            extra_headers  = extra_headers
        )

        return http_messages.ProducedResponse(
            status_code = response_info.status_code,
            headers     = [(h.encode(), v.encode()) for h, v in merged_headers],
            body        = response_info.body,
        )


resource_blocked_response = http_messages.ProducedResponse(
    403,
    [(b'Content-Type', b'text/plain; charset=utf-8')],
    _('api.resource_not_enabled_for_access').encode()
)

@dc.dataclass(frozen=True)
class BlockedResponsePolicy(base.Policy):
    """...."""
    _process_request: t.ClassVar[bool] = True

    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._THREE

    def consume_request(self, request_info: http_messages.RequestInfo) \
        -> http_messages.ProducedResponse:
        """...."""
        return resource_blocked_response


@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class PayloadResourcePolicyFactory(PayloadAwarePolicyFactory):
    """...."""
    def make_policy(self, haketilo_state: state.HaketiloState) \
        -> t.Union[PayloadResourcePolicy, BlockedResponsePolicy]:
        """...."""
        try:
            payload_data = self.payload_ref.get_data()
        except state.MissingItemError:
            return BlockedResponsePolicy()

        if not payload_data.explicitly_enabled and \
           haketilo_state.get_settings().mapping_use_mode != \
               state.MappingUseMode.AUTO:
            return BlockedResponsePolicy()

        return PayloadResourcePolicy(payload_data)
