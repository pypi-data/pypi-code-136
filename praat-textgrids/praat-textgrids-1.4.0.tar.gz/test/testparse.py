#!/usr/bin/env python3
"""testparse.py"""

import sys
import io
import struct


class ParseError(Exception):
    pass


def parse_long(data):
    grab = lambda s: s.split(" = ")[1]
    tier_xmin, tier_xmax = [float(grab(s)) for s in buff[:2]]
    if buff[2] != "tiers? <exists>":
        sys.exit(0)
    tiers = int(grab(buff[3]))
    p = 6
    for i in range(tiers):
        tier_type, tier_name = [grab(s).strip('"') for s in buff[p : p + 2]]
        print('{} "{}"'.format(tier_type, tier_name))
        is_point_tier = True if tier_type != "IntervalTier" else False
        p += 2
        tier_xmin, tier_xmax = [float(grab(s)) for s in buff[p : p + 2]]
        tier_len = int(grab(buff[p + 2]))
        p += 4
        print(buff[p])
        for j in range(tier_len):
            if is_point_tier:
                x1 = float(grab(buff[p]))
                text = grab(buff[p + 1]).strip('"')
                print('Point(text="{}", xpos={}'.format(text, x1))
                p += 3
            else:
                x0, x1 = [float(grab(s)) for s in buff[p : p + 2]]
                text = grab(buff[p + 2]).strip('"')
                print('Interval(text="{}", xmin={}, xmax={}'.format(text, x0, x1))
                p += 4


def parse_short(data):
    tier_xmin, tier_xmax = [float(s) for s in buff[:2]]
    if buff[2] != "<exists>":
        sys.exit(0)
    tiers = int(buff[3])
    p = 4
    for i in range(tiers):
        tier_type, tier_name = [s.strip('"') for s in buff[p : p + 2]]
        print('{} "{}"'.format(tier_type, tier_name))
        is_point_tier = tier_type == "PointTier"
        p += 4
        elems = int(buff[p])
        p += 1
        for j in range(elems):
            if is_point_tier:
                x1, text = buff[p : p + 2]
                x1 = float(x1)
                text = text.strip('"')
                print('Point(text="{}", xpos={})'.format(text, x1))
                p += 2
            else:
                x0, x1, text = buff[p : p + 3]
                x0 = float(x0)
                x1 = float(x1)
                text = text.strip('"')
                print('Interval(text="{}", xmin={}, xmax={})'.format(text, x0, x1))
                p += 3


def parse_binary(data):
    sBool, sByte, sShort, sInt, sDouble = [struct.calcsize(c) for c in "?Bhid"]

    tier_xmin, tier_xmax = struct.unpack(">2d", data.read(2 * sDouble))
    if not struct.unpack("?", data.read(sBool))[0]:
        sys.exit(0)

    tiers = struct.unpack(">i", data.read(sInt))[0]
    for i in range(tiers):
        size = struct.unpack("B", data.read(sByte))[0]
        desc = data.read(size)
        if desc in (b"PointTier", b"TextTier"):
            point_tier = True
        elif desc == b"IntervalTier":
            point_tier = False
        else:
            raise ParseError
        size = struct.unpack(">h", data.read(sShort))[0]
        tier_name = data.read(size).decode()
        print('{} "{}"'.format(desc.decode(), tier_name))
        # Discard tier xmin, xmax as redundant
        data.read(2 * sDouble)
        elems = struct.unpack(">i", data.read(sInt))[0]
        for j in range(elems):
            if point_tier:
                xpos = struct.unpack(">d", data.read(sDouble))[0]
            else:
                xmin, xmax = struct.unpack(">2d", data.read(2 * sDouble))
            size = struct.unpack(">h", data.read(sShort))[0]
            # Apparently size -1 is an index that UTF-16 follows
            if size == -1:
                size = struct.unpack(">h", data.read(sShort))[0] * 2
                coding = "utf-16-be"
            else:
                coding = "ascii"
            text = data.read(size).decode(coding)
            if point_tier:
                print('Point(text="{}", xpos={})'.format(text, xpos))
            else:
                print('Interval(text="{}", xmin={}, xmax={})'.format(text, xmin, xmax))


for arg in sys.argv[1:]:
    # read()

    with open(arg, "rb") as infile:
        data = infile.read()

    # parse()

    binary = b"ooBinaryFile\x08TextGrid"
    text = ['File type = "ooTextFile"', 'Object class = "TextGrid"', ""]
    # Check and then discard binary header
    if data[: len(binary)] == binary:
        buff = io.BytesIO(data[len(binary) :])
        parse_binary(buff)
    else:
        coding = "utf-8"
        # Note and then discard BOM
        if data[:2] == b"\xfe\xff":
            coding = "utf-16-be"
            data = data[2:]
        # Now convert to a text buffer
        buff = [s.strip() for s in data.decode(coding).split("\n")]
        # Check and then discard header
        if buff[: len(text)] != text:
            raise TypeError
        buff = buff[len(text) :]
        # If the next line starts with a number, this is a short textgrid
        if buff[0][0] in "-0123456789":
            parse_short(buff)
        else:
            parse_long(buff)
