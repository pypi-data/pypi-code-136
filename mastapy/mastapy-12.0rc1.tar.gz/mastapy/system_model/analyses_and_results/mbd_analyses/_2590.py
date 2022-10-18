"""_2590.py

MultibodyDynamicsAnalysis
"""


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
from mastapy.nodal_analysis.system_solvers import (
    _117, _99, _100, _103,
    _104, _105, _106, _107,
    _108, _109, _110, _115,
    _118
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.analysis_cases import _7475
from mastapy._internal.python_net import python_net_import

_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'MultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MultibodyDynamicsAnalysis',)


class MultibodyDynamicsAnalysis(_7475.TimeSeriesLoadAnalysisCase):
    """MultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'MultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_interface_analysis_results_available(self) -> 'bool':
        """bool: 'HasInterfaceAnalysisResultsAvailable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasInterfaceAnalysisResultsAvailable

        if temp is None:
            return False

        return temp

    @property
    def percentage_time_spent_in_masta_solver(self) -> 'float':
        """float: 'PercentageTimeSpentInMASTASolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageTimeSpentInMASTASolver

        if temp is None:
            return 0.0

        return temp

    @property
    def mbd_options(self) -> '_5398.MBDAnalysisOptions':
        """MBDAnalysisOptions: 'MBDOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MBDOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver(self) -> '_117.TransientSolver':
        """TransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _117.TransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to TransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_backward_euler_acceleration_step_halving_transient_solver(self) -> '_99.BackwardEulerAccelerationStepHalvingTransientSolver':
        """BackwardEulerAccelerationStepHalvingTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _99.BackwardEulerAccelerationStepHalvingTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to BackwardEulerAccelerationStepHalvingTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_backward_euler_transient_solver(self) -> '_100.BackwardEulerTransientSolver':
        """BackwardEulerTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _100.BackwardEulerTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to BackwardEulerTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_internal_transient_solver(self) -> '_103.InternalTransientSolver':
        """InternalTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _103.InternalTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to InternalTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_lobatto_iiia_transient_solver(self) -> '_104.LobattoIIIATransientSolver':
        """LobattoIIIATransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _104.LobattoIIIATransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to LobattoIIIATransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_lobatto_iiic_transient_solver(self) -> '_105.LobattoIIICTransientSolver':
        """LobattoIIICTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _105.LobattoIIICTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to LobattoIIICTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_newmark_acceleration_transient_solver(self) -> '_106.NewmarkAccelerationTransientSolver':
        """NewmarkAccelerationTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _106.NewmarkAccelerationTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to NewmarkAccelerationTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_newmark_transient_solver(self) -> '_107.NewmarkTransientSolver':
        """NewmarkTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _107.NewmarkTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to NewmarkTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_semi_implicit_transient_solver(self) -> '_108.SemiImplicitTransientSolver':
        """SemiImplicitTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _108.SemiImplicitTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to SemiImplicitTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_simple_acceleration_based_step_halving_transient_solver(self) -> '_109.SimpleAccelerationBasedStepHalvingTransientSolver':
        """SimpleAccelerationBasedStepHalvingTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _109.SimpleAccelerationBasedStepHalvingTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to SimpleAccelerationBasedStepHalvingTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_simple_velocity_based_step_halving_transient_solver(self) -> '_110.SimpleVelocityBasedStepHalvingTransientSolver':
        """SimpleVelocityBasedStepHalvingTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _110.SimpleVelocityBasedStepHalvingTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to SimpleVelocityBasedStepHalvingTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_step_halving_transient_solver(self) -> '_115.StepHalvingTransientSolver':
        """StepHalvingTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _115.StepHalvingTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to StepHalvingTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver_of_type_wilson_theta_transient_solver(self) -> '_118.WilsonThetaTransientSolver':
        """WilsonThetaTransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        if _118.WilsonThetaTransientSolver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast transient_solver to WilsonThetaTransientSolver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
