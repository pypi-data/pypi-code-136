#!/usr/bin/env python3
# encoding: utf-8
#
# ** header v3.0
# This file is a part of the CaosDB Project.
#
# Copyright (C) 2021 Indiscale GmbH <info@indiscale.com>
# Copyright (C) 2021 Henrik tom Wörden <h.tomwoerden@indiscale.com>
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
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ** end header
#

"""
stores identified records and is able to detect duplicates
"""

import caosdb as db

from hashlib import sha256


def _create_hashable_string(identifiable: db.Record):
    """
    creates a string from the attributes of an identifiable that can be hashed
    """
    if identifiable.role == "File":
        # Special treatment for files:
        return "P<>N<>{}:{}".format("path", identifiable.path)
    if len(identifiable.parents) != 1:
        # TODO: extend this
        # maybe something like this:
        # parent_names = ",".join(
        #   sorted([p.name for p in identifiable.parents])
        raise RuntimeError("Cache entry can only be generated for entities with 1 parent.")
    rec_string = "P<{}>N<{}>".format(identifiable.parents[0].name, identifiable.name)
    for pname in sorted([p.name for p in identifiable.properties]):
        value = str(identifiable.get_property(pname).value)

        # TODO: (for review)
        #       This expansion of the hash function was introduced recently
        #       to allow the special case of Files as values of properties.
        #       We need to review the completeness of all the cases here, as the cache
        #       is crucial for correct identification of insertion and updates.
        if isinstance(identifiable.get_property(pname).value, db.File):
            value = str(identifiable.get_property(pname).value.path)
        elif isinstance(identifiable.get_property(pname).value, db.Entity):
            value = str(identifiable.get_property(pname).value.id)
        elif isinstance(identifiable.get_property(pname).value, list):
            tmplist = []
            for val in identifiable.get_property(pname).value:
                if isinstance(val, db.Entity):
                    tmplist.append(val.id)
                else:
                    tmplist.append(val)
            value = str(tmplist)

        rec_string += "{}:".format(pname) + value
    return rec_string


def _create_hash(identifiable: db.Record) -> str:
    return sha256(_create_hashable_string(identifiable).encode('utf-8')).hexdigest()


class IdentifiedCache(object):
    def __init__(self):
        self._cache = {}

    def __contains__(self, identifiable: db.Record):
        return _create_hash(identifiable) in self._cache

    def __getitem__(self, identifiable: db.Record):
        return self._cache[_create_hash(identifiable)]

    def add(self, record: db.Record, identifiable: db.Record):
        self._cache[_create_hash(identifiable)] = record
