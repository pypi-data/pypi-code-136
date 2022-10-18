"""_6782.py

CVTPulleyLoadCase
"""


from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2538
from mastapy.system_model.analyses_and_results.static_loads import _6866
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTPulleyLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyLoadCase',)


class CVTPulleyLoadCase(_6866.PulleyLoadCase):
    """CVTPulleyLoadCase

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_LOAD_CASE

    def __init__(self, instance_to_wrap: 'CVTPulleyLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clamping_force(self) -> 'float':
        """float: 'ClampingForce' is the original name of this property."""

        temp = self.wrapped.ClampingForce

        if temp is None:
            return 0.0

        return temp

    @clamping_force.setter
    def clamping_force(self, value: 'float'):
        self.wrapped.ClampingForce = float(value) if value else 0.0

    @property
    def effective_diameter(self) -> 'float':
        """float: 'EffectiveDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_nodes(self) -> 'int':
        """int: 'NumberOfNodes' is the original name of this property."""

        temp = self.wrapped.NumberOfNodes

        if temp is None:
            return 0

        return temp

    @number_of_nodes.setter
    def number_of_nodes(self, value: 'int'):
        self.wrapped.NumberOfNodes = int(value) if value else 0

    @property
    def component_design(self) -> '_2538.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
