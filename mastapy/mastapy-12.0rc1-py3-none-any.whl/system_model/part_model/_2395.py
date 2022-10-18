"""_2395.py

BoltedJoint
"""


from mastapy.bolts import _1442
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2428
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'BoltedJoint')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJoint',)


class BoltedJoint(_2428.SpecialisedAssembly):
    """BoltedJoint

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT

    def __init__(self, instance_to_wrap: 'BoltedJoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def detailed_bolted_joint(self) -> '_1442.DetailedBoltedJointDesign':
        """DetailedBoltedJointDesign: 'DetailedBoltedJoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DetailedBoltedJoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
