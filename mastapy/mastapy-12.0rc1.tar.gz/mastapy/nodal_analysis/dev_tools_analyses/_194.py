"""_194.py

ModelSplittingMethod
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_MODEL_SPLITTING_METHOD = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'ModelSplittingMethod')


__docformat__ = 'restructuredtext en'
__all__ = ('ModelSplittingMethod',)


class ModelSplittingMethod(Enum):
    """ModelSplittingMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MODEL_SPLITTING_METHOD

    NONE = 0
    ELEMENT_PROPERTY_ID = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ModelSplittingMethod.__setattr__ = __enum_setattr
ModelSplittingMethod.__delattr__ = __enum_delattr
