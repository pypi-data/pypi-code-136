"""_2352.py

NodeGroupWithSelection
"""


from mastapy.system_model.fe import _2329
from mastapy.nodal_analysis.component_mode_synthesis import _222
from mastapy._internal.python_net import python_net_import

_NODE_GROUP_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'NodeGroupWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('NodeGroupWithSelection',)


class NodeGroupWithSelection(_2329.FEEntityGroupWithSelection['_222.CMSNodeGroup', 'int']):
    """NodeGroupWithSelection

    This is a mastapy class.
    """

    TYPE = _NODE_GROUP_WITH_SELECTION

    def __init__(self, instance_to_wrap: 'NodeGroupWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
