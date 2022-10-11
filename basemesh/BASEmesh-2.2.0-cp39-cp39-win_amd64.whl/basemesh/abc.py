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

"""Abstract base class definitions for BASEmesh."""

# pylint: disable=too-few-public-methods

from abc import ABCMeta, abstractmethod
from typing import Iterator, Collection, Generic, TypeVar
from .types import Point2D

SpatialT = TypeVar('SpatialT', bound='Spatial')


class ElevationSource(metaclass=ABCMeta):
    """Interface for classes that can be used for mesh interpolation.

    The function interface for :meth:`elevation_at` is fixed and may
    not be modified. If additional parameters such as error tolerance
    are needed, set them elsewhere and generate the
    :meth:`elevation_at` method via :func:`functools.partial` to avoid
    attribute access for each interpolated point. See the following
    example:

    .. code-block:: python3

        def _interpolate(self, point: Point2D, tol: float) -> float:
            # Custom interpolation function with error tolerance
            ...

        def set_error_tolerance(self, tolerance: float) -> None:
            if self._error_tolerance != tolerance:
                # Update elevation function for new error tolerance
                self.elevation_at = functools.partial(
                    self._interpolate, tolerance=tolerance)
                self._error_tolerance = tolerance

        def elevation_at(self, point: Point2D) -> float:
            # Default implementation, to be overridden by
            # set_error_tolerance() call
            raise NotImplementedError(
                f'{self.__class__.__name__}.set_error_tolerance() '
                'must be called prior to interpolation')

    """

    @abstractmethod
    def elevation_at(self, point: Point2D) -> float:
        """Return the surface elevation at the given point.

        If the point lies outside the intended area of this elevation
        source, a :class:`ValueError` should be raised instead. The
        interpolator may then fall through to the next elevation source
        and attempt to use its elevation data instead.

        :param point: The point to query the elevation of
        :type point: :class:`tuple` [:class:`float`, :class:`float`]
        :return: The elevation at the given point
        :rtype: :class:`float`
        :raises ValueError: If the given point is outside the valid
            area of the elevation source
        """


class Spatial(metaclass=ABCMeta):
    """Marker interface for spatial data.

    The :attr:`Spatial.spatial_marker` attribute of a :class:`Spatial`
    object is used by the :class:`SpatialCollection` interface to
    determine the sample point of a given object. For point features,
    this may  simply be its location. For lines or elements, it can be
    an arbitrary 2D point that is representative of the object, e.g.
    its centroid.
    """

    @property
    @abstractmethod
    def spatial_marker(self) -> Point2D:
        """Return a 2D point representing this object.

        This point will be used by space-aware containers to optimise
        memory layout.

        :type: :class:`tuple` [:class:`float`, :class:`float`]
        """


class SpatialCollection(Generic[SpatialT], Collection[SpatialT], metaclass=ABCMeta):
    """Represents a spatial container type.

    In addition to the standard collection interface (``__contains__``,
    ``__iter__``, ``__next__``, and ``__len__``), this class provides
    the :meth:`iter_spatial` method for iterating over its contents
    with a predefined starting point.

    There is no guarantee that :meth:`iter_spatial` will return nearby
    elements first, only a vague promise to prioritize nearby elements.

    :meth:`iter_spatial` will fall back to the default iterator if not
    overridden by a subclass.
    """

    def iter_spatial(self, point: Point2D) -> Iterator[SpatialT]:
        """Iterate over the contents, starting near the seed point.

        The order of the elements returned by this iterator should be
        treated as arbitrary and depends on the sample point.

        :param point: The point to start the iteration from
        :type point: :class:`tuple` [:class:`float`, :class:`float`]
        :return: An iterator over the contents of the collection
        :rtype: :class:`collections.abc.Iterator` [T]
        """
        _ = point
        return iter(self)
