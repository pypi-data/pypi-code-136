"""_463.py

CylindricalPlasticGearRatingSettingsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.gears.rating.cylindrical import _464
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalPlasticGearRatingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlasticGearRatingSettingsDatabase',)


class CylindricalPlasticGearRatingSettingsDatabase(_1791.NamedDatabase['_464.CylindricalPlasticGearRatingSettingsItem']):
    """CylindricalPlasticGearRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_DATABASE

    def __init__(self, instance_to_wrap: 'CylindricalPlasticGearRatingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
