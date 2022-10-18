"""_752.py

PlungeShavingDynamicsCalculationForHobbedGears
"""


from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _761, _748
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'PlungeShavingDynamicsCalculationForHobbedGears')


__docformat__ = 'restructuredtext en'
__all__ = ('PlungeShavingDynamicsCalculationForHobbedGears',)


class PlungeShavingDynamicsCalculationForHobbedGears(_761.ShavingDynamicsCalculationForHobbedGears['_748.PlungeShaverDynamics']):
    """PlungeShavingDynamicsCalculationForHobbedGears

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS

    def __init__(self, instance_to_wrap: 'PlungeShavingDynamicsCalculationForHobbedGears.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
