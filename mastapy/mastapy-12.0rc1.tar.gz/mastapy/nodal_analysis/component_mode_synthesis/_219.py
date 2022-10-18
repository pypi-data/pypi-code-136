"""_219.py

CMSElementFaceGroup
"""


from mastapy._internal import constructor
from mastapy.nodal_analysis.dev_tools_analyses import _175
from mastapy._internal.python_net import python_net_import

_CMS_ELEMENT_FACE_GROUP = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'CMSElementFaceGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('CMSElementFaceGroup',)


class CMSElementFaceGroup(_175.ElementFaceGroup):
    """CMSElementFaceGroup

    This is a mastapy class.
    """

    TYPE = _CMS_ELEMENT_FACE_GROUP

    def __init__(self, instance_to_wrap: 'CMSElementFaceGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def area(self) -> 'float':
        """float: 'Area' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Area

        if temp is None:
            return 0.0

        return temp

    def create_node_group(self):
        """ 'CreateNodeGroup' is the original name of this method."""

        self.wrapped.CreateNodeGroup()

    def populate_rms_values_cache(self):
        """ 'PopulateRMSValuesCache' is the original name of this method."""

        self.wrapped.PopulateRMSValuesCache()
