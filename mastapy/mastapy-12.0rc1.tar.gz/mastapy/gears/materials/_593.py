"""_593.py

KlingelnbergConicalGearMaterialDatabase
"""


from mastapy.gears.materials import _588, _594
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'KlingelnbergConicalGearMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergConicalGearMaterialDatabase',)


class KlingelnbergConicalGearMaterialDatabase(_588.GearMaterialDatabase['_594.KlingelnbergCycloPalloidConicalGearMaterial']):
    """KlingelnbergConicalGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE

    def __init__(self, instance_to_wrap: 'KlingelnbergConicalGearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
