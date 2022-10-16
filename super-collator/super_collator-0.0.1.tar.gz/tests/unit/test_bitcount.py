""" Test python < 3.10 bitcount. """

# pylint: disable=missing-docstring

import pytest

from super_collator.strategy import bit_count


class TestBitCount:
    def test_bit_count(self):
        assert bit_count(0x0000000000000000) == 0
        assert bit_count(0xffffffffffffffff) == 64

        assert bit_count(0x0000000000000001) == 1
        assert bit_count(0x0000000000000002) == 1
        assert bit_count(0x4000000000000000) == 1
        assert bit_count(0x8000000000000000) == 1

        assert bit_count(0x0000000000000003) == 2
        assert bit_count(0x0000000000000007) == 3
        assert bit_count(0x000000000000000f) == 4

        assert bit_count(0x1111111111111111) == 16
        assert bit_count(0x5555555555555555) == 32
        assert bit_count(0xaaaaaaaaaaaaaaaa) == 32
        assert bit_count(0x7777777777777777) == 48

