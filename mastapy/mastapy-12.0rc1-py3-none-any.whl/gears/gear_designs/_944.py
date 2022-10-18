"""_944.py

SelectedDesignConstraintsCollection
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_SELECTED_DESIGN_CONSTRAINTS_COLLECTION = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'SelectedDesignConstraintsCollection')


__docformat__ = 'restructuredtext en'
__all__ = ('SelectedDesignConstraintsCollection',)


class SelectedDesignConstraintsCollection(_0.APIBase):
    """SelectedDesignConstraintsCollection

    This is a mastapy class.
    """

    TYPE = _SELECTED_DESIGN_CONSTRAINTS_COLLECTION

    def __init__(self, instance_to_wrap: 'SelectedDesignConstraintsCollection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
