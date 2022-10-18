"""_1239.py

CADToothAndSlot
"""


from mastapy.electric_machines import _1234
from mastapy._internal.python_net import python_net_import

_CAD_TOOTH_AND_SLOT = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADToothAndSlot')


__docformat__ = 'restructuredtext en'
__all__ = ('CADToothAndSlot',)


class CADToothAndSlot(_1234.AbstractToothAndSlot):
    """CADToothAndSlot

    This is a mastapy class.
    """

    TYPE = _CAD_TOOTH_AND_SLOT

    def __init__(self, instance_to_wrap: 'CADToothAndSlot.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
