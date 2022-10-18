"""_666.py

HobbingProcessSimulationNew
"""


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _660, _661, _662, _663,
    _664, _668, _679, _665
)
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_SIMULATION_NEW = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessSimulationNew')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessSimulationNew',)


class HobbingProcessSimulationNew(_679.ProcessSimulationNew['_665.HobbingProcessSimulationInput']):
    """HobbingProcessSimulationNew

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_SIMULATION_NEW

    def __init__(self, instance_to_wrap: 'HobbingProcessSimulationNew.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hobbing_process_gear_shape_calculation(self) -> '_660.HobbingProcessGearShape':
        """HobbingProcessGearShape: 'HobbingProcessGearShapeCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessGearShapeCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_lead_calculation(self) -> '_661.HobbingProcessLeadCalculation':
        """HobbingProcessLeadCalculation: 'HobbingProcessLeadCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessLeadCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_mark_on_shaft_calculation(self) -> '_662.HobbingProcessMarkOnShaft':
        """HobbingProcessMarkOnShaft: 'HobbingProcessMarkOnShaftCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessMarkOnShaftCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_pitch_calculation(self) -> '_663.HobbingProcessPitchCalculation':
        """HobbingProcessPitchCalculation: 'HobbingProcessPitchCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessPitchCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_profile_calculation(self) -> '_664.HobbingProcessProfileCalculation':
        """HobbingProcessProfileCalculation: 'HobbingProcessProfileCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessProfileCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_total_modification(self) -> '_668.HobbingProcessTotalModificationCalculation':
        """HobbingProcessTotalModificationCalculation: 'HobbingProcessTotalModification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessTotalModification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
