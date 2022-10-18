"""_933.py

BevelHypoidGearDesignSettingsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.gears.gear_designs import _934
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_DESIGN_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'BevelHypoidGearDesignSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearDesignSettingsDatabase',)


class BevelHypoidGearDesignSettingsDatabase(_1791.NamedDatabase['_934.BevelHypoidGearDesignSettingsItem']):
    """BevelHypoidGearDesignSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_DESIGN_SETTINGS_DATABASE

    def __init__(self, instance_to_wrap: 'BevelHypoidGearDesignSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
