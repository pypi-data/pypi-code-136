"""_935.py

BevelHypoidGearRatingSettingsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.gears.gear_designs import _936
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'BevelHypoidGearRatingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearRatingSettingsDatabase',)


class BevelHypoidGearRatingSettingsDatabase(_1791.NamedDatabase['_936.BevelHypoidGearRatingSettingsItem']):
    """BevelHypoidGearRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS_DATABASE

    def __init__(self, instance_to_wrap: 'BevelHypoidGearRatingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
