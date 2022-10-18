"""_1312.py

MaximumTorqueResultsPoints
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_MAXIMUM_TORQUE_RESULTS_POINTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'MaximumTorqueResultsPoints')


__docformat__ = 'restructuredtext en'
__all__ = ('MaximumTorqueResultsPoints',)


class MaximumTorqueResultsPoints(_0.APIBase):
    """MaximumTorqueResultsPoints

    This is a mastapy class.
    """

    TYPE = _MAXIMUM_TORQUE_RESULTS_POINTS

    def __init__(self, instance_to_wrap: 'MaximumTorqueResultsPoints.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_angle(self) -> 'float':
        """float: 'CurrentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_current(self) -> 'float':
        """float: 'DAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_flux_linkage(self) -> 'float':
        """float: 'DAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_voltage(self) -> 'float':
        """float: 'DAxisVoltage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_speed(self) -> 'float':
        """float: 'ElectricalSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_phase_current_magnitude(self) -> 'float':
        """float: 'PeakPhaseCurrentMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakPhaseCurrentMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_phase_voltage(self) -> 'float':
        """float: 'PeakPhaseVoltage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakPhaseVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def power(self) -> 'float':
        """float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_current(self) -> 'float':
        """float: 'QAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_flux_linkage(self) -> 'float':
        """float: 'QAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_voltage(self) -> 'float':
        """float: 'QAxisVoltage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp
