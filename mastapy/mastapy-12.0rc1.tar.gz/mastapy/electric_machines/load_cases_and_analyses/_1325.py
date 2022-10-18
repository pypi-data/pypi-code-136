"""_1325.py

ElectricMachineFEAnalysis
"""


from mastapy._internal import constructor
from mastapy.electric_machines.results import _1296, _1308
from mastapy.nodal_analysis.elmer import _168
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines.load_cases_and_analyses import _1337
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_FE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineFEAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineFEAnalysis',)


class ElectricMachineFEAnalysis(_1337.SingleOperatingPointAnalysis):
    """ElectricMachineFEAnalysis

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_FE_ANALYSIS

    def __init__(self, instance_to_wrap: 'ElectricMachineFEAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electro_magnetic_solver_analysis_time(self) -> 'float':
        """float: 'ElectroMagneticSolverAnalysisTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectroMagneticSolverAnalysisTime

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_force_results(self) -> '_1296.DynamicForceResults':
        """DynamicForceResults: 'DynamicForceResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicForceResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def viewable(self) -> '_168.ElmerResultsViewable':
        """ElmerResultsViewable: 'Viewable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Viewable

        if temp is None:
            return None

        if _168.ElmerResultsViewable.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast viewable to ElmerResultsViewable. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def viewable_of_type_electric_machine_results_viewable(self) -> '_1308.ElectricMachineResultsViewable':
        """ElectricMachineResultsViewable: 'Viewable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Viewable

        if temp is None:
            return None

        if _1308.ElectricMachineResultsViewable.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast viewable to ElectricMachineResultsViewable. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
