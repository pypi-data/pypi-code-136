"""_1961.py

LoadedCrossedRollerBearingResults
"""


from mastapy.bearings.bearing_results.rolling import _1985
from mastapy._internal.python_net import python_net_import

_LOADED_CROSSED_ROLLER_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedCrossedRollerBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedCrossedRollerBearingResults',)


class LoadedCrossedRollerBearingResults(_1985.LoadedRollerBearingResults):
    """LoadedCrossedRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CROSSED_ROLLER_BEARING_RESULTS

    def __init__(self, instance_to_wrap: 'LoadedCrossedRollerBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
