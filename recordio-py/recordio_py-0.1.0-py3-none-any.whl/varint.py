"""Varint encoder/decoder

Varints are a common encoding for variable length integer data.

The encoding is:
- unsigned integers are serialized 7 bits at a time, starting with the
  least significant bits
- the most significant bit (msb) in each output byte indicates if there
  is a continuation byte (msb = 1)
- signed integers are mapped to unsigned integers using "zig-zag"
  encoding: Positive values x are written as 2*x + 0, negative values
  are written as 2*(^x) + 1; that is, negative numbers are complemented
  and whether to complement is encoded in bit 0.
"""

from io import BufferedReader


def encode(x: int) -> bytes:
    ux = x << 1
    if x < 0:
        ux = ~ux
    return encode_unsigned(ux)


def encode_unsigned(ux: int) -> bytes:
    if ux < 0:
        raise ValueError(f"Cannot encode negative number: {ux} as unsigned.")
    buf = b""
    while ux >= 0x80:
        byte = bytes([(ux & 0x7F) | 0x80])
        buf += byte
        ux >>= 7
    buf += bytes([ux])
    return buf


def decode(file: BufferedReader) -> int:
    ux = decode_unsigned(file)
    x = ux >> 1
    if ux & 1:
        x = ~x
    return x


def decode_unsigned(file: BufferedReader) -> int:
    result = 0
    shift = 0
    while True:
        byte = _read_byte(file)
        result |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            break
        shift += 7
    return result


def _read_byte(file: BufferedReader) -> int:
    c = file.read(1)
    if c == b"":
        raise EOFError("Unexpected EOF while reading bytes")
    return ord(c)
