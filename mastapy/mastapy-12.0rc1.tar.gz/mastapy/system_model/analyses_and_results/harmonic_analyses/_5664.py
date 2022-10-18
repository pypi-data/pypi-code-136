"""_5664.py

CylindricalGearMeshHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7246
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.gears import _2261
from mastapy.system_model.analyses_and_results.static_loads import _6789
from mastapy.system_model.analyses_and_results.system_deflections import _2685, _2686, _2687
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5689
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'CylindricalGearMeshHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshHarmonicAnalysis',)


class CylindricalGearMeshHarmonicAnalysis(_5689.GearMeshHarmonicAnalysis):
    """CylindricalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_system_deflection_results(self) -> '_7246.CylindricalGearMeshAdvancedSystemDeflection':
        """CylindricalGearMeshAdvancedSystemDeflection: 'AdvancedSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedSystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2261.CylindricalGearMesh':
        """CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6789.CylindricalGearMeshLoadCase':
        """CylindricalGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2685.CylindricalGearMeshSystemDeflection':
        """CylindricalGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2685.CylindricalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_mesh_system_deflection_timestep(self) -> '_2686.CylindricalGearMeshSystemDeflectionTimestep':
        """CylindricalGearMeshSystemDeflectionTimestep: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2686.CylindricalGearMeshSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearMeshSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_mesh_system_deflection_with_ltca_results(self) -> '_2687.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        """CylindricalGearMeshSystemDeflectionWithLTCAResults: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2687.CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearMeshSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[CylindricalGearMeshHarmonicAnalysis]':
        """List[CylindricalGearMeshHarmonicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
