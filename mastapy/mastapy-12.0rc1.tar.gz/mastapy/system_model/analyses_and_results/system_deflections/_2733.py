"""_2733.py

PartToPartShearCouplingHalfSystemDeflection
"""


from mastapy.system_model.part_model.couplings import _2540
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6856
from mastapy.system_model.analyses_and_results.power_flows import _4058
from mastapy.system_model.analyses_and_results.system_deflections import _2676
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'PartToPartShearCouplingHalfSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfSystemDeflection',)


class PartToPartShearCouplingHalfSystemDeflection(_2676.CouplingHalfSystemDeflection):
    """PartToPartShearCouplingHalfSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2540.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6856.PartToPartShearCouplingHalfLoadCase':
        """PartToPartShearCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4058.PartToPartShearCouplingHalfPowerFlow':
        """PartToPartShearCouplingHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
