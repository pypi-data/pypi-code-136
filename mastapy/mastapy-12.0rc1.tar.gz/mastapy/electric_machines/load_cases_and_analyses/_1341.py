"""_1341.py

SpeedTorqueCurveAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1342, _1321
from mastapy.electric_machines.results import _1312
from mastapy._internal.python_net import python_net_import

_SPEED_TORQUE_CURVE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SpeedTorqueCurveAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedTorqueCurveAnalysis',)


class SpeedTorqueCurveAnalysis(_1321.ElectricMachineAnalysis):
    """SpeedTorqueCurveAnalysis

    This is a mastapy class.
    """

    TYPE = _SPEED_TORQUE_CURVE_ANALYSIS

    def __init__(self, instance_to_wrap: 'SpeedTorqueCurveAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_speed(self) -> 'float':
        """float: 'BaseSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_speed(self) -> 'float':
        """float: 'MaximumSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_torque_at_rated_inverter_current(self) -> 'float':
        """float: 'MaximumTorqueAtRatedInverterCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTorqueAtRatedInverterCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_magnet_flux_linkage_at_reference_temperature(self) -> 'float':
        """float: 'PermanentMagnetFluxLinkageAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentMagnetFluxLinkageAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case(self) -> '_1342.SpeedTorqueCurveLoadCase':
        """SpeedTorqueCurveLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_points(self) -> 'List[_1312.MaximumTorqueResultsPoints]':
        """List[MaximumTorqueResultsPoints]: 'ResultsPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
