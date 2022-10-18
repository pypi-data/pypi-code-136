"""_2648.py

BevelDifferentialGearSetSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2467
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6751
from mastapy.gears.rating.bevel import _549
from mastapy.gears.rating.zerol_bevel import _365
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.straight_bevel import _391
from mastapy.gears.rating.spiral_bevel import _398
from mastapy.system_model.analyses_and_results.power_flows import _3989
from mastapy.system_model.analyses_and_results.system_deflections import _2649, _2647, _2653
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BevelDifferentialGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetSystemDeflection',)


class BevelDifferentialGearSetSystemDeflection(_2653.BevelGearSetSystemDeflection):
    """BevelDifferentialGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2467.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6751.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_549.BevelGearSetRating':
        """BevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _549.BevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to BevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_zerol_bevel_gear_set_rating(self) -> '_365.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _365.ZerolBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ZerolBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_straight_bevel_gear_set_rating(self) -> '_391.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _391.StraightBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_spiral_bevel_gear_set_rating(self) -> '_398.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _398.SpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to SpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_549.BevelGearSetRating':
        """BevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _549.BevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to BevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_zerol_bevel_gear_set_rating(self) -> '_365.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _365.ZerolBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to ZerolBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_straight_bevel_gear_set_rating(self) -> '_391.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _391.StraightBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to StraightBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_spiral_bevel_gear_set_rating(self) -> '_398.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _398.SpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to SpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3989.BevelDifferentialGearSetPowerFlow':
        """BevelDifferentialGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_differential_gears_system_deflection(self) -> 'List[_2649.BevelDifferentialGearSystemDeflection]':
        """List[BevelDifferentialGearSystemDeflection]: 'BevelDifferentialGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_system_deflection(self) -> 'List[_2647.BevelDifferentialGearMeshSystemDeflection]':
        """List[BevelDifferentialGearMeshSystemDeflection]: 'BevelDifferentialMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
