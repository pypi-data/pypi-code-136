"""_588.py

GearMaterialDatabase
"""


from typing import Generic, TypeVar

from mastapy.utility.databases import _1791
from mastapy.gears.materials import _587
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'GearMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMaterialDatabase',)


T = TypeVar('T', bound='_587.GearMaterial')


class GearMaterialDatabase(_1791.NamedDatabase['T'], Generic[T]):
    """GearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GEAR_MATERIAL_DATABASE

    def __init__(self, instance_to_wrap: 'GearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
