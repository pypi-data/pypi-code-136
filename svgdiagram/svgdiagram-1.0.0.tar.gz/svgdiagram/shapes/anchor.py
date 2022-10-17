import math


class Anchor:
    def __init__(self, x, y, normal_x, normal_y):
        self.x = x
        self.y = y
        self.normal_x = normal_x
        self.normal_y = normal_y

        self._normalize()

    def _normalize(self):
        normal_len = math.sqrt(self.normal_x**2 + self.normal_y**2)
        assert normal_len > 0, "Normal length is zero!"
        self.normal_x /= normal_len
        self.normal_y /= normal_len
