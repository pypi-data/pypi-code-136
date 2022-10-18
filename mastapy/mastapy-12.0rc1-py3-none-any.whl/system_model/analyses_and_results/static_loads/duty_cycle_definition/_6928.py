"""_6928.py

TimeStepInputOptions
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility_gui import _1809
from mastapy._internal.python_net import python_net_import

_TIME_STEP_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'TimeStepInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('TimeStepInputOptions',)


class TimeStepInputOptions(_1809.ColumnInputOptions):
    """TimeStepInputOptions

    This is a mastapy class.
    """

    TYPE = _TIME_STEP_INPUT_OPTIONS

    def __init__(self, instance_to_wrap: 'TimeStepInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def time_increment(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TimeIncrement' is the original name of this property."""

        temp = self.wrapped.TimeIncrement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @time_increment.setter
    def time_increment(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TimeIncrement = value
