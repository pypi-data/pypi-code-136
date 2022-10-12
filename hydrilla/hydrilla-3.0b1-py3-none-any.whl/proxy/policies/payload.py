# SPDX-License-Identifier: GPL-3.0-or-later

# Policies for applying payload injections to HTTP requests.
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
import re

from urllib.parse import urlencode

from itsdangerous.url_safe import URLSafeSerializer
import bs4 # type: ignore

from ...exceptions import HaketiloException
from ...url_patterns import ParsedUrl
from .. import csp
from .. import state
from .. import http_messages
from . import base

@dc.dataclass(frozen=True) # type: ignore[misc]
class PayloadAwarePolicy(base.Policy):
    """...."""
    payload_data:   state.PayloadData

    def assets_base_url(self, request_url: ParsedUrl):
        """...."""
        token = self.payload_data.unique_token

        base_path_segments = (*self.payload_data.pattern_path_segments, token)

        return f'{request_url.url_without_path}/{"/".join(base_path_segments)}/'

    def _payload_details_to_signed_query_string(
            self,
            _salt:        str,
            **extra_keys: str
    ) -> str:
        params: t.Mapping[str, str] = {
            'payload_id': self.payload_data.ref.id,
            **extra_keys
        }

        serializer = URLSafeSerializer(self.payload_data.global_secret, _salt)

        return urlencode({'details': serializer.dumps(params)})


@dc.dataclass(frozen=True) # type: ignore[misc]
class PayloadAwarePolicyFactory(base.PolicyFactory):
    """...."""
    payload_key: state.PayloadKey

    @property
    def payload_ref(self) -> state.PayloadRef:
        """...."""
        return self.payload_key.ref

    def __lt__(self, other: base.PolicyFactory) -> bool:
        """...."""
        if isinstance(other, type(self)):
            return self.payload_key < other.payload_key

        return super().__lt__(other)


# For details of 'Content-Type' header's structure, see:
# https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.1.1
content_type_reg = re.compile(r'''
^
(?P<mime>[\w-]+/[\w-]+)
\s*
(?:
    ;
    (?:[^;]*;)* # match possible parameter other than "charset"
)
\s*
charset=        # no whitespace allowed in parameter as per RFC
(?P<encoding>
    [\w-]+
    |
    "[\w-]+"    # quotes are optional per RFC
)
(?:;[^;]+)*     # match possible parameter other than "charset"
$               # forbid possible dangling characters after closing '"'
''', re.VERBOSE | re.IGNORECASE)

def deduce_content_type(headers: http_messages.IHeaders) \
    -> tuple[t.Optional[str], t.Optional[str]]:
    """...."""
    content_type = headers.get('content-type')
    if content_type is None:
        return (None, None)

    match = content_type_reg.match(content_type)
    if match is None:
        return (None, None)

    mime, encoding = match.group('mime'), match.group('encoding')

    if encoding is not None:
        encoding = encoding.lower()

    return mime, encoding

UTF8_BOM = b'\xEF\xBB\xBF'
BOMs = (
    (UTF8_BOM,    'utf-8'),
    (b'\xFE\xFF', 'utf-16be'),
    (b'\xFF\xFE', 'utf-16le')
)

def block_attr(element: bs4.PageElement, attr_name: str) -> None:
    """
    Disable HTML node attributes by prepending `blocked-'. This allows them to
    still be relatively easily accessed in case they contain some useful data.
    """
    blocked_value = element.attrs.pop(attr_name, None)

    while blocked_value is not None:
        attr_name = f'blocked-{attr_name}'
        next_blocked_value = element.attrs.pop(attr_name, None)
        element.attrs[attr_name] = blocked_value

        blocked_value = next_blocked_value

@dc.dataclass(frozen=True)
class PayloadInjectPolicy(PayloadAwarePolicy):
    """...."""
    _process_response: t.ClassVar[bool] = True

    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._TWO

    def _new_csp(self, request_url: ParsedUrl) -> str:
        """...."""
        assets_base = self.assets_base_url(request_url)

        script_src = f"script-src {assets_base}"

        if self.payload_data.eval_allowed:
            script_src = f"{script_src} 'unsafe-eval'"

        return '; '.join((
            script_src,
            "script-src-elem 'none'",
            "script-src-attr 'none'"
        ))

    def _modify_headers(self, response_info: http_messages.ResponseInfo) \
        -> t.Iterable[tuple[bytes, bytes]]:
        """...."""
        for header_name, header_value in response_info.headers.items():
            if header_name.lower() not in csp.header_names_and_dispositions:
                yield header_name.encode(), header_value.encode()

        new_csp = self._new_csp(response_info.url)

        yield b'Content-Security-Policy', new_csp.encode()

    def _script_urls(self, url: ParsedUrl) -> t.Iterable[str]:
        """...."""
        base_url = self.assets_base_url(url)
        payload_ref = self.payload_data.ref

        yield base_url + 'api/page_init_script.js'

        for path in payload_ref.get_script_paths():
            yield base_url + '/'.join(('static', *path))

    def _modify_body(
            self,
            url:      ParsedUrl,
            body:     bytes,
            encoding: t.Optional[str]
    ) -> bytes:
        """...."""
        soup = bs4.BeautifulSoup(
            markup        = body,
            from_encoding = encoding,
            features      = 'html5lib'
        )

        # Inject scripts.
        script_parent = soup.find('body') or soup.find('html')
        if script_parent is None:
            return body

        for script_url in self._script_urls(url):
            tag = bs4.Tag(name='script', attrs={'src': script_url})
            script_parent.append(tag)

        # Remove Content Security Policy that could possibly block injected
        # scripts.
        for meta in soup.select('head meta[http-equiv]'):
            header_name = meta.attrs.get('http-equiv', '').lower().strip()
            if header_name in csp.enforce_header_names_set:
                block_attr(meta, 'http-equiv')
                block_attr(meta, 'content')

        # Appending a three-byte Byte Order Mark (BOM) will force the browser to
        # decode this as UTF-8 regardless of the 'Content-Type' header. See:
        # https://www.w3.org/International/tests/repository/html5/the-input-byte-stream/results-basics#precedence
        return UTF8_BOM + soup.encode()

    def _consume_response_unsafe(
            self,
            response_info: http_messages.ResponseInfo
    ) -> http_messages.ProducedResponse:
        """...."""
        new_response = response_info.make_produced_response()

        new_headers = self._modify_headers(response_info)

        new_response = dc.replace(new_response, headers=new_headers)

        mime, encoding = deduce_content_type(response_info.headers)
        if mime is None or 'html' not in mime.lower():
            return new_response

        data = response_info.body
        if data is None:
            data = b''

        # A UTF BOM overrides encoding specified by the header.
        for bom, encoding_name in BOMs:
            if data.startswith(bom):
                encoding = encoding_name

        new_data = self._modify_body(response_info.url, data, encoding)

        return dc.replace(new_response, body=new_data)

    def consume_response(self, response_info: http_messages.ResponseInfo) \
        -> http_messages.ProducedResponse:
        """...."""
        try:
            return self._consume_response_unsafe(response_info)
        except Exception as e:
            # TODO: actually describe the errors
            import traceback

            error_info_list = traceback.format_exception(
                type(e),
                e,
                e.__traceback__
            )

            return http_messages.ProducedResponse(
                500,
                ((b'Content-Type', b'text/plain; charset=utf-8'),),
                '\n'.join(error_info_list).encode()
            )


class _PayloadHasProblemsError(HaketiloException):
    pass

class AutoPayloadInjectPolicy(PayloadInjectPolicy):
    """...."""
    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._ONE

    def consume_response(self, response_info: http_messages.ResponseInfo) \
        -> http_messages.ProducedResponse:
        try:
            if self.payload_data.ref.has_problems():
                raise _PayloadHasProblemsError()

            self.payload_data.ref.ensure_items_installed()

            return super().consume_response(response_info)
        except (state.RepoCommunicationError, state.FileInstallationError,
                _PayloadHasProblemsError) as ex:
            extra_params: dict[str, str] = {
                'next_url': response_info.url.orig_url
            }
            if isinstance(ex, state.FileInstallationError):
                extra_params['repo_id']     = ex.repo_id
                extra_params['file_sha256'] = ex.sha256

            query = self._payload_details_to_signed_query_string(
                _salt = 'auto_install_error',
                **extra_params
            )

            redirect_url = 'https://hkt.mitm.it/auto_install_error?' + query
            msg = 'Error occured when installing payload. Redirecting.'

            return http_messages.ProducedResponse(
                status_code = 303,
                headers     = [(b'Location', redirect_url.encode())],
                body        = msg.encode()
            )


@dc.dataclass(frozen=True)
class PayloadSuggestPolicy(PayloadAwarePolicy):
    """...."""
    _process_request: t.ClassVar[bool] = True

    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._ONE

    def consume_request(self, request_info: http_messages.RequestInfo) \
        -> http_messages.ProducedResponse:
        query = self._payload_details_to_signed_query_string(
            _salt    = 'package_suggestion',
            next_url = request_info.url.orig_url
        )

        redirect_url = 'https://hkt.mitm.it/package_suggestion?' + query
        msg = 'A package was found that could be used on this site. Redirecting.'

        return http_messages.ProducedResponse(
            status_code = 303,
            headers     = [(b'Location', redirect_url.encode())],
            body        = msg.encode()
        )


@dc.dataclass(frozen=True, unsafe_hash=True)
class PayloadPolicyFactory(PayloadAwarePolicyFactory):
    """...."""
    def make_policy(self, haketilo_state: state.HaketiloState) \
        -> t.Optional[base.Policy]:
        """...."""
        try:
            payload_data = self.payload_ref.get_data()
        except:
            return None

        if payload_data.explicitly_enabled:
            return PayloadInjectPolicy(payload_data)

        mode = haketilo_state.get_settings().mapping_use_mode

        if mode == state.MappingUseMode.QUESTION:
            return PayloadSuggestPolicy(payload_data)

        if mode == state.MappingUseMode.WHEN_ENABLED:
            return None

        # mode == state.MappingUseMode.AUTO
        return AutoPayloadInjectPolicy(payload_data)
