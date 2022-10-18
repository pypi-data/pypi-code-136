#  Copyright (c) 2022 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tests for map range in conversion
"""
import logging

import numpy as np

import pytest

from hvl_ccb.utils.conversion import (
    MapBitSymRange,
    MapBitAsymRange,
    MapRanges,
)


def test_external_or_internal_logger():
    logger = logging.getLogger(__name__)

    r = MapRanges((0, 10), (-5, 5), int, float)
    assert r.logger is not logger

    r = MapRanges((0, 10), (-5, 5), int, float, logger=logger)
    assert r.logger is logger


def test_bit_asym_range():
    bit10_10v = MapBitAsymRange(10, 10)
    assert bit10_10v.convert_to_bits(5) == 512
    assert round(bit10_10v.convert_to_number(512), 3) == 5.005


def test_bit_sym_range():
    bit10_10v = MapBitSymRange(5, 10)
    assert bit10_10v.convert_to_bits(5) == 1023
    assert round(bit10_10v.convert_to_number(20), 3) == -4.804
    assert bit10_10v.convert_to_bits(0) == 512


def test_check_dtype():
    assert MapRanges((0, 10), (-5, 5), float, float)
    assert MapRanges((0, 10), (-5, 5), float, np.float)
    assert MapRanges((0, 10), (-5, 5), float, np.int)

    with pytest.raises(TypeError):
        MapRanges((0, 10), (-5, 5), float, str)

    with pytest.raises(TypeError):
        MapRanges((0, 10), (-5, 5), float, np.complex)

    with pytest.raises(TypeError):
        MapRanges((0, 10), (-5, 5), float, bool)


def test_check_range_type():
    assert MapRanges((0, 10), (-5, 5), float, float)

    with pytest.raises(TypeError):
        MapRanges((0, 10.5), (-5, 5), int, float)

    with pytest.raises(TypeError):
        MapRanges(("0", "10.5"), (-5, 5), int, float)


def test_check_value():
    r = MapRanges((0, 10), (-5, 5), int, float)
    assert r.convert_to_range1(0) == 5
    assert r.convert_to_range1((-5, 0, 5)) == (0, 5, 10)
    with pytest.raises(ValueError):
        r.convert_to_range2(11)

    with pytest.raises(TypeError):
        r.convert_to_range2("11")

    with pytest.raises(ValueError):
        r.convert_to_range1(11)

    with pytest.raises(TypeError):
        r.convert_to_range1("11")

    with pytest.raises(TypeError):
        r.convert_to_range2(11.1)
