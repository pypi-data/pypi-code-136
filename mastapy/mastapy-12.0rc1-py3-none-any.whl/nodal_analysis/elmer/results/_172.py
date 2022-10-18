"""_172.py

Data3D
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.elmer.results import _170
from mastapy._internal.python_net import python_net_import

_DATA_3D = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer.Results', 'Data3D')


__docformat__ = 'restructuredtext en'
__all__ = ('Data3D',)


class Data3D(_170.Data):
    """Data3D

    This is a mastapy class.
    """

    TYPE = _DATA_3D

    def __init__(self, instance_to_wrap: 'Data3D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_data(self) -> 'List[float]':
        """List[float]: 'XData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def y_data(self) -> 'List[float]':
        """List[float]: 'YData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def z_data(self) -> 'List[float]':
        """List[float]: 'ZData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value
