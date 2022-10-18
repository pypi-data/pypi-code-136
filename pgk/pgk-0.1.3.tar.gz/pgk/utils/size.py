import math


class Size:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    @property
    def width(self):
        return self.w

    @property
    def height(self):
        return self.h

    @width.setter
    def width(self, value):
        self.w = value

    @height.setter
    def height(self, value):
        self.h = value

    @property
    def wh(self):
        return (self.width, self.height)

    @wh.setter
    def wh(self, value):
        self.w, self.h = value

    # int
    @property
    def int_w(self):
        return math.floor(self.w)

    @property
    def int_h(self):
        return math.floor(self.h)

    @property
    def int_width(self):
        return self.int_w

    @property
    def int_height(self):
        return self.int_h

    @property
    def int_wh(self):
        return (self.int_width, self.int_height)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(w={self.w}, h={self.h})"
