"""_2794.py

RigidlyConnectedComponentGroupSystemDeflection
"""


from typing import List

from mastapy.math_utility import _1481
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2661
from mastapy.system_model.analyses_and_results import _2603
from mastapy._internal.python_net import python_net_import

_RIGIDLY_CONNECTED_COMPONENT_GROUP_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting', 'RigidlyConnectedComponentGroupSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RigidlyConnectedComponentGroupSystemDeflection',)


class RigidlyConnectedComponentGroupSystemDeflection(_2603.DesignEntityGroupAnalysis):
    """RigidlyConnectedComponentGroupSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RIGIDLY_CONNECTED_COMPONENT_GROUP_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'RigidlyConnectedComponentGroupSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_properties(self) -> '_1481.MassProperties':
        """MassProperties: 'MassProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def components(self) -> 'List[_2661.ComponentSystemDeflection]':
        """List[ComponentSystemDeflection]: 'Components' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Components

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
