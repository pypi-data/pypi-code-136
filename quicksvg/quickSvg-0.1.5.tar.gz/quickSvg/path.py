# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     path
   Description :
   Author :       liaozhaoyan
   date：          2022/10/13
-------------------------------------------------
   Change Activity:
                   2022/10/13:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

from .tag import T


class Cell(object):
    # M x y
    @staticmethod
    def moveto(x, y, relative=False):
        prefix = "Mm"[relative]
        return " ".join(map(str, [prefix, x, y]))

    @staticmethod
    def M(x, y):
        return Cell.moveto(x, y, relative=False)

    @staticmethod
    def m(x, y):
        return Cell.moveto(x, y, relative=True)

    # L x y
    @staticmethod
    def line(x, y, relative=False):
        prefix = "Ll"[relative]
        return " ".join(map(str, [prefix, x, y]))

    @staticmethod
    def L(x, y):
        return Cell.line(x, y, relative=False)

    @staticmethod
    def l(x, y):
        return Cell.line(x, y, relative=True)

    # V y
    @staticmethod
    def vertical(y, relative=False):
        prefix = "Vv"[relative]
        return " ".join(map(str, [prefix, y]))

    @staticmethod
    def V(y):
        return Cell.vertical(y, relative=False)

    @staticmethod
    def v(y):
        return Cell.vertical(y, relative=True)

    # H x
    @staticmethod
    def horizontal(x, relative=False):
        prefix = "Hh"[relative]
        return " ".join(map(str, [prefix, x]))

    @staticmethod
    def H(x):
        return Cell.horizontal(x, relative=False)

    @staticmethod
    def h(x):
        return Cell.horizontal(x, relative=True)

    # Z
    @staticmethod
    def close(relative=False):
        # there's no difference between two, but consistent API is better
        return "Zz"[relative]

    @staticmethod
    def Z():
        return Cell.close(relative=False)

    @staticmethod
    def z():
        return Cell.close(relative=True)

    # C x1 y1 x2 y2 x y
    @staticmethod
    def cubic(x1, y1, x2, y2, x, y, relative=False):
        prefix = "Cc"[relative]
        return " ".join(map(str, [prefix, x1, y1, x2, y2, x, y]))

    @staticmethod
    def C(x1, y1, x2, y2, x, y):
        return Cell.cubic(x1, y1, x2, y2, x, y, relative=False)

    @staticmethod
    def c(x1, y1, x2, y2, x, y):
        return Cell.cubic(x1, y1, x2, y2, x, y, relative=True)

    # S x2 y2, x y
    @staticmethod
    def shorthand(x2, y2, x, y, relative=False):
        prefix = "Ss"[relative]
        return " ".join(map(str, [prefix, x2, y2, x, y]))

    @staticmethod
    def S(x2, y2, x, y):
        return Cell.shorthand(x2, y2, x, y, relative=False)

    @staticmethod
    def s(x2, y2, x, y):
        return Cell.shorthand(x2, y2, x, y, relative=True)

    # Q x1 y1 x y
    @staticmethod
    def quadratic(x1, y1, x, y, relative=False):
        prefix = "Qq"[relative]
        return " ".join(map(str, [prefix, x1, y1, x, y]))

    @staticmethod
    def Q(x1, y1, x, y):
        return Cell.quadratic(x1, y1, x, y, relative=False)

    @staticmethod
    def q(x1, y1, x, y):
        return Cell.quadratic(x1, y1, x, y, relative=True)

    # T x y
    @staticmethod
    def q_shorthand(x, y, relative=False):
        prefix = "Tt"[relative]
        return " ".join(map(str, [prefix, x, y]))

    @staticmethod
    def T(x, y):
        return Cell.q_shorthand(x, y, relative=False)

    @staticmethod
    def t(x, y):
        return Cell.q_shorthand(x, y, relative=True)

    # A rx ry x-axis-rotation large-arc-flag sweep-flag x y
    @staticmethod
    def arc(radius_x, radius_y, x_axis_rotation, large_arc_flag, sweep_flag, x, y, relative=False):
        prefix = "Aa"[relative]
        return " ".join(map(str, [prefix, radius_x, radius_y, x_axis_rotation, large_arc_flag, sweep_flag, x, y]))

    @staticmethod
    def A(radius_x, radius_y, x_axis_rotation, large_arc_flag, sweep_flag, x, y):
        return Cell.arc(radius_x, radius_y, x_axis_rotation, large_arc_flag, sweep_flag, x, y,
                        relative=False)

    @staticmethod
    def a(radius_x, radius_y, x_axis_rotation, large_arc_flag, sweep_flag, x, y):
        return Cell.arc(radius_x, radius_y, x_axis_rotation, large_arc_flag, sweep_flag, x, y,
                        relative=True)

    @staticmethod
    def build(commands):
        return " ".join(commands)


class Path(T):
    def __init__(self, cells, **attributes):
        dString = Cell.build(cells)
        attributes['d'] = dString
        super(Path, self).__init__("path", **attributes)


if __name__ == "__main__":
    p = Path(
        (Cell.line(10, 10),
         Cell.moveto(3, 3)),
        style="stroke: black; fill: #ffcccc"
    )
    print(p.build())
    pass
