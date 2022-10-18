"""_2007.py

LoadedThreePointContactBallBearingResults
"""


from mastapy.bearings.bearing_results.rolling import _1958
from mastapy._internal.python_net import python_net_import

_LOADED_THREE_POINT_CONTACT_BALL_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedThreePointContactBallBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedThreePointContactBallBearingResults',)


class LoadedThreePointContactBallBearingResults(_1958.LoadedBallBearingResults):
    """LoadedThreePointContactBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_THREE_POINT_CONTACT_BALL_BEARING_RESULTS

    def __init__(self, instance_to_wrap: 'LoadedThreePointContactBallBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
