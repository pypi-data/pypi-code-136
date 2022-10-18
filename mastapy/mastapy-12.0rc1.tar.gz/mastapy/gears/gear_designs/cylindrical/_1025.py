"""_1025.py

CylindricalGearSetMicroGeometrySettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearSetMicroGeometrySettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetMicroGeometrySettings',)


class CylindricalGearSetMicroGeometrySettings(_0.APIBase):
    """CylindricalGearSetMicroGeometrySettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_SETTINGS

    def __init__(self, instance_to_wrap: 'CylindricalGearSetMicroGeometrySettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
