from io import BytesIO

import pytest

from recordio import varint


@pytest.mark.parametrize(
    "number",
    [
        -1 << 63,
        -1 << 63 + 1,
        -1,
        0,
        1,
        2,
        10,
        20,
        63,
        64,
        65,
        127,
        128,
        129,
        255,
        256,
        257,
        1 << 63 - 1,
    ],
)
def test_varint(number):
    buf = varint.encode(number)
    assert varint.decode(BytesIO(buf)) == number


@pytest.mark.parametrize(
    "number",
    [
        0,
        1,
        2,
        10,
        20,
        63,
        64,
        65,
        127,
        128,
        129,
        255,
        256,
        257,
        1 << 63 - 1,
    ],
)
def test_unsigned_varint(number):
    buf = varint.encode_unsigned(number)
    assert varint.decode_unsigned(BytesIO(buf)) == number


@pytest.mark.parametrize(
    "number",
    [
        -1 << 63,
        -1 << 63 + 1,
        -1,
    ],
)
def test_negative_unsigned_varint_raises_exception(number):
    with pytest.raises(ValueError):
        varint.encode_unsigned(number)
