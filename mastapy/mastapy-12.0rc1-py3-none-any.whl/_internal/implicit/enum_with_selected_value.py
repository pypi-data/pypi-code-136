"""enum_with_selected_value.py

Implementations of 'EnumWithSelectedValue' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""


from enum import Enum
from typing import List

from mastapy._internal import (
    mixins, enum_with_selected_value_runtime, constructor, conversion
)
from mastapy.shafts import _34, _45
from mastapy._internal.python_net import python_net_import
from mastapy.nodal_analysis import (
    _71, _90, _77, _86,
    _53
)
from mastapy.nodal_analysis.varying_input_components import _97
from mastapy.math_utility import (
    _1490, _1473, _1469, _1456,
    _1455, _1459, _1468
)
from mastapy.nodal_analysis.elmer import _169, _166
from mastapy.fe_tools.enums import _1232
from mastapy.materials import _255, _259, _245
from mastapy.gears import _331, _329, _332
from mastapy.gears.rating.cylindrical import _474, _475
from mastapy.gears.micro_geometry import (
    _566, _567, _568, _569
)
from mastapy.gears.manufacturing.cylindrical import (
    _616, _617, _620, _602
)
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _638, _639, _636
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _651
from mastapy.geometry.two_d.curves import _307
from mastapy.gears.gear_designs.cylindrical import _1071, _1042, _1063
from mastapy.gears.gear_designs.conical import _1147, _1148, _1159
from mastapy.gears.gear_set_pareto_optimiser import _896
from mastapy.utility.model_validation import _1757, _1760
from mastapy.gears.ltca import _820
from mastapy.gears.gear_designs.creation_options import _1136
from mastapy.gears.gear_designs.bevel import _1180, _1169
from mastapy.fe_tools.vfx_tools.vfx_enums import _1229, _1230
from mastapy.electric_machines import _1241
from mastapy.electric_machines.load_cases_and_analyses import _1331
from mastapy.electric_machines.harmonic_load_data import _1350, _1347
from mastapy.bearings.tolerances import (
    _1871, _1884, _1864, _1863,
    _1865
)
from mastapy.detailed_rigid_connectors.splines import (
    _1360, _1383, _1369, _1370,
    _1378, _1384, _1361
)
from mastapy.detailed_rigid_connectors.interference_fits import _1414
from mastapy.utility import _1546
from mastapy.utility.report import _1710
from mastapy.bearings import (
    _1845, _1852, _1853, _1831,
    _1832, _1856, _1858, _1838
)
from mastapy.bearings.bearing_results import (
    _1922, _1921, _1923, _1924
)
from mastapy.bearings.bearing_designs.rolling import _2107
from mastapy.materials.efficiency import _286, _294
from mastapy.system_model.part_model import _2427
from mastapy.system_model.drawing.options import _2214
from mastapy.utility.enums import _1785, _1786, _1784
from mastapy.system_model.fe import (
    _2318, _2362, _2339, _2315,
    _2349
)
from mastapy.system_model import (
    _2160, _2174, _2169, _2172
)
from mastapy.nodal_analysis.fe_export_utility import _165, _164
from mastapy.system_model.part_model.couplings import _2542, _2545, _2546
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4291
from mastapy.system_model.analyses_and_results.static_loads import (
    _6744, _6902, _6823, _6864,
    _6903
)
from mastapy.system_model.analyses_and_results.modal_analyses import _4568
from mastapy.system_model.analyses_and_results.mbd_analyses import (
    _5323, _5375, _5420, _5445
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5679, _5697
from mastapy.bearings.bearing_results.rolling import _1932, _1926
from mastapy.nodal_analysis.nodal_entities import _129
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2065
from mastapy.math_utility.hertzian_contact import _1538
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6917

_ARRAY = python_net_import('System', 'Array')
_ENUM_WITH_SELECTED_VALUE = python_net_import('SMT.MastaAPI.Utility.Property', 'EnumWithSelectedValue')


__docformat__ = 'restructuredtext en'
__all__ = (
    'EnumWithSelectedValue_ShaftRatingMethod', 'EnumWithSelectedValue_SurfaceFinishes',
    'EnumWithSelectedValue_IntegrationMethod', 'EnumWithSelectedValue_ValueInputOption',
    'EnumWithSelectedValue_SinglePointSelectionMethod', 'EnumWithSelectedValue_ResultOptionsFor3DVector',
    'EnumWithSelectedValue_ElmerResultType', 'EnumWithSelectedValue_ModeInputType',
    'EnumWithSelectedValue_MaterialPropertyClass', 'EnumWithSelectedValue_LubricantDefinition',
    'EnumWithSelectedValue_LubricantViscosityClassISO', 'EnumWithSelectedValue_MicroGeometryModel',
    'EnumWithSelectedValue_ExtrapolationOptions', 'EnumWithSelectedValue_CylindricalGearRatingMethods',
    'EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod', 'EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod',
    'EnumWithSelectedValue_LocationOfEvaluationLowerLimit', 'EnumWithSelectedValue_LocationOfEvaluationUpperLimit',
    'EnumWithSelectedValue_LocationOfRootReliefEvaluation', 'EnumWithSelectedValue_LocationOfTipReliefEvaluation',
    'EnumWithSelectedValue_CylindricalMftFinishingMethods', 'EnumWithSelectedValue_CylindricalMftRoughingMethods',
    'EnumWithSelectedValue_MicroGeometryDefinitionMethod', 'EnumWithSelectedValue_MicroGeometryDefinitionType',
    'EnumWithSelectedValue_ChartType', 'EnumWithSelectedValue_Flank',
    'EnumWithSelectedValue_ActiveProcessMethod', 'EnumWithSelectedValue_CutterFlankSections',
    'EnumWithSelectedValue_BasicCurveTypes', 'EnumWithSelectedValue_ThicknessType',
    'EnumWithSelectedValue_ConicalMachineSettingCalculationMethods', 'EnumWithSelectedValue_ConicalManufactureMethods',
    'EnumWithSelectedValue_CandidateDisplayChoice', 'EnumWithSelectedValue_Severity',
    'EnumWithSelectedValue_GeometrySpecificationType', 'EnumWithSelectedValue_StatusItemSeverity',
    'EnumWithSelectedValue_LubricationMethods', 'EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod',
    'EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods', 'EnumWithSelectedValue_ContactResultType',
    'EnumWithSelectedValue_StressResultsType', 'EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption',
    'EnumWithSelectedValue_ToothThicknessSpecificationMethod', 'EnumWithSelectedValue_LoadDistributionFactorMethods',
    'EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods', 'EnumWithSelectedValue_ProSolveMpcType',
    'EnumWithSelectedValue_ProSolveSolverType', 'EnumWithSelectedValue_CoilPositionInSlot',
    'EnumWithSelectedValue_ElectricMachineAnalysisPeriod', 'EnumWithSelectedValue_LoadCaseType',
    'EnumWithSelectedValue_HarmonicLoadDataType', 'EnumWithSelectedValue_ForceDisplayOption',
    'EnumWithSelectedValue_ITDesignation', 'EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption',
    'EnumWithSelectedValue_SplineRatingTypes', 'EnumWithSelectedValue_Modules',
    'EnumWithSelectedValue_PressureAngleTypes', 'EnumWithSelectedValue_SplineFitClassType',
    'EnumWithSelectedValue_SplineToleranceClassTypes', 'EnumWithSelectedValue_Table4JointInterfaceTypes',
    'EnumWithSelectedValue_DynamicsResponseScaling', 'EnumWithSelectedValue_ExecutableDirectoryCopier_Option',
    'EnumWithSelectedValue_CadPageOrientation', 'EnumWithSelectedValue_FluidFilmTemperatureOptions',
    'EnumWithSelectedValue_SupportToleranceLocationDesignation', 'EnumWithSelectedValue_LoadedBallElementPropertyType',
    'EnumWithSelectedValue_RollerBearingProfileTypes', 'EnumWithSelectedValue_RollingBearingArrangement',
    'EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod', 'EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod',
    'EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum', 'EnumWithSelectedValue_RollingBearingRaceType',
    'EnumWithSelectedValue_RotationalDirections', 'EnumWithSelectedValue_BearingEfficiencyRatingMethod',
    'EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing', 'EnumWithSelectedValue_ExcitationAnalysisViewOption',
    'EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection', 'EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection',
    'EnumWithSelectedValue_ComponentOrientationOption', 'EnumWithSelectedValue_Axis',
    'EnumWithSelectedValue_AlignmentAxis', 'EnumWithSelectedValue_DesignEntityId',
    'EnumWithSelectedValue_ThermalExpansionOption', 'EnumWithSelectedValue_FESubstructureType',
    'EnumWithSelectedValue_FEExportFormat', 'EnumWithSelectedValue_ThreeDViewContourOption',
    'EnumWithSelectedValue_BoundaryConditionType', 'EnumWithSelectedValue_BearingNodeOption',
    'EnumWithSelectedValue_LinkNodeSource', 'EnumWithSelectedValue_BearingToleranceClass',
    'EnumWithSelectedValue_BearingModel', 'EnumWithSelectedValue_PreloadType',
    'EnumWithSelectedValue_RaceAxialMountingType', 'EnumWithSelectedValue_RaceRadialMountingType',
    'EnumWithSelectedValue_InternalClearanceClass', 'EnumWithSelectedValue_BearingToleranceDefinitionOptions',
    'EnumWithSelectedValue_OilSealLossCalculationMethod', 'EnumWithSelectedValue_PowerLoadType',
    'EnumWithSelectedValue_RigidConnectorStiffnessType', 'EnumWithSelectedValue_RigidConnectorToothSpacingType',
    'EnumWithSelectedValue_RigidConnectorTypes', 'EnumWithSelectedValue_FitTypes',
    'EnumWithSelectedValue_DoeValueSpecificationOption', 'EnumWithSelectedValue_AnalysisType',
    'EnumWithSelectedValue_BarModelExportType', 'EnumWithSelectedValue_ComplexPartDisplayOption',
    'EnumWithSelectedValue_DynamicsResponseType', 'EnumWithSelectedValue_BearingStiffnessModel',
    'EnumWithSelectedValue_GearMeshStiffnessModel', 'EnumWithSelectedValue_ShaftAndHousingFlexibilityOption',
    'EnumWithSelectedValue_ExportOutputType', 'EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput',
    'EnumWithSelectedValue_FrictionModelForGyroscopicMoment', 'EnumWithSelectedValue_MeshStiffnessModel',
    'EnumWithSelectedValue_ShearAreaFactorMethod', 'EnumWithSelectedValue_StressConcentrationMethod',
    'EnumWithSelectedValue_BallBearingAnalysisMethod', 'EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod',
    'EnumWithSelectedValue_TorqueRippleInputType', 'EnumWithSelectedValue_HarmonicExcitationType',
    'EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification', 'EnumWithSelectedValue_TorqueSpecificationForSystemDeflection',
    'EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod', 'EnumWithSelectedValue_TorqueConverterLockupRule',
    'EnumWithSelectedValue_DegreesOfFreedom', 'EnumWithSelectedValue_DestinationDesignState'
)


class EnumWithSelectedValue_ShaftRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftRatingMethod' types.
    """
    __qualname__ = 'ShaftRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_34.ShaftRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _34.ShaftRatingMethod

    @classmethod
    def implicit_type(cls) -> '_34.ShaftRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _34.ShaftRatingMethod.type_()

    @property
    def selected_value(self) -> '_34.ShaftRatingMethod':
        """ShaftRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_34.ShaftRatingMethod]':
        """List[ShaftRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SurfaceFinishes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SurfaceFinishes

    A specific implementation of 'EnumWithSelectedValue' for 'SurfaceFinishes' types.
    """
    __qualname__ = 'SurfaceFinishes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_45.SurfaceFinishes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _45.SurfaceFinishes

    @classmethod
    def implicit_type(cls) -> '_45.SurfaceFinishes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _45.SurfaceFinishes.type_()

    @property
    def selected_value(self) -> '_45.SurfaceFinishes':
        """SurfaceFinishes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_45.SurfaceFinishes]':
        """List[SurfaceFinishes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_IntegrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_IntegrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'IntegrationMethod' types.
    """
    __qualname__ = 'IntegrationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_71.IntegrationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _71.IntegrationMethod

    @classmethod
    def implicit_type(cls) -> '_71.IntegrationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _71.IntegrationMethod.type_()

    @property
    def selected_value(self) -> '_71.IntegrationMethod':
        """IntegrationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_71.IntegrationMethod]':
        """List[IntegrationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ValueInputOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ValueInputOption

    A specific implementation of 'EnumWithSelectedValue' for 'ValueInputOption' types.
    """
    __qualname__ = 'ValueInputOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_90.ValueInputOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _90.ValueInputOption

    @classmethod
    def implicit_type(cls) -> '_90.ValueInputOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _90.ValueInputOption.type_()

    @property
    def selected_value(self) -> '_90.ValueInputOption':
        """ValueInputOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_90.ValueInputOption]':
        """List[ValueInputOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SinglePointSelectionMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SinglePointSelectionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'SinglePointSelectionMethod' types.
    """
    __qualname__ = 'SinglePointSelectionMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_97.SinglePointSelectionMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _97.SinglePointSelectionMethod

    @classmethod
    def implicit_type(cls) -> '_97.SinglePointSelectionMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _97.SinglePointSelectionMethod.type_()

    @property
    def selected_value(self) -> '_97.SinglePointSelectionMethod':
        """SinglePointSelectionMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_97.SinglePointSelectionMethod]':
        """List[SinglePointSelectionMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ResultOptionsFor3DVector(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ResultOptionsFor3DVector

    A specific implementation of 'EnumWithSelectedValue' for 'ResultOptionsFor3DVector' types.
    """
    __qualname__ = 'ResultOptionsFor3DVector'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1490.ResultOptionsFor3DVector':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1490.ResultOptionsFor3DVector

    @classmethod
    def implicit_type(cls) -> '_1490.ResultOptionsFor3DVector.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1490.ResultOptionsFor3DVector.type_()

    @property
    def selected_value(self) -> '_1490.ResultOptionsFor3DVector':
        """ResultOptionsFor3DVector: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1490.ResultOptionsFor3DVector]':
        """List[ResultOptionsFor3DVector]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ElmerResultType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ElmerResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ElmerResultType' types.
    """
    __qualname__ = 'ElmerResultType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_169.ElmerResultType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _169.ElmerResultType

    @classmethod
    def implicit_type(cls) -> '_169.ElmerResultType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _169.ElmerResultType.type_()

    @property
    def selected_value(self) -> '_169.ElmerResultType':
        """ElmerResultType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_169.ElmerResultType]':
        """List[ElmerResultType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ModeInputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ModeInputType

    A specific implementation of 'EnumWithSelectedValue' for 'ModeInputType' types.
    """
    __qualname__ = 'ModeInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_77.ModeInputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _77.ModeInputType

    @classmethod
    def implicit_type(cls) -> '_77.ModeInputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _77.ModeInputType.type_()

    @property
    def selected_value(self) -> '_77.ModeInputType':
        """ModeInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_77.ModeInputType]':
        """List[ModeInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MaterialPropertyClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MaterialPropertyClass

    A specific implementation of 'EnumWithSelectedValue' for 'MaterialPropertyClass' types.
    """
    __qualname__ = 'MaterialPropertyClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1232.MaterialPropertyClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1232.MaterialPropertyClass

    @classmethod
    def implicit_type(cls) -> '_1232.MaterialPropertyClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1232.MaterialPropertyClass.type_()

    @property
    def selected_value(self) -> '_1232.MaterialPropertyClass':
        """MaterialPropertyClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1232.MaterialPropertyClass]':
        """List[MaterialPropertyClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricantDefinition(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricantDefinition

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantDefinition' types.
    """
    __qualname__ = 'LubricantDefinition'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_255.LubricantDefinition':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _255.LubricantDefinition

    @classmethod
    def implicit_type(cls) -> '_255.LubricantDefinition.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _255.LubricantDefinition.type_()

    @property
    def selected_value(self) -> '_255.LubricantDefinition':
        """LubricantDefinition: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_255.LubricantDefinition]':
        """List[LubricantDefinition]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricantViscosityClassISO(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricantViscosityClassISO

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantViscosityClassISO' types.
    """
    __qualname__ = 'LubricantViscosityClassISO'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_259.LubricantViscosityClassISO':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _259.LubricantViscosityClassISO

    @classmethod
    def implicit_type(cls) -> '_259.LubricantViscosityClassISO.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _259.LubricantViscosityClassISO.type_()

    @property
    def selected_value(self) -> '_259.LubricantViscosityClassISO':
        """LubricantViscosityClassISO: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_259.LubricantViscosityClassISO]':
        """List[LubricantViscosityClassISO]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryModel

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryModel' types.
    """
    __qualname__ = 'MicroGeometryModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_331.MicroGeometryModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _331.MicroGeometryModel

    @classmethod
    def implicit_type(cls) -> '_331.MicroGeometryModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _331.MicroGeometryModel.type_()

    @property
    def selected_value(self) -> '_331.MicroGeometryModel':
        """MicroGeometryModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_331.MicroGeometryModel]':
        """List[MicroGeometryModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExtrapolationOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExtrapolationOptions

    A specific implementation of 'EnumWithSelectedValue' for 'ExtrapolationOptions' types.
    """
    __qualname__ = 'ExtrapolationOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1473.ExtrapolationOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1473.ExtrapolationOptions

    @classmethod
    def implicit_type(cls) -> '_1473.ExtrapolationOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1473.ExtrapolationOptions.type_()

    @property
    def selected_value(self) -> '_1473.ExtrapolationOptions':
        """ExtrapolationOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1473.ExtrapolationOptions]':
        """List[ExtrapolationOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalGearRatingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalGearRatingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearRatingMethods' types.
    """
    __qualname__ = 'CylindricalGearRatingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_245.CylindricalGearRatingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _245.CylindricalGearRatingMethods

    @classmethod
    def implicit_type(cls) -> '_245.CylindricalGearRatingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _245.CylindricalGearRatingMethods.type_()

    @property
    def selected_value(self) -> '_245.CylindricalGearRatingMethods':
        """CylindricalGearRatingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_245.CylindricalGearRatingMethods]':
        """List[CylindricalGearRatingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingFlashTemperatureRatingMethod' types.
    """
    __qualname__ = 'ScuffingFlashTemperatureRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_474.ScuffingFlashTemperatureRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _474.ScuffingFlashTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> '_474.ScuffingFlashTemperatureRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _474.ScuffingFlashTemperatureRatingMethod.type_()

    @property
    def selected_value(self) -> '_474.ScuffingFlashTemperatureRatingMethod':
        """ScuffingFlashTemperatureRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_474.ScuffingFlashTemperatureRatingMethod]':
        """List[ScuffingFlashTemperatureRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingIntegralTemperatureRatingMethod' types.
    """
    __qualname__ = 'ScuffingIntegralTemperatureRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_475.ScuffingIntegralTemperatureRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _475.ScuffingIntegralTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> '_475.ScuffingIntegralTemperatureRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _475.ScuffingIntegralTemperatureRatingMethod.type_()

    @property
    def selected_value(self) -> '_475.ScuffingIntegralTemperatureRatingMethod':
        """ScuffingIntegralTemperatureRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_475.ScuffingIntegralTemperatureRatingMethod]':
        """List[ScuffingIntegralTemperatureRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfEvaluationLowerLimit(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfEvaluationLowerLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationLowerLimit' types.
    """
    __qualname__ = 'LocationOfEvaluationLowerLimit'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_566.LocationOfEvaluationLowerLimit':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _566.LocationOfEvaluationLowerLimit

    @classmethod
    def implicit_type(cls) -> '_566.LocationOfEvaluationLowerLimit.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _566.LocationOfEvaluationLowerLimit.type_()

    @property
    def selected_value(self) -> '_566.LocationOfEvaluationLowerLimit':
        """LocationOfEvaluationLowerLimit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_566.LocationOfEvaluationLowerLimit]':
        """List[LocationOfEvaluationLowerLimit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfEvaluationUpperLimit(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfEvaluationUpperLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationUpperLimit' types.
    """
    __qualname__ = 'LocationOfEvaluationUpperLimit'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_567.LocationOfEvaluationUpperLimit':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _567.LocationOfEvaluationUpperLimit

    @classmethod
    def implicit_type(cls) -> '_567.LocationOfEvaluationUpperLimit.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _567.LocationOfEvaluationUpperLimit.type_()

    @property
    def selected_value(self) -> '_567.LocationOfEvaluationUpperLimit':
        """LocationOfEvaluationUpperLimit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_567.LocationOfEvaluationUpperLimit]':
        """List[LocationOfEvaluationUpperLimit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfRootReliefEvaluation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfRootReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfRootReliefEvaluation' types.
    """
    __qualname__ = 'LocationOfRootReliefEvaluation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_568.LocationOfRootReliefEvaluation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _568.LocationOfRootReliefEvaluation

    @classmethod
    def implicit_type(cls) -> '_568.LocationOfRootReliefEvaluation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _568.LocationOfRootReliefEvaluation.type_()

    @property
    def selected_value(self) -> '_568.LocationOfRootReliefEvaluation':
        """LocationOfRootReliefEvaluation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_568.LocationOfRootReliefEvaluation]':
        """List[LocationOfRootReliefEvaluation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfTipReliefEvaluation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfTipReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfTipReliefEvaluation' types.
    """
    __qualname__ = 'LocationOfTipReliefEvaluation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_569.LocationOfTipReliefEvaluation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _569.LocationOfTipReliefEvaluation

    @classmethod
    def implicit_type(cls) -> '_569.LocationOfTipReliefEvaluation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _569.LocationOfTipReliefEvaluation.type_()

    @property
    def selected_value(self) -> '_569.LocationOfTipReliefEvaluation':
        """LocationOfTipReliefEvaluation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_569.LocationOfTipReliefEvaluation]':
        """List[LocationOfTipReliefEvaluation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalMftFinishingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalMftFinishingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftFinishingMethods' types.
    """
    __qualname__ = 'CylindricalMftFinishingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_616.CylindricalMftFinishingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _616.CylindricalMftFinishingMethods

    @classmethod
    def implicit_type(cls) -> '_616.CylindricalMftFinishingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _616.CylindricalMftFinishingMethods.type_()

    @property
    def selected_value(self) -> '_616.CylindricalMftFinishingMethods':
        """CylindricalMftFinishingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_616.CylindricalMftFinishingMethods]':
        """List[CylindricalMftFinishingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalMftRoughingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalMftRoughingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftRoughingMethods' types.
    """
    __qualname__ = 'CylindricalMftRoughingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_617.CylindricalMftRoughingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _617.CylindricalMftRoughingMethods

    @classmethod
    def implicit_type(cls) -> '_617.CylindricalMftRoughingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _617.CylindricalMftRoughingMethods.type_()

    @property
    def selected_value(self) -> '_617.CylindricalMftRoughingMethods':
        """CylindricalMftRoughingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_617.CylindricalMftRoughingMethods]':
        """List[CylindricalMftRoughingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryDefinitionMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryDefinitionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionMethod' types.
    """
    __qualname__ = 'MicroGeometryDefinitionMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_638.MicroGeometryDefinitionMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _638.MicroGeometryDefinitionMethod

    @classmethod
    def implicit_type(cls) -> '_638.MicroGeometryDefinitionMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _638.MicroGeometryDefinitionMethod.type_()

    @property
    def selected_value(self) -> '_638.MicroGeometryDefinitionMethod':
        """MicroGeometryDefinitionMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_638.MicroGeometryDefinitionMethod]':
        """List[MicroGeometryDefinitionMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryDefinitionType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryDefinitionType

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionType' types.
    """
    __qualname__ = 'MicroGeometryDefinitionType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_639.MicroGeometryDefinitionType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _639.MicroGeometryDefinitionType

    @classmethod
    def implicit_type(cls) -> '_639.MicroGeometryDefinitionType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _639.MicroGeometryDefinitionType.type_()

    @property
    def selected_value(self) -> '_639.MicroGeometryDefinitionType':
        """MicroGeometryDefinitionType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_639.MicroGeometryDefinitionType]':
        """List[MicroGeometryDefinitionType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ChartType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ChartType

    A specific implementation of 'EnumWithSelectedValue' for 'ChartType' types.
    """
    __qualname__ = 'ChartType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_636.ChartType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _636.ChartType

    @classmethod
    def implicit_type(cls) -> '_636.ChartType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _636.ChartType.type_()

    @property
    def selected_value(self) -> '_636.ChartType':
        """ChartType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_636.ChartType]':
        """List[ChartType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Flank(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Flank

    A specific implementation of 'EnumWithSelectedValue' for 'Flank' types.
    """
    __qualname__ = 'Flank'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_620.Flank':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _620.Flank

    @classmethod
    def implicit_type(cls) -> '_620.Flank.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _620.Flank.type_()

    @property
    def selected_value(self) -> '_620.Flank':
        """Flank: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_620.Flank]':
        """List[Flank]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ActiveProcessMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ActiveProcessMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ActiveProcessMethod' types.
    """
    __qualname__ = 'ActiveProcessMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_651.ActiveProcessMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _651.ActiveProcessMethod

    @classmethod
    def implicit_type(cls) -> '_651.ActiveProcessMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _651.ActiveProcessMethod.type_()

    @property
    def selected_value(self) -> '_651.ActiveProcessMethod':
        """ActiveProcessMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_651.ActiveProcessMethod]':
        """List[ActiveProcessMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CutterFlankSections(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CutterFlankSections

    A specific implementation of 'EnumWithSelectedValue' for 'CutterFlankSections' types.
    """
    __qualname__ = 'CutterFlankSections'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_602.CutterFlankSections':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _602.CutterFlankSections

    @classmethod
    def implicit_type(cls) -> '_602.CutterFlankSections.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _602.CutterFlankSections.type_()

    @property
    def selected_value(self) -> '_602.CutterFlankSections':
        """CutterFlankSections: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_602.CutterFlankSections]':
        """List[CutterFlankSections]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicCurveTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicCurveTypes

    A specific implementation of 'EnumWithSelectedValue' for 'BasicCurveTypes' types.
    """
    __qualname__ = 'BasicCurveTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_307.BasicCurveTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _307.BasicCurveTypes

    @classmethod
    def implicit_type(cls) -> '_307.BasicCurveTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _307.BasicCurveTypes.type_()

    @property
    def selected_value(self) -> '_307.BasicCurveTypes':
        """BasicCurveTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_307.BasicCurveTypes]':
        """List[BasicCurveTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThicknessType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThicknessType

    A specific implementation of 'EnumWithSelectedValue' for 'ThicknessType' types.
    """
    __qualname__ = 'ThicknessType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1071.ThicknessType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1071.ThicknessType

    @classmethod
    def implicit_type(cls) -> '_1071.ThicknessType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1071.ThicknessType.type_()

    @property
    def selected_value(self) -> '_1071.ThicknessType':
        """ThicknessType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1071.ThicknessType]':
        """List[ThicknessType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ConicalMachineSettingCalculationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ConicalMachineSettingCalculationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalMachineSettingCalculationMethods' types.
    """
    __qualname__ = 'ConicalMachineSettingCalculationMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1147.ConicalMachineSettingCalculationMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1147.ConicalMachineSettingCalculationMethods

    @classmethod
    def implicit_type(cls) -> '_1147.ConicalMachineSettingCalculationMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1147.ConicalMachineSettingCalculationMethods.type_()

    @property
    def selected_value(self) -> '_1147.ConicalMachineSettingCalculationMethods':
        """ConicalMachineSettingCalculationMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1147.ConicalMachineSettingCalculationMethods]':
        """List[ConicalMachineSettingCalculationMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ConicalManufactureMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ConicalManufactureMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalManufactureMethods' types.
    """
    __qualname__ = 'ConicalManufactureMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1148.ConicalManufactureMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1148.ConicalManufactureMethods

    @classmethod
    def implicit_type(cls) -> '_1148.ConicalManufactureMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1148.ConicalManufactureMethods.type_()

    @property
    def selected_value(self) -> '_1148.ConicalManufactureMethods':
        """ConicalManufactureMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1148.ConicalManufactureMethods]':
        """List[ConicalManufactureMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CandidateDisplayChoice(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CandidateDisplayChoice

    A specific implementation of 'EnumWithSelectedValue' for 'CandidateDisplayChoice' types.
    """
    __qualname__ = 'CandidateDisplayChoice'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_896.CandidateDisplayChoice':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _896.CandidateDisplayChoice

    @classmethod
    def implicit_type(cls) -> '_896.CandidateDisplayChoice.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _896.CandidateDisplayChoice.type_()

    @property
    def selected_value(self) -> '_896.CandidateDisplayChoice':
        """CandidateDisplayChoice: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_896.CandidateDisplayChoice]':
        """List[CandidateDisplayChoice]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Severity(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Severity

    A specific implementation of 'EnumWithSelectedValue' for 'Severity' types.
    """
    __qualname__ = 'Severity'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1757.Severity':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1757.Severity

    @classmethod
    def implicit_type(cls) -> '_1757.Severity.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1757.Severity.type_()

    @property
    def selected_value(self) -> '_1757.Severity':
        """Severity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1757.Severity]':
        """List[Severity]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_GeometrySpecificationType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_GeometrySpecificationType

    A specific implementation of 'EnumWithSelectedValue' for 'GeometrySpecificationType' types.
    """
    __qualname__ = 'GeometrySpecificationType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1042.GeometrySpecificationType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1042.GeometrySpecificationType

    @classmethod
    def implicit_type(cls) -> '_1042.GeometrySpecificationType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1042.GeometrySpecificationType.type_()

    @property
    def selected_value(self) -> '_1042.GeometrySpecificationType':
        """GeometrySpecificationType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1042.GeometrySpecificationType]':
        """List[GeometrySpecificationType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StatusItemSeverity(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StatusItemSeverity

    A specific implementation of 'EnumWithSelectedValue' for 'StatusItemSeverity' types.
    """
    __qualname__ = 'StatusItemSeverity'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1760.StatusItemSeverity':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1760.StatusItemSeverity

    @classmethod
    def implicit_type(cls) -> '_1760.StatusItemSeverity.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1760.StatusItemSeverity.type_()

    @property
    def selected_value(self) -> '_1760.StatusItemSeverity':
        """StatusItemSeverity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1760.StatusItemSeverity]':
        """List[StatusItemSeverity]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LubricationMethods' types.
    """
    __qualname__ = 'LubricationMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_329.LubricationMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _329.LubricationMethods

    @classmethod
    def implicit_type(cls) -> '_329.LubricationMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _329.LubricationMethods.type_()

    @property
    def selected_value(self) -> '_329.LubricationMethods':
        """LubricationMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_329.LubricationMethods]':
        """List[LubricationMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicropittingCoefficientOfFrictionCalculationMethod' types.
    """
    __qualname__ = 'MicropittingCoefficientOfFrictionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_332.MicropittingCoefficientOfFrictionCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _332.MicropittingCoefficientOfFrictionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_332.MicropittingCoefficientOfFrictionCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _332.MicropittingCoefficientOfFrictionCalculationMethod.type_()

    @property
    def selected_value(self) -> '_332.MicropittingCoefficientOfFrictionCalculationMethod':
        """MicropittingCoefficientOfFrictionCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_332.MicropittingCoefficientOfFrictionCalculationMethod]':
        """List[MicropittingCoefficientOfFrictionCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingCoefficientOfFrictionMethods' types.
    """
    __qualname__ = 'ScuffingCoefficientOfFrictionMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1063.ScuffingCoefficientOfFrictionMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1063.ScuffingCoefficientOfFrictionMethods

    @classmethod
    def implicit_type(cls) -> '_1063.ScuffingCoefficientOfFrictionMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1063.ScuffingCoefficientOfFrictionMethods.type_()

    @property
    def selected_value(self) -> '_1063.ScuffingCoefficientOfFrictionMethods':
        """ScuffingCoefficientOfFrictionMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1063.ScuffingCoefficientOfFrictionMethods]':
        """List[ScuffingCoefficientOfFrictionMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ContactResultType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ContactResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ContactResultType' types.
    """
    __qualname__ = 'ContactResultType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_820.ContactResultType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _820.ContactResultType

    @classmethod
    def implicit_type(cls) -> '_820.ContactResultType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _820.ContactResultType.type_()

    @property
    def selected_value(self) -> '_820.ContactResultType':
        """ContactResultType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_820.ContactResultType]':
        """List[ContactResultType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StressResultsType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StressResultsType

    A specific implementation of 'EnumWithSelectedValue' for 'StressResultsType' types.
    """
    __qualname__ = 'StressResultsType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_86.StressResultsType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _86.StressResultsType

    @classmethod
    def implicit_type(cls) -> '_86.StressResultsType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _86.StressResultsType.type_()

    @property
    def selected_value(self) -> '_86.StressResultsType':
        """StressResultsType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_86.StressResultsType]':
        """List[StressResultsType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearPairCreationOptions.DerivedParameterOption' types.
    """
    __qualname__ = 'CylindricalGearPairCreationOptions.DerivedParameterOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1136.CylindricalGearPairCreationOptions.DerivedParameterOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1136.CylindricalGearPairCreationOptions.DerivedParameterOption

    @classmethod
    def implicit_type(cls) -> '_1136.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1136.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()

    @property
    def selected_value(self) -> '_1136.CylindricalGearPairCreationOptions.DerivedParameterOption':
        """CylindricalGearPairCreationOptions.DerivedParameterOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1136.CylindricalGearPairCreationOptions.DerivedParameterOption]':
        """List[CylindricalGearPairCreationOptions.DerivedParameterOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ToothThicknessSpecificationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ToothThicknessSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ToothThicknessSpecificationMethod' types.
    """
    __qualname__ = 'ToothThicknessSpecificationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1180.ToothThicknessSpecificationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1180.ToothThicknessSpecificationMethod

    @classmethod
    def implicit_type(cls) -> '_1180.ToothThicknessSpecificationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1180.ToothThicknessSpecificationMethod.type_()

    @property
    def selected_value(self) -> '_1180.ToothThicknessSpecificationMethod':
        """ToothThicknessSpecificationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1180.ToothThicknessSpecificationMethod]':
        """List[ToothThicknessSpecificationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadDistributionFactorMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadDistributionFactorMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LoadDistributionFactorMethods' types.
    """
    __qualname__ = 'LoadDistributionFactorMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1159.LoadDistributionFactorMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1159.LoadDistributionFactorMethods

    @classmethod
    def implicit_type(cls) -> '_1159.LoadDistributionFactorMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1159.LoadDistributionFactorMethods.type_()

    @property
    def selected_value(self) -> '_1159.LoadDistributionFactorMethods':
        """LoadDistributionFactorMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1159.LoadDistributionFactorMethods]':
        """List[LoadDistributionFactorMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods

    A specific implementation of 'EnumWithSelectedValue' for 'AGMAGleasonConicalGearGeometryMethods' types.
    """
    __qualname__ = 'AGMAGleasonConicalGearGeometryMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1169.AGMAGleasonConicalGearGeometryMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1169.AGMAGleasonConicalGearGeometryMethods

    @classmethod
    def implicit_type(cls) -> '_1169.AGMAGleasonConicalGearGeometryMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1169.AGMAGleasonConicalGearGeometryMethods.type_()

    @property
    def selected_value(self) -> '_1169.AGMAGleasonConicalGearGeometryMethods':
        """AGMAGleasonConicalGearGeometryMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1169.AGMAGleasonConicalGearGeometryMethods]':
        """List[AGMAGleasonConicalGearGeometryMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ProSolveMpcType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ProSolveMpcType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveMpcType' types.
    """
    __qualname__ = 'ProSolveMpcType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1229.ProSolveMpcType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1229.ProSolveMpcType

    @classmethod
    def implicit_type(cls) -> '_1229.ProSolveMpcType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1229.ProSolveMpcType.type_()

    @property
    def selected_value(self) -> '_1229.ProSolveMpcType':
        """ProSolveMpcType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1229.ProSolveMpcType]':
        """List[ProSolveMpcType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ProSolveSolverType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ProSolveSolverType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveSolverType' types.
    """
    __qualname__ = 'ProSolveSolverType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1230.ProSolveSolverType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1230.ProSolveSolverType

    @classmethod
    def implicit_type(cls) -> '_1230.ProSolveSolverType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1230.ProSolveSolverType.type_()

    @property
    def selected_value(self) -> '_1230.ProSolveSolverType':
        """ProSolveSolverType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1230.ProSolveSolverType]':
        """List[ProSolveSolverType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CoilPositionInSlot(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CoilPositionInSlot

    A specific implementation of 'EnumWithSelectedValue' for 'CoilPositionInSlot' types.
    """
    __qualname__ = 'CoilPositionInSlot'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1241.CoilPositionInSlot':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1241.CoilPositionInSlot

    @classmethod
    def implicit_type(cls) -> '_1241.CoilPositionInSlot.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1241.CoilPositionInSlot.type_()

    @property
    def selected_value(self) -> '_1241.CoilPositionInSlot':
        """CoilPositionInSlot: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1241.CoilPositionInSlot]':
        """List[CoilPositionInSlot]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ElectricMachineAnalysisPeriod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ElectricMachineAnalysisPeriod

    A specific implementation of 'EnumWithSelectedValue' for 'ElectricMachineAnalysisPeriod' types.
    """
    __qualname__ = 'ElectricMachineAnalysisPeriod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_166.ElectricMachineAnalysisPeriod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _166.ElectricMachineAnalysisPeriod

    @classmethod
    def implicit_type(cls) -> '_166.ElectricMachineAnalysisPeriod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _166.ElectricMachineAnalysisPeriod.type_()

    @property
    def selected_value(self) -> '_166.ElectricMachineAnalysisPeriod':
        """ElectricMachineAnalysisPeriod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_166.ElectricMachineAnalysisPeriod]':
        """List[ElectricMachineAnalysisPeriod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadCaseType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadCaseType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadCaseType' types.
    """
    __qualname__ = 'LoadCaseType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1331.LoadCaseType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1331.LoadCaseType

    @classmethod
    def implicit_type(cls) -> '_1331.LoadCaseType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1331.LoadCaseType.type_()

    @property
    def selected_value(self) -> '_1331.LoadCaseType':
        """LoadCaseType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1331.LoadCaseType]':
        """List[LoadCaseType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicLoadDataType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicLoadDataType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicLoadDataType' types.
    """
    __qualname__ = 'HarmonicLoadDataType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1350.HarmonicLoadDataType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1350.HarmonicLoadDataType

    @classmethod
    def implicit_type(cls) -> '_1350.HarmonicLoadDataType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1350.HarmonicLoadDataType.type_()

    @property
    def selected_value(self) -> '_1350.HarmonicLoadDataType':
        """HarmonicLoadDataType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1350.HarmonicLoadDataType]':
        """List[HarmonicLoadDataType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ForceDisplayOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ForceDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ForceDisplayOption' types.
    """
    __qualname__ = 'ForceDisplayOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1347.ForceDisplayOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1347.ForceDisplayOption

    @classmethod
    def implicit_type(cls) -> '_1347.ForceDisplayOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1347.ForceDisplayOption.type_()

    @property
    def selected_value(self) -> '_1347.ForceDisplayOption':
        """ForceDisplayOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1347.ForceDisplayOption]':
        """List[ForceDisplayOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ITDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ITDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'ITDesignation' types.
    """
    __qualname__ = 'ITDesignation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1871.ITDesignation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1871.ITDesignation

    @classmethod
    def implicit_type(cls) -> '_1871.ITDesignation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1871.ITDesignation.type_()

    @property
    def selected_value(self) -> '_1871.ITDesignation':
        """ITDesignation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1871.ITDesignation]':
        """List[ITDesignation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DudleyEffectiveLengthApproximationOption' types.
    """
    __qualname__ = 'DudleyEffectiveLengthApproximationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1360.DudleyEffectiveLengthApproximationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1360.DudleyEffectiveLengthApproximationOption

    @classmethod
    def implicit_type(cls) -> '_1360.DudleyEffectiveLengthApproximationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1360.DudleyEffectiveLengthApproximationOption.type_()

    @property
    def selected_value(self) -> '_1360.DudleyEffectiveLengthApproximationOption':
        """DudleyEffectiveLengthApproximationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1360.DudleyEffectiveLengthApproximationOption]':
        """List[DudleyEffectiveLengthApproximationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineRatingTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineRatingTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineRatingTypes' types.
    """
    __qualname__ = 'SplineRatingTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1383.SplineRatingTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1383.SplineRatingTypes

    @classmethod
    def implicit_type(cls) -> '_1383.SplineRatingTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1383.SplineRatingTypes.type_()

    @property
    def selected_value(self) -> '_1383.SplineRatingTypes':
        """SplineRatingTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1383.SplineRatingTypes]':
        """List[SplineRatingTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Modules(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Modules

    A specific implementation of 'EnumWithSelectedValue' for 'Modules' types.
    """
    __qualname__ = 'Modules'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1369.Modules':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1369.Modules

    @classmethod
    def implicit_type(cls) -> '_1369.Modules.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1369.Modules.type_()

    @property
    def selected_value(self) -> '_1369.Modules':
        """Modules: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1369.Modules]':
        """List[Modules]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PressureAngleTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PressureAngleTypes

    A specific implementation of 'EnumWithSelectedValue' for 'PressureAngleTypes' types.
    """
    __qualname__ = 'PressureAngleTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1370.PressureAngleTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1370.PressureAngleTypes

    @classmethod
    def implicit_type(cls) -> '_1370.PressureAngleTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1370.PressureAngleTypes.type_()

    @property
    def selected_value(self) -> '_1370.PressureAngleTypes':
        """PressureAngleTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1370.PressureAngleTypes]':
        """List[PressureAngleTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineFitClassType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineFitClassType

    A specific implementation of 'EnumWithSelectedValue' for 'SplineFitClassType' types.
    """
    __qualname__ = 'SplineFitClassType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1378.SplineFitClassType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1378.SplineFitClassType

    @classmethod
    def implicit_type(cls) -> '_1378.SplineFitClassType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1378.SplineFitClassType.type_()

    @property
    def selected_value(self) -> '_1378.SplineFitClassType':
        """SplineFitClassType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1378.SplineFitClassType]':
        """List[SplineFitClassType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineToleranceClassTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineToleranceClassTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineToleranceClassTypes' types.
    """
    __qualname__ = 'SplineToleranceClassTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1384.SplineToleranceClassTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1384.SplineToleranceClassTypes

    @classmethod
    def implicit_type(cls) -> '_1384.SplineToleranceClassTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1384.SplineToleranceClassTypes.type_()

    @property
    def selected_value(self) -> '_1384.SplineToleranceClassTypes':
        """SplineToleranceClassTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1384.SplineToleranceClassTypes]':
        """List[SplineToleranceClassTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Table4JointInterfaceTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Table4JointInterfaceTypes

    A specific implementation of 'EnumWithSelectedValue' for 'Table4JointInterfaceTypes' types.
    """
    __qualname__ = 'Table4JointInterfaceTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1414.Table4JointInterfaceTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1414.Table4JointInterfaceTypes

    @classmethod
    def implicit_type(cls) -> '_1414.Table4JointInterfaceTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1414.Table4JointInterfaceTypes.type_()

    @property
    def selected_value(self) -> '_1414.Table4JointInterfaceTypes':
        """Table4JointInterfaceTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1414.Table4JointInterfaceTypes]':
        """List[Table4JointInterfaceTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DynamicsResponseScaling(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DynamicsResponseScaling

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseScaling' types.
    """
    __qualname__ = 'DynamicsResponseScaling'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1469.DynamicsResponseScaling':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1469.DynamicsResponseScaling

    @classmethod
    def implicit_type(cls) -> '_1469.DynamicsResponseScaling.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1469.DynamicsResponseScaling.type_()

    @property
    def selected_value(self) -> '_1469.DynamicsResponseScaling':
        """DynamicsResponseScaling: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1469.DynamicsResponseScaling]':
        """List[DynamicsResponseScaling]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExecutableDirectoryCopier_Option(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExecutableDirectoryCopier_Option

    A specific implementation of 'EnumWithSelectedValue' for 'ExecutableDirectoryCopier.Option' types.
    """
    __qualname__ = 'ExecutableDirectoryCopier.Option'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1546.ExecutableDirectoryCopier.Option':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1546.ExecutableDirectoryCopier.Option

    @classmethod
    def implicit_type(cls) -> '_1546.ExecutableDirectoryCopier.Option.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1546.ExecutableDirectoryCopier.Option.type_()

    @property
    def selected_value(self) -> '_1546.ExecutableDirectoryCopier.Option':
        """ExecutableDirectoryCopier.Option: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1546.ExecutableDirectoryCopier.Option]':
        """List[ExecutableDirectoryCopier.Option]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CadPageOrientation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CadPageOrientation

    A specific implementation of 'EnumWithSelectedValue' for 'CadPageOrientation' types.
    """
    __qualname__ = 'CadPageOrientation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1710.CadPageOrientation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1710.CadPageOrientation

    @classmethod
    def implicit_type(cls) -> '_1710.CadPageOrientation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1710.CadPageOrientation.type_()

    @property
    def selected_value(self) -> '_1710.CadPageOrientation':
        """CadPageOrientation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1710.CadPageOrientation]':
        """List[CadPageOrientation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FluidFilmTemperatureOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FluidFilmTemperatureOptions

    A specific implementation of 'EnumWithSelectedValue' for 'FluidFilmTemperatureOptions' types.
    """
    __qualname__ = 'FluidFilmTemperatureOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1845.FluidFilmTemperatureOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1845.FluidFilmTemperatureOptions

    @classmethod
    def implicit_type(cls) -> '_1845.FluidFilmTemperatureOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1845.FluidFilmTemperatureOptions.type_()

    @property
    def selected_value(self) -> '_1845.FluidFilmTemperatureOptions':
        """FluidFilmTemperatureOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1845.FluidFilmTemperatureOptions]':
        """List[FluidFilmTemperatureOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SupportToleranceLocationDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SupportToleranceLocationDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'SupportToleranceLocationDesignation' types.
    """
    __qualname__ = 'SupportToleranceLocationDesignation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1884.SupportToleranceLocationDesignation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1884.SupportToleranceLocationDesignation

    @classmethod
    def implicit_type(cls) -> '_1884.SupportToleranceLocationDesignation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1884.SupportToleranceLocationDesignation.type_()

    @property
    def selected_value(self) -> '_1884.SupportToleranceLocationDesignation':
        """SupportToleranceLocationDesignation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1884.SupportToleranceLocationDesignation]':
        """List[SupportToleranceLocationDesignation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadedBallElementPropertyType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadedBallElementPropertyType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadedBallElementPropertyType' types.
    """
    __qualname__ = 'LoadedBallElementPropertyType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1922.LoadedBallElementPropertyType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1922.LoadedBallElementPropertyType

    @classmethod
    def implicit_type(cls) -> '_1922.LoadedBallElementPropertyType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1922.LoadedBallElementPropertyType.type_()

    @property
    def selected_value(self) -> '_1922.LoadedBallElementPropertyType':
        """LoadedBallElementPropertyType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1922.LoadedBallElementPropertyType]':
        """List[LoadedBallElementPropertyType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollerBearingProfileTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollerBearingProfileTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RollerBearingProfileTypes' types.
    """
    __qualname__ = 'RollerBearingProfileTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1852.RollerBearingProfileTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1852.RollerBearingProfileTypes

    @classmethod
    def implicit_type(cls) -> '_1852.RollerBearingProfileTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1852.RollerBearingProfileTypes.type_()

    @property
    def selected_value(self) -> '_1852.RollerBearingProfileTypes':
        """RollerBearingProfileTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1852.RollerBearingProfileTypes]':
        """List[RollerBearingProfileTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollingBearingArrangement(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollingBearingArrangement

    A specific implementation of 'EnumWithSelectedValue' for 'RollingBearingArrangement' types.
    """
    __qualname__ = 'RollingBearingArrangement'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1853.RollingBearingArrangement':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1853.RollingBearingArrangement

    @classmethod
    def implicit_type(cls) -> '_1853.RollingBearingArrangement.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1853.RollingBearingArrangement.type_()

    @property
    def selected_value(self) -> '_1853.RollingBearingArrangement':
        """RollingBearingArrangement: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1853.RollingBearingArrangement]':
        """List[RollingBearingArrangement]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicDynamicLoadRatingCalculationMethod' types.
    """
    __qualname__ = 'BasicDynamicLoadRatingCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1831.BasicDynamicLoadRatingCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1831.BasicDynamicLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1831.BasicDynamicLoadRatingCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1831.BasicDynamicLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1831.BasicDynamicLoadRatingCalculationMethod':
        """BasicDynamicLoadRatingCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1831.BasicDynamicLoadRatingCalculationMethod]':
        """List[BasicDynamicLoadRatingCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicStaticLoadRatingCalculationMethod' types.
    """
    __qualname__ = 'BasicStaticLoadRatingCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1832.BasicStaticLoadRatingCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1832.BasicStaticLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1832.BasicStaticLoadRatingCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1832.BasicStaticLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1832.BasicStaticLoadRatingCalculationMethod':
        """BasicStaticLoadRatingCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1832.BasicStaticLoadRatingCalculationMethod]':
        """List[BasicStaticLoadRatingCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum

    A specific implementation of 'EnumWithSelectedValue' for 'FatigueLoadLimitCalculationMethodEnum' types.
    """
    __qualname__ = 'FatigueLoadLimitCalculationMethodEnum'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2107.FatigueLoadLimitCalculationMethodEnum':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2107.FatigueLoadLimitCalculationMethodEnum

    @classmethod
    def implicit_type(cls) -> '_2107.FatigueLoadLimitCalculationMethodEnum.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2107.FatigueLoadLimitCalculationMethodEnum.type_()

    @property
    def selected_value(self) -> '_2107.FatigueLoadLimitCalculationMethodEnum':
        """FatigueLoadLimitCalculationMethodEnum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2107.FatigueLoadLimitCalculationMethodEnum]':
        """List[FatigueLoadLimitCalculationMethodEnum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollingBearingRaceType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollingBearingRaceType

    A specific implementation of 'EnumWithSelectedValue' for 'RollingBearingRaceType' types.
    """
    __qualname__ = 'RollingBearingRaceType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1856.RollingBearingRaceType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1856.RollingBearingRaceType

    @classmethod
    def implicit_type(cls) -> '_1856.RollingBearingRaceType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1856.RollingBearingRaceType.type_()

    @property
    def selected_value(self) -> '_1856.RollingBearingRaceType':
        """RollingBearingRaceType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1856.RollingBearingRaceType]':
        """List[RollingBearingRaceType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RotationalDirections(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RotationalDirections

    A specific implementation of 'EnumWithSelectedValue' for 'RotationalDirections' types.
    """
    __qualname__ = 'RotationalDirections'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1858.RotationalDirections':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1858.RotationalDirections

    @classmethod
    def implicit_type(cls) -> '_1858.RotationalDirections.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1858.RotationalDirections.type_()

    @property
    def selected_value(self) -> '_1858.RotationalDirections':
        """RotationalDirections: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1858.RotationalDirections]':
        """List[RotationalDirections]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingEfficiencyRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingEfficiencyRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BearingEfficiencyRatingMethod' types.
    """
    __qualname__ = 'BearingEfficiencyRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_286.BearingEfficiencyRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _286.BearingEfficiencyRatingMethod

    @classmethod
    def implicit_type(cls) -> '_286.BearingEfficiencyRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _286.BearingEfficiencyRatingMethod.type_()

    @property
    def selected_value(self) -> '_286.BearingEfficiencyRatingMethod':
        """BearingEfficiencyRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_286.BearingEfficiencyRatingMethod]':
        """List[BearingEfficiencyRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftDiameterModificationDueToRollingBearingRing' types.
    """
    __qualname__ = 'ShaftDiameterModificationDueToRollingBearingRing'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2427.ShaftDiameterModificationDueToRollingBearingRing':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2427.ShaftDiameterModificationDueToRollingBearingRing

    @classmethod
    def implicit_type(cls) -> '_2427.ShaftDiameterModificationDueToRollingBearingRing.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2427.ShaftDiameterModificationDueToRollingBearingRing.type_()

    @property
    def selected_value(self) -> '_2427.ShaftDiameterModificationDueToRollingBearingRing':
        """ShaftDiameterModificationDueToRollingBearingRing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2427.ShaftDiameterModificationDueToRollingBearingRing]':
        """List[ShaftDiameterModificationDueToRollingBearingRing]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExcitationAnalysisViewOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExcitationAnalysisViewOption

    A specific implementation of 'EnumWithSelectedValue' for 'ExcitationAnalysisViewOption' types.
    """
    __qualname__ = 'ExcitationAnalysisViewOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2214.ExcitationAnalysisViewOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2214.ExcitationAnalysisViewOption

    @classmethod
    def implicit_type(cls) -> '_2214.ExcitationAnalysisViewOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2214.ExcitationAnalysisViewOption.type_()

    @property
    def selected_value(self) -> '_2214.ExcitationAnalysisViewOption':
        """ExcitationAnalysisViewOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2214.ExcitationAnalysisViewOption]':
        """List[ExcitationAnalysisViewOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionFirstSelection' types.
    """
    __qualname__ = 'ThreeDViewContourOptionFirstSelection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1785.ThreeDViewContourOptionFirstSelection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1785.ThreeDViewContourOptionFirstSelection

    @classmethod
    def implicit_type(cls) -> '_1785.ThreeDViewContourOptionFirstSelection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1785.ThreeDViewContourOptionFirstSelection.type_()

    @property
    def selected_value(self) -> '_1785.ThreeDViewContourOptionFirstSelection':
        """ThreeDViewContourOptionFirstSelection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1785.ThreeDViewContourOptionFirstSelection]':
        """List[ThreeDViewContourOptionFirstSelection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionSecondSelection' types.
    """
    __qualname__ = 'ThreeDViewContourOptionSecondSelection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1786.ThreeDViewContourOptionSecondSelection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1786.ThreeDViewContourOptionSecondSelection

    @classmethod
    def implicit_type(cls) -> '_1786.ThreeDViewContourOptionSecondSelection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1786.ThreeDViewContourOptionSecondSelection.type_()

    @property
    def selected_value(self) -> '_1786.ThreeDViewContourOptionSecondSelection':
        """ThreeDViewContourOptionSecondSelection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1786.ThreeDViewContourOptionSecondSelection]':
        """List[ThreeDViewContourOptionSecondSelection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ComponentOrientationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ComponentOrientationOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComponentOrientationOption' types.
    """
    __qualname__ = 'ComponentOrientationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2318.ComponentOrientationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2318.ComponentOrientationOption

    @classmethod
    def implicit_type(cls) -> '_2318.ComponentOrientationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2318.ComponentOrientationOption.type_()

    @property
    def selected_value(self) -> '_2318.ComponentOrientationOption':
        """ComponentOrientationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2318.ComponentOrientationOption]':
        """List[ComponentOrientationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Axis(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Axis

    A specific implementation of 'EnumWithSelectedValue' for 'Axis' types.
    """
    __qualname__ = 'Axis'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1456.Axis':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1456.Axis

    @classmethod
    def implicit_type(cls) -> '_1456.Axis.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1456.Axis.type_()

    @property
    def selected_value(self) -> '_1456.Axis':
        """Axis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1456.Axis]':
        """List[Axis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AlignmentAxis(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AlignmentAxis

    A specific implementation of 'EnumWithSelectedValue' for 'AlignmentAxis' types.
    """
    __qualname__ = 'AlignmentAxis'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1455.AlignmentAxis':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1455.AlignmentAxis

    @classmethod
    def implicit_type(cls) -> '_1455.AlignmentAxis.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1455.AlignmentAxis.type_()

    @property
    def selected_value(self) -> '_1455.AlignmentAxis':
        """AlignmentAxis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1455.AlignmentAxis]':
        """List[AlignmentAxis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DesignEntityId(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DesignEntityId

    A specific implementation of 'EnumWithSelectedValue' for 'DesignEntityId' types.
    """
    __qualname__ = 'DesignEntityId'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2160.DesignEntityId':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2160.DesignEntityId

    @classmethod
    def implicit_type(cls) -> '_2160.DesignEntityId.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2160.DesignEntityId.type_()

    @property
    def selected_value(self) -> '_2160.DesignEntityId':
        """DesignEntityId: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2160.DesignEntityId]':
        """List[DesignEntityId]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThermalExpansionOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThermalExpansionOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThermalExpansionOption' types.
    """
    __qualname__ = 'ThermalExpansionOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2362.ThermalExpansionOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2362.ThermalExpansionOption

    @classmethod
    def implicit_type(cls) -> '_2362.ThermalExpansionOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2362.ThermalExpansionOption.type_()

    @property
    def selected_value(self) -> '_2362.ThermalExpansionOption':
        """ThermalExpansionOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2362.ThermalExpansionOption]':
        """List[ThermalExpansionOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FESubstructureType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FESubstructureType

    A specific implementation of 'EnumWithSelectedValue' for 'FESubstructureType' types.
    """
    __qualname__ = 'FESubstructureType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2339.FESubstructureType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2339.FESubstructureType

    @classmethod
    def implicit_type(cls) -> '_2339.FESubstructureType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2339.FESubstructureType.type_()

    @property
    def selected_value(self) -> '_2339.FESubstructureType':
        """FESubstructureType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2339.FESubstructureType]':
        """List[FESubstructureType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FEExportFormat(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FEExportFormat

    A specific implementation of 'EnumWithSelectedValue' for 'FEExportFormat' types.
    """
    __qualname__ = 'FEExportFormat'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_165.FEExportFormat':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _165.FEExportFormat

    @classmethod
    def implicit_type(cls) -> '_165.FEExportFormat.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _165.FEExportFormat.type_()

    @property
    def selected_value(self) -> '_165.FEExportFormat':
        """FEExportFormat: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_165.FEExportFormat]':
        """List[FEExportFormat]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOption' types.
    """
    __qualname__ = 'ThreeDViewContourOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1784.ThreeDViewContourOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1784.ThreeDViewContourOption

    @classmethod
    def implicit_type(cls) -> '_1784.ThreeDViewContourOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1784.ThreeDViewContourOption.type_()

    @property
    def selected_value(self) -> '_1784.ThreeDViewContourOption':
        """ThreeDViewContourOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1784.ThreeDViewContourOption]':
        """List[ThreeDViewContourOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BoundaryConditionType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BoundaryConditionType

    A specific implementation of 'EnumWithSelectedValue' for 'BoundaryConditionType' types.
    """
    __qualname__ = 'BoundaryConditionType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_164.BoundaryConditionType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _164.BoundaryConditionType

    @classmethod
    def implicit_type(cls) -> '_164.BoundaryConditionType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _164.BoundaryConditionType.type_()

    @property
    def selected_value(self) -> '_164.BoundaryConditionType':
        """BoundaryConditionType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_164.BoundaryConditionType]':
        """List[BoundaryConditionType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingNodeOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingNodeOption

    A specific implementation of 'EnumWithSelectedValue' for 'BearingNodeOption' types.
    """
    __qualname__ = 'BearingNodeOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2315.BearingNodeOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2315.BearingNodeOption

    @classmethod
    def implicit_type(cls) -> '_2315.BearingNodeOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2315.BearingNodeOption.type_()

    @property
    def selected_value(self) -> '_2315.BearingNodeOption':
        """BearingNodeOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2315.BearingNodeOption]':
        """List[BearingNodeOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LinkNodeSource(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LinkNodeSource

    A specific implementation of 'EnumWithSelectedValue' for 'LinkNodeSource' types.
    """
    __qualname__ = 'LinkNodeSource'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2349.LinkNodeSource':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2349.LinkNodeSource

    @classmethod
    def implicit_type(cls) -> '_2349.LinkNodeSource.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2349.LinkNodeSource.type_()

    @property
    def selected_value(self) -> '_2349.LinkNodeSource':
        """LinkNodeSource: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2349.LinkNodeSource]':
        """List[LinkNodeSource]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingToleranceClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingToleranceClass

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceClass' types.
    """
    __qualname__ = 'BearingToleranceClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1864.BearingToleranceClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1864.BearingToleranceClass

    @classmethod
    def implicit_type(cls) -> '_1864.BearingToleranceClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1864.BearingToleranceClass.type_()

    @property
    def selected_value(self) -> '_1864.BearingToleranceClass':
        """BearingToleranceClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1864.BearingToleranceClass]':
        """List[BearingToleranceClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingModel' types.
    """
    __qualname__ = 'BearingModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1838.BearingModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1838.BearingModel

    @classmethod
    def implicit_type(cls) -> '_1838.BearingModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1838.BearingModel.type_()

    @property
    def selected_value(self) -> '_1838.BearingModel':
        """BearingModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1838.BearingModel]':
        """List[BearingModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PreloadType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PreloadType

    A specific implementation of 'EnumWithSelectedValue' for 'PreloadType' types.
    """
    __qualname__ = 'PreloadType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1921.PreloadType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1921.PreloadType

    @classmethod
    def implicit_type(cls) -> '_1921.PreloadType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1921.PreloadType.type_()

    @property
    def selected_value(self) -> '_1921.PreloadType':
        """PreloadType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1921.PreloadType]':
        """List[PreloadType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RaceAxialMountingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RaceAxialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceAxialMountingType' types.
    """
    __qualname__ = 'RaceAxialMountingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1923.RaceAxialMountingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1923.RaceAxialMountingType

    @classmethod
    def implicit_type(cls) -> '_1923.RaceAxialMountingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1923.RaceAxialMountingType.type_()

    @property
    def selected_value(self) -> '_1923.RaceAxialMountingType':
        """RaceAxialMountingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1923.RaceAxialMountingType]':
        """List[RaceAxialMountingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RaceRadialMountingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RaceRadialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceRadialMountingType' types.
    """
    __qualname__ = 'RaceRadialMountingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1924.RaceRadialMountingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1924.RaceRadialMountingType

    @classmethod
    def implicit_type(cls) -> '_1924.RaceRadialMountingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1924.RaceRadialMountingType.type_()

    @property
    def selected_value(self) -> '_1924.RaceRadialMountingType':
        """RaceRadialMountingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1924.RaceRadialMountingType]':
        """List[RaceRadialMountingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_InternalClearanceClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_InternalClearanceClass

    A specific implementation of 'EnumWithSelectedValue' for 'InternalClearanceClass' types.
    """
    __qualname__ = 'InternalClearanceClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1863.InternalClearanceClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1863.InternalClearanceClass

    @classmethod
    def implicit_type(cls) -> '_1863.InternalClearanceClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1863.InternalClearanceClass.type_()

    @property
    def selected_value(self) -> '_1863.InternalClearanceClass':
        """InternalClearanceClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1863.InternalClearanceClass]':
        """List[InternalClearanceClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingToleranceDefinitionOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingToleranceDefinitionOptions

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceDefinitionOptions' types.
    """
    __qualname__ = 'BearingToleranceDefinitionOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1865.BearingToleranceDefinitionOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1865.BearingToleranceDefinitionOptions

    @classmethod
    def implicit_type(cls) -> '_1865.BearingToleranceDefinitionOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1865.BearingToleranceDefinitionOptions.type_()

    @property
    def selected_value(self) -> '_1865.BearingToleranceDefinitionOptions':
        """BearingToleranceDefinitionOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1865.BearingToleranceDefinitionOptions]':
        """List[BearingToleranceDefinitionOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_OilSealLossCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_OilSealLossCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'OilSealLossCalculationMethod' types.
    """
    __qualname__ = 'OilSealLossCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_294.OilSealLossCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _294.OilSealLossCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_294.OilSealLossCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _294.OilSealLossCalculationMethod.type_()

    @property
    def selected_value(self) -> '_294.OilSealLossCalculationMethod':
        """OilSealLossCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_294.OilSealLossCalculationMethod]':
        """List[OilSealLossCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PowerLoadType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PowerLoadType

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadType' types.
    """
    __qualname__ = 'PowerLoadType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2174.PowerLoadType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2174.PowerLoadType

    @classmethod
    def implicit_type(cls) -> '_2174.PowerLoadType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2174.PowerLoadType.type_()

    @property
    def selected_value(self) -> '_2174.PowerLoadType':
        """PowerLoadType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2174.PowerLoadType]':
        """List[PowerLoadType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorStiffnessType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorStiffnessType

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorStiffnessType' types.
    """
    __qualname__ = 'RigidConnectorStiffnessType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2542.RigidConnectorStiffnessType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2542.RigidConnectorStiffnessType

    @classmethod
    def implicit_type(cls) -> '_2542.RigidConnectorStiffnessType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2542.RigidConnectorStiffnessType.type_()

    @property
    def selected_value(self) -> '_2542.RigidConnectorStiffnessType':
        """RigidConnectorStiffnessType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2542.RigidConnectorStiffnessType]':
        """List[RigidConnectorStiffnessType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorToothSpacingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorToothSpacingType

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorToothSpacingType' types.
    """
    __qualname__ = 'RigidConnectorToothSpacingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2545.RigidConnectorToothSpacingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2545.RigidConnectorToothSpacingType

    @classmethod
    def implicit_type(cls) -> '_2545.RigidConnectorToothSpacingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2545.RigidConnectorToothSpacingType.type_()

    @property
    def selected_value(self) -> '_2545.RigidConnectorToothSpacingType':
        """RigidConnectorToothSpacingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2545.RigidConnectorToothSpacingType]':
        """List[RigidConnectorToothSpacingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorTypes' types.
    """
    __qualname__ = 'RigidConnectorTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2546.RigidConnectorTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2546.RigidConnectorTypes

    @classmethod
    def implicit_type(cls) -> '_2546.RigidConnectorTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2546.RigidConnectorTypes.type_()

    @property
    def selected_value(self) -> '_2546.RigidConnectorTypes':
        """RigidConnectorTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2546.RigidConnectorTypes]':
        """List[RigidConnectorTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FitTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FitTypes

    A specific implementation of 'EnumWithSelectedValue' for 'FitTypes' types.
    """
    __qualname__ = 'FitTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1361.FitTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1361.FitTypes

    @classmethod
    def implicit_type(cls) -> '_1361.FitTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1361.FitTypes.type_()

    @property
    def selected_value(self) -> '_1361.FitTypes':
        """FitTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1361.FitTypes]':
        """List[FitTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DoeValueSpecificationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DoeValueSpecificationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DoeValueSpecificationOption' types.
    """
    __qualname__ = 'DoeValueSpecificationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_4291.DoeValueSpecificationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4291.DoeValueSpecificationOption

    @classmethod
    def implicit_type(cls) -> '_4291.DoeValueSpecificationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4291.DoeValueSpecificationOption.type_()

    @property
    def selected_value(self) -> '_4291.DoeValueSpecificationOption':
        """DoeValueSpecificationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_4291.DoeValueSpecificationOption]':
        """List[DoeValueSpecificationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AnalysisType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AnalysisType

    A specific implementation of 'EnumWithSelectedValue' for 'AnalysisType' types.
    """
    __qualname__ = 'AnalysisType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6744.AnalysisType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6744.AnalysisType

    @classmethod
    def implicit_type(cls) -> '_6744.AnalysisType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6744.AnalysisType.type_()

    @property
    def selected_value(self) -> '_6744.AnalysisType':
        """AnalysisType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6744.AnalysisType]':
        """List[AnalysisType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BarModelExportType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BarModelExportType

    A specific implementation of 'EnumWithSelectedValue' for 'BarModelExportType' types.
    """
    __qualname__ = 'BarModelExportType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_53.BarModelExportType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _53.BarModelExportType

    @classmethod
    def implicit_type(cls) -> '_53.BarModelExportType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _53.BarModelExportType.type_()

    @property
    def selected_value(self) -> '_53.BarModelExportType':
        """BarModelExportType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_53.BarModelExportType]':
        """List[BarModelExportType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ComplexPartDisplayOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ComplexPartDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComplexPartDisplayOption' types.
    """
    __qualname__ = 'ComplexPartDisplayOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1459.ComplexPartDisplayOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1459.ComplexPartDisplayOption

    @classmethod
    def implicit_type(cls) -> '_1459.ComplexPartDisplayOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1459.ComplexPartDisplayOption.type_()

    @property
    def selected_value(self) -> '_1459.ComplexPartDisplayOption':
        """ComplexPartDisplayOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1459.ComplexPartDisplayOption]':
        """List[ComplexPartDisplayOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DynamicsResponseType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DynamicsResponseType

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseType' types.
    """
    __qualname__ = 'DynamicsResponseType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_4568.DynamicsResponseType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4568.DynamicsResponseType

    @classmethod
    def implicit_type(cls) -> '_4568.DynamicsResponseType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4568.DynamicsResponseType.type_()

    @property
    def selected_value(self) -> '_4568.DynamicsResponseType':
        """DynamicsResponseType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_4568.DynamicsResponseType]':
        """List[DynamicsResponseType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingStiffnessModel' types.
    """
    __qualname__ = 'BearingStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5323.BearingStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5323.BearingStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_5323.BearingStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5323.BearingStiffnessModel.type_()

    @property
    def selected_value(self) -> '_5323.BearingStiffnessModel':
        """BearingStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5323.BearingStiffnessModel]':
        """List[BearingStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_GearMeshStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_GearMeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'GearMeshStiffnessModel' types.
    """
    __qualname__ = 'GearMeshStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5375.GearMeshStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5375.GearMeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_5375.GearMeshStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5375.GearMeshStiffnessModel.type_()

    @property
    def selected_value(self) -> '_5375.GearMeshStiffnessModel':
        """GearMeshStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5375.GearMeshStiffnessModel]':
        """List[GearMeshStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShaftAndHousingFlexibilityOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftAndHousingFlexibilityOption

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftAndHousingFlexibilityOption' types.
    """
    __qualname__ = 'ShaftAndHousingFlexibilityOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5420.ShaftAndHousingFlexibilityOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5420.ShaftAndHousingFlexibilityOption

    @classmethod
    def implicit_type(cls) -> '_5420.ShaftAndHousingFlexibilityOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5420.ShaftAndHousingFlexibilityOption.type_()

    @property
    def selected_value(self) -> '_5420.ShaftAndHousingFlexibilityOption':
        """ShaftAndHousingFlexibilityOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5420.ShaftAndHousingFlexibilityOption]':
        """List[ShaftAndHousingFlexibilityOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExportOutputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExportOutputType

    A specific implementation of 'EnumWithSelectedValue' for 'ExportOutputType' types.
    """
    __qualname__ = 'ExportOutputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5679.ExportOutputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5679.ExportOutputType

    @classmethod
    def implicit_type(cls) -> '_5679.ExportOutputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5679.ExportOutputType.type_()

    @property
    def selected_value(self) -> '_5679.ExportOutputType':
        """ExportOutputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5679.ExportOutputType]':
        """List[ExportOutputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput' types.
    """
    __qualname__ = 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5697.HarmonicAnalysisFEExportOptions.ComplexNumberOutput':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5697.HarmonicAnalysisFEExportOptions.ComplexNumberOutput

    @classmethod
    def implicit_type(cls) -> '_5697.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5697.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()

    @property
    def selected_value(self) -> '_5697.HarmonicAnalysisFEExportOptions.ComplexNumberOutput':
        """HarmonicAnalysisFEExportOptions.ComplexNumberOutput: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5697.HarmonicAnalysisFEExportOptions.ComplexNumberOutput]':
        """List[HarmonicAnalysisFEExportOptions.ComplexNumberOutput]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FrictionModelForGyroscopicMoment(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FrictionModelForGyroscopicMoment

    A specific implementation of 'EnumWithSelectedValue' for 'FrictionModelForGyroscopicMoment' types.
    """
    __qualname__ = 'FrictionModelForGyroscopicMoment'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1932.FrictionModelForGyroscopicMoment':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1932.FrictionModelForGyroscopicMoment

    @classmethod
    def implicit_type(cls) -> '_1932.FrictionModelForGyroscopicMoment.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1932.FrictionModelForGyroscopicMoment.type_()

    @property
    def selected_value(self) -> '_1932.FrictionModelForGyroscopicMoment':
        """FrictionModelForGyroscopicMoment: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1932.FrictionModelForGyroscopicMoment]':
        """List[FrictionModelForGyroscopicMoment]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MeshStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'MeshStiffnessModel' types.
    """
    __qualname__ = 'MeshStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2169.MeshStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2169.MeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_2169.MeshStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2169.MeshStiffnessModel.type_()

    @property
    def selected_value(self) -> '_2169.MeshStiffnessModel':
        """MeshStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2169.MeshStiffnessModel]':
        """List[MeshStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShearAreaFactorMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShearAreaFactorMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ShearAreaFactorMethod' types.
    """
    __qualname__ = 'ShearAreaFactorMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_129.ShearAreaFactorMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _129.ShearAreaFactorMethod

    @classmethod
    def implicit_type(cls) -> '_129.ShearAreaFactorMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _129.ShearAreaFactorMethod.type_()

    @property
    def selected_value(self) -> '_129.ShearAreaFactorMethod':
        """ShearAreaFactorMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_129.ShearAreaFactorMethod]':
        """List[ShearAreaFactorMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StressConcentrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StressConcentrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'StressConcentrationMethod' types.
    """
    __qualname__ = 'StressConcentrationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2065.StressConcentrationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2065.StressConcentrationMethod

    @classmethod
    def implicit_type(cls) -> '_2065.StressConcentrationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2065.StressConcentrationMethod.type_()

    @property
    def selected_value(self) -> '_2065.StressConcentrationMethod':
        """StressConcentrationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2065.StressConcentrationMethod]':
        """List[StressConcentrationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BallBearingAnalysisMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BallBearingAnalysisMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BallBearingAnalysisMethod' types.
    """
    __qualname__ = 'BallBearingAnalysisMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1926.BallBearingAnalysisMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1926.BallBearingAnalysisMethod

    @classmethod
    def implicit_type(cls) -> '_1926.BallBearingAnalysisMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1926.BallBearingAnalysisMethod.type_()

    @property
    def selected_value(self) -> '_1926.BallBearingAnalysisMethod':
        """BallBearingAnalysisMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1926.BallBearingAnalysisMethod]':
        """List[BallBearingAnalysisMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'HertzianContactDeflectionCalculationMethod' types.
    """
    __qualname__ = 'HertzianContactDeflectionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1538.HertzianContactDeflectionCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1538.HertzianContactDeflectionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1538.HertzianContactDeflectionCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1538.HertzianContactDeflectionCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1538.HertzianContactDeflectionCalculationMethod':
        """HertzianContactDeflectionCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1538.HertzianContactDeflectionCalculationMethod]':
        """List[HertzianContactDeflectionCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueRippleInputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueRippleInputType

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueRippleInputType' types.
    """
    __qualname__ = 'TorqueRippleInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6902.TorqueRippleInputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6902.TorqueRippleInputType

    @classmethod
    def implicit_type(cls) -> '_6902.TorqueRippleInputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6902.TorqueRippleInputType.type_()

    @property
    def selected_value(self) -> '_6902.TorqueRippleInputType':
        """TorqueRippleInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6902.TorqueRippleInputType]':
        """List[TorqueRippleInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicExcitationType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicExcitationType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicExcitationType' types.
    """
    __qualname__ = 'HarmonicExcitationType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6823.HarmonicExcitationType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6823.HarmonicExcitationType

    @classmethod
    def implicit_type(cls) -> '_6823.HarmonicExcitationType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6823.HarmonicExcitationType.type_()

    @property
    def selected_value(self) -> '_6823.HarmonicExcitationType':
        """HarmonicExcitationType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6823.HarmonicExcitationType]':
        """List[HarmonicExcitationType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification

    A specific implementation of 'EnumWithSelectedValue' for 'PointLoadLoadCase.ForceSpecification' types.
    """
    __qualname__ = 'PointLoadLoadCase.ForceSpecification'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6864.PointLoadLoadCase.ForceSpecification':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6864.PointLoadLoadCase.ForceSpecification

    @classmethod
    def implicit_type(cls) -> '_6864.PointLoadLoadCase.ForceSpecification.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6864.PointLoadLoadCase.ForceSpecification.type_()

    @property
    def selected_value(self) -> '_6864.PointLoadLoadCase.ForceSpecification':
        """PointLoadLoadCase.ForceSpecification: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6864.PointLoadLoadCase.ForceSpecification]':
        """List[PointLoadLoadCase.ForceSpecification]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueSpecificationForSystemDeflection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueSpecificationForSystemDeflection

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueSpecificationForSystemDeflection' types.
    """
    __qualname__ = 'TorqueSpecificationForSystemDeflection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6903.TorqueSpecificationForSystemDeflection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6903.TorqueSpecificationForSystemDeflection

    @classmethod
    def implicit_type(cls) -> '_6903.TorqueSpecificationForSystemDeflection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6903.TorqueSpecificationForSystemDeflection.type_()

    @property
    def selected_value(self) -> '_6903.TorqueSpecificationForSystemDeflection':
        """TorqueSpecificationForSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6903.TorqueSpecificationForSystemDeflection]':
        """List[TorqueSpecificationForSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadInputTorqueSpecificationMethod' types.
    """
    __qualname__ = 'PowerLoadInputTorqueSpecificationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2172.PowerLoadInputTorqueSpecificationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2172.PowerLoadInputTorqueSpecificationMethod

    @classmethod
    def implicit_type(cls) -> '_2172.PowerLoadInputTorqueSpecificationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2172.PowerLoadInputTorqueSpecificationMethod.type_()

    @property
    def selected_value(self) -> '_2172.PowerLoadInputTorqueSpecificationMethod':
        """PowerLoadInputTorqueSpecificationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2172.PowerLoadInputTorqueSpecificationMethod]':
        """List[PowerLoadInputTorqueSpecificationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueConverterLockupRule(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueConverterLockupRule

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueConverterLockupRule' types.
    """
    __qualname__ = 'TorqueConverterLockupRule'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5445.TorqueConverterLockupRule':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5445.TorqueConverterLockupRule

    @classmethod
    def implicit_type(cls) -> '_5445.TorqueConverterLockupRule.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5445.TorqueConverterLockupRule.type_()

    @property
    def selected_value(self) -> '_5445.TorqueConverterLockupRule':
        """TorqueConverterLockupRule: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5445.TorqueConverterLockupRule]':
        """List[TorqueConverterLockupRule]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DegreesOfFreedom(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DegreesOfFreedom

    A specific implementation of 'EnumWithSelectedValue' for 'DegreesOfFreedom' types.
    """
    __qualname__ = 'DegreesOfFreedom'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1468.DegreesOfFreedom':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1468.DegreesOfFreedom

    @classmethod
    def implicit_type(cls) -> '_1468.DegreesOfFreedom.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1468.DegreesOfFreedom.type_()

    @property
    def selected_value(self) -> '_1468.DegreesOfFreedom':
        """DegreesOfFreedom: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1468.DegreesOfFreedom]':
        """List[DegreesOfFreedom]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DestinationDesignState(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DestinationDesignState

    A specific implementation of 'EnumWithSelectedValue' for 'DestinationDesignState' types.
    """
    __qualname__ = 'DestinationDesignState'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6917.DestinationDesignState':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6917.DestinationDesignState

    @classmethod
    def implicit_type(cls) -> '_6917.DestinationDesignState.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6917.DestinationDesignState.type_()

    @property
    def selected_value(self) -> '_6917.DestinationDesignState':
        """DestinationDesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6917.DestinationDesignState]':
        """List[DestinationDesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None
