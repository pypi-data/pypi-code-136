"""_1428.py

RingPinsMaterialDatabase
"""


from mastapy.materials import _264
from mastapy.cycloidal import _1427
from mastapy._internal.python_net import python_net_import

_RING_PINS_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Cycloidal', 'RingPinsMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsMaterialDatabase',)


class RingPinsMaterialDatabase(_264.MaterialDatabase['_1427.RingPinsMaterial']):
    """RingPinsMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MATERIAL_DATABASE

    def __init__(self, instance_to_wrap: 'RingPinsMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
