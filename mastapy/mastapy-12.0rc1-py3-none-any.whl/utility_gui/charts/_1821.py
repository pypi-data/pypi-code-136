"""_1821.py

PointsForSurface
"""


from typing import List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_POINTS_FOR_SURFACE = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'PointsForSurface')


__docformat__ = 'restructuredtext en'
__all__ = ('PointsForSurface',)


class PointsForSurface(_0.APIBase):
    """PointsForSurface

    This is a mastapy class.
    """

    TYPE = _POINTS_FOR_SURFACE

    def __init__(self, instance_to_wrap: 'PointsForSurface.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def points(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'Points' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Points

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
