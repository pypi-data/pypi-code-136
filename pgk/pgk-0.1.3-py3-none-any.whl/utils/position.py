import math


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def xy(self):
        return (self.x, self.y)

    @xy.setter
    def xy(self, value):
        self.x, self.y = value

    # int
    @property
    def int_x(self):
        return math.floor(self.x)

    @property
    def int_y(self):
        return math.floor(self.y)

    @property
    def int_xy(self):
        return (self.int_x, self.int_y)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(x={self.x}, y={self.y})"
