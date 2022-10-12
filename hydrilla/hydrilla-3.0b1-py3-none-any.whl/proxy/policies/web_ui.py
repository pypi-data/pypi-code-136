# SPDX-License-Identifier: GPL-3.0-or-later

# Policy for serving the web UI from within mitmproxy.
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

from ...translations import smart_gettext as _
from .. import state
from .. import http_messages
from .. import web_ui
from . import base


@dc.dataclass(frozen=True)
class WebUIPolicy(base.Policy):
    """...."""
    _process_request:  t.ClassVar[bool] = True

    priority: t.ClassVar[base.PolicyPriority] = base.PolicyPriority._THREE

    haketilo_state: state.HaketiloState

    def consume_request(self, request_info: http_messages.RequestInfo) \
        -> http_messages.ProducedResponse:
        return web_ui.process_request(request_info, self.haketilo_state)


@dc.dataclass(frozen=True, unsafe_hash=True)
class WebUIPolicyFactory(base.PolicyFactory):
    """...."""
    def make_policy(self, haketilo_state: state.HaketiloState) -> WebUIPolicy:
        return WebUIPolicy(haketilo_state)
