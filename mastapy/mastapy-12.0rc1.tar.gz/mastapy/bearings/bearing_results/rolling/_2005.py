"""_2005.py

LoadedTaperRollerBearingRow
"""


from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2004, _1981
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedTaperRollerBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedTaperRollerBearingRow',)


class LoadedTaperRollerBearingRow(_1981.LoadedNonBarrelRollerBearingRow):
    """LoadedTaperRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_ROW

    def __init__(self, instance_to_wrap: 'LoadedTaperRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def major_rib_normal_contact_stress(self) -> 'Image':
        """Image: 'MajorRibNormalContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MajorRibNormalContactStress

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def loaded_bearing(self) -> '_2004.LoadedTaperRollerBearingResults':
        """LoadedTaperRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
