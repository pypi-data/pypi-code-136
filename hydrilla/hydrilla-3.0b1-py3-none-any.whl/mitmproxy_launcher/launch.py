# SPDX-License-Identifier: GPL-3.0-or-later

# Code for starting mitmproxy
#
# This file is part of Hydrilla
#
# Copyright (C) 2021, 2022 Wojtek Kosior
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


# We want to run mitmproxy with our script as an addon. A simple way would be to
# find something like a 'main' function in mitmproxy, import it and call here.
# Unfortunately, there is currently no guarantee that such function can be
# considered mitmproxy's stable programming API. For this reason we instead
# spawn a new process.

import sys
import os
import subprocess as sp

from pathlib import Path
# The following import requires at least Python 3.8. There is no point adding
# a workaround for Python 3.7 because mitmproxy itself (which we're loading
# here) relies on Python 3.9+. This does not affect the Hydrilla server and
# builder which continue to work under Python 3.7.
from importlib.metadata import distribution

import click

from .. import _version
from ..translations import smart_gettext as _


addon_script_text = '''
from hydrilla.proxy.addon import HaketiloAddon

addons = [HaketiloAddon()]
'''

@click.command(help=_('cli_help.haketilo'))
@click.option('-p', '--port', default=8080, type=click.IntRange(1, 65535),
              help=_('cli_opt.haketilo.port'))
@click.option('-d', '--directory', default='~/.haketilo/',
              type=click.Path(file_okay=False),
              help=_('cli_opt.haketilo.dir'))
@click.version_option(version=_version.version, prog_name='Haketilo proxy',
                      message=_('%(prog)s_%(version)s_license'),
                      help=_('cli_opt.haketilo.version'))
def launch(port: int, directory: str):
    """
    ....
    """
    directory_path = Path(os.path.expanduser(directory)).resolve()

    directory_path.mkdir(parents=True, exist_ok=True)

    script_path = directory_path / 'addon.py'

    script_path.write_text(addon_script_text)

    sys.argv = [
        'mitmdump',
        '-p', str(port),
        '--set', f'confdir={directory_path / "mitmproxy"}',
        '--set', 'upstream_cert=false',
        '--set', 'connection_strategy=lazy',
        '--set', f'haketilo_dir={directory_path}',
        '--scripts', str(script_path)
    ]

    for entry_point in distribution('mitmproxy').entry_points:
        if entry_point.group == 'console_scripts' and \
           entry_point.name == 'mitmdump':
            sys.exit(entry_point.load()())

    sys.exit(1)
