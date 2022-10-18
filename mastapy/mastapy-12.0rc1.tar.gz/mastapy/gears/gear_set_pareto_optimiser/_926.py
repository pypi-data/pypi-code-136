"""_926.py

ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
"""


from mastapy.gears.gear_set_pareto_optimiser import _916
from mastapy._internal.python_net import python_net_import

_PARETO_SPIRAL_BEVEL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase',)


class ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase(_916.ParetoConicalRatingOptimisationStrategyDatabase):
    """ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_SPIRAL_BEVEL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE

    def __init__(self, instance_to_wrap: 'ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
