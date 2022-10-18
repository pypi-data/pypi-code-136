"""_1265.py

MagnetMaterialDatabase
"""


from mastapy.materials import _264
from mastapy.electric_machines import _1264
from mastapy._internal.python_net import python_net_import

_MAGNET_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'MagnetMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetMaterialDatabase',)


class MagnetMaterialDatabase(_264.MaterialDatabase['_1264.MagnetMaterial']):
    """MagnetMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _MAGNET_MATERIAL_DATABASE

    def __init__(self, instance_to_wrap: 'MagnetMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
