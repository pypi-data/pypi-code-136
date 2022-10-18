"""_1823.py

Series2D
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_SERIES_2D = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'Series2D')


__docformat__ = 'restructuredtext en'
__all__ = ('Series2D',)


class Series2D(_0.APIBase):
    """Series2D

    This is a mastapy class.
    """

    TYPE = _SERIES_2D

    def __init__(self, instance_to_wrap: 'Series2D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def points(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'Points' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Points

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
