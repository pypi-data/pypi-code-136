# SPDX-License-Identifier: GPL-3.0-or-later

# Proxy web UI script blocking rule management.
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

import flask
import werkzeug

from .. import state as st
from . import _app


bp = flask.Blueprint('rules', __package__)

@bp.route('/rules/add', methods=['GET'])
def add_rule(errors: t.Mapping[str, bool] = {}) -> werkzeug.Response:
    html = flask.render_template('rules/add.html.jinja', **errors)
    return flask.make_response(html, 200)

@bp.route('/rules/add', methods=['POST'])
def add_rule_post() -> werkzeug.Response:
    form_data = flask.request.form

    try:
        new_rule_ref = _app.get_haketilo_state().rule_store().add(
            pattern = form_data['pattern'],
            allow   = form_data['allow'] == 'true'
        )
    except st.RulePatternInvalid:
        return add_rule({'rule_pattern_invalid': True})

    return flask.redirect(flask.url_for('.show_rule', rule_id=new_rule_ref.id))

@bp.route('/rules', methods=['GET'])
def rules(errors: t.Mapping[str, bool] = {}) -> werkzeug.Response:
    store = _app.get_haketilo_state().rule_store()

    html = flask.render_template(
        'rules/index.html.jinja',
        display_infos = store.get_display_infos(),
        **errors
    )
    return flask.make_response(html, 200)

@bp.route('/rules/view/<string:rule_id>')
def show_rule(rule_id: str, errors: t.Mapping[str, bool] = {}) \
    -> werkzeug.Response:
    try:
        store = _app.get_haketilo_state().rule_store()
        display_info = store.get(rule_id).get_display_info()

        html = flask.render_template(
            'rules/show_single.html.jinja',
            display_info = display_info,
            **errors
        )
        return flask.make_response(html, 200)
    except st.MissingItemError:
        flask.abort(404)

@bp.route('/rules/view/<string:rule_id>', methods=['POST'])
def alter_rule(rule_id: str) -> werkzeug.Response:
    form_data = flask.request.form
    action = form_data['action']

    try:
        rule_ref = _app.get_haketilo_state().rule_store().get(rule_id)

        if action == 'remove_rule':
            rule_ref.remove()
            return flask.redirect(flask.url_for('.rules'))
        elif action == 'update_rule_data':
            allow_param = form_data.get('allow')
            rule_ref.update(
                pattern = form_data.get('pattern'),
                allow   = None if allow_param is None else allow_param == 'true'
            )
        else:
            raise ValueError()
    except st.RulePatternInvalid:
        return show_rule(rule_id, {'rule_pattern_invalid': True})
    except st.MissingItemError:
        flask.abort(404)

    return flask.redirect(flask.url_for('.show_rule', rule_id=rule_id))
