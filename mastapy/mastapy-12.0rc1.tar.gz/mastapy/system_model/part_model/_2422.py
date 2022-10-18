"""_2422.py

PlanetCarrierSettings
"""


from mastapy.system_model import _2170
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility import _1559
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_SETTINGS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PlanetCarrierSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierSettings',)


class PlanetCarrierSettings(_1559.PerMachineSettings):
    """PlanetCarrierSettings

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_SETTINGS

    def __init__(self, instance_to_wrap: 'PlanetCarrierSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_pin_manufacturing_errors_coordinate_system(self) -> '_2170.PlanetPinManufacturingErrorsCoordinateSystem':
        """PlanetPinManufacturingErrorsCoordinateSystem: 'PlanetPinManufacturingErrorsCoordinateSystem' is the original name of this property."""

        temp = self.wrapped.PlanetPinManufacturingErrorsCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2170.PlanetPinManufacturingErrorsCoordinateSystem)(value) if value is not None else None

    @planet_pin_manufacturing_errors_coordinate_system.setter
    def planet_pin_manufacturing_errors_coordinate_system(self, value: '_2170.PlanetPinManufacturingErrorsCoordinateSystem'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PlanetPinManufacturingErrorsCoordinateSystem = value
