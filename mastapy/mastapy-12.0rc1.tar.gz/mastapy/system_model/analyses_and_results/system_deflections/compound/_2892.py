"""_2892.py

RootAssemblyCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.analyses_and_results.system_deflections.compound import _2849, _2804
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4203
from mastapy.system_model.analyses_and_results.system_deflections import _2746
from mastapy.system_model.fe import _2358
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1091
from mastapy.utility_gui.charts import _1827
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'RootAssemblyCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundSystemDeflection',)


class RootAssemblyCompoundSystemDeflection(_2804.AssemblyCompoundSystemDeflection):
    """RootAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_efficiency_results(self) -> '_2849.DutyCycleEfficiencyResults':
        """DutyCycleEfficiencyResults: 'DutyCycleEfficiencyResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleEfficiencyResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_assembly_compound_power_flow(self) -> '_4203.RootAssemblyCompoundPowerFlow':
        """RootAssemblyCompoundPowerFlow: 'RootAssemblyCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootAssemblyCompoundPowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2746.RootAssemblySystemDeflection]':
        """List[RootAssemblySystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bearing_race_f_es(self) -> 'List[_2358.RaceBearingFESystemDeflection]':
        """List[RaceBearingFESystemDeflection]: 'BearingRaceFEs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingRaceFEs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2746.RootAssemblySystemDeflection]':
        """List[RootAssemblySystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def peak_to_peak_transmission_error_chart(self, mesh_duty_cycles: 'List[_1091.CylindricalGearMeshMicroGeometryDutyCycle]', header: 'str', x_axis_title: 'str', y_axis_title: 'str') -> '_1827.TwoDChartDefinition':
        """ 'PeakToPeakTransmissionErrorChart' is the original name of this method.

        Args:
            mesh_duty_cycles (List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMeshMicroGeometryDutyCycle])
            header (str)
            x_axis_title (str)
            y_axis_title (str)

        Returns:
            mastapy.utility_gui.charts.TwoDChartDefinition
        """

        mesh_duty_cycles = conversion.mp_to_pn_objects_in_list(mesh_duty_cycles)
        header = str(header)
        x_axis_title = str(x_axis_title)
        y_axis_title = str(y_axis_title)
        method_result = self.wrapped.PeakToPeakTransmissionErrorChart(mesh_duty_cycles, header if header else '', x_axis_title if x_axis_title else '', y_axis_title if y_axis_title else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
