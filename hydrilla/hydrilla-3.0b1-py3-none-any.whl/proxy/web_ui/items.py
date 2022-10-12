# SPDX-License-Identifier: GPL-3.0-or-later

# Proxy web UI package/library management.
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

from urllib.parse import unquote

import flask
import werkzeug

from ... import item_infos
from .. import state as st
from . import _app


bp = flask.Blueprint('items', __package__)

@bp.route('/packages')
def packages() -> werkzeug.Response:
    store = _app.get_haketilo_state().mapping_store()

    html = flask.render_template(
        'items/packages.html.jinja',
        display_infos = store.get_display_infos()
    )
    return flask.make_response(html, 200)

@bp.route('/libraries')
def libraries() -> werkzeug.Response:
    store = _app.get_haketilo_state().resource_store()

    html = flask.render_template(
        'items/libraries.html.jinja',
        display_infos = store.get_display_infos()
    )
    return flask.make_response(html, 200)

def item_store(state: st.HaketiloState, item_type: item_infos.ItemType) \
    -> t.Union[st.MappingStore, st.ResourceStore]:
        if item_type == item_infos.ItemType.RESOURCE:
            return state.resource_store()
        else:
            return state.mapping_store()

def show_item(
        item_id:   str,
        item_type: item_infos.ItemType,
        errors:    t.Mapping[str, bool] = {}
) -> werkzeug.Response:
    try:
        store = item_store(_app.get_haketilo_state(), item_type)
        display_info = store.get(str(item_id)).get_display_info()

        html = flask.render_template(
            f'items/{item_type.alt_name}_view.html.jinja',
            display_info = display_info,
            **errors
        )
        return flask.make_response(html, 200)
    except st.MissingItemError:
        flask.abort(404)


@bp.route('/libraries/view/<string:item_id>')
def show_library(item_id: str) -> werkzeug.Response:
    return show_item(item_id, item_infos.ItemType.RESOURCE)

@bp.route('/packages/view/<string:item_id>')
def show_package(item_id: str) -> werkzeug.Response:
    return show_item(item_id, item_infos.ItemType.MAPPING)

def alter_item(item_id: str, item_type: item_infos.ItemType) \
    -> werkzeug.Response:
    form_data = flask.request.form
    action = form_data['action']

    try:
        store = item_store(_app.get_haketilo_state(), item_type)
        item_ref = store.get(item_id)

        if action == 'disable_item':
            assert isinstance(item_ref, st.MappingRef)
            item_ref.update_status(st.EnabledStatus.DISABLED)
        elif action == 'unenable_item':
            assert isinstance(item_ref, st.MappingRef)
            item_ref.update_status(st.EnabledStatus.NO_MARK)
        elif action in ('enable_item', 'unfreeze_item'):
            assert isinstance(item_ref, st.MappingRef)
            item_ref.update_status(
                enabled = st.EnabledStatus.ENABLED,
                frozen  = st.FrozenStatus.NOT_FROZEN,
            )
        elif action == 'freeze_to_repo':
            assert isinstance(item_ref, st.MappingRef)
            item_ref.update_status(
                enabled = st.EnabledStatus.ENABLED,
                frozen  = st.FrozenStatus.REPOSITORY,
            )
        elif action == 'freeze_to_version':
            assert isinstance(item_ref, st.MappingRef)
            item_ref.update_status(
                enabled = st.EnabledStatus.ENABLED,
                frozen  = st.FrozenStatus.EXACT_VERSION,
            )
        else:
            raise ValueError()
    except st.RepoCommunicationError:
        return show_item(item_id, item_type, {'repo_communication_error': True})
    except st.FileInstallationError:
        return show_item(item_id, item_type, {'file_installation_error': True})
    except st.ImpossibleSituation:
        errors = {'impossible_situation_error': True}
        return show_item(item_id, item_type, errors)
    except st.MissingItemError:
        flask.abort(404)

    return flask.redirect(
        flask.url_for(f'.show_{item_type.alt_name}', item_id=item_id)
    )

@bp.route('/libraries/view/<string:item_id>', methods=['POST'])
def alter_library(item_id: str) -> werkzeug.Response:
    return alter_item(item_id, item_infos.ItemType.RESOURCE)

@bp.route('/packages/view/<string:item_id>', methods=['POST'])
def alter_package(item_id: str) -> werkzeug.Response:
    return alter_item(item_id, item_infos.ItemType.MAPPING)


ItemVersionDisplayInfo = t.Union[
    st.MappingVersionDisplayInfo,
    st.ResourceVersionDisplayInfo
]

def item_version_store(
        state:     st.HaketiloState,
        item_type: item_infos.ItemType
) -> t.Union[st.MappingVersionStore, st.ResourceVersionStore]:
        if item_type == item_infos.ItemType.RESOURCE:
            return state.resource_version_store()
        else:
            return state.mapping_version_store()

def show_item_version(
        item_version_id: str,
        item_type:          item_infos.ItemType,
        errors:             t.Mapping[str, bool] = {}
) -> werkzeug.Response:
    state = _app.get_haketilo_state()

    try:
        store = item_version_store(state, item_type)
        version_ref = store.get(item_version_id)
        display_info = version_ref.get_item_display_info()

        this_info:   t.Optional[ItemVersionDisplayInfo] = None

        for info in display_info.all_versions:
            if info.ref == version_ref:
                this_info = info

        assert this_info is not None

        html = flask.render_template(
            f'items/{item_type.alt_name}_viewversion.html.jinja',
            display_info         = display_info,
            version_display_info = this_info,
            **errors
        )
        return flask.make_response(html, 200)
    except st.MissingItemError:
        flask.abort(404)

@bp.route('/libraries/viewversion/<string:item_version_id>')
def show_library_version(item_version_id: str) -> werkzeug.Response:
    return show_item_version(item_version_id, item_infos.ItemType.RESOURCE)

@bp.route('/packages/viewversion/<string:item_version_id>')
def show_package_version(item_version_id: str) -> werkzeug.Response:
    return show_item_version(item_version_id, item_infos.ItemType.MAPPING)

def alter_item_version(item_version_id: str, item_type: item_infos.ItemType) \
    -> werkzeug.Response:
    form_data = flask.request.form
    action = form_data['action']

    try:
        store = item_version_store(_app.get_haketilo_state(), item_type)
        item_version_ref = store.get(item_version_id)

        if action == 'disable_item':
            assert isinstance(item_version_ref, st.MappingVersionRef)
            item_version_ref.update_mapping_status(st.EnabledStatus.DISABLED)
        elif action == 'unenable_item':
            assert isinstance(item_version_ref, st.MappingVersionRef)
            item_version_ref.update_mapping_status(st.EnabledStatus.NO_MARK)
        elif action in ('enable_item_version', 'freeze_to_version'):
            assert isinstance(item_version_ref, st.MappingVersionRef)
            item_version_ref.update_mapping_status(
                enabled = st.EnabledStatus.ENABLED,
                frozen  = st.FrozenStatus.EXACT_VERSION,
            )
        elif action == 'unfreeze_item':
            assert isinstance(item_version_ref, st.MappingVersionRef)
            item_version_ref.update_mapping_status(
                enabled = st.EnabledStatus.ENABLED,
                frozen  = st.FrozenStatus.NOT_FROZEN,
            )
        elif action == 'freeze_to_repo':
            assert isinstance(item_version_ref, st.MappingVersionRef)
            item_version_ref.update_mapping_status(
                enabled = st.EnabledStatus.ENABLED,
                frozen  = st.FrozenStatus.REPOSITORY,
            )
        elif action == 'install_item_version':
            item_version_ref.install()
        elif action == 'uninstall_item_version':
            item_version_ref_after = item_version_ref.uninstall()
            if item_version_ref_after is None:
                url = flask.url_for(f'.{item_type.alt_name_plural}')
                return flask.redirect(url)
            else:
                return show_item_version(item_version_id, item_type)
        else:
            raise ValueError()
    except st.RepoCommunicationError:
        return show_item_version(
            item_version_id = item_version_id,
            item_type       = item_type,
            errors          = {'repo_communication_error': True}
        )
    except st.FileInstallationError:
        return show_item_version(
            item_version_id = item_version_id,
            item_type       = item_type,
            errors          = {'file_installation_error': True}
        )
    except st.ImpossibleSituation:
        return show_item_version(
            item_version_id = item_version_id,
            item_type       = item_type,
            errors          = {'impossible_situation_error': True}
        )
    except st.MissingItemError:
        flask.abort(404)

    return flask.redirect(
        flask.url_for(
            f'.show_{item_type.alt_name}_version',
            item_version_id = item_version_id
        )
    )

@bp.route('/libraries/viewversion/<string:item_version_id>', methods=['POST'])
def alter_library_version(item_version_id: str) -> werkzeug.Response:
    return alter_item_version(item_version_id, item_infos.ItemType.RESOURCE)

@bp.route('/packages/viewversion/<string:item_version_id>', methods=['POST'])
def alter_package_version(item_version_id: str) -> werkzeug.Response:
    return alter_item_version(item_version_id, item_infos.ItemType.MAPPING)

def show_file(
        item_version_id: str,
        item_type:       item_infos.ItemType,
        file_type:       str,
        name:            str,
) -> werkzeug.Response:
    if file_type not in ('license', 'web_resource'):
        flask.abort(404)

    try:
        store = item_version_store(_app.get_haketilo_state(), item_type)
        item_version_ref = store.get(item_version_id)

        try:
            if file_type == 'license':
                file_data = item_version_ref.get_license_file(name)
            else:
                assert isinstance(item_version_ref, st.ResourceVersionRef)
                file_data = item_version_ref.get_resource_file(name)

            return werkzeug.Response(
                file_data.contents,
                mimetype = file_data.mime_type
            )
        except st.MissingItemError:
            if file_type == 'license':
                url = item_version_ref.get_upstream_license_file_url(name)
            else:
                assert isinstance(item_version_ref, st.ResourceVersionRef)
                url = item_version_ref.get_upstream_resource_file_url(name)

            return flask.redirect(url)

    except st.MissingItemError:
        flask.abort(404)

@bp.route('/packages/viewversion/<string:item_version_id>/<string:file_type>/<path:name>')
def show_mapping_file(item_version_id: str, file_type: str, name: str) \
    -> werkzeug.Response:
    item_type = item_infos.ItemType.MAPPING
    return show_file(item_version_id, item_type, file_type, name)

@bp.route('/libraries/viewversion/<string:item_version_id>/<string:file_type>/<path:name>')
def show_resource_file(item_version_id: str, file_type: str, name: str) \
    -> werkzeug.Response:
    item_type = item_infos.ItemType.RESOURCE
    return show_file(item_version_id, item_type, file_type, name)

@bp.route('/libraries/viewdep/<string:item_version_id>/<string:dep_identifier>')
def show_library_dep(item_version_id: str, dep_identifier: str) \
    -> werkzeug.Response:
    state = _app.get_haketilo_state()

    try:
        store = state.resource_version_store()
        dep_id = store.get(item_version_id).get_dependency(dep_identifier).id
        url = flask.url_for('.show_library_version', item_version_id=dep_id)
    except st.MissingItemError:
        try:
            versionless_store = state.resource_store()
            item_ref = versionless_store.get_by_identifier(dep_identifier)
            url = flask.url_for('.show_library', item_id=item_ref.id)
        except st.MissingItemError:
            flask.abort(404)

    return flask.redirect(url)

@bp.route('/<string:item_type>/viewrequired/<string:item_version_id>/<string:required_identifier>')
def show_required_mapping(
        item_type:           str,
        item_version_id:     str,
        required_identifier: str
) -> werkzeug.Response:
    state = _app.get_haketilo_state()

    if item_type not in ('package', 'library'):
        flask.abort(404)

    found = False

    if item_type == 'package':
        try:
            ref = state.mapping_version_store().get(item_version_id)
            mapping_ver_id = ref.get_required_mapping(required_identifier).id
            url = flask.url_for(
                '.show_package_version',
                item_version_id = mapping_ver_id
            )
            found = True
        except st.MissingItemError:
            pass

    if not found:
        try:
            versionless_store = state.mapping_store()
            mapping_ref = versionless_store\
                .get_by_identifier(required_identifier)
            url = flask.url_for('.show_package', item_id=mapping_ref.id)
        except st.MissingItemError:
            flask.abort(404)

    return flask.redirect(url)

@bp.route('/package/viewpayload/<string:item_version_id>/<string:pattern>/<string:lib_identifier>')
def show_payload(item_version_id: str, pattern: str, lib_identifier: str) \
    -> werkzeug.Response:
    state = _app.get_haketilo_state()

    try:
        ref = state.mapping_version_store().get(item_version_id)

        try:
            resource_ver_ref = \
                ref.get_payload_resource(unquote(pattern), lib_identifier)
            url = flask.url_for(
                '.show_library_version',
                item_version_id = resource_ver_ref.id
            )
        except st.MissingItemError:
            resource_ref = \
                state.resource_store().get_by_identifier(lib_identifier)
            url = flask.url_for('.show_library', item_id=resource_ref.id)
    except st.MissingItemError:
        flask.abort(404)

    return flask.redirect(url)
