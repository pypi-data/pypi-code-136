"""_710.py

CylindricalWormGrinderDatabase
"""


from mastapy.gears.manufacturing.cylindrical import _603
from mastapy.gears.manufacturing.cylindrical.cutters import _701
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_WORM_GRINDER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalWormGrinderDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalWormGrinderDatabase',)


class CylindricalWormGrinderDatabase(_603.CylindricalCutterDatabase['_701.CylindricalGearGrindingWorm']):
    """CylindricalWormGrinderDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_WORM_GRINDER_DATABASE

    def __init__(self, instance_to_wrap: 'CylindricalWormGrinderDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
