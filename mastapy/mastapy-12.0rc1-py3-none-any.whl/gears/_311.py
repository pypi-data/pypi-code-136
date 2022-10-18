"""_311.py

BevelHypoidGearRatingSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS = python_net_import('SMT.MastaAPI.Gears', 'BevelHypoidGearRatingSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearRatingSettings',)


class BevelHypoidGearRatingSettings(_0.APIBase):
    """BevelHypoidGearRatingSettings

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS

    def __init__(self, instance_to_wrap: 'BevelHypoidGearRatingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
