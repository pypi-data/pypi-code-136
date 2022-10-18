"""_170.py

Data
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DATA = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer.Results', 'Data')


__docformat__ = 'restructuredtext en'
__all__ = ('Data',)


class Data(_0.APIBase):
    """Data

    This is a mastapy class.
    """

    TYPE = _DATA

    def __init__(self, instance_to_wrap: 'Data.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def quantity_name(self) -> 'str':
        """str: 'QuantityName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QuantityName

        if temp is None:
            return ''

        return temp
