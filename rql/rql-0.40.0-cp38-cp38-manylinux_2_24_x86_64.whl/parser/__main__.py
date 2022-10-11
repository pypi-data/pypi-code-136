# copyright 2004-2021 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of rql.
#
# rql is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# rql is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with rql. If not, see <http://www.gnu.org/licenses/>.
"""Main parser command.

"""
import argparse
from argparse import RawDescriptionHelpFormatter
from typing import Dict, Any
from rql.parser import Hercule, HerculeScanner
from yapps.runtime import print_error

__docformat__: str = "restructuredtext en"


def main() -> None:
    arg_parser = argparse.ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description="Parse an RQL string, for example:\n $ python3 -m rql 'Any 1+1;'",
    )
    arg_parser.add_argument("rqlstring", help="the rql string that should be parsed")
    args = arg_parser.parse_args()

    rqlstring = args.rqlstring.strip()

    if not rqlstring.endswith(";"):
        rqlstring += ";"

    parser = Hercule(HerculeScanner(rqlstring))
    e_types: Dict[Any, Any] = {}

    try:
        tree = parser.goal(e_types)
        print("-" * 80)
        print(tree)
        print("-" * 80)
        print(repr(tree))
        print(e_types)
    except SyntaxError as ex:
        print_error(ex, parser._scanner)


main()
