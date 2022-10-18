"""_1926.py

BallBearingAnalysisMethod
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_BALL_BEARING_ANALYSIS_METHOD = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'BallBearingAnalysisMethod')


__docformat__ = 'restructuredtext en'
__all__ = ('BallBearingAnalysisMethod',)


class BallBearingAnalysisMethod(Enum):
    """BallBearingAnalysisMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BALL_BEARING_ANALYSIS_METHOD

    TWO_DEGREES_OF_FREEDOM = 0
    TWO_DEGREES_OF_FREEDOM_IN_SIX_DOF_FRAMEWORK = 1
    SIX_DEGREES_OF_FREEDOM_COULOMB = 2
    SIX_DEGREES_OF_FREEDOM_ADVANCED = 3


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


BallBearingAnalysisMethod.__setattr__ = __enum_setattr
BallBearingAnalysisMethod.__delattr__ = __enum_delattr
