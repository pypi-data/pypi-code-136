import math
import numpy as np
from ..utils import cal_distance
from ..utils import is_iterable


def cartesian_to_polar(point_xy, center_xy, reverse_y=True):
    x, y = point_xy
    center_x, center_y = center_xy
    r = cal_distance(point_xy, center_xy)
    if r == 0:
        theta = 0
    elif r > 0:
        y_ = y - center_y
        if reverse_y:
            y_ = - y_
        x_ = x - center_x
        theta = math.asin(abs(y_) / max(1, abs(r)))
        if y_ >= 0 and x_ >= 0:
            pass
        elif y_ >= 0 and x_ < 0:
            theta = np.pi - theta
        elif y_ < 0 and x_ < 0:
            theta = np.pi + theta
        elif y_ < 0 and x_ >= 0:
            theta = 2 * np.pi - theta
        else:
            raise RuntimeError(f'bad y_ {y_} x_ {x_}')
    else:
        raise RuntimeError(f'bad distance {r}')
    return r, theta

def polar_to_cartesian(r, theta, center_xy, reverse_y=False):
    center_x, center_y = center_xy
    r = np.array(r)
    theta = np.array(theta)
    if reverse_y:
        y = center_y - r * np.sin(theta)
    else:
        y = center_y + r * np.sin(theta)
    x = center_x + r * np.cos(theta)

    point_xy = np.vstack([x, y]).T.tolist()
    return point_xy

def cal_length(vector):
    return (np.array(vector) ** 2).sum() ** 0.5

def get_angle_from_vector(vector, degree=False):
    assert len(vector) == 2
    assert (np.array(vector) ** 2).sum() > 0
    length = cal_length(vector)
    x, y = vector[:2]
    sin_res = y / length
    cos_res = x / length
    radians = np.arccos(cos_res)
    if sin_res < 0:
        radians = np.pi * 2 - radians
    if degree:
        return radians / np.pi * 180
    else:
        return radians


class LogicOp:
    @staticmethod
    def EqualTo(value):
        def func(input):
            if input == value:
                return True
            else:
                return False
        return func

    @staticmethod
    def NotEqualTo(value):
        def func(input):
            if input != value:
                return True
            else:
                return False
        return func

    @staticmethod
    def LargerThan(value):
        def func(input):
            if input > value:
                return True
            else:
                return False
        return func

    @staticmethod
    def LessThan(value):
        def func(input):
            if input < value:
                return True
            else:
                return False
        return func

    @staticmethod
    def NotLessThan(value):
        def func(input):
            if input >= value:
                return True
            else:
                return False
        return func
    
    @staticmethod
    def NotLargerThan(value):
        def func(input):
            if input <= value:
                return True
            else:
                return False
        return func
    
    @staticmethod
    def In(value):
        assert is_iterable(value)
        def func(input):
            if input in value:
                return True
            else:
                return False
        return func

    @staticmethod
    def NotIn(value):
        assert is_iterable(value)
        def func(input):
            if input in value:
                return False
            else:
                return True
        return func
    
    @staticmethod
    def Is(value):
        def func(input):
            if input is value:
                return True
            else:
                return False
        return func
    
    @staticmethod
    def IsNot(value):
        def func(input):
            if input is not value:
                return True
            else:
                return False
        return func
    
    @staticmethod
    def IsTrue():
        def func(input):
            if input:
                return True
            else:
                return False
        return func
    
    @staticmethod
    def IsFalse():
        def func(input):
            if not input:
                return True
            else:
                return False
        return func


def make_rotate_matrix_2d(alpha, radian_mode=True):
    """
    x 轴正方向 - 3 点
    y 轴正方向 - 12 点
    顺时针旋转 alpha 角
    """
    if not radian_mode:
        alpha = alpha / 180 * np.pi
    matrix = np.array([
        [np.cos(alpha), - np.sin(alpha)],
        [np.sin(alpha), np.cos(alpha)]
        ])
    return matrix


def point_rotate(point, center, alpha=0, rotate_matrix=None, radian_mode=True):
    """_summary_

    Args:
        point ([x,y]): point to be rotated
        center ([x,y]): center of rotation
        alpha (float): rotate angle, if rotate_matrix set, this value will be ignored. Defaults to 0.
        rotate_matrix (2d matrix): rotate matrix 2d, if not set, will build by angle. Defaults to None.
        radian_mode (bool, optional): if True, alpha is considered to be a radian. Defaults to True.

    Returns:
        _type_: _description_
    """
    point = np.array(point)
    center = np.array(center)
    if (point == center).all():
        return point
    if rotate_matrix is None:
        rotate_matrix = make_rotate_matrix_2d(alpha, radian_mode)
    delt_x, delt_y = point - center
    new_point = np.matmul(np.array([delt_x, delt_y]), rotate_matrix)
    return new_point


def polygon_rotate(polygon, center, alpha=0, rotate_matrix=None, radian_mode=True):
    if len(polygon):
        polygon_matrix = np.array(polygon) - center
    else:
        return polygon

    assert polygon_matrix.ndim == 2
    assert polygon_matrix.shape[1] == 2

    if rotate_matrix is None:
        rotate_matrix = make_rotate_matrix_2d(alpha, radian_mode)

    rotated_polygon = np.matmul(polygon_matrix, rotate_matrix) + center

    return rotated_polygon.tolist()