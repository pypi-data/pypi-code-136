"""_5729.py

ResponseCacheLevel
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_RESPONSE_CACHE_LEVEL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ResponseCacheLevel')


__docformat__ = 'restructuredtext en'
__all__ = ('ResponseCacheLevel',)


class ResponseCacheLevel(Enum):
    """ResponseCacheLevel

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RESPONSE_CACHE_LEVEL

    FASTEST_CALCULATION = 0
    MEDIUM = 1
    LOWEST_MEMORY = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ResponseCacheLevel.__setattr__ = __enum_setattr
ResponseCacheLevel.__delattr__ = __enum_delattr
