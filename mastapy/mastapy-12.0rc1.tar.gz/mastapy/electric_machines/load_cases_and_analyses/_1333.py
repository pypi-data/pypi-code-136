"""_1333.py

MotoringOrGenerating
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_MOTORING_OR_GENERATING = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'MotoringOrGenerating')


__docformat__ = 'restructuredtext en'
__all__ = ('MotoringOrGenerating',)


class MotoringOrGenerating(Enum):
    """MotoringOrGenerating

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MOTORING_OR_GENERATING

    MOTORING = 0
    GENERATING = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


MotoringOrGenerating.__setattr__ = __enum_setattr
MotoringOrGenerating.__delattr__ = __enum_delattr
