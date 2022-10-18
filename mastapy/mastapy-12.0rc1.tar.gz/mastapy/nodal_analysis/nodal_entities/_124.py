"""_124.py

ArbitraryNodalComponent
"""


from mastapy.nodal_analysis.nodal_entities import _141
from mastapy._internal.python_net import python_net_import

_ARBITRARY_NODAL_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'ArbitraryNodalComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('ArbitraryNodalComponent',)


class ArbitraryNodalComponent(_141.NodalComponent):
    """ArbitraryNodalComponent

    This is a mastapy class.
    """

    TYPE = _ARBITRARY_NODAL_COMPONENT

    def __init__(self, instance_to_wrap: 'ArbitraryNodalComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
