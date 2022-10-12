# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo addon for Mitmproxy.
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
This module contains the definition of a mitmproxy addon that gets instantiated
from addon script.
"""

import sys
import re
import typing as t
import dataclasses as dc
import traceback as tb

from threading import Lock
from pathlib import Path
from contextlib import contextmanager
from urllib.parse import urlparse

from mitmproxy import tls, http, addonmanager, ctx
from mitmproxy.script import concurrent

from ..exceptions import HaketiloException
from ..translations import smart_gettext as _
from ..url_patterns import parse_url, ParsedUrl
from .state_impl import ConcreteHaketiloState
from . import policies
from . import http_messages


DefaultGetValue = t.TypeVar('DefaultGetValue', str, None)

class MitmproxyHeadersWrapper():
    """...."""
    def __init__(self, headers: http.Headers) -> None:
        """...."""
        self.headers = headers

    __getitem__ = lambda self, key: self.headers[key]
    get_all     = lambda self, key: self.headers.get_all(key)

    @t.overload
    def get(self, key: str) -> t.Optional[str]:
        ...
    @t.overload
    def get(self, key: str, default: DefaultGetValue) \
        -> t.Union[str, DefaultGetValue]:
        ...
    def get(self, key, default = None):
        value = self.headers.get(key)

        if value is None:
            return default
        else:
            return t.cast(str, value)

    def items(self) -> t.Iterable[tuple[str, str]]:
        """...."""
        return self.headers.items(multi=True)


@dc.dataclass(frozen=True)
class FlowHandlingData:
    request_url: ParsedUrl
    policy:      policies.Policy


magical_mitm_it_url_reg = re.compile(r'^http://mitm.it(/.*)?$')
dummy_url = parse_url('http://dummy.replacement.url')


@dc.dataclass
class HaketiloAddon:
    """
    .......
    """
    configured:      bool = False
    configured_lock: Lock = dc.field(default_factory=Lock)

    flows_data:      dict[int, FlowHandlingData] = dc.field(default_factory=dict)
    flows_data_lock: Lock                        = dc.field(default_factory=Lock)

    state: t.Optional[ConcreteHaketiloState] = None

    def load(self, loader: addonmanager.Loader) -> None:
        """...."""
        loader.add_option(
            name     = 'haketilo_dir',
            typespec = str,
            default  = '~/.haketilo/',
            help     = "Point to a Haketilo data directory to use",
        )

    def configure(self, updated: set[str]) -> None:
        """...."""
        if 'haketilo_dir' not in updated:
            return

        with self.configured_lock:
            if self.configured:
                ctx.log.warn(_('haketilo_dir_already_configured'))
                return

            try:
                haketilo_dir = Path(ctx.options.haketilo_dir)

                self.state = ConcreteHaketiloState.make(haketilo_dir / 'store')
            except Exception as e:
                tb.print_exception(None, e, e.__traceback__)
                sys.exit(1)

            self.configured = True

    def get_handling_data(self, flow: http.HTTPFlow) -> FlowHandlingData:
        policy: policies.Policy

        assert self.state is not None

        with self.flows_data_lock:
            handling_data = self.flows_data.get(id(flow))

        if handling_data is None:
            parsed_url = dummy_url

            if magical_mitm_it_url_reg.match(flow.request.url):
                policy = policies.DoNothingPolicy()
            else:
                try:
                    parsed_url = parse_url(flow.request.url)
                    policy = self.state.select_policy(parsed_url)
                except HaketiloException as e:
                    policy = policies.ErrorBlockPolicy(builtin=True, error=e)

            handling_data = FlowHandlingData(parsed_url, policy)

            with self.flows_data_lock:
                self.flows_data[id(flow)] = handling_data

        return handling_data

    def forget_handling_data(self, flow: http.HTTPFlow) -> None:
        """...."""
        with self.flows_data_lock:
            self.flows_data.pop(id(flow), None)

    @contextmanager
    def http_safe_event_handling(self, flow: http.HTTPFlow) -> t.Iterator:
        """...."""
        with self.configured_lock:
            assert self.configured

        try:
            yield
        except Exception as e:
            tb_string = ''.join(tb.format_exception(None, e, e.__traceback__))
            error_text = _('err.proxy.unknown_error_{}_try_again')\
                .format(tb_string)\
                .encode()
            flow.response = http.Response.make(
                status_code = 500,
                content     = error_text,
                headers     = [(b'Content-Type', b'text/plain; charset=utf-8')]
            )

            self.forget_handling_data(flow)

    @concurrent
    def requestheaders(self, flow: http.HTTPFlow) -> None:
        with self.http_safe_event_handling(flow):
            referrer = flow.request.headers.get('referer')
            if referrer is not None:
                if urlparse(referrer).netloc == 'hkt.mitm.it' and \
                   urlparse(flow.request.url).netloc != 'hkt.mitm.it':
                    # Do not reveal to the site that Haketilo meta-site was
                    # visited before.
                    flow.request.headers.pop('referer', None)

            handling_data = self.get_handling_data(flow)
            policy = handling_data.policy

            if not policy.should_process_request(handling_data.request_url):
                flow.request.stream = True
            if policy.anticache:
                flow.request.anticache()

    @concurrent
    def request(self, flow: http.HTTPFlow) -> None:
        """
        ....
        """
        if flow.request.stream:
            return

        with self.http_safe_event_handling(flow):
            handling_data = self.get_handling_data(flow)

            request_info = http_messages.RequestInfo(
                url     = handling_data.request_url,
                method  = flow.request.method,
                headers = MitmproxyHeadersWrapper(flow.request.headers),
                body    = flow.request.get_content(strict=False) or b''
            )

            result = handling_data.policy.consume_request(request_info)

            if result is not None:
                if isinstance(result, http_messages.ProducedRequest):
                    flow.request.url     = result.url
                    flow.request.method  = result.method
                    flow.request.headers = http.Headers(result.headers)
                    flow.request.set_content(result.body or None)
                else:
                    # isinstance(result, http_messages.ProducedResponse)
                    flow.response = http.Response.make(
                        status_code = result.status_code,
                         headers     = http.Headers(result.headers),
                         content     = result.body
                    )

    def responseheaders(self, flow: http.HTTPFlow) -> None:
        """
        ......
        """
        assert flow.response is not None

        with self.http_safe_event_handling(flow):
            handling_data = self.get_handling_data(flow)
            policy = handling_data.policy

            if not policy.should_process_response(handling_data.request_url):
                flow.response.stream = True

    @concurrent
    def response(self, flow: http.HTTPFlow) -> None:
        """
        ......
        """
        assert flow.response is not None

        if flow.response.stream:
            return

        with self.http_safe_event_handling(flow):
            handling_data = self.get_handling_data(flow)

            response_info = http_messages.ResponseInfo(
                url         = parse_url(flow.request.url),
                orig_url    = handling_data.request_url,
                status_code = flow.response.status_code,
                headers     = MitmproxyHeadersWrapper(flow.response.headers),
                body        = flow.response.get_content(strict=False) or b''
            )

            result = handling_data.policy.consume_response(response_info)
            if result is not None:
                flow.response.status_code = result.status_code
                flow.response.headers     = http.Headers(result.headers)
                flow.response.set_content(result.body)

            self.forget_handling_data(flow)

    def tls_clienthello(self, data: tls.ClientHelloData):
        if data.context.server.address is None:
            return

        host, port = data.context.server.address
        if (host == 'hkt.mitm.it' or host.endswith('.hkt.mitm.it')) and \
           port == 443:
            return

        data.establish_server_tls_first = True

    def error(self, flow: http.HTTPFlow) -> None:
        """...."""
        self.forget_handling_data(flow)
