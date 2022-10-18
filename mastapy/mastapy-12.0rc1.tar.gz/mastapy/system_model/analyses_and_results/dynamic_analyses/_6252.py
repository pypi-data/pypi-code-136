"""_6252.py

CylindricalGearDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2476, _2478
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6787, _6792
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6264
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'CylindricalGearDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDynamicAnalysis',)


class CylindricalGearDynamicAnalysis(_6264.GearDynamicAnalysis):
    """CylindricalGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'CylindricalGearDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2476.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2476.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6787.CylindricalGearLoadCase':
        """CylindricalGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        if _6787.CylindricalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to CylindricalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[CylindricalGearDynamicAnalysis]':
        """List[CylindricalGearDynamicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
