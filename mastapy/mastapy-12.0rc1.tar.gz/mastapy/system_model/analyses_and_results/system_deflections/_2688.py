"""_2688.py

CylindricalGearSetSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2477, _2493
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6791, _6859
from mastapy.gears.rating.cylindrical import _458
from mastapy.gears.manufacturing.cylindrical import _614
from mastapy.system_model.analyses_and_results.power_flows import _4026, _4061
from mastapy.system_model.analyses_and_results.system_deflections import _2691, _2685, _2706
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetSystemDeflection',)


class CylindricalGearSetSystemDeflection(_2706.GearSetSystemDeflection):
    """CylindricalGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'CylindricalGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2477.CylindricalGearSet':
        """CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2477.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6791.CylindricalGearSetLoadCase':
        """CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        if _6791.CylindricalGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to CylindricalGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_458.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_458.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_analysis(self) -> '_614.CylindricalManufacturedGearSetLoadCase':
        """CylindricalManufacturedGearSetLoadCase: 'ManufacturingAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4026.CylindricalGearSetPowerFlow':
        """CylindricalGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4026.CylindricalGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CylindricalGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gears_system_deflection(self) -> 'List[_2691.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'CylindricalGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_system_deflection(self) -> 'List[_2685.CylindricalGearMeshSystemDeflection]':
        """List[CylindricalGearMeshSystemDeflection]: 'CylindricalMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
