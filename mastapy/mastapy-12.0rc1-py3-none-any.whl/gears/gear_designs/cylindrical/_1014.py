"""_1014.py

CylindricalGearMicroGeometrySettingsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.gears.gear_designs.cylindrical import _1015
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearMicroGeometrySettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometrySettingsDatabase',)


class CylindricalGearMicroGeometrySettingsDatabase(_1791.NamedDatabase['_1015.CylindricalGearMicroGeometrySettingsItem']):
    """CylindricalGearMicroGeometrySettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometrySettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
