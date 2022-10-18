"""_171.py

Data1D
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.elmer.results import _170
from mastapy._internal.python_net import python_net_import

_DATA_1D = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer.Results', 'Data1D')


__docformat__ = 'restructuredtext en'
__all__ = ('Data1D',)


class Data1D(_170.Data):
    """Data1D

    This is a mastapy class.
    """

    TYPE = _DATA_1D

    def __init__(self, instance_to_wrap: 'Data1D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data(self) -> 'List[float]':
        """List[float]: 'Data' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Data

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value
