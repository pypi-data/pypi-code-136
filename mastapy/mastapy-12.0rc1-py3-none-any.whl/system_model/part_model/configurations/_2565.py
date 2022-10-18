"""_2565.py

ActiveShaftDesignSelectionGroup
"""


from mastapy.system_model.part_model.configurations import _2568, _2564
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.shafts import _43
from mastapy._internal.python_net import python_net_import

_ACTIVE_SHAFT_DESIGN_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveShaftDesignSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveShaftDesignSelectionGroup',)


class ActiveShaftDesignSelectionGroup(_2568.PartDetailConfiguration['_2564.ActiveShaftDesignSelection', '_2434.Shaft', '_43.SimpleShaftDefinition']):
    """ActiveShaftDesignSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_SHAFT_DESIGN_SELECTION_GROUP

    def __init__(self, instance_to_wrap: 'ActiveShaftDesignSelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
