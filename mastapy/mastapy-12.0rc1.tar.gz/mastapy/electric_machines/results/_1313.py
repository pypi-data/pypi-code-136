"""_1313.py

NonLinearDQModel
"""


from mastapy.utility_gui.charts import (
    _1825, _1827, _1813, _1820,
    _1822
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines.results import _1314, _1298
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'NonLinearDQModel')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearDQModel',)


class NonLinearDQModel(_1298.ElectricMachineDQModel):
    """NonLinearDQModel

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_DQ_MODEL

    def __init__(self, instance_to_wrap: 'NonLinearDQModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alignment_torque_map_at_reference_temperatures(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'AlignmentTorqueMapAtReferenceTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AlignmentTorqueMapAtReferenceTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def d_axis_armature_flux_linkage_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'DAxisArmatureFluxLinkageMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisArmatureFluxLinkageMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def number_of_current_angle_values(self) -> 'int':
        """int: 'NumberOfCurrentAngleValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfCurrentAngleValues

        if temp is None:
            return 0

        return temp

    @property
    def number_of_current_values(self) -> 'int':
        """int: 'NumberOfCurrentValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfCurrentValues

        if temp is None:
            return 0

        return temp

    @property
    def q_axis_armature_flux_linkage_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'QAxisArmatureFluxLinkageMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisArmatureFluxLinkageMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def reluctance_torque_map_at_reference_temperatures(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'ReluctanceTorqueMapAtReferenceTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReluctanceTorqueMapAtReferenceTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_eddy_current_loss_per_frequency_exponent_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorEddyCurrentLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorEddyCurrentLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_excess_loss_per_frequency_exponent_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorExcessLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorExcessLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_hysteresis_loss_per_frequency_exponent_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorHysteresisLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorHysteresisLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_eddy_current_loss_per_frequency_exponent_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorEddyCurrentLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorEddyCurrentLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_excess_loss_per_frequency_exponent_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorExcessLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorExcessLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_hysteresis_loss_per_frequency_exponent_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorHysteresisLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorHysteresisLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_taken_to_generate_non_linear_dq_model(self) -> 'float':
        """float: 'TimeTakenToGenerateNonLinearDQModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeTakenToGenerateNonLinearDQModel

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_map_at_reference_temperatures(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TorqueMapAtReferenceTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueMapAtReferenceTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def torque_at_max_current_and_reference_temperatures(self) -> '_1827.TwoDChartDefinition':
        """TwoDChartDefinition: 'TorqueAtMaxCurrentAndReferenceTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueAtMaxCurrentAndReferenceTemperatures

        if temp is None:
            return None

        if _1827.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast torque_at_max_current_and_reference_temperatures to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def non_linear_dq_model_generator_settings(self) -> '_1314.NonLinearDQModelSettings':
        """NonLinearDQModelSettings: 'NonLinearDQModelGeneratorSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonLinearDQModelGeneratorSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
