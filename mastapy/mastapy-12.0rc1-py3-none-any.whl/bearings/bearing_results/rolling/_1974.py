"""_1974.py

LoadedFourPointContactBallBearingRow
"""


from typing import List

from mastapy.bearings.bearing_results.rolling import _1973, _1972, _1959
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedFourPointContactBallBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedFourPointContactBallBearingRow',)


class LoadedFourPointContactBallBearingRow(_1959.LoadedBallBearingRow):
    """LoadedFourPointContactBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ROW

    def __init__(self, instance_to_wrap: 'LoadedFourPointContactBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1973.LoadedFourPointContactBallBearingResults':
        """LoadedFourPointContactBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def race_results(self) -> 'List[_1972.LoadedFourPointContactBallBearingRaceResults]':
        """List[LoadedFourPointContactBallBearingRaceResults]: 'RaceResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
