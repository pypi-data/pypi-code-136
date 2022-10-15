"""
The :mod:`gtFrame.basic` module implements basic Frames. These do
not account for any dynamics and just convert a static position and rotation
into another.

---------------
Module Contents
---------------
Variables:
    * origin2d
Classes:
    * RootFrame2d
    * Frame2d
    * RootFrame3d
    * Frame3d

"""

import numpy as np
from scipy.spatial.transform import Rotation as Rotation3d

import gtFrame.rotation


class RootFrame2d:
    """
    The RootFrame2d is the origin of the 2d-system and has a position vector of
    [0, 0] and a rotation of 0.
    """
    def __init__(self):
        """
        Constructor method. Sets position to [0, 0] and rotation to 0.
        """
        self.position = np.array([0, 0], dtype=np.float64)
        self.rotation = gtFrame.rotation.Rotation2d(0)

    def find_transform_path(self, frame):
        """
        Finds the transform path from this frame of reference to the given
        frame.

        :param frame: the frame of reference to find a transform path to
        :type frame: Frame2d
        :return: the transform path in a format that can be interpreted by
            Frame2d.transform_via_path().
        """
        path = list()
        current_frame = frame
        while current_frame != self:
            path.append((current_frame, "from"))
            current_frame = current_frame.parent()

        return path[::-1]      # path is generated in reverse


# Module variables
origin2d = RootFrame2d()


class Frame2d:
    """
    The frame 2d class represents a static 2d-frame.

    :param position: the relative position to the parent frame of reference
    :type position: np.ndarray
    :param rotation: the relative rotation to the parent frame of reference
    :type rotation: gtFrame.rotation.Rotation2d
    :param parent_frame: The parent frame of reference. The default value for
        this is :data:`gtFrame.basic.origin2d`.
    :type parent_frame: gtFrame.basic.Frame2d
    """
    def __init__(self, position, rotation,
                 parent_frame=origin2d):
        """
        Constructor method.
        """
        # Check if position is 2d-Vector
        if position.shape != (2,):
            raise ValueError("The given position vector is not of shape (2,)")

        self.position = position.copy()
        self.rotation = rotation
        self._parent = parent_frame

    def find_transform_path(self, frame):
        """
        Finds the reference path from this frame of reference to the given
        frame of reference. This is mainly used for the .transform_from and
        .transform_to methods. (This method is identical to
        :meth:`Frame3d.find_transform_path`.)

        :param frame: the destination frame of reference
        :type frame: Frame2d
        :return: the path as a list with the first step on [0] and the last at
            [-1]
        :rtype: list
        """
        # This is not the most algorithm, but I can't be bothered to implement
        # a tree and a pathfinding algorithm. Someday I might eventually ...
        # The algorithm can be improved by finding the duplicates in the path
        # and removing them.

        # ------------------------
        # this frame to the origin
        self_to_origin = list()
        current_frame = self

        while current_frame != origin2d:

            # check if desired frame is in the branch
            if current_frame == frame:
                return self_to_origin

            self_to_origin.append((current_frame, "to"))
            current_frame = current_frame.parent()

        # -------------------------------
        # destination frame to the origin
        frame_to_origin = list()
        current_frame = frame

        while current_frame != origin2d:

            # check if self frame is on the branch of frame
            if current_frame == self:
                return frame_to_origin[::-1]        # invert path to flip ends

            frame_to_origin.append((current_frame, "from"))
            current_frame = current_frame.parent()

        path = self_to_origin + frame_to_origin[::-1]
        return path

    def parent(self):
        """
        Returns the parent frame.

        :return: parent frame
        :rtype: Frame2d
        """
        return self._parent

    def transform_from_parent(self, vector):
        """
        Transform a vector, expressed in the parent frame, into this frame.

        :param vector: vector expressed in parent frame
        :type vector: np.ndarray
        :return: the vector expressed in this frame of reference
        :rtype: np.ndarray
        """
        relative_vector = vector - self.position
        return self.rotation.apply_inverse(relative_vector)

    def transform_to_parent(self, vector):
        """
        Return the given vector expressed in the parent frame of reference.

        :return: the vector in the parent frame of reference
        :rtype: np.ndarray
        """
        rotated_vector = self.rotation.apply(vector)
        return rotated_vector + self.position

    def transform_from(self, frame, vector):
        """
        Transform a vector expressed in an arbitrary frame of reference into
        this frame.

        :param frame: the frame of reference, in which the vector is defined
        :type frame: Frame2d
        :param vector: the vector to be transformed
        :type vector: np.ndarray
        :return: the transformed vector
        :rtype: np.ndarray
        """
        path = frame.find_transform_path(self)
        return Frame2d.transform_via_path(vector, path)

    def transform_to(self, frame, vector):
        """
        Transform a vector expressed in this frame of reference into a given
        frame of reference.

        :param frame: the frame to which to transform to
        :type frame: Frame2d
        :param vector: the vector to be transformed
        :type vector: np.ndarray
        :return: the transformed vector
        :rtype: np.ndarray
        """
        path = self.find_transform_path(frame)
        return Frame2d.transform_via_path(vector, path)

    @staticmethod
    def transform_via_path(vector, path):
        """
        Transforms a vector according to a given transform path.

        :param vector: the vector to be transformed
        :type vector: np.ndarray
        :param path: the path for the transformation, as returned by
            :meth:`gtFrame.basic.Frame2d.find_transform_path`
        :type path: list
        :return: the final vector after the transformations
        :rtype: np.ndarray
        """
        transformed = vector
        for frame, method in path:
            if method == "from":
                transformed = frame.transform_from_parent(transformed)
            elif method == "to":
                transformed = frame.transform_to_parent(transformed)
            else:
                raise ValueError("The used method was neither 'to' nor 'from'."
                                 " The path seems to be corrupted.")
        return transformed


class RootFrame3d:
    """
    The RootFrame3d is the origin of the 3d-system and has a position vector of
    [0, 0, 0] and a rotation of 0.
    """
    def __init__(self):
        """
        Constructor method
        """
        self.position = np.array([0, 0, 0], dtype=np.float64)
        self.rotation = Rotation3d.from_euler('xyz', np.array(
                                                        [0, 0, 0],
                                                        dtype=np.float64))

    def find_transform_path(self, frame):
        """
        Finds the transform path from this frame of reference to the given
        frame.

        :param frame: the frame of reference to find a transform path to
        :type frame: Frame3d
        :return: the transform path in a format that can be interpreted by
            Frame3d.transform_via_path().
        """
        path = list()
        current_frame = frame
        while current_frame != self:
            path.append((current_frame, "from"))
            current_frame = current_frame.parent()

        return path[::-1]      # path is generated in reverse


origin3d = RootFrame3d()


class Frame3d:
    """
    The Frame3d class represents a static 3d-frame.

    :param position: the relative position to the parent frame of reference
    :type position: np.ndarray
    :param rotation: the relative rotation to the parent frame of reference
    :type rotation: gtFrame.rotation.Rotation3d
    :param parent_frame: The parent frame of reference. The default value for
        this is :data:`gtFrame.basic.origin3d`.
    :type parent_frame: gtFrame.basic.Frame3d
    """
    def __init__(self, position, rotation, parent_frame=origin3d):
        """
        Constructor method
        """
        if position.shape != (3,):
            raise ValueError('The given position vector is not of shape (3,)')
        self.position = position.copy()
        self.rotation = rotation
        self._parent = parent_frame

    def find_transform_path(self, frame):
        """
        Finds the reference path from this frame of reference to the given
        frame of reference. This is mainly used for the .transform_from and
        .transform_to methods. (This method is identical to
        :meth:`Frame2d.find_transform_path`.)

        :param frame: the destination frame of reference
        :type frame: Frame3d
        :return: the path as a list with the first step on [0] and the last at
            [-1]
        :rtype: list
        """
        # This is not the most algorithm, but I can't be bothered to implement
        # a tree and a pathfinding algorithm. Someday I might eventually ...
        # The algorithm can be improved by finding the duplicates in the path
        # and removing them.

        # ------------------------
        # this frame to the origin
        self_to_origin = list()
        current_frame = self

        while current_frame != origin3d:

            # check if desired frame is in the branch
            if current_frame == frame:
                return self_to_origin

            self_to_origin.append((current_frame, "to"))
            current_frame = current_frame.parent()

        # -------------------------------
        # destination frame to the origin
        frame_to_origin = list()
        current_frame = frame

        while current_frame != origin3d:

            # check if self frame is on the branch of frame
            if current_frame == self:
                return frame_to_origin[::-1]        # invert path to flip ends

            frame_to_origin.append((current_frame, "from"))
            current_frame = current_frame.parent()

        path = self_to_origin + frame_to_origin[::-1]
        return path

    def parent(self):
        """
        Return the parent frame.

        :return: the parent frame
        :rtype: Frame3d
        """
        return self._parent

    def transform_from(self, frame, vector):
        """
        Transform a vector expressed in an arbitrary frame of reference into
        this frame.

        :param frame: the frame of reference, in which the vector is defined
        :type frame: Frame3d
        :param vector: the vector to be transformed
        :type vector: np.ndarray
        :return: the transformed vector
        :rtype: np.ndarray
        """
        path = frame.find_transform_path(self)
        return Frame3d.transform_via_path(vector, path)

    def transform_to(self, frame, vector):
        """
        Transform a vector expressed in this frame of reference into a given
        frame of reference.

        :param frame: the frame to which to transform to
        :type frame: Frame3d
        :param vector: the vector to be transformed
        :type vector: np.ndarray
        :return: the transformed vector
        :rtype: np.ndarray
        """
        path = self.find_transform_path(frame)
        return Frame3d.transform_via_path(vector, path)

    def transform_from_parent(self, vector):
        """
        Transform a vector given in the parent frame of reference into this
        frame.

        :param vector: the vector to be transformed
        :type vector: np.ndarray
        :return: the transformed vector
        :rtype: np.ndarray
        """
        interim = vector - self.position
        inverse_rotation = self.rotation.inv()
        return inverse_rotation.apply(interim)

    def transform_to_parent(self, vector):
        """
        Transform a vector given in this frame of reference into the parent
        frame.

        :param vector: the vector to be transformed
        :type vector: np.ndarray
        :return: the transformed vector
        :rtype: np.ndarray
        """
        interim = self.rotation.apply(vector)
        return interim + self.position

    @staticmethod
    def transform_via_path(vector, path):
        """
        Transforms a vector according to a given transform path.

        :param vector: the vector to be transformed
        :type vector: np.ndarray
        :param path: the path for the transformation, as returned by
            :meth:`gtFrame.basic.Frame3d.find_transform_path`
        :type path: list
        :return: the final vector after the transformations
        :rtype: np.ndarray
        """
        transformed = vector
        for frame, method in path:
            if method == "from":
                transformed = frame.transform_from_parent(transformed)
            elif method == "to":
                transformed = frame.transform_to_parent(transformed)
            else:
                raise ValueError("The used method was neither 'to' nor 'from'."
                                 " The path seems to be corrupted.")
        return transformed
