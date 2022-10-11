#
# control-tmux: Wrapper script around tmux that enables quickly switching between
# sessions, history saving and loading.
#
# Copyright 2018 Katie Rust (https://ktpanda.org)
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list
# of conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import sys
import re
from pathlib import Path

if sys.version_info >= (3, 9):
    from importlib.resources import files
else:
    from importlib_resources import files

import argcomplete

from controltmux import runproc

def file_contains(path, text):
    try:
        with path.open(encoding='latin1') as fp:
            for line in fp:
                if text in line:
                    return True
    except FileNotFoundError:
        pass
    return False

def setup_user(ctl, aliases=()):
    home = Path.home()

    ctl.save_path.mkdir(parents=True, exist_ok=True)

    # Use latin1 encoding - the only things we're manipulating are ascii, so if it's UTF8
    # it won't change it and if it's broken it won't throw errors.
    data_files = files('controltmux')
    conf_data = data_files.joinpath('tmux-default-2.0.conf').read_text(encoding='latin1')
    shell_data = data_files.joinpath('tmux.setup.sh').read_text(encoding='latin1')

    dest = home / '.tmux.default.conf'
    print(f'Installing configuration in {dest}')
    dest.write_text(conf_data, encoding='latin1')

    # Assume that if .bashrc.d exists, then .bashrc will run scripts from it.
    bashrc_d = home / '.bashrc.d'
    bashrc = home / '.bashrc'

    if bashrc_d.is_dir():
        script_path = bashrc_d / '95-tmux-setup.local.sh'
    else:
        run_line = '[ -e $HOME/.tmux.setup.sh ] && . $HOME/.tmux.setup.sh'
        if not file_contains(bashrc, run_line):
            print(f'Adding the following line to {bashrc}:')
            print(f'   {run_line}')
            with bashrc.open('a', encoding='ascii') as fp:
                fp.write('\n\n' + run_line + '\n')

        script_path = home / '.tmux.setup.sh'

    if not aliases:
        try:
            existing_data = script_path.read_text(encoding='latin1')
        except FileNotFoundError:
            existing_data = ''

        aliases = []
        for m in re.finditer(r'alias (.*)=control-tmux', existing_data):
            aliases.append(m.group(1))

    if aliases:
        shell_data += ('\n' + ''.join(f'alias {alias}=control-tmux\n' for alias in aliases) + '\n')

    executables = set(aliases)
    executables.add('control-tmux')
    shell_data += argcomplete.shellcode(executables, True, 'bash', [], None)

    dest = script_path
    print(f'Installing setup script in {dest}, with aliases: {aliases}')
    dest.write_text(shell_data)
