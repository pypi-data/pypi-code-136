"""_1116.py

ParabolicCylindricalGearTriangularEndModification
"""


from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1121
from mastapy._internal.python_net import python_net_import

_PARABOLIC_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'ParabolicCylindricalGearTriangularEndModification')


__docformat__ = 'restructuredtext en'
__all__ = ('ParabolicCylindricalGearTriangularEndModification',)


class ParabolicCylindricalGearTriangularEndModification(_1121.SingleCylindricalGearTriangularEndModification):
    """ParabolicCylindricalGearTriangularEndModification

    This is a mastapy class.
    """

    TYPE = _PARABOLIC_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION

    def __init__(self, instance_to_wrap: 'ParabolicCylindricalGearTriangularEndModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
