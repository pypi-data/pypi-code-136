# SPDX-License-Identifier: AGPL-3.0-or-later

# Main repository logic.
#
# This file is part of Hydrilla
#
# Copyright (C) 2021, 2022 Wojtek Kosior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
# I, Wojtek Kosior, thereby promise not to sue for violation of this
# file's license. Although I request that you do not make use of this
# code in a proprietary program, I am not going to enforce this in
# court.

import re
import os
import json
import typing as t

from pathlib import Path

import click
import flask
import werkzeug

from ..exceptions import HaketiloException
from .. import _version
from ..translations import smart_gettext as _, translation as make_translation
from .. import versions
from .. import item_infos
from . import config
from . import malcontent


generated_by = {
    'name': 'hydrilla.server',
    'version': _version.version
}


bp = flask.Blueprint('bp', __package__)

class HydrillaApp(flask.Flask):
    """Flask app that implements a Hydrilla server."""
    def __init__(self, hydrilla_config: dict, flask_config: dict={}):
        """Create the Flask instance according to the configuration"""
        super().__init__(__package__, static_url_path='/',
                         static_folder=hydrilla_config['malcontent_dir'])
        self.config.update(flask_config)

        # https://stackoverflow.com/questions/9449101/how-to-stop-flask-from-initialising-twice-in-debug-mode
        if self.debug and os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
            return

        self.jinja_options = {
            **self.jinja_options,
            'extensions': [
                *self.jinja_options.get('extensions', []),
                'jinja2.ext.i18n'
            ]
        }

        self._hydrilla_port = hydrilla_config['port']
        self._hydrilla_werror = hydrilla_config.get('werror', False)
        verify_files = hydrilla_config.get('verify_files', True)

        if 'hydrilla_parent' in hydrilla_config:
            raise HaketiloException(_('err.server.opt_hydrilla_parent_not_implemented'))

        malcontent_dir_path = Path(hydrilla_config['malcontent_dir']).resolve()
        self._hydrilla_malcontent = malcontent.Malcontent(
            malcontent_dir_path = malcontent_dir_path,
            werror              = self._hydrilla_werror,
            verify_files        = verify_files
        )

        self.jinja_env.install_gettext_translations(make_translation())

        self.jinja_env.globals['hydrilla_project_url'] = \
            hydrilla_config['hydrilla_project_url']

        self.register_blueprint(bp)

    def run(self, *args, **kwargs):
        """
        Flask's run() but tweaked to use the port from hydrilla configuration by
        default.
        """
        return super().run(*args, port=self._hydrilla_port, **kwargs)

def get_malcontent() -> malcontent.Malcontent:
    return t.cast(HydrillaApp, flask.current_app)._hydrilla_malcontent

@bp.route('/')
def index():
    return flask.render_template('index.html')

identifier_json_re = re.compile(r'^([-0-9a-z.]+)\.json$')

def get_resource_or_mapping(item_type: str, identifier: str) \
    -> werkzeug.Response:
    """
    Strip '.json' from 'identifier', look the item up and send its JSON
    description.
    """
    match = identifier_json_re.match(identifier)
    if not match:
        flask.abort(404)

    identifier = match.group(1)

    infos: t.Mapping[str, item_infos.VersionedItemInfo]
    if item_type == 'resource':
        infos = get_malcontent().resource_infos
    else:
        infos = get_malcontent().mapping_infos

    versioned_info = infos.get(identifier)

    if versioned_info is None:
        flask.abort(404)

    info = versioned_info.newest_info

    # no need for send_from_directory(); path is safe, constructed by us
    info_path = f'{info.identifier}/{versions.version_string(info.version)}'
    file_path = get_malcontent().malcontent_dir_path / item_type / info_path

    if flask.__version__[0:2] in ('0.', '1.'):
        caching_args = {'add_etags': False, 'cache_timeout': 0}
    else:
        caching_args = {'etag': False}

    return flask.send_file(
        str(file_path),
        mimetype    = 'application/json',
        conditional = False,
        **caching_args # type: ignore
    )

@bp.route('/mapping/<string:identifier_dot_json>')
def get_newest_mapping(identifier_dot_json: str) -> werkzeug.Response:
    return get_resource_or_mapping('mapping', identifier_dot_json)

@bp.route('/resource/<string:identifier_dot_json>')
def get_newest_resource(identifier_dot_json: str) -> werkzeug.Response:
    return get_resource_or_mapping('resource', identifier_dot_json)

def make_ref(info: item_infos.AnyInfo) -> t.Dict[str, t.Any]:
    ref: t.Dict[str, t.Any] = {
        'version':    info.version,
        'identifier': info.identifier,
        'long_name':  info.long_name
    }

    if isinstance(info, item_infos.ResourceInfo):
        ref['revision'] = info.revision

    return ref

@bp.route('/query')
def query():
    url = flask.request.args['url']

    mapping_refs = [make_ref(info) for info in get_malcontent().query(url)]

    result = {
        '$schema': 'https://hydrilla.koszko.org/schemas/api_query_result-1.schema.json',
        'mappings': mapping_refs,
        'generated_by': generated_by
    }

    return werkzeug.Response(json.dumps(result), mimetype='application/json')

@bp.route('/list_all')
def list_all_packages():
    malcontent = get_malcontent()

    resource_refs = [make_ref(info) for info in malcontent.get_all_resources()]
    mapping_refs  = [make_ref(info) for info in malcontent.get_all_mappings()]

    result = {
        '$schema': 'https://hydrilla.koszko.org/schemas/api_package_list-2.schema.json',
        'resources': resource_refs,
        'mappings':  mapping_refs,
        'generated_by': generated_by
    }

    return werkzeug.Response(json.dumps(result), mimetype='application/json')

@bp.route('/--help')
def mm_help():
    return start.get_help(click.Context(start_wsgi)) + '\n'

@bp.route('/--version')
def mm_version():
    prog_info = {'prog': 'Hydrilla', 'version': _version.version}
    return _('%(prog)s_%(version)s_license') % prog_info + '\n'

default_config_path = Path('/etc/hydrilla/config.json')
default_malcontent_dir = '/var/lib/hydrilla/malcontent'
default_project_url = 'https://hydrillabugs.koszko.org/projects/hydrilla/wiki'

@click.command(help=_('serve_hydrilla_packages_explain_wsgi_considerations'))
@click.option('-m', '--malcontent-dir',
              type=click.Path(exists=True, file_okay=False),
              help=_('directory_to_serve_from_overrides_config'))
@click.option('-h', '--hydrilla-project-url', type=click.STRING,
              help=_('project_url_to_display_overrides_config'))
@click.option('-p', '--port', type=click.INT,
              help=_('tcp_port_to_listen_on_overrides_config'))
@click.option('-c', '--config', 'config_path',
              type=click.Path(exists=True, dir_okay=False, resolve_path=True),
              help=_('path_to_config_file_explain_default'))
@click.version_option(version=_version.version, prog_name='Hydrilla',
                      message=_('%(prog)s_%(version)s_license'),
                      help=_('version_printing'))
def start(
        malcontent_dir:       t.Optional[str],
        hydrilla_project_url: t.Optional[str],
        port:                 t.Optional[int],
        config_path:          t.Optional[str]
) -> None:
    """
    Run a development Hydrilla server.

    This command is meant to be the entry point of hydrilla command exported by
    this package.
    """
    if config_path is None:
        hydrilla_config = config.load()
    else:
        hydrilla_config = config.load(config_paths=[Path(config_path)])

    if malcontent_dir is not None:
        hydrilla_config['malcontent_dir'] = str(Path(malcontent_dir).resolve())

    if hydrilla_project_url is not None:
        hydrilla_config['hydrilla_project_url'] = hydrilla_project_url

    if port is not None:
        hydrilla_config['port'] = port

    for opt in ('malcontent_dir', 'hydrilla_project_url', 'port'):
        if opt not in hydrilla_config:
            raise ValueError(_('config_option_{}_not_supplied').format(opt))

    HydrillaApp(hydrilla_config).run()

@click.command(help=_('serve_hydrilla_packages_wsgi_help'),
               context_settings={
                   'ignore_unknown_options': True,
                   'allow_extra_args': True
               })
@click.version_option(version=_version.version, prog_name='Hydrilla',
                      message=_('%(prog)s_%(version)s_license'),
                      help=_('version_printing'))
def start_wsgi() -> flask.Flask:
    """
    Create application object for use in WSGI deployment.

    This command Also handles --help and --version options in case it gets
    called outside WSGI environment.
    """
    return HydrillaApp(click.get_current_context().obj or config.load())
