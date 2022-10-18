"""_1814.py

ConstantLine
"""


from mastapy.utility_gui.charts import _1824
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CONSTANT_LINE = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'ConstantLine')


__docformat__ = 'restructuredtext en'
__all__ = ('ConstantLine',)


class ConstantLine(_0.APIBase):
    """ConstantLine

    This is a mastapy class.
    """

    TYPE = _CONSTANT_LINE

    def __init__(self, instance_to_wrap: 'ConstantLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axis(self) -> '_1824.SMTAxis':
        """SMTAxis: 'Axis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Axis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1824.SMTAxis)(value) if value is not None else None

    @property
    def end(self) -> 'float':
        """float: 'End' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.End

        if temp is None:
            return 0.0

        return temp

    @property
    def label(self) -> 'str':
        """str: 'Label' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Label

        if temp is None:
            return ''

        return temp

    @property
    def start(self) -> 'float':
        """float: 'Start' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Start

        if temp is None:
            return 0.0

        return temp

    @property
    def value(self) -> 'float':
        """float: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp
