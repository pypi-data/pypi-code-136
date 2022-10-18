"""_1818.py

ModeConstantLine
"""


from mastapy.utility_gui.charts import _1814
from mastapy._internal.python_net import python_net_import

_MODE_CONSTANT_LINE = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'ModeConstantLine')


__docformat__ = 'restructuredtext en'
__all__ = ('ModeConstantLine',)


class ModeConstantLine(_1814.ConstantLine):
    """ModeConstantLine

    This is a mastapy class.
    """

    TYPE = _MODE_CONSTANT_LINE

    def __init__(self, instance_to_wrap: 'ModeConstantLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
