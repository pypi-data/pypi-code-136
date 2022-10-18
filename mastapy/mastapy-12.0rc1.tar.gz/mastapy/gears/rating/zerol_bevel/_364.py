"""_364.py

ZerolBevelGearRating
"""


from mastapy.gears.gear_designs.zerol_bevel import _945
from mastapy._internal import constructor
from mastapy.gears.rating.bevel import _548
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.ZerolBevel', 'ZerolBevelGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearRating',)


class ZerolBevelGearRating(_548.BevelGearRating):
    """ZerolBevelGearRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_RATING

    def __init__(self, instance_to_wrap: 'ZerolBevelGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear(self) -> '_945.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'ZerolBevelGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
