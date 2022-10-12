# SPDX-License-Identifier: GPL-3.0-or-later

# Proxy web UI packages loading.
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

import tempfile
import zipfile
import re
import json
import typing as t

from pathlib import Path

import flask
import werkzeug

from ...url_patterns import normalize_pattern
from ...builder import build
from ... import versions
from .. import state as st
from . import _app


bp = flask.Blueprint('import', __package__)

@bp.route('/import', methods=['GET'])
def items_import(errors: t.Mapping[str, bool] = {}) -> werkzeug.Response:
    html = flask.render_template('import.html.jinja', **errors)
    return flask.make_response(html, 200)

def items_import_from_file() -> werkzeug.Response:
    zip_file_storage = flask.request.files.get('items_zipfile')
    if zip_file_storage is None:
        return items_import()

    with tempfile.TemporaryDirectory() as tmpdir_str:
        tmpdir = Path(tmpdir_str)
        tmpdir_child = tmpdir / 'childdir'
        tmpdir_child.mkdir()

        try:
            with zipfile.ZipFile(zip_file_storage) as zip_file:
                zip_file.extractall(tmpdir_child)
        except:
            return items_import({'uploaded_file_not_zip': True})

        extracted_top_level_files = tuple(tmpdir_child.iterdir())
        if extracted_top_level_files == ():
            return items_import({'invalid_uploaded_malcontent': True})

        if len(extracted_top_level_files) == 1 and \
           extracted_top_level_files[0].is_dir():
            malcontent_dir_path = extracted_top_level_files[0]
        else:
            malcontent_dir_path = tmpdir_child

        try:
            _app.get_haketilo_state().import_items(malcontent_dir_path)
        except:
            return items_import({'invalid_uploaded_malcontent': True})

    return flask.redirect(flask.url_for('items.packages'))

identifier_re = re.compile(r'^[-0-9a-z.]+$')

def item_import_ad_hoc() -> werkzeug.Response:
    form = flask.request.form
    def get_as_str(field_name: str) -> str:
        value = form[field_name]
        assert isinstance(value, str)
        return value.strip()

    try:
        identifier = get_as_str('identifier')
        assert identifier
        assert identifier_re.match(identifier)
    except:
        return items_import({'invalid_ad_hoc_identifier': True})

    long_name = get_as_str('long_name') or identifier

    resource_ref = {'identifier': identifier}

    try:
        ver = versions.parse(get_as_str('version') or '1')
    except:
        return items_import({'invalid_ad_hoc_version': True})

    try:
        pat_str = get_as_str('patterns')
        patterns = [
            normalize_pattern(p.strip())
            for p in pat_str.split('\n')
            if p and not p.isspace()
        ]
        assert patterns
    except:
        return items_import({'invalid_ad_hoc_patterns': True})

    common_definition_fields: t.Mapping[str, t.Any] = {
        'identifier':   identifier,
        'long_name':    long_name,
        'version':      ver,
        'description':  get_as_str('description')
    }

    schema_url = \
        'https://hydrilla.koszko.org/schemas/package_source-1.schema.json'

    package_index_json = {
        '$schema':      schema_url,
        'source_name':  'haketilo-ad-hoc-package',
        'copyright':    [],
        'upstream_url': '<local ad hoc package>',
        'definitions': [{
            **common_definition_fields,
            'type':     'mapping',
            'payloads': dict((p, resource_ref) for p in patterns)
        }, {
            **common_definition_fields,
            'type':         'resource',
            'revision':     1,
            'dependencies': [],
            'scripts':      [{'file': 'script.js'}]
        }]
    }

    with tempfile.TemporaryDirectory() as tmpdir_str:
        tmpdir = Path(tmpdir_str)

        source_dir = tmpdir / 'src'
        source_dir.mkdir()

        malcontent_dir = tmpdir / 'malcontent'
        malcontent_dir.mkdir()

        license_text = get_as_str('license_text')
        if license_text:
            package_index_json['copyright'] = [{'file': 'COPYING'}]
            (source_dir / 'COPYING').write_text(license_text)

        (source_dir / 'script.js').write_text(get_as_str('script_text'))

        (source_dir / 'index.json').write_text(json.dumps(package_index_json))

        try:
            builder_args = ['-s', str(source_dir), '-d', str(malcontent_dir)]
            build.perform(builder_args, standalone_mode=False)
            build.perform(['-s', str(source_dir), '-d', '/tmp/haketilodebug'], standalone_mode=False)
            _app.get_haketilo_state().import_items(malcontent_dir)
        except:
            import traceback
            traceback.print_exc()
            return items_import({'invalid_ad_hoc_package': True})

    return flask.redirect(flask.url_for('items.packages'))

@bp.route('/import', methods=['POST'])
def items_import_post() -> werkzeug.Response:
    action = flask.request.form['action']

    if action == 'import_from_file':
        return items_import_from_file()
    elif action == 'import_ad_hoc':
        return item_import_ad_hoc()
    else:
        raise ValueError()
