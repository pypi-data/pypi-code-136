"""_184.py

FEModelPart
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FE_MODEL_PART = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModelPart')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModelPart',)


class FEModelPart(_0.APIBase):
    """FEModelPart

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_PART

    def __init__(self, instance_to_wrap: 'FEModelPart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def id(self) -> 'int':
        """int: 'ID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ID

        if temp is None:
            return 0

        return temp
