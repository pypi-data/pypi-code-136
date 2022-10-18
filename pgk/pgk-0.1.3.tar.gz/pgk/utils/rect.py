import pygame

from .position import Position
from .size import Size


class Rect(Position, Size):
    def __init__(self, pos, size):
        Position.__init__(self, *pos)
        Size.__init__(self, *size)

    @classmethod
    def from_pygame_rect(cls, rect):
        return cls(rect.topleft, rect.size)

    def colliderect(self, rect):
        return (
            min(self.x, self.x + self.w) < max(rect.x, rect.x + rect.w)
            and min(self.y, self.y + self.h) < max(rect.y, rect.y + rect.h)
            and max(self.x, self.x + self.w) > min(rect.x, rect.x + rect.w)
            and max(self.y, self.y + self.h) > min(rect.y, rect.y + rect.h)
        )

    @property
    def pygame_rect(self):
        return pygame.Rect(self.int_xy, self.int_wh)

    # basic
    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.h

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.w

    @top.setter
    def top(self, value):
        self.y = value

    @bottom.setter
    def bottom(self, value):
        self.y = value - self.h

    @left.setter
    def left(self, value):
        self.x = value

    @right.setter
    def right(self, value):
        self.x = value - self.w

    # advanced
    @property
    def topleft(self):
        return self.left, self.top

    @property
    def topright(self):
        return self.right, self.top

    @property
    def bottomleft(self):
        return self.left, self.bottom

    @property
    def bottomright(self):
        return self.right, self.bottom

    def __repr__(self):
        class_name = self.__class__.__name__
        x, y = self.xy
        w, h = self.wh
        return f"<{class_name}(x={x}, y={y}, width={w}, height={h})>"
