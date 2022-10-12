# SPDX-FileCopyrightText: 2021-2 Galagic Limited, et. al. <https://galagic.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# figular generates visualisations from flexible, reusable parts
#
# For full copyright information see the AUTHORS file at the top-level
# directory of this distribution or at
# [AUTHORS](https://gitlab.com/thegalagic/figular/AUTHORS.md)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import subprocess
import sys
from figular.models import Message, Style


def usage():
    usage = '''
fig is short for figular which generates visualisations from reusable
parts.

Usage:
  fig [flags] FIGURE DATA [style]

Specify a FIGURE by name (list below) OR provide the path to your own Asymptote
source code file to which the Figular figures will be available as imports.

The form of the DATA argument depends on the figure. The optional style
argument should contain a JSON document with style settings. See the
examples below and refer to the online documentation for more information at
https://gitlab.com/thegalagic/figular/-/blob/main/docs/Figular.md

Available figures:
  concept/circle     A circle of text blobs with (optionally) one in the
                     centre. It can be rotated and the font changed. It takes
                     data in the form of one blobs separated by newlines.
  org/orgchart       An organisational chart depicting the structure of an
                     organisation and the relationships of its positions or
                     roles. It takes data in the form:
                     "Name|Description|Parent"

Flags:
  --help             Help for Figular

Examples:
  fig concept/circle $'Hello\\nThere\\nYou'
  fig concept/circle $'Hello\\nThere\\nRotated' \\
    '{ "figure_concept_circle": { "rotation": 30 }}'
  fig org/orgchart $'Boss|CEO|\\nEmployee|Team Lead|Boss'
  fig myfile.asy'''
    print(usage)
    exit(0)


def main(args=None):
    """ Marshall the args and run the figure """
    if args is None:
        args = sys.argv[1:]
    if len(args) == 0:
        exit(0)
    if args[0] == "--help":
        usage()

    cmd = ['asy',
           '-safe', '-noView', '-noglobalread',
           '-f', 'svg', '-tex', 'xelatex',
           '-o', 'out.svg']
    runcmd = ""
    runcmdprefix = ""
    sourcefile = args.pop(0)
    figurefile = os.path.join(os.path.dirname(__file__), f"{sourcefile}.asy")

    if os.path.exists(sourcefile):
        finalfile = sourcefile
        # We must create a dom/import the style types as first thing
        # so available for users' custom figures and for any style
        # arg provided.
        runcmdprefix = 'import "figular/styledom" as istyledom; '
    elif os.path.exists(figurefile):
        finalfile = figurefile
    else:
        print(f"fig: argument {sourcefile} was neither a figure nor a file!")
        exit(1)

    cmd.extend(['-autoimport', finalfile])
    runcmd = 'run(currentpicture, input(comment=""));'

    input = None
    data = None
    style = None

    for arg in args:
        if not data:
            data = arg
            input = data
        else:
            style = Style.parse_raw(arg)
            msg = Message(data=data, style=style)
            runcmd = msg.getasy() + runcmd
            break
    if data and not style:
        Message(data=data)

    if runcmd:
        cmd.extend(['-c', runcmdprefix + runcmd])

    # Add the right dir to environ for Asymptote to find our figures
    os.environ["ASYMPTOTE_DIR"] = os.path.join(os.path.dirname(__file__))
    return subprocess.run(cmd, input=input, text=True).returncode
