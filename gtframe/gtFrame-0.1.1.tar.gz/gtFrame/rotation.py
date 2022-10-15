"""
This module contains helper functions and classes to work with rotations.
Mainly this is used for 2d-rotations as 3d-rotations are handled with scipy.

---------------
Module Contents
---------------
Classes:
    * Rotation2d
"""

import math

import numpy as np


class Rotation2d:
    """
    Describes a rotation in two-dimensional space.

    :param angle: the rotation angle from the reference direction [0, 0]
        expressed in radians
    :type angle: float
    """
    def __init__(self, angle):
        """
        Constructor method.
        """
        self._angle = angle
        self._matrix = np.array([
            [math.cos(self._angle), - math.sin(self._angle)],
            [math.sin(self._angle), math.cos(self._angle)]], dtype=np.float64)

    def apply(self, vector):
        """
        Apply the rotation to a given 2d-vector.

        :param vector: the vector as a numpy array
        :type vector: np.ndarray
        :return: the transformed vector as a numpy array
        :rtype: np.ndarray
        """
        vector = vector.copy()
        return self._matrix @ vector

    def apply_inverse(self, vector):
        """
        Apply the inverse of the rotation. This reverts the rotation.
        I.e. it reverts the :meth:`.apply` method.

        :param vector: the vector on which to apply the inverse rotation as a
            numpy array
        :type vector: np.ndarray
        :return: the transformed vector as a numpy array
        :rtype: np.ndarray
        """
        inverse = self.as_inverse()
        return inverse @ vector

    def as_degrees(self):
        """
        Returns the rotation as an angle expressed in degrees.

        :return: the rotation as an angle expressed in degrees
        :rtype: float
        """
        return math.degrees(self._angle)

    def as_inverse(self):
        """
        Returns the rotation as the inverse of the rotation matrix.

        :return: the inverse rotation matrix
        :rtype: np.ndarray
        """
        return np.linalg.inv(self._matrix)

    def as_matrix(self):
        """
        Returns the rotation as a rotation matrix (numpy array).

        :return: the rotation as a rotation matrix
        :rtype: numpy.ndarray
        """
        return self._matrix

    def as_rad(self):
        """
        Returns the rotation as an angle expressed in radians.

        :return: the rotation as an angle expressed in radians
        :rtype: float
        """
        return self._angle

    def is_close(self, rotation, rtol=1e-09, atol=0.0):
        """
        Checks wether two :class:`gtFrame.rotation.Rotation2d` objects are
        close.

        :param rotation: the other rotation object
        :type rotation: Rotation2d
        :param rtol: relative tolerance
        :type rtol: float
        :param atol: absolute tolerance
        :type atol: float
        :return: Wether the two rotations are close.
        :rtype: bool
        """
        return math.isclose(self._angle, rotation.as_rad(), rel_tol=rtol,
                            abs_tol=atol)

    def update(self, angle):
        """
        Updates (changes) the rotation.

        :param angle: the new desired angle expressed in radians
        :type angle: float
        :return: None
        :rtype: None
        """
        self._angle = angle
        self._matrix = np.array([
            [math.cos(self._angle), - math.sin(self._angle)],
            [math.sin(self._angle), math.cos(self._angle)]], dtype=np.float64)
