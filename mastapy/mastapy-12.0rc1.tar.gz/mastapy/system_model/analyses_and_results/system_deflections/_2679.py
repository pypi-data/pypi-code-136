"""_2679.py

CVTPulleySystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2538
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4018
from mastapy.math_utility.measured_vectors import _1526
from mastapy.system_model.analyses_and_results.system_deflections import _2739
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CVTPulleySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleySystemDeflection',)


class CVTPulleySystemDeflection(_2739.PulleySystemDeflection):
    """CVTPulleySystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'CVTPulleySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2538.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4018.CVTPulleyPowerFlow':
        """CVTPulleyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fixed_sheave_contact_results(self) -> 'List[_1526.NodeResults]':
        """List[NodeResults]: 'FixedSheaveContactResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FixedSheaveContactResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def moving_sheave_contact_results(self) -> 'List[_1526.NodeResults]':
        """List[NodeResults]: 'MovingSheaveContactResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MovingSheaveContactResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
