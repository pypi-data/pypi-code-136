"""_2156.py

MastaSettings
"""


from mastapy.bearings.bearing_results.rolling import _1935
from mastapy._internal import constructor
from mastapy.bearings import (
    _1840, _1841, _1854, _1860
)
from mastapy.bolts import _1433, _1435, _1440
from mastapy.cycloidal import _1422, _1428
from mastapy.electric_machines import _1265, _1282, _1292
from mastapy.gears import _310, _311, _337
from mastapy.gears.gear_designs import (
    _933, _935, _938, _944
)
from mastapy.gears.gear_designs.cylindrical import (
    _1004, _1008, _1009, _1014,
    _1025
)
from mastapy.gears.gear_set_pareto_optimiser import (
    _913, _914, _917, _918,
    _920, _921, _923, _924,
    _926, _927, _928, _929
)
from mastapy.gears.ltca.cylindrical import _848
from mastapy.gears.manufacturing.bevel import _793
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _698, _704, _709, _710
)
from mastapy.gears.manufacturing.cylindrical import _608, _619
from mastapy.gears.materials import (
    _579, _581, _582, _583,
    _586, _589, _592, _593,
    _600
)
from mastapy.gears.rating.cylindrical import (
    _446, _447, _462, _463
)
from mastapy.materials import (
    _240, _243, _262, _265,
    _266
)
from mastapy.nodal_analysis import _48, _49, _68
from mastapy.nodal_analysis.geometry_modeller_link import _159
from mastapy.shafts import _25, _38, _39
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6510
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5695
from mastapy.system_model.analyses_and_results.mbd_analyses import _5397
from mastapy.system_model.analyses_and_results.modal_analyses import _4596
from mastapy.system_model.analyses_and_results.power_flows import _4065, _4023
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.stability_analyses import _3815
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3036
from mastapy.system_model.analyses_and_results.system_deflections import _2772
from mastapy.system_model.drawing import _2203
from mastapy.system_model.optimization import _2183, _2192
from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2515
from mastapy.system_model.part_model import _2422
from mastapy.utility.cad_export import _1795
from mastapy.utility.databases import _1790
from mastapy.utility import _1561, _1562
from mastapy.utility.scripting import _1704
from mastapy.utility.units_and_measurements import _1571
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_MASTA_SETTINGS = python_net_import('SMT.MastaAPI.SystemModel', 'MastaSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MastaSettings',)


class MastaSettings(_0.APIBase):
    """MastaSettings

    This is a mastapy class.
    """

    TYPE = _MASTA_SETTINGS

    def __init__(self, instance_to_wrap: 'MastaSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def iso14179_settings_database(self) -> '_1935.ISO14179SettingsDatabase':
        """ISO14179SettingsDatabase: 'ISO14179SettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179SettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_settings(self) -> '_1840.BearingSettings':
        """BearingSettings: 'BearingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_settings_database(self) -> '_1841.BearingSettingsDatabase':
        """BearingSettingsDatabase: 'BearingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rolling_bearing_database(self) -> '_1854.RollingBearingDatabase':
        """RollingBearingDatabase: 'RollingBearingDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingBearingDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def skf_settings(self) -> '_1860.SKFSettings':
        """SKFSettings: 'SKFSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bolt_geometry_database(self) -> '_1433.BoltGeometryDatabase':
        """BoltGeometryDatabase: 'BoltGeometryDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltGeometryDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bolt_material_database(self) -> '_1435.BoltMaterialDatabase':
        """BoltMaterialDatabase: 'BoltMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clamped_section_material_database(self) -> '_1440.ClampedSectionMaterialDatabase':
        """ClampedSectionMaterialDatabase: 'ClampedSectionMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClampedSectionMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cycloidal_disc_material_database(self) -> '_1422.CycloidalDiscMaterialDatabase':
        """CycloidalDiscMaterialDatabase: 'CycloidalDiscMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_pins_material_database(self) -> '_1428.RingPinsMaterialDatabase':
        """RingPinsMaterialDatabase: 'RingPinsMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinsMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def magnet_material_database(self) -> '_1265.MagnetMaterialDatabase':
        """MagnetMaterialDatabase: 'MagnetMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnetMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_rotor_material_database(self) -> '_1282.StatorRotorMaterialDatabase':
        """StatorRotorMaterialDatabase: 'StatorRotorMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorRotorMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def winding_material_database(self) -> '_1292.WindingMaterialDatabase':
        """WindingMaterialDatabase: 'WindingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_design_settings(self) -> '_310.BevelHypoidGearDesignSettings':
        """BevelHypoidGearDesignSettings: 'BevelHypoidGearDesignSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearDesignSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_rating_settings(self) -> '_311.BevelHypoidGearRatingSettings':
        """BevelHypoidGearRatingSettings: 'BevelHypoidGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_design_settings_database(self) -> '_933.BevelHypoidGearDesignSettingsDatabase':
        """BevelHypoidGearDesignSettingsDatabase: 'BevelHypoidGearDesignSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearDesignSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_rating_settings_database(self) -> '_935.BevelHypoidGearRatingSettingsDatabase':
        """BevelHypoidGearRatingSettingsDatabase: 'BevelHypoidGearRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_defaults(self) -> '_1004.CylindricalGearDefaults':
        """CylindricalGearDefaults: 'CylindricalGearDefaults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDefaults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_constraints_database(self) -> '_1008.CylindricalGearDesignConstraintsDatabase':
        """CylindricalGearDesignConstraintsDatabase: 'CylindricalGearDesignConstraintsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignConstraintsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_constraint_settings(self) -> '_1009.CylindricalGearDesignConstraintSettings':
        """CylindricalGearDesignConstraintSettings: 'CylindricalGearDesignConstraintSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignConstraintSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometry_settings_database(self) -> '_1014.CylindricalGearMicroGeometrySettingsDatabase':
        """CylindricalGearMicroGeometrySettingsDatabase: 'CylindricalGearMicroGeometrySettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometrySettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_micro_geometry_settings(self) -> '_1025.CylindricalGearSetMicroGeometrySettings':
        """CylindricalGearSetMicroGeometrySettings: 'CylindricalGearSetMicroGeometrySettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetMicroGeometrySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_constraint_collection_database(self) -> '_938.DesignConstraintCollectionDatabase':
        """DesignConstraintCollectionDatabase: 'DesignConstraintCollectionDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignConstraintCollectionDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_design_constraints_collection(self) -> '_944.SelectedDesignConstraintsCollection':
        """SelectedDesignConstraintsCollection: 'SelectedDesignConstraintsCollection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedDesignConstraintsCollection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_gear_set_design_space_search_strategy_database(self) -> '_913.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase':
        """MicroGeometryGearSetDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self) -> '_914.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase':
        """MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_917.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_cylindrical_gear_set_optimisation_strategy_database(self) -> '_918.ParetoCylindricalGearSetOptimisationStrategyDatabase':
        """ParetoCylindricalGearSetOptimisationStrategyDatabase: 'ParetoCylindricalGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoCylindricalGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_920.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_face_gear_set_optimisation_strategy_database(self) -> '_921.ParetoFaceGearSetOptimisationStrategyDatabase':
        """ParetoFaceGearSetOptimisationStrategyDatabase: 'ParetoFaceGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoFaceGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_923.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_hypoid_gear_set_optimisation_strategy_database(self) -> '_924.ParetoHypoidGearSetOptimisationStrategyDatabase':
        """ParetoHypoidGearSetOptimisationStrategyDatabase: 'ParetoHypoidGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoHypoidGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_926.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_spiral_bevel_gear_set_optimisation_strategy_database(self) -> '_927.ParetoSpiralBevelGearSetOptimisationStrategyDatabase':
        """ParetoSpiralBevelGearSetOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoSpiralBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_928.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_straight_bevel_gear_set_optimisation_strategy_database(self) -> '_929.ParetoStraightBevelGearSetOptimisationStrategyDatabase':
        """ParetoStraightBevelGearSetOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoStraightBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_fe_settings(self) -> '_848.CylindricalGearFESettings':
        """CylindricalGearFESettings: 'CylindricalGearFESettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearFESettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_machine_database(self) -> '_793.ManufacturingMachineDatabase':
        """ManufacturingMachineDatabase: 'ManufacturingMachineDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingMachineDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_formed_wheel_grinder_database(self) -> '_698.CylindricalFormedWheelGrinderDatabase':
        """CylindricalFormedWheelGrinderDatabase: 'CylindricalFormedWheelGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalFormedWheelGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_plunge_shaver_database(self) -> '_704.CylindricalGearPlungeShaverDatabase':
        """CylindricalGearPlungeShaverDatabase: 'CylindricalGearPlungeShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearPlungeShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_shaver_database(self) -> '_709.CylindricalGearShaverDatabase':
        """CylindricalGearShaverDatabase: 'CylindricalGearShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_worm_grinder_database(self) -> '_710.CylindricalWormGrinderDatabase':
        """CylindricalWormGrinderDatabase: 'CylindricalWormGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalWormGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_hob_database(self) -> '_608.CylindricalHobDatabase':
        """CylindricalHobDatabase: 'CylindricalHobDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalHobDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_shaper_database(self) -> '_619.CylindricalShaperDatabase':
        """CylindricalShaperDatabase: 'CylindricalShaperDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalShaperDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_iso_material_database(self) -> '_579.BevelGearIsoMaterialDatabase':
        """BevelGearIsoMaterialDatabase: 'BevelGearIsoMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearIsoMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_database(self) -> '_581.BevelGearMaterialDatabase':
        """BevelGearMaterialDatabase: 'BevelGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_agma_material_database(self) -> '_582.CylindricalGearAGMAMaterialDatabase':
        """CylindricalGearAGMAMaterialDatabase: 'CylindricalGearAGMAMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearAGMAMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_iso_material_database(self) -> '_583.CylindricalGearISOMaterialDatabase':
        """CylindricalGearISOMaterialDatabase: 'CylindricalGearISOMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearISOMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_plastic_material_database(self) -> '_586.CylindricalGearPlasticMaterialDatabase':
        """CylindricalGearPlasticMaterialDatabase: 'CylindricalGearPlasticMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearPlasticMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_material_expert_system_factor_settings(self) -> '_589.GearMaterialExpertSystemFactorSettings':
        """GearMaterialExpertSystemFactorSettings: 'GearMaterialExpertSystemFactorSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMaterialExpertSystemFactorSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def isotr1417912001_coefficient_of_friction_constants_database(self) -> '_592.ISOTR1417912001CoefficientOfFrictionConstantsDatabase':
        """ISOTR1417912001CoefficientOfFrictionConstantsDatabase: 'ISOTR1417912001CoefficientOfFrictionConstantsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISOTR1417912001CoefficientOfFrictionConstantsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_conical_gear_material_database(self) -> '_593.KlingelnbergConicalGearMaterialDatabase':
        """KlingelnbergConicalGearMaterialDatabase: 'KlingelnbergConicalGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergConicalGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def raw_material_database(self) -> '_600.RawMaterialDatabase':
        """RawMaterialDatabase: 'RawMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RawMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pocketing_power_loss_coefficients_database(self) -> '_337.PocketingPowerLossCoefficientsDatabase':
        """PocketingPowerLossCoefficientsDatabase: 'PocketingPowerLossCoefficientsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PocketingPowerLossCoefficientsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_and_rating_settings(self) -> '_446.CylindricalGearDesignAndRatingSettings':
        """CylindricalGearDesignAndRatingSettings: 'CylindricalGearDesignAndRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignAndRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_and_rating_settings_database(self) -> '_447.CylindricalGearDesignAndRatingSettingsDatabase':
        """CylindricalGearDesignAndRatingSettingsDatabase: 'CylindricalGearDesignAndRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignAndRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_plastic_gear_rating_settings(self) -> '_462.CylindricalPlasticGearRatingSettings':
        """CylindricalPlasticGearRatingSettings: 'CylindricalPlasticGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalPlasticGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_plastic_gear_rating_settings_database(self) -> '_463.CylindricalPlasticGearRatingSettingsDatabase':
        """CylindricalPlasticGearRatingSettingsDatabase: 'CylindricalPlasticGearRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalPlasticGearRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_material_database(self) -> '_240.BearingMaterialDatabase':
        """BearingMaterialDatabase: 'BearingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_material_database(self) -> '_243.ComponentMaterialDatabase':
        """ComponentMaterialDatabase: 'ComponentMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lubrication_detail_database(self) -> '_262.LubricationDetailDatabase':
        """LubricationDetailDatabase: 'LubricationDetailDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricationDetailDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def materials_settings(self) -> '_265.MaterialsSettings':
        """MaterialsSettings: 'MaterialsSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def materials_settings_database(self) -> '_266.MaterialsSettingsDatabase':
        """MaterialsSettingsDatabase: 'MaterialsSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialsSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_settings(self) -> '_48.AnalysisSettings':
        """AnalysisSettings: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_settings_database(self) -> '_49.AnalysisSettingsDatabase':
        """AnalysisSettingsDatabase: 'AnalysisSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fe_user_settings(self) -> '_68.FEUserSettings':
        """FEUserSettings: 'FEUserSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEUserSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def geometry_modeller_settings(self) -> '_159.GeometryModellerSettings':
        """GeometryModellerSettings: 'GeometryModellerSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryModellerSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_material_database(self) -> '_25.ShaftMaterialDatabase':
        """ShaftMaterialDatabase: 'ShaftMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_settings(self) -> '_38.ShaftSettings':
        """ShaftSettings: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_settings_database(self) -> '_39.ShaftSettingsDatabase':
        """ShaftSettingsDatabase: 'ShaftSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def critical_speed_analysis_draw_style(self) -> '_6510.CriticalSpeedAnalysisDrawStyle':
        """CriticalSpeedAnalysisDrawStyle: 'CriticalSpeedAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeedAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_draw_style(self) -> '_5695.HarmonicAnalysisDrawStyle':
        """HarmonicAnalysisDrawStyle: 'HarmonicAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mbd_analysis_draw_style(self) -> '_5397.MBDAnalysisDrawStyle':
        """MBDAnalysisDrawStyle: 'MBDAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MBDAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modal_analysis_draw_style(self) -> '_4596.ModalAnalysisDrawStyle':
        """ModalAnalysisDrawStyle: 'ModalAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_draw_style(self) -> '_4065.PowerFlowDrawStyle':
        """PowerFlowDrawStyle: 'PowerFlowDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowDrawStyle

        if temp is None:
            return None

        if _4065.PowerFlowDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_draw_style to PowerFlowDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stability_analysis_draw_style(self) -> '_3815.StabilityAnalysisDrawStyle':
        """StabilityAnalysisDrawStyle: 'StabilityAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def steady_state_synchronous_response_draw_style(self) -> '_3036.SteadyStateSynchronousResponseDrawStyle':
        """SteadyStateSynchronousResponseDrawStyle: 'SteadyStateSynchronousResponseDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponseDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_draw_style(self) -> '_2772.SystemDeflectionDrawStyle':
        """SystemDeflectionDrawStyle: 'SystemDeflectionDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def model_view_options_draw_style(self) -> '_2203.ModelViewOptionsDrawStyle':
        """ModelViewOptionsDrawStyle: 'ModelViewOptionsDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModelViewOptionsDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_optimization_strategy_database(self) -> '_2183.ConicalGearOptimizationStrategyDatabase':
        """ConicalGearOptimizationStrategyDatabase: 'ConicalGearOptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearOptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimization_strategy_database(self) -> '_2192.OptimizationStrategyDatabase':
        """OptimizationStrategyDatabase: 'OptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def supercharger_rotor_set_database(self) -> '_2515.SuperchargerRotorSetDatabase':
        """SuperchargerRotorSetDatabase: 'SuperchargerRotorSetDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerRotorSetDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planet_carrier_settings(self) -> '_2422.PlanetCarrierSettings':
        """PlanetCarrierSettings: 'PlanetCarrierSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarrierSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cad_export_settings(self) -> '_1795.CADExportSettings':
        """CADExportSettings: 'CADExportSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CADExportSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def database_settings(self) -> '_1790.DatabaseSettings':
        """DatabaseSettings: 'DatabaseSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DatabaseSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def program_settings(self) -> '_1561.ProgramSettings':
        """ProgramSettings: 'ProgramSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProgramSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pushbullet_settings(self) -> '_1562.PushbulletSettings':
        """PushbulletSettings: 'PushbulletSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PushbulletSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def scripting_setup(self) -> '_1704.ScriptingSetup':
        """ScriptingSetup: 'ScriptingSetup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScriptingSetup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def measurement_settings(self) -> '_1571.MeasurementSettings':
        """MeasurementSettings: 'MeasurementSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
