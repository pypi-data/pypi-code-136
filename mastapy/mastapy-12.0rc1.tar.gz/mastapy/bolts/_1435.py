"""_1435.py

BoltMaterialDatabase
"""


from mastapy.bolts import _1431, _1434
from mastapy._internal.python_net import python_net_import

_BOLT_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Bolts', 'BoltMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltMaterialDatabase',)


class BoltMaterialDatabase(_1431.BoltedJointMaterialDatabase['_1434.BoltMaterial']):
    """BoltMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BOLT_MATERIAL_DATABASE

    def __init__(self, instance_to_wrap: 'BoltMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
