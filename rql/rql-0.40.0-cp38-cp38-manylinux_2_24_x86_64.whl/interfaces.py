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
"""Interfaces used by the RQL package.

"""

from typing import Protocol, Any, Optional

__docformat__: str = "restructuredtext en"


class ISchema(Protocol):
    """RQL expects some base types to exists: String, Float, Int, Boolean, Date
    and a base relation : is
    """

    def has_entity(self, etype: Any):
        """Return true if the given type is defined in the schema."""

    def has_relation(self, rtype):
        """Return true if the given relation's type is defined in the schema."""

    def entities(self, schema: Optional[Any] = None):
        """Return the list of possible types.

        If schema is not None, return a list of schemas instead of types.
        """

    def relations(self, schema: Optional[Any] = None):
        """Return the list of possible relations.

        If schema is not None, return a list of schemas instead of relation's
        types.
        """

    def relation_schema(self, rtype: Any):
        """Return the relation schema for the given relation type."""

    def __contains__(self, ertype: Any):
        """Return if schema has ertype as a relation or as en entity."""

    # "ISchema" has no attribute "rschema"  [attr-defined]
    def rschema(self, rtype: Any):
        ...

    # "ISchema" has no attribute "eschema"  [attr-defined]
    def eschema(self, etype: Any):
        ...


class IRelationSchema(Protocol):
    """Interface for Relation schema (a relation is a named oriented link
    between two entities).
    """

    def associations(self):
        """Return a list of (fromtype, [totypes]) defining between which types
        this relation may exists.
        """

    def subjects(self):
        """Return a list of types which can be subject of this relation."""

    def objects(self):
        """Return a list of types which can be object of this relation."""


class IEntitySchema(Protocol):
    """Interface for Entity schema."""

    def is_final(self):
        """Return true if the entity is a final entity (ie cannot be used
        as subject of a relation).
        """
