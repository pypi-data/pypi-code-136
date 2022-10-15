import math
from enum import Enum

import numpy as np


class Color(tuple, Enum):
    """Color enum"""

    def __new__(cls, bgr):
        obj = tuple.__new__(cls, bgr)
        return obj

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    YELLOW = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    CYAN = (255, 255, 0)

    def __add__(self, other):
        return tuple(int((a[0] + a[1] + 1) / 2) for a in zip(self, other))

    def __str__(self):
        return f'{self.name} {self.value}'


def random_color():
    return tuple(np.random.randint(0, 255, 3))


def generate_color(i):
    rot = 3.88322207745*i
    r = 255 * max(np.cos(rot / 2) ** 2, 0)
    g = 255 * max(np.cos(rot / 2 + 2 * math.pi / 3) ** 2, 0)
    b = 255 * max(np.cos(rot / 2 + 4 * math.pi / 3) ** 2, 0)

    return tuple(np.array([r, g, b], dtype=np.uint8))
