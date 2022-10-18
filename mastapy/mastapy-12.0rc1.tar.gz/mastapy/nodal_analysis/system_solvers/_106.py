"""_106.py

NewmarkAccelerationTransientSolver
"""


from mastapy.nodal_analysis.system_solvers import _109
from mastapy._internal.python_net import python_net_import

_NEWMARK_ACCELERATION_TRANSIENT_SOLVER = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'NewmarkAccelerationTransientSolver')


__docformat__ = 'restructuredtext en'
__all__ = ('NewmarkAccelerationTransientSolver',)


class NewmarkAccelerationTransientSolver(_109.SimpleAccelerationBasedStepHalvingTransientSolver):
    """NewmarkAccelerationTransientSolver

    This is a mastapy class.
    """

    TYPE = _NEWMARK_ACCELERATION_TRANSIENT_SOLVER

    def __init__(self, instance_to_wrap: 'NewmarkAccelerationTransientSolver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
