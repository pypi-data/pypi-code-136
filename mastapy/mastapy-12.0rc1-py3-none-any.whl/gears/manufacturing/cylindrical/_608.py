"""_608.py

CylindricalHobDatabase
"""


from mastapy.gears.manufacturing.cylindrical import _603
from mastapy.gears.manufacturing.cylindrical.cutters import _702
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_HOB_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalHobDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalHobDatabase',)


class CylindricalHobDatabase(_603.CylindricalCutterDatabase['_702.CylindricalGearHobDesign']):
    """CylindricalHobDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_HOB_DATABASE

    def __init__(self, instance_to_wrap: 'CylindricalHobDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
