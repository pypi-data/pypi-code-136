"""_2519.py

CycloidalAssembly
"""


from mastapy.cycloidal import _1419
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2428
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalAssembly')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssembly',)


class CycloidalAssembly(_2428.SpecialisedAssembly):
    """CycloidalAssembly

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY

    def __init__(self, instance_to_wrap: 'CycloidalAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cycloidal_assembly_design(self) -> '_1419.CycloidalAssemblyDesign':
        """CycloidalAssemblyDesign: 'CycloidalAssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
