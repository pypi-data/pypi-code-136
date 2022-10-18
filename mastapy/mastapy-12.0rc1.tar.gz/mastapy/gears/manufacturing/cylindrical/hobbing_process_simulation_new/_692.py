"""_692.py

WormGrindingProcessSimulationInput
"""


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _684, _678
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_INPUT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessSimulationInput')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessSimulationInput',)


class WormGrindingProcessSimulationInput(_678.ProcessSimulationInput):
    """WormGrindingProcessSimulationInput

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_INPUT

    def __init__(self, instance_to_wrap: 'WormGrindingProcessSimulationInput.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinder_manufacture_error(self) -> '_684.WormGrinderManufactureError':
        """WormGrinderManufactureError: 'WormGrinderManufactureError' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrinderManufactureError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
