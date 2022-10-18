"""_1248.py

Eccentricity
"""


from mastapy._internal import constructor
from mastapy.utility import _1552
from mastapy._internal.python_net import python_net_import

_ECCENTRICITY = python_net_import('SMT.MastaAPI.ElectricMachines', 'Eccentricity')


__docformat__ = 'restructuredtext en'
__all__ = ('Eccentricity',)


class Eccentricity(_1552.IndependentReportablePropertiesBase['Eccentricity']):
    """Eccentricity

    This is a mastapy class.
    """

    TYPE = _ECCENTRICITY

    def __init__(self, instance_to_wrap: 'Eccentricity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_x(self) -> 'float':
        """float: 'DynamicX' is the original name of this property."""

        temp = self.wrapped.DynamicX

        if temp is None:
            return 0.0

        return temp

    @dynamic_x.setter
    def dynamic_x(self, value: 'float'):
        self.wrapped.DynamicX = float(value) if value else 0.0

    @property
    def dynamic_y(self) -> 'float':
        """float: 'DynamicY' is the original name of this property."""

        temp = self.wrapped.DynamicY

        if temp is None:
            return 0.0

        return temp

    @dynamic_y.setter
    def dynamic_y(self, value: 'float'):
        self.wrapped.DynamicY = float(value) if value else 0.0

    @property
    def static_x(self) -> 'float':
        """float: 'StaticX' is the original name of this property."""

        temp = self.wrapped.StaticX

        if temp is None:
            return 0.0

        return temp

    @static_x.setter
    def static_x(self, value: 'float'):
        self.wrapped.StaticX = float(value) if value else 0.0

    @property
    def static_y(self) -> 'float':
        """float: 'StaticY' is the original name of this property."""

        temp = self.wrapped.StaticY

        if temp is None:
            return 0.0

        return temp

    @static_y.setter
    def static_y(self, value: 'float'):
        self.wrapped.StaticY = float(value) if value else 0.0
