# A component of the BASEmesh pre-processing toolkit.
# Copyright (C) 2020  ETH Zürich
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

"""Custom container and iterator definitions for BASEmesh."""

from typing import Any, Iterable, Iterator, Optional, Set
from .abc import SpatialCollection, SpatialT


class SpatialSet(SpatialCollection[SpatialT]):
    """A :class:`set` subclass supporting the SpatialCollection ABC.

    This behaves exactly like a normal set and is used as a temporary
    container until proper space-aware containers are added.

    Please note that this is a temporary solution that will not be
    satisfactory for large data sets.
    It can be considered "deprecated by design" and should be replaced
    with a proper spatial index.
    """

    def __init__(self, iterable: Optional[Iterable[SpatialT]] = None) -> None:
        self._data: Set[SpatialT] = set()
        if iterable is not None:
            self._data.update(iterable)

    def __contains__(self, element: Any) -> bool:
        """Return whether the element is contained.

        :param element: The element to check for
        :type element: Any
        :return: Whether the element is contained
        """
        return element in self._data

    def __iter__(self) -> Iterator[SpatialT]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def add(self, element: SpatialT) -> None:
        """Add the given element to the collection.

        :param element: The element to add
        :type element: Spatial
        """
        self._data.add(element)

    def clear(self) -> None:
        """Remove all items from the container."""
        self._data.clear()

    def discard(self, element: SpatialT) -> None:
        """Remove an item from the container.

        If the item cannot be found, do nothing.

        :param element: The element to remove
        :type element: Spatial
        """
        self._data.discard(element)

    def remove(self, element: SpatialT) -> None:
        """Remove an element from the container.

        If the element cannot be found, a KeyError will be raised.

        :param element: The element to remove
        :type element: Spatial
        :raises KeyError: If the element cannot be found
        """
        self._data.remove(element)

    def pop(self) -> SpatialT:
        """Remove and return any item from the container.

        :return: The removed item
        :rtype: Spatial
        :raises KeyError: If the container is empty
        """
        return self._data.pop()
