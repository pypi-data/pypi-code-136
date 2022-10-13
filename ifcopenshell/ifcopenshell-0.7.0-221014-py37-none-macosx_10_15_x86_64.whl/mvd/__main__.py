# IfcOpenShell - IFC toolkit and geometry engine
# Copyright (C) 2021 Thomas Krijnen <thomas@aecgeeks.com>
#
# This file is part of IfcOpenShell.
#
# IfcOpenShell is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IfcOpenShell is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with IfcOpenShell.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

if __name__ == "__main__":
    import sys
    from . import concept_root

    if len(sys.argv) == 2:
        mvdfn = sys.argv[1]
        for mvd in concept_root.parse(mvdfn):

            def dump(rule, parents):
                print(" " * len(parents), rule.tag, rule.attribute)

            for c in mvd.concepts():
                print(c.name)
                print()

                t = c.template()
                print("RootEntity", t.entity)
                t.traverse(dump, with_parents=True)
                print(" ".join(map(str, t.constraints)))

                print()

    elif len(sys.argv) == 3:
        from . import sparql

        ttlfn, mvdfn = sys.argv[1:]
        sparql.derive_prefix(ttlfn)
        ttlfn = sparql.infer_subtypes(ttlfn)
        for mvd in concept_root.parse(mvdfn):
            sparql.executor.run(mvd, mvdfn, ttlfn)

    else:
        print(sys.executable, "ifcopenshell.mvd", "<.mvdxml>")
        print(sys.executable, "ifcopenshell.mvd", "<.mvdxml>", "<.ifc>")
