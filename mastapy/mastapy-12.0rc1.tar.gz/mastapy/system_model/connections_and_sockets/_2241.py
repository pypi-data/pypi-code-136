"""_2241.py

PlanetarySocketBase
"""


from mastapy._internal import constructor
from mastapy.gears import _334
from mastapy.system_model.connections_and_sockets import _2228
from mastapy._internal.python_net import python_net_import

_PLANETARY_SOCKET_BASE = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PlanetarySocketBase')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetarySocketBase',)


class PlanetarySocketBase(_2228.CylindricalSocket):
    """PlanetarySocketBase

    This is a mastapy class.
    """

    TYPE = _PLANETARY_SOCKET_BASE

    def __init__(self, instance_to_wrap: 'PlanetarySocketBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def draw_on_lower_half_of_2d(self) -> 'bool':
        """bool: 'DrawOnLowerHalfOf2D' is the original name of this property."""

        temp = self.wrapped.DrawOnLowerHalfOf2D

        if temp is None:
            return False

        return temp

    @draw_on_lower_half_of_2d.setter
    def draw_on_lower_half_of_2d(self, value: 'bool'):
        self.wrapped.DrawOnLowerHalfOf2D = bool(value) if value else False

    @property
    def draw_on_upper_half_of_2d(self) -> 'bool':
        """bool: 'DrawOnUpperHalfOf2D' is the original name of this property."""

        temp = self.wrapped.DrawOnUpperHalfOf2D

        if temp is None:
            return False

        return temp

    @draw_on_upper_half_of_2d.setter
    def draw_on_upper_half_of_2d(self, value: 'bool'):
        self.wrapped.DrawOnUpperHalfOf2D = bool(value) if value else False

    @property
    def editable_name(self) -> 'str':
        """str: 'EditableName' is the original name of this property."""

        temp = self.wrapped.EditableName

        if temp is None:
            return ''

        return temp

    @editable_name.setter
    def editable_name(self, value: 'str'):
        self.wrapped.EditableName = str(value) if value else ''

    @property
    def planetary_load_sharing_factor(self) -> 'float':
        """float: 'PlanetaryLoadSharingFactor' is the original name of this property."""

        temp = self.wrapped.PlanetaryLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @planetary_load_sharing_factor.setter
    def planetary_load_sharing_factor(self, value: 'float'):
        self.wrapped.PlanetaryLoadSharingFactor = float(value) if value else 0.0

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

    @property
    def planetary_details(self) -> '_334.PlanetaryDetail':
        """PlanetaryDetail: 'PlanetaryDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetaryDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
