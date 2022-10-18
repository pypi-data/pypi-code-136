"""_1536.py

DataScalingReferenceValuesBase
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_REFERENCE_VALUES_BASE = python_net_import('SMT.MastaAPI.MathUtility.MeasuredDataScaling', 'DataScalingReferenceValuesBase')


__docformat__ = 'restructuredtext en'
__all__ = ('DataScalingReferenceValuesBase',)


class DataScalingReferenceValuesBase(_0.APIBase):
    """DataScalingReferenceValuesBase

    This is a mastapy class.
    """

    TYPE = _DATA_SCALING_REFERENCE_VALUES_BASE

    def __init__(self, instance_to_wrap: 'DataScalingReferenceValuesBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_db(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumDB' is the original name of this property."""

        temp = self.wrapped.MaximumDB

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum_db.setter
    def maximum_db(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumDB = value

    @property
    def minimum_db(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumDB' is the original name of this property."""

        temp = self.wrapped.MinimumDB

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @minimum_db.setter
    def minimum_db(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumDB = value
