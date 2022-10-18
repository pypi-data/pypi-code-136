"""_4017.py

CVTPowerFlow
"""


from mastapy.system_model.part_model.couplings import _2537
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _3986
from mastapy._internal.python_net import python_net_import

_CVT_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CVTPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPowerFlow',)


class CVTPowerFlow(_3986.BeltDrivePowerFlow):
    """CVTPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_POWER_FLOW

    def __init__(self, instance_to_wrap: 'CVTPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2537.CVT':
        """CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
