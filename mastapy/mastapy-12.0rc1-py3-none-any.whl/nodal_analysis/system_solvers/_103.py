"""_103.py

InternalTransientSolver
"""


from mastapy.nodal_analysis.system_solvers import _117
from mastapy._internal.python_net import python_net_import

_INTERNAL_TRANSIENT_SOLVER = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'InternalTransientSolver')


__docformat__ = 'restructuredtext en'
__all__ = ('InternalTransientSolver',)


class InternalTransientSolver(_117.TransientSolver):
    """InternalTransientSolver

    This is a mastapy class.
    """

    TYPE = _INTERNAL_TRANSIENT_SOLVER

    def __init__(self, instance_to_wrap: 'InternalTransientSolver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
