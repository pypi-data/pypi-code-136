"""_4336.py

PartToPartShearCouplingConnectionParametricStudyTool
"""


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2300
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6855
from mastapy.system_model.analyses_and_results.system_deflections import _2732
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4275
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'PartToPartShearCouplingConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingConnectionParametricStudyTool',)


class PartToPartShearCouplingConnectionParametricStudyTool(_4275.CouplingConnectionParametricStudyTool):
    """PartToPartShearCouplingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2300.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6855.PartToPartShearCouplingConnectionLoadCase':
        """PartToPartShearCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2732.PartToPartShearCouplingConnectionSystemDeflection]':
        """List[PartToPartShearCouplingConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
