# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log
from typing import Optional, Tuple, Union

import pandas as pd
from pandas._libs.tslibs import BaseOffset
from pandas._libs.tslibs.offsets import Tick, delta_to_tick
from pandas.tseries.frequencies import to_offset
from public import private, public

from ._uom import Unit, convert_units, parse_unit, units

FreqType = Union[str, BaseOffset]

__nanos = units.s * units.Prefix.nano


@private
def parse_offset(expr: FreqType) -> BaseOffset:
    """
    Transforms a string to a pandas offset
    https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects for codes and info.
    """
    if isinstance(expr, str):
        return to_offset(expr)

    return expr


@public
class Index:
    def __init__(self, sparse: bool, mask: int) -> None:
        self._sparse = sparse
        self._mask = mask

    @property
    def is_sparse(self) -> bool:
        return self._sparse

    @property
    def mask(self) -> int:
        return self._mask


class SequentialIndex(Index):
    def __init__(self, sparse: bool, mask: int) -> None:
        super().__init__(sparse, mask)


@public
def sequential_index(sparse: bool = False) -> Index:
    """
    This is the simplest index, where positions are just interpreted as
    ordinal positions (first, second, third ... values) without any
    interpretation of time.
    """
    return SequentialIndex(sparse, 1 << 15)


FreqType = Union[
    str, BaseOffset, pd.Timedelta, Tuple[Union[float, int], Union[Unit, str]]
]


def _intraDayFreqToNano(expr: FreqType) -> float:

    if isinstance(expr, (str, BaseOffset)):
        baseOffset = expr if isinstance(expr, BaseOffset) else to_offset(expr)
        if not isinstance(baseOffset, Tick):
            raise ValueError(
                f"Frequency [{expr}] must resolve to a non calendar based unit of time."
            )
        return float(baseOffset.nanos)

    if isinstance(expr, pd.Timedelta):
        return float(delta_to_tick(expr).nanos)

    if not (isinstance(expr, tuple) and len(expr) == 2):
        raise ValueError(
            f"[{expr}] must be a string, a Pandas BaseOffset or Timedelta, or a tuple."
        )

    magnitude, unitsExpr = expr
    if not isinstance(magnitude, (float, int)):
        raise ValueError(
            f"Frequency [{expr}] was expected to be a tuple (number, units)"
        )

    unit = None
    if isinstance(unitsExpr, str):
        unit = parse_unit(unitsExpr)
        if unit is None:
            raise ValueError(f"Couldn't interpret [{unitsExpr}] as a valid unit")
    elif not isinstance(unitsExpr, Unit):
        # TODO
        # raise ValueError(f"[{unitsExpr}] must be a string or a time unit (was {type(unitsExpr)})")
        unit = unitsExpr

    if unit.base_units != units.s:
        raise ValueError(f"[{unitsExpr}] is not valid time unit")

    return convert_units(unit, float(magnitude), __nanos)


@public
def intraday_index(
    precision: FreqType | None = "s",
    frequency: FreqType = None,
    blockSize: int | None = 32768,
    forceSparse: bool | None = False,
):

    precNano = _intraDayFreqToNano(precision)
    freqNano = precNano if freqNano is None else _intraDayFreqToNano(frequency)

    if precNano < 1.0:
        raise ValueError("The precision of this index is below 1 nanosecond.")

    if freqNano < 1.0:
        raise ValueError("The expected arrival frequency is less than a nanosecond.")

    if freqNano < precNano:
        raise ValueError(
            "Precision should be lower than the expected arrival frequency"
        )

    ratio = freqNano / precNano
    extraBits = int(ceil(log(ratio, 2)))
    blockBits = int(ceil(log(blockSize, 2)))
    bits = extraBits + blockBits
    sparse = forceSparse or ratio > 8

    return (freqNano * __nanos, precNano * __nanos, bits, sparse, blockSize)


def _offsets_freq_to_units(expr: FreqType) -> Unit:
    if isinstance(expr, str):
        # The string may denote a unit or a pandas expression
        asUnit = parse_unit(expr)
        if asUnit is not None:
            return asUnit

        asBaseOffset = to_offset(expr)
        if asBaseOffset is None:
            raise ValueError(
                f"[{expr}] cannot be evaluated as unit of measure nor as a Pandas offset"
            )
        if not isinstance(asBaseOffset, Tick):
            raise ValueError(
                f"Frequency [{expr}] must resolve to a non calendar based unit of time."
            )
        return asBaseOffset.nanos * __nanos

    if isinstance(expr, BaseOffset):
        if not isinstance(expr, Tick):
            raise ValueError(
                f"Frequency [{expr}] must resolve to a non calendar based unit of time."
            )
        return expr.nanos * __nanos

    if isinstance(expr, pd.Timedelta):
        return delta_to_tick(expr).nanos * __nanos

    if not (isinstance(expr, tuple) and len(expr) == 2):
        raise ValueError(
            f"[{expr}] must be a string, a Pandas BaseOffset or Timedelta, or a tuple."
        )

    magnitude, unitsExpr = expr
    if not isinstance(magnitude, (float, int)):
        raise ValueError(
            f"Frequency [{expr}] was expected to be a tuple (number, units)"
        )

    unit = None
    if isinstance(unitsExpr, str):
        _, unit = _offsets_freq_to_units(unitsExpr)
    elif not isinstance(unitsExpr, Unit):
        # TODO
        # raise ValueError(f"[{unitsExpr}] must be a string or a time unit (was {type(unitsExpr)})")
        unit = unitsExpr

    return magnitude * unit


@public
def offsets_index(
    frequency: FreqType = "s",
    precision: FreqType | None = None,
    blockSize: int | None = 32768,
    forceSparse: bool | None = False,
):

    freqUnit = _offsets_freq_to_units(frequency)
    precUnit = freqUnit if precision is None else _offsets_freq_to_units(precision)

    if not freqUnit.is_convertible(precUnit):
        raise ValueError(
            f"Incompatible units: Frequency [{freqUnit}]; Precision [{precUnit}]"
        )

    ratio = convert_units(freqUnit, 1.0, precUnit)
    if ratio < 1.0:
        raise ValueError(f"Precision is larger than arrival frequency")

    extraBits = int(ceil(log(ratio, 2)))
    blockBits = int(ceil(log(blockSize, 2)))
    bits = extraBits + blockBits
    sparse = forceSparse or ratio > 8

    return (freqUnit, precUnit, bits, sparse, blockSize)


@public
def calendar_index(
    frequency: FreqType = "d", precision: FreqType | None = None
) -> Index:
    pass
