"""_140.py

LineContactStiffnessEntity
"""


from mastapy.nodal_analysis import _78
from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _124
from mastapy._internal.python_net import python_net_import

_LINE_CONTACT_STIFFNESS_ENTITY = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'LineContactStiffnessEntity')


__docformat__ = 'restructuredtext en'
__all__ = ('LineContactStiffnessEntity',)


class LineContactStiffnessEntity(_124.ArbitraryNodalComponent):
    """LineContactStiffnessEntity

    This is a mastapy class.
    """

    TYPE = _LINE_CONTACT_STIFFNESS_ENTITY

    def __init__(self, instance_to_wrap: 'LineContactStiffnessEntity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_in_local_coordinate_system(self) -> '_78.NodalMatrix':
        """NodalMatrix: 'StiffnessInLocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessInLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
