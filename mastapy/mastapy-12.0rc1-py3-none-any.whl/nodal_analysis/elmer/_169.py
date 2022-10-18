"""_169.py

ElmerResultType
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELMER_RESULT_TYPE = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer', 'ElmerResultType')


__docformat__ = 'restructuredtext en'
__all__ = ('ElmerResultType',)


class ElmerResultType(Enum):
    """ElmerResultType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELMER_RESULT_TYPE

    MAGNETIC_FLUX_DENSITY = 0
    MAGNETIC_VECTOR_POTENTIAL = 1
    CURRENT_DENSITY = 2
    NODAL_FORCE = 3
    TOTAL_CORE_LOSS = 4
    NODAL_CORE_LOSS = 5
    GEOMETRY_ID = 6
    HYSTERESIS_CORE_LOSS = 7
    EDDY_CURRENT_CORE_LOSS = 8
    EXCESS_CORE_LOSS = 9
    MAGNET_LOSS = 10
    MAGNET_EDDY_CURRENT_DENSITY = 11
    NONE = 12


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ElmerResultType.__setattr__ = __enum_setattr
ElmerResultType.__delattr__ = __enum_delattr
