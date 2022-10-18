#  Copyright (c) 2021-2022 ETH Zurich, SIS ID and HVL D-ITET
#

"""
Unit conversion, within in the same group of units, for example Kelvin <-> Celsius
"""

from __future__ import annotations

import logging
from abc import abstractmethod
from enum import Enum
from typing import Union

from hvl_ccb.utils.typing import ConvertableTypes
from hvl_ccb.utils.conversion.utils import preserve_type

logger = logging.getLogger(__name__)


class Unit(Enum):
    @classmethod
    @abstractmethod
    @preserve_type
    def convert(cls, value: ConvertableTypes, source, target) -> ConvertableTypes:
        pass  # pragma: no cover


class Temperature(Unit):
    K = "K"
    C = "C"
    F = "F"
    KELVIN = K
    CELSIUS = C
    FAHRENHEIT = F

    @classmethod
    @preserve_type
    def convert(
        cls,
        value: ConvertableTypes,
        source: Union[str, Temperature] = KELVIN,
        target: Union[str, Temperature] = CELSIUS,
    ) -> ConvertableTypes:
        try:
            source = Temperature(source)
            target = Temperature(target)
        except ValueError:
            logger.warning(
                "One unit or both units for source and / or target temperature "
                "are not valid."
            )
            raise ValueError
        if source == target:
            return value

        # convert source to kelvin
        if source == cls.CELSIUS:
            value = value + 273.15  # type: ignore
        elif source == cls.FAHRENHEIT:
            value = (value - 32) / 1.8 + 273.15  # type: ignore

        # convert kelvin to target
        if target == cls.CELSIUS:
            value = value - 273.15  # type: ignore
        elif target == cls.FAHRENHEIT:
            value = (value - 273.15) * 1.8 + 32  # type: ignore
        return value


class Pressure(Unit):
    PA = "Pa"
    BAR = "bar"
    ATM = "atm"
    PSI = "psi"
    MMHG = "mmHg"
    TORR = "torr"
    PASCAL = PA
    ATMOSPHERE = ATM
    POUNDS_PER_SQUARE_INCH = PSI
    MILLIMETER_MERCURY = MMHG

    @classmethod
    @preserve_type
    def convert(
        cls,
        value: ConvertableTypes,
        source: Union[str, Pressure] = BAR,
        target: Union[str, Pressure] = PASCAL,
    ) -> ConvertableTypes:
        try:
            source = Pressure(source)
            target = Pressure(target)
        except ValueError:
            logger.warning(
                "One unit or both units for source and / or target pressure "
                "are not valid."
            )
            raise ValueError
        if source == target:
            return value
        # convert source to Pascal
        if source == cls.BAR:
            value = value * 1e5  # type: ignore
        elif source == cls.ATMOSPHERE:
            value = value * 101_325  # type: ignore
        elif source == cls.TORR:
            value = value * 101_325 / 760  # type: ignore
        elif source == cls.MMHG:
            value = value * 101_325 / 760 * 1.000_000_142_466  # type: ignore
        elif source == cls.PSI:
            value = value * 6_894.75728  # type: ignore

        # convert from Pascal to target
        if target == cls.BAR:
            value = value / 1e5  # type: ignore
        elif target == cls.ATMOSPHERE:
            value = value / 101_325  # type: ignore
        elif target == cls.TORR:
            value = value / 101_325 * 760  # type: ignore
        elif target == cls.MMHG:
            value = value / 101_325 * 760 / 1.000_000_142_466  # type: ignore
        elif target == cls.PSI:
            value = value / 6_894.75728  # type: ignore
        return value
