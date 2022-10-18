"""_2540.py

PartToPartShearCouplingHalf
"""


from mastapy.system_model.part_model.couplings import _2535
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCouplingHalf')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalf',)


class PartToPartShearCouplingHalf(_2535.CouplingHalf):
    """PartToPartShearCouplingHalf

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalf.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
