"""_895.py

BarForPareto
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy.math_utility.optimisation import _1514
from mastapy.gears.analysis import _1207
from mastapy._internal.python_net import python_net_import

_BAR_FOR_PARETO = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'BarForPareto')


__docformat__ = 'restructuredtext en'
__all__ = ('BarForPareto',)


TAnalysis = TypeVar('TAnalysis', bound='_1207.AbstractGearSetAnalysis')
TCandidate = TypeVar('TCandidate')


class BarForPareto(_1514.ParetoOptimisationStrategyBars, Generic[TAnalysis, TCandidate]):
    """BarForPareto

    This is a mastapy class.

    Generic Types:
        TAnalysis
        TCandidate
    """

    TYPE = _BAR_FOR_PARETO

    def __init__(self, instance_to_wrap: 'BarForPareto.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def remove_bar(self):
        """ 'RemoveBar' is the original name of this method."""

        self.wrapped.RemoveBar()
