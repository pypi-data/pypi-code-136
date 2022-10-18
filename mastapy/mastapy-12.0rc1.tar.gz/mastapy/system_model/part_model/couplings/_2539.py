"""_2539.py

PartToPartShearCoupling
"""


from mastapy.system_model.connections_and_sockets.couplings import _2300
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2534
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCoupling')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCoupling',)


class PartToPartShearCoupling(_2534.Coupling):
    """PartToPartShearCoupling

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING

    def __init__(self, instance_to_wrap: 'PartToPartShearCoupling.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part_to_part_shear_coupling_connection(self) -> '_2300.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'PartToPartShearCouplingConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplingConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
