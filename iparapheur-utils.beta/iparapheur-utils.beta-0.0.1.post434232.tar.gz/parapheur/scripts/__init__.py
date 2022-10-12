#  i-Parapheur Utils
#  Copyright (C) 2017-2022 Libriciel-SCOP
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
from subprocess import check_call, CalledProcessError


def checkinstallation():
    import checkInstallationIP


def recuparchives():
    import recupArchives


def import_data():
    import import_data


def export_data():
    import export_data


def rename():
    import change_name


def remove_ldap():
    import remove_ldap


def pushdoc():
    import pushdoc


def ipclean():
    import ipclean


def ldapsearch():
    import ldapsearch


def count_files():
    import count_files


def reset_admin_password():
    import reset_admin_password


def patch():
    import patch


def recupfull():
    import recupfull


def template():
    import template


def orphan():
    import orphan


def properties_merger():
    args = sys.argv[1:]
    args.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/shell/properties-merger/properties-merger.sh")
    try:
        check_call(args)
    except CalledProcessError:
        pass
