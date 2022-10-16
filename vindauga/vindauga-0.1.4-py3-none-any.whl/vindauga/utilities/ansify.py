# -*- coding: utf-8 -*-
import curses
import logging

from dataclasses import dataclass

from PIL import Image

from vindauga.types.draw_buffer import DrawBuffer
from vindauga.types.rect import Rect
from vindauga.utilities.colours.colours import colourFindRGB
logger = logging.getLogger(__name__)


@dataclass
class BitMap:
    pattern: int
    charOrd: int
    char: str


BLOCK = BitMap(0x0000ffff, 0x2584, '▄')  # lower 1/2


@dataclass
class Color:
    r: int
    g: int
    b: int

    def __floordiv__(self, other):
        self.r //= other
        self.g //= other
        self.b //= other
        return self

    def __add__(self, other):
        self.r += other[0]
        self.g += other[1]
        self.b += other[2]


@dataclass
class CharData:
    fgColor: Color = Color(0, 0, 0)
    bgColor: Color = Color(0, 0, 0)
    char: str = '▄'


@dataclass
class Size:
    width: int
    height: int

    def scaled(self, scale):
        return Size(int(self.width * scale), int(self.height * scale))

    def fittedWithin(self, container):
        scale = min(container.width / self.width, container.height / self.height)
        return self.scaled(scale)


def openFile(filename):
    im = Image.open(filename)
    im.draft("RGB", im.size)
    return im


def getBitmapCharData(bitmap: BitMap, input_image, x0: int, y0: int):
    result = CharData()
    result.char = bitmap.char

    fgCount = 0
    bgCount = 0
    mask = 0x80000000

    for y in range(y0, y0 + 8):
        for x in range(x0, x0 + 4):
            if bitmap.pattern & mask:
                avg = result.fgColor
                fgCount += 1
            else:
                avg = result.bgColor
                bgCount += 1

            avg += input_image[x, y]
            mask >>= 1

    if bgCount:
        result.bgColor //= bgCount

    if fgCount:
        result.fgColor //= fgCount
    return result


def emitImage(image):
    w, h = image.size
    pixels = image.load()
    lines = []
    for y in range(0, h - 8, 8):
        buffer = DrawBuffer(True)
        for i, x in enumerate(range(0, w - 4, 4)):
            charData = getBitmapCharData(BLOCK, pixels, x, y)
            bg = colourFindRGB(charData.bgColor.r, charData.bgColor.g, charData.bgColor.b)
            fg = colourFindRGB(charData.fgColor.r, charData.fgColor.g, charData.fgColor.b)
            pair = (fg * 256 + bg)
            buffer.putChar(i, charData.char)
            buffer.putAttribute(i, pair)
        lines.append(buffer)
    return lines


def wallpaper(filename, bounds: Rect):
    if curses.COLOR_PAIRS <= 256:
        return 0, 0, []

    maxWidth = bounds.width * 4
    maxHeight = bounds.height * 8

    img = openFile(filename).convert('RGB')
    iw, ih = img.size
    size = Size(iw, ih)
    if iw > maxWidth or ih > maxHeight:
        size = size.fittedWithin(Size(maxWidth, maxHeight))
        img = img.resize((size.width, size.height))
    return size.width // 4, size.height // 8, emitImage(img)
