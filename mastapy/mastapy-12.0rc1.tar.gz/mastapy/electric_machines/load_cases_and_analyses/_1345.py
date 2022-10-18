"""_1345.py

Temperatures
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility import _1552
from mastapy._internal.python_net import python_net_import

_TEMPERATURES = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'Temperatures')


__docformat__ = 'restructuredtext en'
__all__ = ('Temperatures',)


class Temperatures(_1552.IndependentReportablePropertiesBase['Temperatures']):
    """Temperatures

    This is a mastapy class.
    """

    TYPE = _TEMPERATURES

    def __init__(self, instance_to_wrap: 'Temperatures.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnet_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MagnetTemperature' is the original name of this property."""

        temp = self.wrapped.MagnetTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @magnet_temperature.setter
    def magnet_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MagnetTemperature = value

    @property
    def windings_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WindingsTemperature' is the original name of this property."""

        temp = self.wrapped.WindingsTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @windings_temperature.setter
    def windings_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WindingsTemperature = value
