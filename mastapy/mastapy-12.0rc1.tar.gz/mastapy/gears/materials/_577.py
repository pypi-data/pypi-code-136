"""_577.py

BevelGearAbstractMaterialDatabase
"""


from typing import Generic, TypeVar

from mastapy.materials import _264
from mastapy.gears.materials import _580
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ABSTRACT_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'BevelGearAbstractMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearAbstractMaterialDatabase',)


T = TypeVar('T', bound='_580.BevelGearMaterial')


class BevelGearAbstractMaterialDatabase(_264.MaterialDatabase['T'], Generic[T]):
    """BevelGearAbstractMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _BEVEL_GEAR_ABSTRACT_MATERIAL_DATABASE

    def __init__(self, instance_to_wrap: 'BevelGearAbstractMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
