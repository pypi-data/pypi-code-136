# SPDX-License-Identifier: GPL-3.0-or-later

# Proxy web UI pages that may be shown to the user without manual navigation to
# Haketilo meta-site.
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

import typing as t

from urllib.parse import urlencode

from itsdangerous.url_safe import URLSafeSerializer
import flask
import werkzeug

from .. import state as st
from . import _app


bp = flask.Blueprint('prompts', __package__)


def deserialized_request_details(salt: str) -> t.Mapping[str, str]:
    serializer = URLSafeSerializer(
        _app.get_haketilo_state().get_secret(),
        salt = salt
    )

    return serializer.loads(flask.request.args['details'])


@bp.route('/auto_install_error', methods=['GET'])
def auto_install_error_prompt(errors: t.Mapping[str, bool] = {}) \
    -> werkzeug.Response:
    try:
        details = deserialized_request_details('auto_install_error')
    except:
        return flask.redirect(flask.url_for('home'))

    try:
        payload_store = _app.get_haketilo_state().payload_store()
        payload_ref = payload_store.get(details['payload_id'])

        display_info = payload_ref.get_display_info()

        if not display_info.has_problems:
            return flask.redirect(details['next_url'])

        html = flask.render_template(
            'prompts/auto_install_error.html.jinja',
            display_info = display_info,
            **errors
        )
        return flask.make_response(html, 200)
    except st.MissingItemError:
        flask.abort(404)

@bp.route('/auto_install_error', methods=['POST'])
def auto_install_error_prompt_post() -> werkzeug.Response:
    try:
        details = deserialized_request_details('auto_install_error')
    except:
        return flask.redirect(flask.url_for('home'), code=303)

    form_data = flask.request.form
    action = form_data['action']

    mapping_ver_id = str(int(form_data['mapping_ver_id']))
    payload_id     = str(int(details['payload_id']))

    state = _app.get_haketilo_state()

    try:
        mapping_ver_store = state.mapping_version_store()
        mapping_ver_ref = mapping_ver_store.get(mapping_ver_id)

        payload_store = _app.get_haketilo_state().payload_store()
        payload_ref = payload_store.get(payload_id)

        if action == 'disable_mapping':
            mapping_ver_ref.update_mapping_status(st.EnabledStatus.DISABLED)
        elif action == 'retry_install':
             payload_ref.ensure_items_installed()
        else:
            raise ValueError()
    except st.RepoCommunicationError:
        assert action == 'retry_install'
        return auto_install_error_prompt({'repo_communication_error': True})
    except st.FileInstallationError:
        assert action == 'retry_install'
        return auto_install_error_prompt({'file_installation_error': True})
    except st.MissingItemError:
        flask.abort(404)

    return flask.redirect(details['next_url'])


@bp.route('/package_suggestion', methods=['GET'])
def package_suggestion_prompt(errors: t.Mapping[str, bool] = {}) \
    -> werkzeug.Response:
    try:
        details = deserialized_request_details('package_suggestion')
    except:
        return flask.redirect(flask.url_for('home'))

    try:
        payload_store = _app.get_haketilo_state().payload_store()
        payload_ref = payload_store.get(details['payload_id'])

        display_info = payload_ref.get_display_info()

        if display_info.mapping_info.active != st.ActiveStatus.AUTO:
            return flask.redirect(details['next_url'])

        html = flask.render_template(
            'prompts/package_suggestion.html.jinja',
            display_info = display_info,
            **errors
        )
        return flask.make_response(html, 200)
    except st.MissingItemError:
        flask.abort(404)

@bp.route('/package_suggestion', methods=['POST'])
def package_suggestion_prompt_post() -> werkzeug.Response:
    try:
        details = deserialized_request_details('package_suggestion')
    except:
        return flask.redirect(flask.url_for('home'))

    form_data = flask.request.form
    action = form_data['action']

    mapping_ver_id = str(int(form_data['mapping_ver_id']))

    state = _app.get_haketilo_state()

    try:
        mapping_ver_store = state.mapping_version_store()
        mapping_ver_ref = mapping_ver_store.get(mapping_ver_id)

        if action == 'disable_mapping':
            mapping_ver_ref.update_mapping_status(st.EnabledStatus.DISABLED)
        elif action == 'enable_mapping':
            mapping_ver_ref.update_mapping_status(
                enabled = st.EnabledStatus.ENABLED,
                frozen  = st.FrozenStatus.EXACT_VERSION
            )
        else:
            raise ValueError()
    except st.RepoCommunicationError:
        assert action == 'enable_mapping'
        return package_suggestion_prompt({'repo_communication_error': True})
    except st.FileInstallationError:
        assert action == 'enable_mapping'
        return package_suggestion_prompt({'file_installation_error': True})
    except st.MissingItemError:
        flask.abort(404)

    return flask.redirect(details['next_url'])
