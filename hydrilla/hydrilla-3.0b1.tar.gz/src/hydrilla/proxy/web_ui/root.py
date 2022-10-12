# SPDX-License-Identifier: GPL-3.0-or-later

# Proxy web UI root.
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

import typing as t

from threading import Lock
from urllib.parse import urlparse

import jinja2
import flask
import werkzeug

from ...translations import translation as make_translation
from ... import versions
from ... import item_infos
from .. import state as st
from .. import http_messages
from . import rules
from . import repos
from . import items
from . import items_import
from . import prompts
from . import _app


def authenticate_by_referrer() -> t.Optional[werkzeug.Response]:
    if flask.request.method == 'GET':
        return None

    parsed_url = urlparse(flask.request.referrer)
    if parsed_url.netloc == 'hkt.mitm.it':
        return None

    flask.abort(403)


def get_current_endpoint() -> str:
    endpoint = flask.request.endpoint
    assert endpoint is not None
    return endpoint

def get_settings() -> st.HaketiloGlobalSettings:
    return _app.get_haketilo_state().get_settings()


class WebUIAppImpl(_app.WebUIApp):
    def __init__(self):
        super().__init__(__name__)

        self.jinja_options = {
            **self.jinja_options,
            'loader':        jinja2.PackageLoader(__package__),
            'autoescape':    jinja2.select_autoescape(['html.jinja']),
            'lstrip_blocks': True,
            'extensions': [
                *self.jinja_options.get('extensions', []),
                'jinja2.ext.i18n',
                'jinja2.ext.do'
            ]
        }

        self.jinja_env.globals['get_current_endpoint'] = get_current_endpoint
        self.jinja_env.globals['get_settings']         = get_settings
        self.jinja_env.globals['EnabledStatus']        = st.EnabledStatus
        self.jinja_env.globals['FrozenStatus']         = st.FrozenStatus
        self.jinja_env.globals['InstalledStatus']      = st.InstalledStatus
        self.jinja_env.globals['ActiveStatus']         = st.ActiveStatus
        self.jinja_env.globals['ItemType']             = item_infos.ItemType
        self.jinja_env.globals['MappingUseMode']       = st.MappingUseMode
        self.jinja_env.globals['versions']             = versions

        self.before_request(authenticate_by_referrer)

        for blueprint in [
                rules.bp, repos.bp, items.bp, items_import.bp, prompts.bp
        ]:
            self.register_blueprint(blueprint)

# Flask app is not thread-safe and has to be accompanied by an ugly lock. This
# can cause slow requests to block other requests, so we might need a better
# workaround at some later point.
app      = WebUIAppImpl()
app_lock = Lock()


@app.route('/', methods=['GET'])
def home(errors: t.Mapping[str, bool] = {}) -> werkzeug.Response:
    state = _app.get_haketilo_state()

    html = flask.render_template(
        'index.html.jinja',
        orphan_item_stats = state.count_orphan_items(),
        **errors
    )
    return flask.make_response(html, 200)

@app.route('/', methods=['POST'])
def home_post() -> werkzeug.Response:
    action = flask.request.form['action']

    state = _app.get_haketilo_state()

    if action == 'use_enabled':
        state.update_settings(mapping_use_mode=st.MappingUseMode.WHEN_ENABLED)
    elif action == 'use_auto':
        state.update_settings(mapping_use_mode=st.MappingUseMode.AUTO)
    elif action == 'use_question':
        state.update_settings(mapping_use_mode=st.MappingUseMode.QUESTION)
    elif action == 'allow_scripts':
        state.update_settings(default_allow_scripts=True)
    elif action == 'block_scripts':
        state.update_settings(default_allow_scripts=False)
    elif action == 'user_make_advanced':
        state.update_settings(advanced_user=True)
    elif action == 'user_make_simple':
        state.update_settings(advanced_user=False)
    elif action == 'prune_orphans':
        state.prune_orphan_items()
    else:
        raise ValueError()

    return flask.redirect(flask.url_for('.home'), 303)

def process_request(
        request_info: http_messages.RequestInfo,
        state: st.HaketiloState
) -> http_messages.ProducedResponse:
    path = '/'.join(('', *request_info.url.path_segments))
    if (request_info.url.has_trailing_slash):
        path += '/'

    with app_lock:
        app._haketilo_state = state

        app.jinja_env.install_gettext_translations(make_translation())

        flask_response = app.test_client().open(
            path         = path,
            base_url     = f'{request_info.url.scheme}://hkt.mitm.it',
            method       = request_info.method,
            query_string = request_info.url.query,
            headers      = [*request_info.headers.items()],
            data         = request_info.body
        )

        headers_bytes = [
            (key.encode(), val.encode())
            for key, val
            in flask_response.headers
        ]

        return http_messages.ProducedResponse(
            status_code = flask_response.status_code,
            headers     = headers_bytes,
            body        = flask_response.data
        )
