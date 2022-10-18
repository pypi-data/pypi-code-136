"""_1096.py

CylindricalGearMicroGeometryPerTooth
"""


from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_PER_TOOTH = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMicroGeometryPerTooth')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometryPerTooth',)


class CylindricalGearMicroGeometryPerTooth(_1093.CylindricalGearMicroGeometryBase):
    """CylindricalGearMicroGeometryPerTooth

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_PER_TOOTH

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometryPerTooth.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
