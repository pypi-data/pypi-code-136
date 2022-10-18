"""_1535.py

DataScalingReferenceValues
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility.measured_data_scaling import _1536
from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_REFERENCE_VALUES = python_net_import('SMT.MastaAPI.MathUtility.MeasuredDataScaling', 'DataScalingReferenceValues')


__docformat__ = 'restructuredtext en'
__all__ = ('DataScalingReferenceValues',)


TMeasurement = TypeVar('TMeasurement', bound='_1570.MeasurementBase')


class DataScalingReferenceValues(_1536.DataScalingReferenceValuesBase, Generic[TMeasurement]):
    """DataScalingReferenceValues

    This is a mastapy class.

    Generic Types:
        TMeasurement
    """

    TYPE = _DATA_SCALING_REFERENCE_VALUES

    def __init__(self, instance_to_wrap: 'DataScalingReferenceValues.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def decibel_reference(self) -> 'float':
        """float: 'DecibelReference' is the original name of this property."""

        temp = self.wrapped.DecibelReference

        if temp is None:
            return 0.0

        return temp

    @decibel_reference.setter
    def decibel_reference(self, value: 'float'):
        self.wrapped.DecibelReference = float(value) if value else 0.0

    @property
    def maximum(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Maximum' is the original name of this property."""

        temp = self.wrapped.Maximum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum.setter
    def maximum(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Maximum = value

    @property
    def minimum(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Minimum' is the original name of this property."""

        temp = self.wrapped.Minimum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @minimum.setter
    def minimum(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Minimum = value
