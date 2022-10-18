"""_1337.py

SingleOperatingPointAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.results import _1301
from mastapy.electric_machines.load_cases_and_analyses import (
    _1326, _1343, _1338, _1321
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_OPERATING_POINT_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SingleOperatingPointAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleOperatingPointAnalysis',)


class SingleOperatingPointAnalysis(_1321.ElectricMachineAnalysis):
    """SingleOperatingPointAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGLE_OPERATING_POINT_ANALYSIS

    def __init__(self, instance_to_wrap: 'SingleOperatingPointAnalysis.TYPE'):
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
    def electrical_frequency(self) -> 'float':
        """float: 'ElectricalFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_period(self) -> 'float':
        """float: 'ElectricalPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def mechanical_period(self) -> 'float':
        """float: 'MechanicalPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MechanicalPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_line_current(self) -> 'float':
        """float: 'PeakLineCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakLineCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_phase_current(self) -> 'float':
        """float: 'PeakPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakPhaseCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_current_drms(self) -> 'float':
        """float: 'PhaseCurrentDRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseCurrentDRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_current_qrms(self) -> 'float':
        """float: 'PhaseCurrentQRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseCurrentQRMS

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
    def rms_phase_current(self) -> 'float':
        """float: 'RMSPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RMSPhaseCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def slot_passing_period(self) -> 'float':
        """float: 'SlotPassingPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlotPassingPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def time_step_increment(self) -> 'float':
        """float: 'TimeStepIncrement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeStepIncrement

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_results(self) -> '_1301.ElectricMachineResultsForOpenCircuitAndOnLoad':
        """ElectricMachineResultsForOpenCircuitAndOnLoad: 'ElectricMachineResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case(self) -> '_1326.ElectricMachineLoadCase':
        """ElectricMachineLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        if _1326.ElectricMachineLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast load_case to ElectricMachineLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def slot_section_details_for_analysis(self) -> 'List[_1338.SlotDetailForAnalysis]':
        """List[SlotDetailForAnalysis]: 'SlotSectionDetailsForAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlotSectionDetailsForAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
