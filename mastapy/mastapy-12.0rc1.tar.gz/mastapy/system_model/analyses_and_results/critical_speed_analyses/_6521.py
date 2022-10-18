"""_6521.py

CylindricalGearSetCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2477, _2493
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6791, _6859
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6519, _6520, _6532
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CylindricalGearSetCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetCriticalSpeedAnalysis',)


class CylindricalGearSetCriticalSpeedAnalysis(_6532.GearSetCriticalSpeedAnalysis):
    """CylindricalGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'CylindricalGearSetCriticalSpeedAnalysis.TYPE'):
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
    def cylindrical_gears_critical_speed_analysis(self) -> 'List[_6519.CylindricalGearCriticalSpeedAnalysis]':
        """List[CylindricalGearCriticalSpeedAnalysis]: 'CylindricalGearsCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_critical_speed_analysis(self) -> 'List[_6520.CylindricalGearMeshCriticalSpeedAnalysis]':
        """List[CylindricalGearMeshCriticalSpeedAnalysis]: 'CylindricalMeshesCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
