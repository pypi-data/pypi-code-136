"""_7311.py

StraightBevelPlanetGearAdvancedSystemDeflection
"""


from mastapy.system_model.part_model.gears import _2500
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'StraightBevelPlanetGearAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelPlanetGearAdvancedSystemDeflection',)


class StraightBevelPlanetGearAdvancedSystemDeflection(_7305.StraightBevelDiffGearAdvancedSystemDeflection):
    """StraightBevelPlanetGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'StraightBevelPlanetGearAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2500.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
