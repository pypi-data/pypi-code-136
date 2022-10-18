"""_1869.py

InterferenceDetail
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.materials import _263, _239
from mastapy.shafts import _24
from mastapy._internal.cast_exception import CastException
from mastapy.gears.materials import (
    _576, _578, _580, _584,
    _587, _590, _594, _596
)
from mastapy.electric_machines import _1264, _1281, _1291
from mastapy.detailed_rigid_connectors.splines import _1382
from mastapy.cycloidal import _1421, _1427
from mastapy.bolts import _1430, _1434
from mastapy.bearings.tolerances import _1862
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_DETAIL = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'InterferenceDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceDetail',)


class InterferenceDetail(_1862.BearingConnectionComponent):
    """InterferenceDetail

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_DETAIL

    def __init__(self, instance_to_wrap: 'InterferenceDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_tolerance_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DiameterToleranceFactor' is the original name of this property."""

        temp = self.wrapped.DiameterToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @diameter_tolerance_factor.setter
    def diameter_tolerance_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DiameterToleranceFactor = value

    @property
    def temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Temperature' is the original name of this property."""

        temp = self.wrapped.Temperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @temperature.setter
    def temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Temperature = value

    @property
    def material(self) -> '_263.Material':
        """Material: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material

        if temp is None:
            return None

        if _263.Material.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to Material. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
