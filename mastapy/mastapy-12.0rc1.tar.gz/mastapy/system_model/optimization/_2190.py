"""_2190.py

OptimizationStrategy
"""


from typing import Generic, TypeVar

from mastapy.system_model.optimization import _2191, _2189
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'OptimizationStrategy')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationStrategy',)


TStep = TypeVar('TStep', bound='_2189.OptimizationStep')


class OptimizationStrategy(_2191.OptimizationStrategyBase, Generic[TStep]):
    """OptimizationStrategy

    This is a mastapy class.

    Generic Types:
        TStep
    """

    TYPE = _OPTIMIZATION_STRATEGY

    def __init__(self, instance_to_wrap: 'OptimizationStrategy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
