"""_5315.py

AbstractShaftOrHousingMultibodyDynamicsAnalysis
"""


from mastapy._internal import constructor
from mastapy.system_model.part_model import _2389, _2388, _2405
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.part_model.cycloidal import _2520
from mastapy.system_model.analyses_and_results.mbd_analyses import _5341
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'AbstractShaftOrHousingMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingMultibodyDynamicsAnalysis',)


class AbstractShaftOrHousingMultibodyDynamicsAnalysis(_5341.ComponentMultibodyDynamicsAnalysis):
    """AbstractShaftOrHousingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_rigid_body_degrees_of_freedom(self) -> 'int':
        """int: 'NumberOfRigidBodyDegreesOfFreedom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfRigidBodyDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def component_design(self) -> '_2389.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2389.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_abstract_shaft(self) -> '_2388.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2388.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_fe_part(self) -> '_2405.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2405.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft(self) -> '_2434.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2434.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_disc(self) -> '_2520.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2520.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
