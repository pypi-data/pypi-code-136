# SPDX-License-Identifier: GPL-3.0-or-later

# Proxy web UI repos view.
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

import flask
import werkzeug

from .. import state as st
from . import _app


bp = flask.Blueprint('repos', __package__)

@bp.route('/repos/add', methods=['GET'])
def add_repo(errors: t.Mapping[str, bool] = {}) -> werkzeug.Response:
    html = flask.render_template('repos/add.html.jinja', **errors)
    return flask.make_response(html, 200)

@bp.route('/repos/add', methods=['POST'])
def add_repo_post() -> werkzeug.Response:
    form_data = flask.request.form
    if 'name' not in form_data or 'url' not in form_data:
        return add_repo()

    try:
        new_repo_ref = _app.get_haketilo_state().repo_store().add(
            name = form_data['name'],
            url  = form_data['url']
        )
    except st.RepoNameInvalid:
        return add_repo({'repo_name_invalid': True})
    except st.RepoNameTaken:
        return add_repo({'repo_name_taken': True})
    except st.RepoUrlInvalid:
        return add_repo({'repo_url_invalid': True})

    return flask.redirect(flask.url_for('.show_repo', repo_id=new_repo_ref.id))

@bp.route('/repos')
def repos() -> werkzeug.Response:
    repo_store = _app.get_haketilo_state().repo_store()

    local_semirepo_info, *repo_infos = repo_store.get_display_infos()

    html = flask.render_template(
        'repos/index.html.jinja',
        local_semirepo_info = local_semirepo_info,
        display_infos       = repo_infos
    )
    return flask.make_response(html, 200)

@bp.route('/repos/view/<string:repo_id>')
def show_repo(repo_id: str, errors: t.Mapping[str, bool] = {}) \
    -> werkzeug.Response:
    try:
        store = _app.get_haketilo_state().repo_store()
        display_info = store.get(repo_id).get_display_info()

        html = flask.render_template(
            'repos/show_single.html.jinja',
            display_info = display_info,
            **errors
        )
        return flask.make_response(html, 200)
    except st.MissingItemError:
        flask.abort(404)

@bp.route('/repos/view/<string:repo_id>', methods=['POST'])
def alter_repo(repo_id: str) -> werkzeug.Response:
    form_data = flask.request.form
    action = form_data['action']

    repo_id = str(int(repo_id))
    if repo_id == '1':
        # Protect local semi-repo.
        flask.abort(403)

    try:
        repo_ref = _app.get_haketilo_state().repo_store().get(repo_id)

        if action == 'remove_repo':
            repo_ref.remove()
            return flask.redirect(flask.url_for('.repos'))
        elif action == 'refresh_repo':
            repo_ref.refresh()
        elif action == 'update_repo_data':
            repo_ref.update(
                url  = form_data.get('url'),
                name = form_data.get('name')
            )
        else:
            raise ValueError()
    except st.RepoNameInvalid:
        return show_repo(repo_id, {'repo_name_invalid': True})
    except st.RepoNameTaken:
        return show_repo(repo_id, {'repo_name_taken': True})
    except st.RepoUrlInvalid:
        return show_repo(repo_id, {'repo_url_invalid': True})
    except st.RepoCommunicationError:
        return show_repo(repo_id, {'repo_communication_error': True})
    except st.FileInstallationError:
        return show_repo(repo_id, {'file_installation_error': True})
    except st.RepoApiVersionUnsupported:
        return show_repo(repo_id, {'repo_api_version_unsupported': True})
    except st.MissingItemError:
        flask.abort(404)

    return flask.redirect(flask.url_for('.show_repo', repo_id=repo_id))
