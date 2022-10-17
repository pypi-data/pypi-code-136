"""
Copyright 2022 David Woodburn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
--------------------------------------------------------------------------------
Conversions
-----------
This library includes three sets of functions: general array checks,
attitude-representation conversions, and reference-frame conversions.  The
following table shows all the attitude-representation conversions provided,
where 'Vector' is short for 'rotation vector,' 'RPY is short for 'roll, pitch,
and yaw,' and 'DCM' is short for 'direction cosine matrix':

    To \\ From | Vector | Axis-angle | RPY    | DCM    | Quaternion
    ---------- | ------ | ---------- | ------ | ------ | ----------
    Vector     |   -    |     x      |        |        |
    Axis-angle |   x    |     -      |   X    |   X    |     x
    RPY        |        |     X      |   -    |   x    |     X
    DCM        |        |     X      |   x    |   -    |     x
    Quaternion |        |     x      |   x    |   x    |     -

Because the conversion from rotation vector to axis-angle is so trivial, none of
the other attitude representations have conversions to rotation vectors.

In addition to the conversion from the z, y, x sequence of Euler angles to a
DCM, the function `rot` is also provided for creating a DCM from a generic set
of Euler angles in any desired sequence of axes.

Passive Rotations
-----------------
All rotations are interpreted as passive.  This means they represent rotations
of reference frames, not of vectors.

Vectorization
-------------
When possible, the functions are vectorized in order to handle processing
batches of values.  A set of scalars is a 1D array.  A set of vectors is a 2D
array, with each vector in a column.  So, a (3, 7) array is a set of seven
vectors, each with 3 elements.  A set of matrices is a 3D array with each matrix
in a stack.  The first index is the stack number.  So, a (2, 5, 5) array is a
stack of two 5x5 matrices.  Roll, pitch, and yaw are not treated as a vector but
as three separate quantities.  The same is true for latitude, longitude, and
height above ellipsoid.  A quaternion is passed around as an array.

Robustness
----------
In general, the functions in this library check that the inputs are of the
correct type and shape.  They do not generally handle converting inputs which do
not conform to the ideal type and shape.
"""

__author__ = "David Woodburn"
__license__ = "MIT"
__date__ = "2022-10-16"
__maintainer__ = "David Woodburn"
__email__ = "david.woodburn@icloud.com"
__status__ = "Development"

import numpy as np

# WGS84 constants (IS-GPS-200M and NIMA TR8350.2)
A_E = 6378137.0             # Earth's semi-major axis [m] (p. 109)
F_E = 298.257223563         # Earth's flattening constant (NIMA)
B_E = 6356752.314245        # Earth's semi-minor axis [m] A_E*(1 - 1/F_E)
E2 = 6.694379990141317e-3   # Earth's eccentricity squared [ND] (derived)
W_EI = 7.2921151467e-5      # sidereal Earth rate [rad/s] (p. 106)
TOL = 1e-7                  # Default tolerance

# --------------------
# General Array Checks
# --------------------

def check_vec(vec):
    """
    Check rotation vector inputs.

    Parameters
    ----------
    vec : (N,) or (N, M) np.ndarray
        Rotation vector or matrix of M rotation vectors as the columns.

    Returns
    -------
    same as parameters
    """
    if not isinstance(vec, np.ndarray):
        raise TypeError("Input vec must be a Numpy array.")
    if vec.ndim != 1 and vec.ndim != 2:
        raise TypeError("Input vec must have one or two dimensions.")
    if vec.shape[0] != 3:
        raise ValueError("Input vec must have 3 elements or 3 rows.")
    if vec.dtype == int:
        vec = vec.astype(float)
    return vec


def check_axang(ax, ang):
    """
    Check axis and angle inputs.

    Parameters
    ----------
    ax : (N,) or (N, M) np.ndarray
        Rotation axis vector or matrix of M rotation axis vectors as the
        columns.
    ang : float or (M,) np.ndarray
        Rotation angle or array of M rotation angles.  This is a positive value.

    Returns
    -------
    same as parameters
    """

    if not isinstance(ax, np.ndarray):
        raise TypeError("Input ax must be a Numpy array.")
    if ax.ndim != 1 and ax.ndim != 2:
        raise ValueError("Input ax must have one or two dimensions.")
    if ax.shape[0] != 3:
        raise ValueError("Input vec must have 3 elements or 3 rows.")
    if ax.dtype == int:
        ax = ax.astype(float)
    if not isinstance(ang, float) and not isinstance(ang, int):
        if isinstance(ang, np.ndarray):
            if ang.ndim != 1:
                raise TypeError("Input ang should be a scalar float or a " +
                    "1D Numpy array.")
            if ax.ndim != 2:
                raise TypeError("Input ang should be a scalar float if " +
                    "input ax is a 1D Numpy array.")
            if len(ang) != ax.shape[1]:
                raise ValueError("Input ang should have as many values " +
                    "as input ax has columns.")
        else:
            raise TypeError("Input ang should be a scalar float.")
    return ax, ang


def check_rpy(r, p, y, degs=None):
    """
    Check roll, pitch, and yaw inputs.

    Parameters
    ----------
    r : float or (M,) np.ndarray
        Roll Euler angle in radians.
    p : float or (M,) np.ndarray
        Pitch Euler angle in radians.
    y : float or (M,) np.ndarray
        Yaw Euler angle in radians.
    degs : bool, default False
        Flag to interpret angles as degrees.

    Returns
    -------
    same as parameters
    """

    if degs is None:
        degs = False
    if degs:
        p_max = 90.0
    else:
        p_max = np.pi/2

    if isinstance(r, (float, int)) and \
            isinstance(p, (float, int)) and \
            isinstance(y, (float, int)):
        if isinstance(r, int):
            r = float(r)
        if isinstance(p, int):
            p = float(p)
        if isinstance(y, int):
            y = float(y)
        if abs(p) > p_max:
            raise ValueError("Pitch must not exceed pi/2 in magnitude.")
    elif isinstance(r, np.ndarray) and \
            isinstance(p, np.ndarray) and \
            isinstance(y, np.ndarray):
        if r.dtype is int:
            r = r.astype(float)
        if p.dtype is int:
            p = p.astype(float)
        if y.dtype is int:
            y = y.astype(float)
        if (np.abs(p) > p_max).any():
            raise ValueError("Pitch must not exceed pi/2 in magnitude.")
        if r.ndim != 1 or p.ndim != 1 or y.ndim != 1:
            raise TypeError("Roll, pitch, and yaw must be 1D arrays.")
        if len(r) != len(p) or len(p) != len(y):
            raise ValueError("Roll, pitch, and yaw must be the same lengths.")
    else:
        raise TypeError("Roll, pitch, and yaw must all be scalars or " +
            "1D arrays.")
    return r, p, y


def is_square(C, N=None):
    """
    Check if the variable `C` is a square matrix or stack of square matrices.
    If `N` is provided, check that `C` is a square matrix with length `N`.

    Parameters
    ----------
    C : (N, N) or (M, N, N) np.ndarray
        Matrix or stack of M matrices.
    N : int, default None
        Intended length of `C` matrix.

    Returns
    -------
    True or False
    """

    # Check the inputs.
    if not isinstance(C, np.ndarray):
        raise TypeError("Input C should be a Numpy array.")
    if N is not None and not isinstance(N, int):
        raise TypeError("Input N should be an integer.")

    # Check the squareness of `C`.
    if C.ndim == 2:
        if N is not None:
            if C.shape == (N, N):
                return True
            else:
                return False
        else:
            if C.shape[0] == C.shape[1]:
                return True
            else:
                return False
    if C.ndim == 3:
        if N is not None:
            if C.shape[1] == N and C.shape[2] == N:
                return True
            else:
                return False
        else:
            if C.shape[1] == C.shape[2]:
                return True
            else:
                return False
    else:
        return False


def is_ortho(C, tol=None):
    """
    Check if the matrix `C` is orthogonal.

    Parameters
    ----------
    C : (N, N) or (M, N, N) np.ndarray
        Square matrix or stack of M square matrices.
    tol : float, default 1e-7
        Tolerance on deviation from true orthogonality.

    Returns
    -------
    True if C is an orthogonal matrix, False otherwise.

    Notes
    -----
    A matrix `C` is defined to be orthogonal if ::

           T
        C C  = I .

    So, by getting the matrix product of `C` with its transpose and subtracting
    the identy matrix, we should have a matrix of zeros.  The default tolerance
    is a reflection of 32-bit, floating-point precision.
    """

    # Check inputs.
    if not isinstance(C, np.ndarray):
        raise TypeError("Input C should be a Numpy array.")
    if C.ndim == 2:
        if C.shape[0] != C.shape[1]:
            raise ValueError("Input C should be a square matrix.")
    elif C.ndim == 3:
        if C.shape[1] != C.shape[2]:
            raise ValueError("Input C should be a stack of square matrices.")
    else:
        raise TypeError("Input C should be a 2D or 3D Numpy array.")
    if tol is None:
        tol = TOL
    elif not isinstance(tol, float):
        raise TypeError("Input tol should be a float.")

    # Check if the matrix is orthogonal.
    if C.ndim == 2:
        Z = np.abs(C @ C.T - np.eye(C.shape[0]))
        if (Z > tol).any():
            return False
        else:
            return True
    elif C.ndim == 3:
        Z = np.abs(C @ C.transpose((0, 2, 1)) - np.eye(C.shape[1]))
        if (Z > tol).any():
            return False
        else:
            return True


def check_dcm(C):
    """
    Check direction cosine matrix inputs.

    Parameters
    ----------
    C : (3, 3) or (M, 3, 3) np.ndarray
        Rotation direction cosine matrix or stack of M such matrices.

    Returns
    -------
    same as parameters
    """

    if not is_square(C, 3):
        raise ValueError('DCM must be a square of size 3')
    if not is_ortho(C):
        raise ValueError('DCM must be orthogonal')
    C = C.astype(float)

    return C


def check_quat(q):
    """
    Check quaternion inputs.

    Parameters
    ----------
    q : (4,) or (4, M) np.ndarray
        Array of quaternion elements or matrix of M arrays of quaternion
        elements as the columns.  The elements are a, b, c, and d where the
        quaterion `q` is a + b i + c j + d k.

    Returns
    -------
    same as parameters
    """

    if not isinstance(q, np.ndarray):
        raise TypeError("Input q must be a Numpy array.")
    if q.ndim != 1 and q.ndim != 2:
        raise ValueError("Input q must have one or two dimensions.")
    if q.shape[0] != 4:
        raise ValueError("Input q must have 4 elements or 4 rows.")
    if q.dtype == int:
        q = q.astype(float)
    return q


def check_xyz(xyz):
    """
    Check x, y, and z inputs.

    Parameters
    ----------
    xyz : (3,) or (3, M) np.ndarray
        x, y, and z-axis position vector in meters or matrix of M such vectors
        as columns.

    Returns
    -------
    same as parameters
    """

    if not isinstance(xyz, np.ndarray):
        raise TypeError("Input xyz must be a Numpy array.")
    if xyz.shape[0] != 3:
        raise ValueError("Input xyz must 3 elements or 3 rows.")
    xyz = xyz.astype(float)

    return xyz


def check_llh(lat, lon, hae, degs=None):
    """
    Check latitude, longitude, and height above ellipsoid inputs.

    Parameters
    ----------
    lat : float or np.ndarray
        Geodetic latitude in radians.
    lon : float or np.ndarray
        Geodetic longitude in radians.
    hae : float or np.ndarray
        Height above ellipsoid in meters.
    degs : bool, default False
        Flag to interpret angles as degrees.

    Returns
    -------
    same as parameters
    """

    if degs is None:
        degs = False
    if degs:
        lat_max = 90.0
    else:
        lat_max = np.pi/2

    if isinstance(lat, np.ndarray) and isinstance(lon, np.ndarray) and \
            isinstance(hae, np.ndarray):
        if (len(lat) != len(lon)) or (len(lon) != len(hae)):
            raise ValueError("lat, lon, and hae must be the same lengths.")
        lat = lat.astype(float)
        lon = lon.astype(float)
        hae = hae.astype(float)
        if (np.abs(lat) > lat_max).any():
            raise ValueError("Input lat must not exceed pi/2 radians.")
    elif isinstance(lat, (float, int)) and isinstance(lon, (float, int)) and \
            isinstance(hae, (float, int)):
        lat = float(lat)
        lon = float(lon)
        hae = float(hae)
        if abs(lat) > lat_max:
            raise ValueError("Input lat must not exceed pi/2 radians.")
    else:
        raise TypeError("lat, lon, and hae must be the same types.")

    return lat, lon, hae

# -----------------------------------
# Attitude-representation Conversions
# -----------------------------------

def axis_angle_to_vector(ax, ang, degs=None):
    """
    Convert an axis vector, `ax`, and a rotation angle, `ang`, to a rotation
    vector.

    Parameters
    ----------
    ax : (N,) or (N, M) np.ndarray
        Rotation axis vector or matrix of M rotation axis vectors as the
        columns.
    ang : float or (M,) np.ndarray
        Rotation angle or array of M rotation angles.  This is a positive value.
    degs : bool, default False
        Flag to interpret angles as degrees.

    Returns
    -------
    vec : (N,) or (N, M) np.ndarray
        Rotation vector or matrix of M rotation vectors as the columns.

    See Also
    --------
    vector_to_axis_angle
    """

    # Check the inputs.
    ax, ang = check_axang(ax, ang)

    # Scale the angle.
    if degs is None:
        degs = False
    if degs:
        ang *= np.pi/180

    # Convert to a rotation vector.
    vec = ax*ang

    return vec


def vector_to_axis_angle(vec):
    """
    Convert a rotation vector, `vec`, to an axis-angle representation.

    Parameters
    ----------
    vec : (N,) or (N, M) np.ndarray
        Rotation vector or matrix of M rotation vectors as the columns.

    Returns
    -------
    ax : (N,) or (N, M) np.ndarray
        Rotation axis vector or matrix of M rotation axis vectors as the
        columns.
    ang : float or (M,) np.ndarray
        Rotation angle or array of M rotation angles.  This is a positive value.

    See Also
    --------
    axis_angle_to_vector
    """

    # Check the input.
    vec = check_vec(vec)

    # Convert to axis vector and angle magnitude.
    if vec.ndim == 1:
        ang = np.linalg.norm(vec)
        ax = vec/ang
    else:
        ang = np.linalg.norm(vec, axis=0)
        ax = vec/ang

    return ax, ang


def rpy_to_axis_angle(r, p, y, degs=None):
    """
    Convert roll, pitch, and yaw Euler angles to rotation axis vector and
    rotation angle.

    Parameters
    ----------
    r : float or (M,) np.ndarray
        Roll Euler angle in radians.
    p : float or (M,) np.ndarray
        Pitch Euler angle in radians.
    y : float or (M,) np.ndarray
        Yaw Euler angle in radians.

    Returns
    -------
    ax : (N,) or (N, M) np.ndarray
        Rotation axis vector or matrix of M rotation axis vectors as the
        columns.
    ang : float or (M,) np.ndarray
        Rotation angle or array of M rotation angles.  This is a positive value.

    See Also
    --------
    axis_angle_to_rpy

    Notes
    -----
    This is a convenience function which converts roll, pitch, and yaw to a
    quaternion and then the quaternion to an axis vector and rotation angle.
    """

    q = rpy_to_quat(r, p, y, degs)
    ax, ang = quat_to_axis_angle(q)

    return ax, ang


def axis_angle_to_rpy(ax, ang, degs=None):
    """
    Convert rotation axis vector, `ax`, and angle, `ang`, to roll, pitch, and
    yaw vectors.

    Parameters
    ----------
    ax : (N,) or (N, M) np.ndarray
        Rotation axis vector or matrix of M rotation axis vectors as the
        columns.
    ang : float or (M,) np.ndarray
        Rotation angle or array of M rotation angles.  This is a positive value.

    Returns
    -------
    r : float or (M,) np.ndarray
        Roll Euler angle in radians.
    p : float or (M,) np.ndarray
        Pitch Euler angle in radians.
    y : float or (M,) np.ndarray
        Yaw Euler angle in radians.

    See Also
    --------
    rpy_to_axis_angle

    Notes
    -----
    This function converts a vector rotation axis, `ax`, and a rotation angle,
    `ang`, to a vector of roll, pitch, and yaw Euler angles.  The sense of the
    rotation is maintained.  To make the conversion, some of the elements of the
    corresponding DCM are calculated as an intermediate step.  The DCM is
    defined in terms of the elements of the corresponding quaternion, `q`, as ::

        q = a + b i + c j + d k

            .-                                                            -.
            |   2    2    2    2                                           |
            | (a  + b  - c  - d )    2 (b c + a d)       2 (b d - a c)     |
            |                                                              |
            |                       2    2    2    2                       |
        C = |    2 (b c - a d)    (a  - b  + c  - d )    2 (c d + a b)     |
            |                                                              |
            |                                           2    2    2    2   |
            |    2 (b d + a c)       2 (c d - a b)    (a  - b  - c  + d )  |
            '-                                                            -'

    where ::

        ax = [x  y  z]'
        a =   cos(ang/2)
        b = x sin(ang/2)
        c = y sin(ang/2)
        d = z sin(ang/2)

    Here `ax` is assumed to be a unit vector.  We will overcome this limitation
    later.  Using the half-angle identities ::

           2.- ang -.   1 - cos(ang)           2.- ang -.   1 + cos(ang)
        sin | ----- | = ------------        cos | ----- | = ------------
            '-  2  -'        2                  '-  2  -'        2

    we can simplify, as an example, the expression ::

          2    2    2    2
        (a  + b  - c  - d )

    to ::

                    2
        cos(ang) + x (1 - cos(ang)) .

    We can also use the fact that ::

              .- ang -.     .- ang -.
        2 cos | ----- | sin | ----- | = sin(ang)
              '-  2  -'     '-  2  -'

    to simplify ::

        2 (b c - a d)

    to ::

        x y (1 - cos(ang)) - z sin(ang)

    Through these simplifications the `C` can be redefined as ::

            .-         2                                     -.
            |    co + x cc     x y cc + z si   x z cc - y si  |
            |                                                 |
            |                           2                     |
        C = |  x y cc - z si     co + y cc     y z cc + x si  |
            |                                                 |
            |                                            2    |
            |  x z cc + y si   y z cc - x si     co + z cc    |
            '-                                               -'

    where `co` is the cosine of the angle, `si` is the sine of the angle, and
    `cc` is the compelement of the cosine: `(1 - co)`.

    Before the algorithm described above is applied, the `ax` input is first
    normalized.  The norm is not thrown away.  Rather it is multiplied into the
    `ang` value.  This overcomes the limitation of assuming the axis vector is a
    unit vector.

    The `C` can also be defined in terms of the roll, pitch, and yaw as ::
            .-             -.
            |  c11 c12 c13  |
        C = |  c21 c22 c23  |
            |  c31 c32 c33  |
            '-             -'
            .-                                                 -.
            |       (cy cp)             (sy cp)          -sp    |
          = |  (cy sp sr - sy cr)  (sy sp sr + cy cr)  (cp sr)  |
            |  (sy sr + cy sp sr)  (sy sp cr - cy sr)  (cp cr)  |
            '-                                                 -'

    where `c` and `s` mean cosine and sine, respectively, and `r`, `p`, and `y`
    mean roll, pitch, and yaw, respectively, then we can see that ::

                                        .- cp sr -.
        r = arctan2(c23, c33) => arctan | ------- |
                                        '- cp cr -'

                                        .- sy cp -.
        y = arctan2(c12, c11) => arctan | ------- |
                                        '- cy cp -'

    where the `cp` values cancel in both cases.  The value for pitch can be
    found from `c13` alone::

        p = -arcsin(c13)

    This function does not take advantage of the more advanced formula for pitch
    that we might use when the input is actually a DCM.

    Putting this together, the `ax` vector is normalized and its norm applied to
    the angle::

                .-----------------
               /   2      2      2
        nm = |/ ax1  + ax2  + ax3

             ax1             ax2
        x = -----       y = -----
             nm              nm

             ax3
        z = -----       ang = ang nm .
             nm

    Then the necessary elements of the DCM are calculated::

                    2
        c11 = co + x (1 - co)       c12 = x y (1 - co) + z si

                                    c13 = x z (1 - co) - y si
                    2
        c33 = co + z (1 - co)       c23 = y z (1 - co) + x si

    where `co` and `si` are the cosine and sine of `ang`.  Now we can get roll,
    pitch, and yaw:

        r =  arctan2(c23, c33)
        p = -arcsin(c13)
        y =  arctan2(c12, c11)
    """

    # Check the inputs.
    ax, ang = check_axang(ax, ang)

    # Scale the angle.
    if degs is None:
        degs = False
    if degs:
        ang *= np.pi/180

    # Normalize and parse the vector rotation axis.
    nm = np.linalg.norm(ax, axis=0)
    x = ax[0]/nm
    y = ax[1]/nm
    z = ax[2]/nm
    ang = ang*nm

    # Get the cosine, sine, and complement of cosine of the angle.
    co = np.cos(ang)
    si = np.sin(ang)
    cc = 1 - co # complement of cosine

    # Populate the DCM.
    c11 = co + (x**2)*cc
    c33 = co + (z**2)*cc
    c12 = x*y*cc + z*si
    c13 = x*z*cc - y*si
    c23 = y*z*cc + x*si

    # Build the output.
    r = np.arctan2(c23, c33)
    p = -np.arcsin(c13)
    y = np.arctan2(c12, c11)

    return r, p, y


def dcm_to_axis_angle(C):
    """
    Convert from a DCM to a rotation axis vector, `ax`, and rotation angle,
    `ang`.

    Parameters
    ----------
    C : (3, 3) or (M, 3, 3) np.ndarray
        Rotation direction cosine matrix or stack of M such matrices.

    Returns
    -------
    ax : (N,) or (N, M) np.ndarray
        Rotation axis vector or matrix of M rotation axis vectors as the
        columns.
    ang : float or (M,) np.ndarray
        Rotation angle or array of M rotation angles.  This is a positive value.

    Notes
    -----
    This function converts a direction cosine matrix, `C`, to a rotation axis
    vector, `ax`, and rotation angle, `ang`.  Here, the DCM is considered to
    represent a zyx sequence of right-handed rotations.  This means it has the
    same sense as the axis vector and angle pair.  The conversion is achieved by
    calculating a quaternion as an intermediate step.

    The implementation here is Cayley's method for obtaining the quaternion.  It
    is used because of its superior numerical accuracy.  This comes from the
    fact that it uses all nine of the elements of the DCM matrix.  It also does
    not suffer from numerical instability due to division as some other methods
    do.

    Defining the rotation axis vector to be a unit vector, we will define the
    quaterion in terms of the axis and angle::

        ax = [x  y  z]'
        a =   cos(ang/2)
        b = x sin(ang/2)
        c = y sin(ang/2)
        d = z sin(ang/2)
        q = a + b i + c j + d k

    where `q` is the quaternion and `ax` is the rotation axis vector.  Then, the
    norm of [b, c, d] will be ::

           .-----------       .---------------------------
          / 2    2    2      /  2    2    2     2.- ang -.       .- ang -.
        |/ b  + c  + d  =   / (x  + y  + z ) sin | ----- | = sin | ----- | .
                          |/                     '-  2  -'       '-  2  -'

    Since a = cos(ang/2), with the above value, we can calculate the angle by ::

                            .-   .-----------    -.
                            |   / 2    2    2     |
        ang = 2 sgn arctan2 | |/ b  + c  + d  , a | ,
                            '-                   -'

    where `sgn` is the sign of the angle based on whether the dot product of the
    vector [b, c, d] with [1, 1, 1] is positive::

       sgn = sign( b + c + d ) .

    Finally, the rotation axis vector is calculated by using the first set of
    equations above::

                 b                    c                    d
       x = -------------    y = -------------    z = ------------- .
               .- ang -.            .- ang -.            .- ang -.
           sin | ----- |        sin | ----- |        sin | ----- |
               '-  2  -'            '-  2  -'            '-  2  -'

    It is true that `ang` and, therefore `sin(ang/2)`, could become 0, which
    would create a singularity.  But, this will happen only if the norm of
    `[b, c, d]` is zero.  In other words, if the quaternion is just a scalar
    value, then we will have a problem.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    .. [2]  Soheil Sarabandi and Federico Thomas, "A Survey on the Computation
            of Quaternions from Rotation Matrices," Journal of Mechanisms and
            Robotics, 2018.
    """

    # Check inputs.
    C = check_dcm(C)

    # Parse and reshape the elements of Dcm.
    if C.ndim == 2:
        c11 = C[0, 0]
        c12 = C[0, 1]
        c13 = C[0, 2]
        c21 = C[1, 0]
        c22 = C[1, 1]
        c23 = C[1, 2]
        c31 = C[2, 0]
        c32 = C[2, 1]
        c33 = C[2, 2]
    else:
        c11 = C[:, 0, 0]
        c12 = C[:, 0, 1]
        c13 = C[:, 0, 2]
        c21 = C[:, 1, 0]
        c22 = C[:, 1, 1]
        c23 = C[:, 1, 2]
        c31 = C[:, 2, 0]
        c32 = C[:, 2, 1]
        c33 = C[:, 2, 2]

    # Get the squared sums and differences of off-diagonal pairs.
    p12 = (c12 + c21)**2
    p23 = (c23 + c32)**2
    p31 = (c31 + c13)**2
    m12 = (c12 - c21)**2
    m23 = (c23 - c32)**2
    m31 = (c31 - c13)**2

    # Get squared expressions of diagonal values.
    d1 = (c11 + c22 + c33 + 1)**2
    d2 = (c11 - c22 - c33 + 1)**2
    d3 = (c22 - c11 - c33 + 1)**2
    d4 = (c33 - c11 - c22 + 1)**2

    # Build the quaternion.
    a = 0.25*np.sqrt(d1 + m23 + m31 + m12)
    b = 0.25*np.sign(c23 - c32)*np.sqrt(m23 + d2 + p12 + p31)
    c = 0.25*np.sign(c31 - c13)*np.sqrt(m31 + p12 + d3 + p23)
    d = 0.25*np.sign(c12 - c21)*np.sqrt(m12 + p31 + p23 + d4)

    # Get the norm and sign of the last three elements of the quaternion.
    nm = np.sqrt(b**2 + c**2 + d**2)
    sgn = np.sign(b + c + d)

    # Get the angle of rotation.
    ang = 2*sgn*np.arctan2(nm, a)

    # Build the rotation axis vector.
    x = b/np.sin(ang/2)
    y = c/np.sin(ang/2)
    z = d/np.sin(ang/2)
    if C.ndim == 2:
        ax = np.array([x, y, z])
    else:
        ax = np.row_stack((x, y, z))

    return ax, ang


def axis_angle_to_dcm(ax, ang, degs=None):
    """
    Create a direction cosine matrix (DCM) (also known as a rotation matrix) to
    rotate from one frame to another given a rotation `ax` vector and a
    right-handed `ang` of rotation.

    Parameters
    ----------
    ax : np.ndarray
        Vector of the rotation axis with three values.
    ang : float
        Rotation ang in radians.

    Returns
    -------
    C : 2D np.ndarray
        3x3 rotation matrix.

    See Also
    --------
    dcm_to_axis_anlge
    """

    # Check the inputs.
    ax, ang = check_axang(ax, ang)

    # Scale the angle.
    if degs is None:
        degs = False
    if degs:
        ang *= np.pi/180

    if ax.ndim == 1:
        # Normalize and parse the rotation axis vector.
        nm = np.linalg.norm(ax)
        ang *= nm
        x = ax[0]/nm
        y = ax[1]/nm
        z = ax[2]/nm

        # Get the cosine and sine of the ang.
        co = np.cos(ang)
        si = np.sin(ang)
        cc = 1 - co

        # Build the direction cosine matrix.
        C = np.array([
            [co + (x**2)*cc,  x*y*cc + z*si,  x*z*cc - y*si],
            [x*y*cc - z*si,  co + (y**2)*cc,  y*z*cc + x*si],
            [x*z*cc + y*si,   y*z*cc - x*si, co + (z**2)*cc]])
    else:
        # Normalize and parse the rotation axis vector.
        nm = np.linalg.norm(ax, axis=0)
        ang *= nm
        x = ax[0, :]/nm
        y = ax[1, :]/nm
        z = ax[2, :]/nm

        # Get the cosine and sine of the ang.
        co = np.cos(ang)
        si = np.sin(ang)
        cc = 1 - co

        # Build the direction cosine matrix.
        C = np.zeros((len(x), 3, 3))
        C[:, 0, 0] = co + (x**2)*cc
        C[:, 0, 1] = x*y*cc + z*si
        C[:, 0, 2] = x*z*cc - y*si
        C[:, 1, 0] = x*y*cc - z*si
        C[:, 1, 1] = co + (y**2)*cc
        C[:, 1, 2] = y*z*cc + x*si
        C[:, 2, 0] = x*z*cc + y*si
        C[:, 2, 1] = y*z*cc - x*si
        C[:, 2, 2] = co + (z**2)*cc

    return C


def quat_to_axis_angle(q):
    """
    Convert a quaternion to a rotation axis vector and angle.  This follows the
    Hamilton convention.

    Parameters
    ----------
    q : (4,) or (4, M) np.ndarray
        Array of quaternion elements or matrix of M arrays of quaternion
        elements as the columns.  The elements are a, b, c, and d where the
        quaterion `q` is a + b i + c j + d k.

    Returns
    -------
    ax : (N,) or (N, M) np.ndarray
        Rotation axis vector or matrix of M rotation axis vectors as the
        columns.
    ang : float or (M,) np.ndarray
        Rotation angle or array of M rotation angles.  This is a positive value.

    See Also
    --------
    axis_angle_to_quat

    Notes
    -----
    The quaternion, `q`, is defined in terms of the unit axis vector, `ax`, and
    angle, `ang`:

        ax = [x, y, z]'                     a =   cos( ang/2 )
        q = a + b i + c j + d k             b = x sin( ang/2 )
                                            c = y sin( ang/2 )
                                            d = z sin( ang/2 ) .

    The norm of [b, c, d]' would be ::

           .-----------       .---------------------------
          / 2    2    2      /  2    2    2     2
        |/ b  + c  + d  =  |/ (x  + y  + z ) sin ( ang/2 ) = sin( ang/2 ) ,

    where [x, y, z]' is a unit vector by design.  Since a = cos(ang/2), with the
    above value we can calculate the angle by ::

                            .-   .-----------   -.
                            |   / 2    2    2    |
        ang = 2 sgn arctan2 | |/ b  + c  + d , a | ,
                            '-                  -'

    where sgn is the sign of the angle based on whether the dot product of the
    vector [b, c, d]' with [1, 1, 1]' is positive:

        sgn = sign( b + c + d ) .

    Finally, the rotation axis vector is calculated by using the first set of
    equations above:

                  b                     c                     d
        x = -------------     y = -------------     z = ------------- .
                .- ang -.             .- ang -.             .- ang -.
            sin | ----- |         sin | ----- |         sin | ----- |
                '-  2  -'             '-  2  -'             '-  2  -'

    It is true that ang and, therefore sin(ang/2), could become 0, which would
    create a singularity.  But, this would happen only if the norm of [b, c, d]'
    is zero.  In other words, if the quaternion is just a scalar value, then we
    will have a problem.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    """

    # Check the inputs.
    q = check_quat(q)

    # Build the quaternion.
    if q.ndim == 1:
        sgn = np.sign(np.sum(q[1:]))
        nm = np.linalg.norm(q[1:])
        ang = 2*sgn*np.arctan2(nm, q[0])
        ax = q[1:]/np.sin(ang/2)
    else:
        sgn = np.sign(np.sum(q[1:, :], axis=0))
        nm = np.linalg.norm(q[1:, :], axis=0)
        ang = 2*sgn*np.arctan2(nm, q[0, :])
        ax = q[1:, :]/np.sin(ang/2)

    return ax, ang


def axis_angle_to_quat(ax, ang, degs=None):
    """
    Convert rotation axis vector and angle to a quaternion.  This follows the
    Hamilton convention.

    Parameters
    ----------
    ax : (N,) or (N, M) np.ndarray
        Rotation axis vector or matrix of M rotation axis vectors as the
        columns.
    ang : float or (M,) np.ndarray
        Rotation angle or array of M rotation angles.  This is a positive value.

    Returns
    -------
    q : (4,) or (4, M) np.ndarray
        Array of quaternion elements or matrix of M arrays of quaternion
        elements as the columns.  The elements are a, b, c, and d where the
        quaterion `q` is a + b i + c j + d k.

    See Also
    --------
    quat_to_axis_angle

    Notes
    -----
    The quaternion, `q`, is defined in terms of the unit axis vector, `ax`,
    and angle, `ang`:

        ax = [x, y, z]'                     a =   cos( ang/2 )
        q = a + b i + c j + d k             b = x sin( ang/2 )
                                            c = y sin( ang/2 )
                                            d = z sin( ang/2 ) .

    The `ax` input is first normalized.  The norm is not thrown away, but rather
    multiplied into the `ang` value.  This overcomes the limitation of assuming
    the axis vector is a unit vector.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    """

    # Check the inputs.
    ax, ang = check_axang(ax, ang)

    # Scale the angle.
    if degs is None:
        degs = False
    if degs:
        ang *= np.pi/180

    # Normalize the vector rotation axis.
    if ax.ndim == 1:
        ax_norm = np.linalg.norm(ax)
    else:
        ax_norm = np.linalg.norm(ax, axis=0)
    ax /= ax_norm
    ang *= ax_norm

    # Build the quaternion.
    if ax.ndim == 1:
        si = np.sin(ang/2)
        q = np.array([np.cos(ang/2), ax[0]*si, ax[1]*si, ax[2]*si])
    else:
        a = np.cos(ang/2)
        si = np.sin(ang/2)
        b = ax[0, :]*si
        c = ax[1, :]*si
        d = ax[2, :]*si
        q = np.row_stack((a, b, c, d))

    return q


def dcm_to_rpy(C):
    """
    Convert the direction cosine matrix, `C`, to vectors of `roll`, `pitch`,
    and `yaw` (in that order) Euler angles.

    This `C` represents the z, y, x sequence of right-handed rotations.  For
    example, if the DCM converted vectors from the navigation frame to the body
    frame, the roll, pitch, and yaw Euler angles would be the consecutive angles
    by which the vector would be rotated from the navigation frame to the body
    frame.  This is as opposed to the Euler angles required to rotate the vector
    from the body frame back to the navigation frame.

    Parameters
    ----------
    C : (3, 3) or (M, 3, 3) np.ndarray
        Rotation direction cosine matrix or stack of M such matrices.

    Returns
    -------
    r : float or (M,) np.ndarray
        Roll Euler angle in radians.
    p : float or (M,) np.ndarray
        Pitch Euler angle in radians.
    y : float or (M,) np.ndarray
        Yaw Euler angle in radians.

    See Also
    --------
    rpy_to_dcm

    Notes
    -----
    If we define `C` as ::

            .-             -.
            |  c11 c12 c13  |
        C = |  c21 c22 c23  |
            |  c31 c32 c33  |
            '-             -'
            .-                                                 -.
            |       (cy cp)             (sy cp)          -sp    |
          = |  (cy sp sr - sy cr)  (sy sp sr + cy cr)  (cp sr)  |
            |  (sy sr + cy sp sr)  (sy sp cr - cy sr)  (cp cr)  |
            '-                                                 -'

    where `c` and `s` mean cosine and sine, respectively, and `r`, `p`, and `y`
    mean roll, pitch, and yaw, respectively, then we can see that ::

                                        .-       -.
                                        |  cp sr  |
        r = arctan2(c23, c33) => arctan | ------- |
                                        |  cp cr  |
                                        '-       -'
                                        .-       -.
                                        |  sy cp  |
        y = arctan2(c12, c11) => arctan | ------- |
                                        |  cy cp  |
                                        '-       -'

    where the cp values cancel in both cases.  The value for pitch could be
    found from c13 alone:

        p = arcsin(-c13)

    However, this tends to suffer from numerical error around +- pi/2.  So,
    instead, we will use the fact that ::

          2     2               2     2
        cy  + sy  = 1   and   cr  + sr  = 1 .

    Therefore, we can use the fact that ::

           .------------------------
          /   2      2      2      2     .--
        |/ c11  + c12  + c23  + c33  = |/ 2  cos( |p| )

    to solve for pitch.  We can use the negative of the sign of c13 to give the
    proper sign to pitch.  The advantage is that in using more values from the
    DCM matrix, we can can get a value which is more accurate.  This works well
    until we get close to a pitch value of zero.  Then, the simple formula for
    pitch is actually better.  So, we will use both and do a weighted average of
    the two, based on pitch.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    """

    # Check inputs.
    C = check_dcm(C)

    if C.ndim == 2:
        c11 = C[0, 0]
        c33 = C[2, 2]
        c12 = C[0, 1]
        c13 = C[0, 2]
        c23 = C[1, 2]
    else:
        c11 = C[:, 0, 0]
        c33 = C[:, 2, 2]
        c12 = C[:, 0, 1]
        c13 = C[:, 0, 2]
        c23 = C[:, 1, 2]

    # Get roll and yaw.
    r = np.arctan2(c23, c33)
    y = np.arctan2(c12, c11)

    # Get pitch.
    sp = -c13
    pa = np.arcsin(sp)
    nm = np.sqrt(c11**2 + c12**2 + c23**2 + c33**2)
    pb = np.arccos(nm/np.sqrt(2))
    p = (1.0 - np.abs(sp))*pa + sp*pb

    return r, p, y


def rpy_to_dcm(r, p, y, degs=None):
    """
    Convert roll, pitch, and yaw Euler angles to a direction cosine matrix that
    represents a zyx sequence of right-handed rotations.

    Parameters
    ----------
    r : float or (M,) np.ndarray
        Roll Euler angle in radians.
    p : float or (M,) np.ndarray
        Pitch Euler angle in radians.
    y : float or (M,) np.ndarray
        Yaw Euler angle in radians.

    Returns
    -------
    C : (3, 3) or (M, 3, 3) np.ndarray
        Rotation matrix or stack of M rotation matrices.

    See Also
    --------
    dcm_to_rpy
    rot

    Notes
    -----
    This is equivalent to generating a rotation matrix for the rotation from the
    navigation frame to the body frame.  However, if you want to rotate from the
    body frame to the navigation frame (an xyz sequence of right-handed
    rotations), transpose the result of this function.  This is a convenience
    function.  You could instead use the `rot` function as follows::

        C = rot([yaw, pitch, roll], [2, 1, 0])

    However, the `rpy_to_dcm` function will compute faster than the `rot`
    function.
    """

    # Check inputs.
    r, p, y = check_rpy(r, p, y, degs)

    # Scale the angle.
    if degs is None:
        degs = False
    if degs:
        r *= np.pi/180
        y *= np.pi/180
        p *= np.pi/180

    # Get the cosine and sine functions.
    cr = np.cos(r)
    sr = np.sin(r)
    cp = np.cos(p)
    sp = np.sin(p)
    cy = np.cos(y)
    sy = np.sin(y)

    if isinstance(r, np.ndarray):
        # Build the stack of M 3x3 matrices.
        C = np.zeros((len(r), 3, 3))
        C[:, 0, 0] = cp*cy
        C[:, 0, 1] = cp*sy
        C[:, 0, 2] = -sp
        C[:, 1, 0] = -cr*sy + sr*sp*cy
        C[:, 1, 1] = cr*cy + sr*sp*sy
        C[:, 1, 2] = sr*cp
        C[:, 2, 0] = sr*sy + cr*sp*cy
        C[:, 2, 1] = -sr*cy + cr*sp*sy
        C[:, 2, 2] = cr*cp
    else:
        # Build the 3x3 matrix.
        C = np.array([
            [            cp*cy,             cp*sy,   -sp],
            [-cr*sy + sr*sp*cy,  cr*cy + sr*sp*sy, sr*cp],
            [ sr*sy + cr*sp*cy, -sr*cy + cr*sp*sy, cr*cp]])

    return C


def rot(ang, ax=None, degs=None):
    """
    Build a three-dimensional rotation matrix from the rotation angles `ang`
    about the successive axes `ax`.

    Parameters
    ----------
    ang : float or int or np.ndarray
        Angle of rotation in radians (or degrees if `degs` is True).
    ax : {0, 1, 2}, float or int or np.ndarray, default 2
        Axis index about which to rotate.  The x axis is 0, the y axis is 1, and
        the z axis is 2.
    degs : bool, default False
        A flag denoting whether the values of `ang` are in degrees.

    Returns
    -------
    C : 2D np.ndarray
        3x3 rotation matrix

    See Also
    --------
    rpy_to_dcm
    """

    # Control the input types.
    if ax is None:
        ax = np.array([2])
    if isinstance(ax, (float, int)):
        ax = np.array([int(ax)])
    elif isinstance(ax, list):
        ax = np.array(ax, dtype=int)
    elif isinstance(ax, np.ndarray) and ax.dtype is not int:
        ax = ax.astype(int)
    if isinstance(ang, (float, int)):
        ang = np.array([float(ang)])
    elif isinstance(ang, list):
        ang = np.array(ang, dtype=float)

    # Check the inputs.
    if ang.ndim != 1 or ax.ndim != 1:
        raise TypeError("Inputs ang and ax must be 1D arrays.")
    if len(ang) != len(ax):
        raise ValueError("Inputs ang and ax must be the same length.")
    if (ax > 2).any() or (ax < 0).any():
        raise ValueError("Input ax must be 0, 1, or 2.")

    # Scale the angle.
    if degs is None:
        degs = False
    if degs:
        ang *= np.pi/180

    # Build the rotation matrix.
    C = np.eye(3)
    for n in range(len(ang)):
        # Skip trivial rotations.
        if ang[n] == 0:
            continue

        # Get the cosine and sine of ang.
        co = np.cos(ang[n])
        si = np.sin(ang[n])

        # Get new rotation matrix.
        if ax[n] == 0:
            C_n = np.array([[1, 0, 0], [0, co, si], [0, -si, co]])
        elif ax[n] == 1:
            C_n = np.array([[co, 0, -si], [0, 1, 0], [si, 0, co]])
        elif ax[n] == 2:
            C_n = np.array([[co, si, 0], [-si, co, 0], [0, 0, 1]])

        # Pre-multiply the old rotation matrix by the new.
        if n == 0:
            C = C_n + 0
        else:
            C = C_n @ C

    return C


def quat_to_rpy(q):
    """
    Convert from a quaternion right-handed frame rotation to a roll, pitch, and
    yaw, z, y, x sequence of right-handed frame rotations.  If frame 1 is
    rotated in a z, y, x sequence to become frame 2, then the quaternion `q`
    would also rotate a vector in frame 1 into frame 2.

    Parameters
    ----------
    q : (4,) np.ndarray or (4, N) np.ndarray
        A quaternion vector or a matrix of such vectors.

    Returns
    -------
    r : float or (N,) np.ndarray
        Roll angles in radians.
    p : float or (N,) np.ndarray
        Pitch angles in radians.
    y : float or (N,) np.ndarray
        Yaw angles in radians.

    See Also
    --------
    rpy_to_quat

    Notes
    -----
    An example use case is the calculation a yaw-roll-pitch (z, y, x) frame
    rotation when given the quaternion that rotates from the [nose, right wing,
    down] body frame to the [north, east, down] navigation frame.

    From the dcm_to_rpy function, we know that the roll, `r`, pitch, `p`, and
    yaw, `y`, can be calculated as follows::

        r = arctan2(c23, c33)
        p = -arcsin(c13)
        y = arctan2(c12, c11)

    where the `d` variables are elements of the DCM.  We also know from the
    quat_to_dcm function that ::

              .-                                                            -.
              |   2    2    2    2                                           |
              | (a  + b  - c  - d )    2 (b c + a d)       2 (b d - a c)     |
              |                                                              |
              |                       2    2    2    2                       |
        Dcm = |    2 (b c - a d)    (a  - b  + c  - d )    2 (c d + a b)     |
              |                                                              |
              |                                           2    2    2    2   |
              |    2 (b d + a c)       2 (c d - a b)    (a  - b  - c  + d )  |
              '-                                                            -'

    This means that the `d` variables can be defined in terms of the quaternion
    elements::

               2    2    2    2
        c11 = a  + b  - c  - d           c12 = 2 (b c + a d)

                                         c13 = 2 (b d - a c)
               2    2    2    2
        c33 = a  - b  - c  + d           c23 = 2 (c d + a b)

    This function does not take advantage of the more advanced formula for pitch
    because testing showed it did not help in this case.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    """

    # Check the inputs.
    q = check_quat(q)

    # Depending on the dimensions of the input,
    if q.ndim == 1:
        # Get the required elements of the DCM.
        c11 = q[0]**2 + q[1]**2 - q[2]**2 - q[3]**2
        c12 = 2*(q[1]*q[2] + q[0]*q[3])
        c13 = 2*(q[1]*q[3] - q[0]*q[2])
        c23 = 2*(q[2]*q[3] + q[0]*q[1])
        c33 = q[0]**2 - q[1]**2 - q[2]**2 + q[3]**2
    else:
        # Get the required elements of the DCM.
        c11 = q[0, :]**2 + q[1, :]**2 - q[2, :]**2 - q[3, :]**2
        c12 = 2*(q[1, :]*q[2, :] + q[0, :]*q[3, :])
        c13 = 2*(q[1, :]*q[3, :] - q[0, :]*q[2, :])
        c23 = 2*(q[2, :]*q[3, :] + q[0, :]*q[1, :])
        c33 = q[0, :]**2 - q[1, :]**2 - q[2, :]**2 + q[3, :]**2

    # Build the output.
    r = np.arctan2(c23, c33)
    p = -np.arcsin(c13)
    y = np.arctan2(c12, c11)

    return r, p, y


def rpy_to_quat(r, p, y, degs=None):
    """
    Convert roll, pitch, and yaw Euler angles to a quaternion, `q`.

    Parameters
    ----------
    r : float or (M,) np.ndarray
        Roll Euler angle in radians.
    p : float or (M,) np.ndarray
        Pitch Euler angle in radians.
    y : float or (M,) np.ndarray
        Yaw Euler angle in radians.

    Returns
    -------
    q : (4,) or (4, M) np.ndarray
        Array of quaternion elements or matrix of M arrays of quaternion
        elements as the columns.  The elements are a, b, c, and d where the
        quaterion `q` is a + b i + c j + d k.

    See Also
    --------
    quat_to_rpy

    Notes
    -----
    The equations to calculate the quaternion are ::

        h = cr cp cy + sr sp sy
        a = abs(h)
        b = sgn(h) (sr cp cy - cr sp sy)
        c = sgn(h) (cr sp cy + sr cp sy)
        d = sgn(h) (cr cp sy - sr sp cy)
        q = a + b i + c j + d k

    where `q` is the quaternion, the `c` and `s` prefixes represent cosine and
    sine, respectively, the `r`, `p`, and `y` suffixes represent roll, pitch,
    and yaw, respectively, and `sgn` is the sign function.  The sign of `h` is
    used to make sure that the first element of the quaternion is always
    positive.  This is simply a matter of convention.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    """

    # Check inputs.
    r, p, y = check_rpy(r, p, y, degs)

    # Scale the angle.
    if degs is None:
        degs = False
    if degs:
        r *= np.pi/180
        y *= np.pi/180
        p *= np.pi/180

    # Get the cosine and sine functions.
    cr = np.cos(r/2)
    sr = np.sin(r/2)
    cp = np.cos(p/2)
    sp = np.sin(p/2)
    cy = np.cos(y/2)
    sy = np.sin(y/2)

    if isinstance(r, float):
        # Build the quaternion vector.
        h = cr*cp*cy + sr*sp*sy
        sgn = np.sign(h)
        q = np.array([sgn*h,
            sgn*(sr*cp*cy - cr*sp*sy),
            sgn*(cr*sp*cy + sr*cp*sy),
            sgn*(cr*cp*sy - sr*sp*cy)])
    else:
        # Build the matrix of quaternion vectors.
        h = cr*cp*cy + sr*sp*sy
        sgn = np.sign(h)
        a = sgn*h
        b = sgn*(sr*cp*cy - cr*sp*sy)
        c = sgn*(cr*sp*cy + sr*cp*sy)
        d = sgn*(cr*cp*sy - sr*sp*cy)
        q = np.row_stack((a, b, c, d))

    return q


def quat_to_dcm(q):
    """
    Convert from a quaternion, `q`, that performs a right-handed frame rotation
    from frame 1 to frame 2 to a direction cosine matrix, `C`, that also
    performs a right-handed frame rotation from frame 1 to frame 2.  The `C`
    represents a z, y, x sequence of right-handed rotations.

    Parameters
    ----------
    q : 4-element 1D np.ndarray
        The 4-element quaternion vector corresponding to the DCM.

    Returns
    -------
    C : float 3x3 np.ndarray
        3-by-3 rotation direction cosine matrix.

    See Also
    --------
    dcm_to_quat

    Notes
    -----
    An example use case is to calculate a direction cosine matrix that rotates
    from the [nose, right wing, down] body frame to the [north, east, down]
    navigation frame when given a quaternion frame rotation that rotates from
    the [nose, right wing, down] body frame to the [north, east, down]
    navigation frame.

    The DCM can be defined in terms of the elements of the quaternion
    [a, b, c, d] as ::

            .-                                                            -.
            |   2    2    2    2                                           |
            | (a  + b  - c  - d )    2 (b c + a d)       2 (b d - a c)     |
            |                                                              |
            |                       2    2    2    2                       |
        C = |    2 (b c - a d)    (a  - b  + c  - d )    2 (c d + a b)     |
            |                                                              |
            |                                           2    2    2    2   |
            |    2 (b d + a c)       2 (c d - a b)    (a  - b  - c  + d )  |
            '-                                                            -'

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    """

    # Check the inputs.
    q = check_quat(q)

    if q.ndim == 1:
        # Square the elements of the quaternion.
        a2 = q[0]**2
        b2 = q[1]**2
        c2 = q[2]**2
        d2 = q[3]**2

        # Build the DCM.
        C = np.array([
            [a2 + b2 - c2 - d2,
                2*(q[1]*q[2] + q[0]*q[3]),
                2*(q[1]*q[3] - q[0]*q[2])],
            [2*(q[1]*q[2] - q[0]*q[3]),
                a2 - b2 + c2 - d2,
                2*(q[2]*q[3] + q[0]*q[1])],
            [2*(q[1]*q[3] + q[0]*q[2]),
                2*(q[2]*q[3] - q[0]*q[1]),
                a2 - b2 - c2 + d2]])
    else:
        # Square the elements of the quaternion.
        a2 = q[0, :]**2
        b2 = q[1, :]**2
        c2 = q[2, :]**2
        d2 = q[3, :]**2

        # Build the DCM.
        C = np.zeros((len(a2), 3, 3))
        C[:, 0, 0] = a2 + b2 - c2 - d2
        C[:, 0, 1] = 2*(q[1]*q[2] + q[0]*q[3])
        C[:, 0, 2] = 2*(q[1]*q[3] - q[0]*q[2])
        C[:, 1, 0] = 2*(q[1]*q[2] - q[0]*q[3])
        C[:, 1, 1] = a2 - b2 + c2 - d2
        C[:, 1, 2] = 2*(q[2]*q[3] + q[0]*q[1])
        C[:, 2, 0] = 2*(q[1]*q[3] + q[0]*q[2])
        C[:, 2, 1] = 2*(q[2]*q[3] - q[0]*q[1])
        C[:, 2, 2] = a2 - b2 - c2 + d2

    return C


def dcm_to_quat(C):
    """
    Convert a direction cosine matrix, `C`, to a quaternion vector, `q`.  Here,
    the `C` is considered to represent a z, y, x sequence of right-handed
    rotations.  This means it has the same sense as the quaternion.

    Parameters
    ----------
    C : (3, 3) np.ndarray
        Rotation direction cosine matrix.

    Returns
    -------
    q : (4,) np.ndarray
        The quaternion vector.

    See Also
    --------
    quat_to_dcm

    Notes
    -----
    The implementation here is Cayley's method for obtaining the quaternion.  It
    is used because of its superior numerical accuracy.  This comes from the
    fact that it uses all nine of the elements of the DCM matrix.  It also does
    not suffer from numerical instability due to division as some other methods
    do.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    .. [2]  Soheil Sarabandi and Federico Thomas, "A Survey on the Computation
            of Quaternions from Rotation Matrices," Journal of Mechanisms and
            Robotics, 2018.
    """

    # Check inputs.
    C = check_dcm(C)

    # Parse the elements of C.
    if C.ndim == 2:
        c11 = C[0, 0]
        c12 = C[0, 1]
        c13 = C[0, 2]
        c21 = C[1, 0]
        c22 = C[1, 1]
        c23 = C[1, 2]
        c31 = C[2, 0]
        c32 = C[2, 1]
        c33 = C[2, 2]
    else:
        c11 = C[:, 0, 0]
        c12 = C[:, 0, 1]
        c13 = C[:, 0, 2]
        c21 = C[:, 1, 0]
        c22 = C[:, 1, 1]
        c23 = C[:, 1, 2]
        c31 = C[:, 2, 0]
        c32 = C[:, 2, 1]
        c33 = C[:, 2, 2]

    # Get the squared sums and differences of off-diagonal pairs.
    p12 = (c12 + c21)**2
    p23 = (c23 + c32)**2
    p31 = (c31 + c13)**2
    m12 = (c12 - c21)**2
    m23 = (c23 - c32)**2
    m31 = (c31 - c13)**2

    # Get squared expressions of diagonal values.
    d1 = (c11 + c22 + c33 + 1)**2
    d2 = (c11 - c22 - c33 + 1)**2
    d3 = (c22 - c11 - c33 + 1)**2
    d4 = (c33 - c11 - c22 + 1)**2

    # Get the components.
    a = 0.25*np.sqrt(d1 + m23 + m31 + m12)
    b = 0.25*np.sign(c23 - c32)*np.sqrt(m23 + d2 + p12 + p31)
    c = 0.25*np.sign(c31 - c13)*np.sqrt(m31 + p12 + d3 + p23)
    d = 0.25*np.sign(c12 - c21)*np.sqrt(m12 + p31 + p23 + d4)

    # Build the quaternion.
    if C.ndim == 2:
        q = np.array([a, b, c, d])
    else:
        q = np.row_stack((a, b, c, d))

    return q

# ---------------------------
# Reference-frame Conversions
# ---------------------------

def geodetic_to_ecef(lat, lon, hae, degs=None):
    """
    Convert position in geodetic coordinates to ECEF (Earth-centered,
    Earth-fixed) coordinates.  This method is direct and not an approximation.
    This follows the WGS-84 definitions (see WGS-84 Reference System (DMA report
    TR 8350.2)).

    Parameters
    ----------
    lat : float or np.ndarray
        Geodetic latitude in radians (or degrees if `degs` is True).
    lon : float or np.ndarray
        Geodetic longitude in radians (or degrees if `degs` is True).
    hae : float or np.ndarray
        Height above ellipsoid in meters.

    Returns
    -------
    xyz : (3,) or (3, M) np.ndarray
        ECEF x, y, and z-axis position vector in meters or matrix of M such
        vectors as columns.

    See Also
    --------
    ecef_to_geodetic

    Notes
    -----
    The distance from the z axis is ::

             .-  aE       -.
        pe = |  ---- + hae | cos(lat)
             '- kphi      -'

    where `aE` is the semi-major radius of the earth and ::

                  .---------------
                 /      2   2
        kphi = |/ 1 - eE sin (lat)

    The `eE` value is the eccentricity of the earth.  Knowing the distance from
    the z axis, we can get the x and y coordinates::

        xe = pe cos(lon)       ye = pe sin(lon) .

    The z-axis coordinate is ::

             .-  aE         2        -.
        ze = |  ---- (1 - eE ) + hae  | sin(lat) .
             '- kphi                 -'

    Several of these equations are admittedly not intuitively obvious.  The
    interested reader should refer to external texts for insight.

    References
    ----------
    .. [1]  WGS-84 Reference System (DMA report TR 8350.2)
    .. [2]  Inertial Navigation: Theory and Implementation by David Woodburn
    """

    # Check inputs.
    lat, lon, hae = check_llh(lat, lon, hae, degs)

    # Scale the angles.
    if degs is None:
        degs = False
    if degs:
        lat *= np.pi/180
        lon *= np.pi/180

    # Get the intermediate values.
    kphi = np.sqrt(1 - E2*np.sin(lat)**2)
    Rm = (A_E/kphi**3)*(1 - E2)
    Rt = A_E/kphi

    # Get the x, y, and z coordinates.
    pe = (Rt + hae)*np.cos(lat)
    xe = pe*np.cos(lon)
    ye = pe*np.sin(lon)
    ze = (Rm*kphi**2 + hae)*np.sin(lat)

    if isinstance(lat, float):
        xyz = np.array([xe, ye, ze])
    else:
        xyz = np.row_stack((xe, ye, ze))

    return xyz


def ecef_to_geodetic(xyz):
    """
    Convert an ECEF (Earth-centered, Earth-fixed) position to geodetic
    coordinates.  This follows the WGS-84 definitions (see WGS-84 Reference
    System (DMA report TR 8350.2)).

    Parameters
    ----------
    xyz : (3,) or (3, M) np.ndarray
        ECEF x, y, and z-axis position vector in meters or matrix of M such
        vectors as columns.

    Returns
    -------
    lat : float or (M,) np.ndarray
        Geodetic latitude in radians.
    lon : float or (M,) np.ndarray
        Geodetic longitude in radians.
    hae : float or (M,) np.ndarray
        Height above ellipsoid in meters.

    See Also
    --------
    geodetic_to_ecef

    Notes
    -----
    Note that inherent in solving the problem of getting the geodetic latitude
    and ellipsoidal height is finding the roots of a quartic polynomial because
    we are looking for the intersection of a line with an ellipse.  While there
    are closed-form solutions to this problem (see Wikipedia), each point has
    potentially four solutions and the solutions are not numerically stable.
    Instead, this function uses the Newton-Raphson method to iteratively solve
    for the geodetic coordinates.

    First, we want to approximate the values for geodetic latitude, `lat`, and
    height above ellipsoid, `hae`, given the (xe, ye, ze) position in the ECEF
    frame::

                                .--------
         ^                     /  2     2            ^
        hae = 0         pe = |/ xe  + ye            lat = arctan2(ze, pe),

    where `pe` is the distance from the z axis of the ECEF frame.  (While there
    are better approximations for `hae` than zero, the improvement in accuracy
    was not enough to reduce the number of iterations and the additional
    computational burden could not be justified.)  Then, we will iteratively use
    this approximation for `lat` and `hae` to calculate what `pe` and `ze` would
    be, get the residuals given the correct `pe` and `ze` values in the ECEF
    frame, use the inverse Jacobian to calculate the corresponding residuals of
    `lat` and `hae`, and update our approximations for `lat` and `hae` with
    those residuals.  In testing millions of randomly generated points, three
    iterations was sufficient to reach the limit of numerical precision for
    64-bit floating-point numbers.

    So, first, let us define the transverse, `Rt`, and meridional, `Rm`, radii
    and the cosine and sine of the latitude::

                                                              .---------------
              aE               aE  .-       2 -.             /      2   2  ^
        Rt = ----       Rm = ----- |  1 - eE   |    kphi = |/ 1 - eE sin (lat) ,
             kphi                3 '-         -'
                             kphi
                  ^                               ^
        co = cos(lat)                   si = sin(lat)

    where `eE` is the eccentricity of the Earth, and `aE` is the semi-major
    radius of the Earth.  The ECEF-frame `pe` and `ze` values given the
    approximations to geodetic latitude and height above ellipsoid are ::

         ^             ^                 ^              2   ^
        pe = co (Rt + hae)              ze = si (Rm kphi + hae) .

    We already know the correct values for `pe` and `ze`, so we can get
    residuals::

         ~         ^                     ~         ^
        pe = pe - pe                    ze = ze - ze .

    We can relate the `pe` and `ze` residuals to the `lat` and `hae` residuals
    by using the inverse Jacobian matrix::

        .-  ~  -.       .-  ~ -.
        |  lat  |    -1 |  pe  |
        |       | = J   |      | .
        |   ~   |       |   ~  |
        '- hae -'       '- ze -'

    With a bit of algebra, we can combine and simplify the calculation of the
    Jacobian with the calculation of the `lat` and `hae` residuals::
        
         ~         ~       ~              ~         ~       ~         ^
        hae = (si ze + co pe)            lat = (co ze - si pe)/(Rm + hae) .

    Conceptually, this is the backwards rotation of the (`pe`, `ze`) residuals
    vector by the angle `lat`, where the resulting y component of the rotated
    vector is treated as an arc length and converted to an angle, `lat`, using
    the radius `Rm` + `hae`.  With the residuals for `lat` and `hae`, we can
    update our approximations for `lat` and `hae`::

         ^     ^     ~                   ^     ^     ~
        hae = hae + hae                 lat = lat + lat             

    and iterate again.  Finally, the longitude, `lon`, is exactly the arctangent
    of the ECEF `xe` and `ye` values::

        lon = arctan2(ye, xe) .

    References
    ----------
    .. [1]  WGS-84 Reference System (DMA report TR 8350.2)
    .. [2]  Inertial Navigation: Theory and Implementation by David Woodburn
    """

    # Check inputs.
    xyz = check_xyz(xyz)

    # Parse the inputs.
    xe = xyz[0]
    ye = xyz[1]
    ze = xyz[2]

    # Initialize the height above the ellipsoid.
    haeh = 0

    # Get the true radial distance from the z axis.
    pe = np.sqrt(xe**2 + ye**2)

    # Initialize the estimated ground latitude.
    lath = np.arctan2(ze, pe) # bound to [-pi/2, pi/2]

    # Iterate to reduce residuals of the estimated closest point on the ellipse.
    for _ in range(3):
        # Using the estimated ground latitude, get the cosine and sine.
        co = np.cos(lath)
        si = np.sin(lath)
        kphi2 = 1 - E2*si**2
        kphi = np.sqrt(kphi2)
        Rt = A_E/kphi
        Rm = A_E*(1 - E2)/(kphi*kphi2)

        # Get the estimated position in the meridional plane (the plane defined
        # by the longitude and the z axis).
        peh = co*(Rt + haeh)
        zeh = si*(Rm*kphi2 + haeh)

        # Get the residuals.
        pet = pe - peh
        zet = ze - zeh

        # Using the inverse Jacobian, get the residuals in lat and hae.
        latt = (co*zet - si*pet)/(Rm + haeh)
        haet = (si*zet + co*pet)

        # Adjust the estimated ground latitude and ellipsoidal height.
        lath = lath + latt
        haeh = haeh + haet

    # Get the longitude.
    lon = np.arctan2(ye, xe)

    return lath, lon, haeh


def ecef_to_tangent(xyze, xyze0=None, ned=None):
    """
    Convert ECEF (Earth-centered, Earth-fixed) coordinates, with a defined local
    origin, to local, tangent Cartesian North, East, Down (NED) or East, North,
    Up (ENU) coordinates.

    Parameters
    ----------
    xyze : (3,) or (3, M) np.ndarray
        ECEF x, y, and z-axis position vector in meters or matrix of M such
        vectors as columns.
    xyze0 : (3,) or (3, M) np.ndarray, default xyze[:, 0]
        ECEF x, y, and z-axis origin values in meters.
    ned : bool, default True
        Flag to use NED (True) or ENU (False) orientation.

    Returns
    -------
    xyzt : (3,) or (3, M) np.ndarray
        Local, tanget x, y, and z-axis position vector in meters or matrix of M
        such vectors as columns.

    See Also
    --------
    tangent_to_ecef

    Notes
    -----
    First, the ECEF origin is converted to geodetic coordinates.  Then, those
    coordinates are used to calculate a rotation matrix from the ECEF frame to
    the local, tangent Cartesian frame::

              .-                     -.
              |  -sp cl  -sp sl   cp  |
        Cte = |    -sl     cl      0  |      NED
              |  -cp cl  -cp sl  -sp  |
              '-                     -'

              .-                     -.
              |    -sl     cl      0  |
        Cte = |  -sp cl  -sp sl   cp  |      ENU
              |   cp cl   cp sl   sp  |
              '-                     -'

    where `sp` and `cp` are the sine and cosine of the origin latitude,
    respectively, and `sl` and `cl` are the sine and cosine of the origin
    longitude, respectively.  Then, the displacement vector of the ECEF position
    relative to the ECEF origin is rotated into the local, tangent frame::

        .-  -.       .-        -.
        | xt |       | xe - xe0 |
        | yt | = Cte | ye - ye0 | .
        | zt |       | ze - ze0 |
        '-  -'       '-        -'

    If `xe0`, `ye0`, and `ze0` are not provided (or are all zeros), the first
    values of `xe`, `ye`, and `ze` will be used as the origin.
    """

    # Check the xyze input.
    xyze = check_xyz(xyze)

    # Use the first point as the origin if otherwise not provided.
    if xyze0 is None:
        if xyze.ndim == 1:
            xyze0 = xyze.copy()
        else:
            xyze0 = xyze[:, 0]
    if not isinstance(xyze0, np.ndarray):
        raise TypeError("xyze0 must be a Numpy array.")
    if xyze0.ndim != 1 or len(xyze0) != 3:
        raise TypeError("xyze0 must be a 1D array of 3 values.")

    # Default `ned` to True.
    if ned is None:
        ned = True

    # Get the local-level coordinates.
    lat0, lon0, _ = ecef_to_geodetic(xyze0)

    # Get the cosines and sines of the latitude and longitude.
    cp = np.cos(lat0)
    sp = np.sin(lat0)
    cl = np.cos(lon0)
    sl = np.sin(lon0)

    # Get the displacement ECEF vector from the origin.
    dxe = xyze[0] - xyze0[0]
    dye = xyze[1] - xyze0[1]
    dze = xyze[2] - xyze0[2]

    # Get the local, tangent coordinates.
    if ned:
        xt = -sp*cl*dxe - sp*sl*dye + cp*dze
        yt =    -sl*dxe +    cl*dye
        zt = -cp*cl*dxe - cp*sl*dye - sp*dze
    else:
        xt =    -sl*dxe +    cl*dye
        yt = -sp*cl*dxe - sp*sl*dye + cp*dze
        zt =  cp*cl*dxe + cp*sl*dye + sp*dze

    # Assemble output.
    if xyze.ndim == 1:
        xyzt = np.array([xt, yt, zt])
    else:
        xyzt = np.row_stack((xt, yt, zt))

    return xyzt


def tangent_to_ecef(xyzt, xyze0, ned=None):
    """
    Convert local, tangent Cartesian North, East, Down (NED) or East, North, Up
    (ENU) coordinates, with a defined local origin, to ECEF (Earth-centered,
    Earth-fixed) coordinates.

    Parameters
    ----------
    xyzt : (3,) or (3, M) np.ndarray
        Local, tangent x, y, and z-axis position vector in meters or matrix of M
        such vectors as columns.
    xyze0 : (3,) or (3, M) np.ndarray
        ECEF x, y, and z-axis origin values in meters.
    ned : bool, default True
        Flag to use NED or ENU orientation.

    Returns
    -------
    xyze : (3,) or (3, M) np.ndarray
        ECEF x, y, and z-axis position vector in meters or matrix of M such
        vectors as columns.

    See Also
    --------
    ecef_to_tangent

    Notes
    -----
    First, the ECEF origin is converted to geodetic coordinates.  Then, those
    coordinates are used to calculate a rotation matrix from the local, tangent
    Cartesian frame to the ECEF frame::

              .-                     -.
              |  -sp cl  -sl  -cp cl  |
        Cet = |  -sp sl   cl  -cp sl  |      NED
              |    cp      0   -sp    |
              '-                     -'

              .-                     -.
              |   -sl  -sp cl  cp cl  |
        Cet = |    cl  -sp sl  cp sl  |      ENU
              |     0    cp     sp    |
              '-                     -'

    where `sp` and `cp` are the sine and cosine of the origin latitude,
    respectively, and `sl` and `cl` are the sine and cosine of the origin
    longitude, respectively.  Then, the displacement vector of the ECEF position
    relative to the ECEF origin is rotated into the local, tangent frame::

        .-  -.       .-  -.   .-   -.
        | xe |       | xt |   | xe0 |
        | ye | = Cet | yt | + | ye0 | .
        | ze |       | zt |   | ze0 |
        '-  -'       '-  -'   '-   -'

    The scalars `xe0`, `ye0`, and `ze0` defining the origin must be given and
    cannot be inferred.
    """

    # Check inputs.
    xyzt = check_xyz(xyzt)
    if not isinstance(xyze0, np.ndarray):
        raise TypeError("xyze0 must be a Numpy array.")
    if xyze0.ndim != 1 or len(xyze0) != 3:
        raise TypeError("xyze0 must be a 1D array of 3 values.")

    # Default `ned` to True.
    if ned is None:
        ned = True

    # Parse inputs.
    xt = xyzt[0]
    yt = xyzt[1]
    zt = xyzt[2]
    xe0 = xyze0[0]
    ye0 = xyze0[1]
    ze0 = xyze0[2]

    # Get the local-level coordinates.
    lat0, lon0, _ = ecef_to_geodetic(xyze0)

    # Get the cosines and sines of the latitude and longitude.
    cp = np.cos(lat0)
    sp = np.sin(lat0)
    cl = np.cos(lon0)
    sl = np.sin(lon0)

    # Get the local, tangent coordinates.
    if ned:
        xe = -sp*cl*xt - sl*yt - cp*cl*zt + xe0
        ye = -sp*sl*xt + cl*yt - cp*sl*zt + ye0
        ze =     cp*xt         -    sp*zt + ze0
    else:
        xe = -sl*xt - sp*cl*yt + cp*cl*zt + xe0
        ye =  cl*xt - sp*sl*yt + cp*sl*zt + ye0
        ze =        +    cp*yt +    sp*zt + ze0

    # Assemble output.
    if xyzt.ndim == 1:
        xyze = np.array([xe, ye, ze])
    else:
        xyze = np.row_stack((xe, ye, ze))

    return xyze


def geodetic_to_curlin(lat, lon, hae, lat0=None, lon0=None, hae0=None,
        ned=None, degs=None):
    """
    Convert geodetic coordinates with a geodetic origin to local, curvilinear
    position in either North, East, Down (NED) or East, North, Up (ENU)
    coordinates.

    Parameters
    ----------
    lat : float or np.ndarray
        Geodetic latitude in radians.
    lon : float or np.ndarray
        Geodetic longitude in radians.
    hae : float or np.ndarray
        Height above ellipsoid in meters.
    lat0 : float, default lat[0]
        Geodetic latitude origin in radians.
    lon0 : float, default lon[0]
        Geodetic longitude origin in radians.
    hae0 : float, default hae[0]
        Heigh above ellipsoid origin in meters.
    ned : bool, default True
        Flag to use NED (True) or ENU (False) orientation.

    Returns
    -------
    xyzc : (3,) or (3, M) np.ndarray
        Local, curvilinear x, y, and z-axis position vector in meters or matrix
        of M such vectors as columns.

    See Also
    --------
    curlin_to_geodetic

    Notes
    -----
    The equations are ::

        .-  -.   .-                                -.
        | xc |   |     (Rm + hae) (lat - lat0)      |
        | yc | = | (Rt + hae) cos(lat) (lon - lon0) |       NED
        | zc |   |           (hae0 - hae)           |
        '-  -'   '-                                -'

    or ::

        .-  -.   .-                                -.
        | xc |   | (Rt + hae) cos(lat) (lon - lon0) |
        | yc | = |     (Rm + hae) (lat - lat0)      |       ENU
        | zc |   |           (hae - hae0)           |
        '-  -'   '-                                -'

    where ::

                             
                                       2                  .---------------
              aE             aE (1 - eE )                /      2   2
        Rt = ----       Rm = ------------       kphi = |/ 1 - eE sin (lat) .
             kphi                  3
                               kphi

    Here, `aE` is the semi-major axis of the Earth, `eE` is the eccentricity of
    the Earth, `Rt` is the transverse radius of curvature of the Earth, and `Rm`
    is the meridional radius of curvature of the Earth.

    If `lat0`, `lon0`, and `hae0` are not provided (are left as `None`), the
    first values of `lat`, `lon`, and `hae` will be used as the origin.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    .. [2]  https://en.wikipedia.org/wiki/Earth_radius#Meridional
    .. [3]  https://en.wikipedia.org/wiki/Earth_radius#Prime_vertical
    """

    # Check inputs.
    lat, lon, hae = check_llh(lat, lon, hae, degs)

    # Check origin latitude.
    if isinstance(lat0, int):
        lat0 = float(lat0)
    if lat0 is None:
        lat0 = lat[0]
    if not isinstance(lat0, float):
        raise TypeError("lat0 must be a float or None.")

    # Check origin longitude.
    if isinstance(lon0, int):
        lon0 = float(lon0)
    if lon0 is None:
        lon0 = lon[0]
    if not isinstance(lon0, float):
        raise TypeError("lon0 must be a float or None.")

    # Check origin height.
    if isinstance(hae0, int):
        hae0 = float(hae0)
    if hae0 is None:
        hae0 = hae[0]
    if not isinstance(hae0, float):
        raise TypeError("hae0 must be a float or None.")

    # Default ned to True.
    if ned is None:
        ned = True

    # Scale the angles.
    if degs is None:
        degs = False
    if degs:
        lat *= np.pi/180
        lon *= np.pi/180
        lat0 *= np.pi/180
        lon0 *= np.pi/180

    # Check origin latitude that's too big.
    if abs(lat0) > np.pi/2:
        raise ValueError("lat0 must not exceed pi/2.")

    # Get the parallel and meridional radii of curvature.
    kphi = np.sqrt(1 - E2*np.sin(lat)**2)
    Rt = A_E/kphi
    Rm = A_E*(1 - E2)/kphi**3

    # Get the curvilinear coordinates.
    if ned: # NED
        xc = (Rm + hae)*(lat - lat0)
        yc = (Rt + hae)*np.cos(lat)*(lon - lon0)
        zc = hae0 - hae
    else:   # ENU
        xc = (Rt + hae)*np.cos(lat)*(lon - lon0)
        yc = (Rm + hae)*(lat - lat0)
        zc = hae - hae0

    # Assemble output.
    if isinstance(lat, float):
        xyzc = np.array([xc, yc, zc])
    else:
        xyzc = np.row_stack((xc, yc, zc))

    return xyzc


def curlin_to_geodetic(xyzc, lat0, lon0, hae0, ned=None):
    """
    Convert local, curvilinear position in either North, East, Down (NED) or
    East, North, Up (ENU) coordinates to geodetic coordinates with a geodetic
    origin.  The solution is iterative, using the Newton-Raphson method.

    Parameters
    ----------
    xyzc : (3,) or (3, M) np.ndarray
        Local, curvilinear x, y, and z-axis position vector in meters or matrix
        of M such vectors as columns.
    lat0 : float
        Geodetic latitude origin in radians.
    lon0 : float
        Geodetic longitude origin in radians.
    hae0 : float
        Heigh above ellipsoid origin in meters.
    ned : bool, default True
        Flag to use NED (True) or ENU (False) orientation.

    Returns
    -------
    lat : float or np.ndarray
        Geodetic latitude in radians.
    lon : float or np.ndarray
        Geodetic longitude in radians.
    hae : float or np.ndarray
        Height above ellipsoid in meters.

    See Also
    --------
    geodetic_to_curlin

    Notes
    -----
    The equations to get curvilinear coordinates from geodetic are ::

        .-  -.   .-                                -.
        | xc |   |     (Rm + hae) (lat - lat0)      |
        | yc | = | (Rt + hae) cos(lat) (lon - lon0) |       NED
        | zc |   |           (hae0 - hae)           |
        '-  -'   '-                                -'

    or ::

        .-  -.   .-                                -.
        | xc |   | (Rt + hae) cos(lat) (lon - lon0) |
        | yc | = |     (Rm + hae) (lat - lat0)      |       ENU
        | zc |   |           (hae - hae0)           |
        '-  -'   '-                                -'

    where ::

                                       2                .---------------
              aE             aE (1 - eE )              /      2   2
        Rt = ----       Rm = ------------     kphi = |/ 1 - eE sin (lat) .
             kphi                  3
                               kphi

    Here, `aE` is the semi-major axis of the Earth, `eE` is the eccentricity of
    the Earth, `Rt` is the transverse radius of curvature of the Earth, and `Rm`
    is the meridional radius of curvature of the Earth.  Unfortunately, the
    reverse process to get geodetic coordinates from curvilinear coordinates is
    not as straightforward.  So the Newton-Raphson method is used.  Using NED as
    an example, with the above equations, we can write the differential relation
    as follows::

        .-  ~ -.     .-  ~  -.              .-           -.
        |  xc  |     |  lat  |              |  J11   J12  |
        |      | = J |       |          J = |             | ,
        |   ~  |     |   ~   |              |  J21   J22  |
        '- yc -'     '- lon -'              '-           -'

    where the elements of the Jacobian J are ::

              .-     2         -.
              |  3 eE Rm si co  |   ^
        J11 = | --------------- | (lat - lat0) + Rm + h
              |          2      |
              '-     kphi      -'

        J12 = 0

              .- .-   2  2    -.         -.
              |  |  eE co      |          |      ^
        J21 = |  | ------- - 1 | Rt - hae | si (lon - lon0)
              |  |      2      |          |
              '- '- kphi      -'         -'

        J22 = (Rt + hae) co .

    where `si` and `co` are the sine and cosine of `lat`, respectively.  Using
    the inverse Jacobian, we can get the residuals of `lat` and `lon` from the
    residuals of `xc` and `yc`::

                     ~        ~
         ~      J22 xc - J12 yc
        lat = -------------------
               J11 J22 - J21 J12

                     ~        ~
         ~      J11 yc - J21 xc
        lon = ------------------- .
               J11 J22 - J21 J12

    These residuals are added to the estimated `lat` and `lon` values and
    another iteration begins.

    References
    ----------
    .. [1]  Titterton & Weston, "Strapdown Inertial Navigation Technology"
    .. [2]  https://en.wikipedia.org/wiki/Earth_radius#Meridional
    .. [3]  https://en.wikipedia.org/wiki/Earth_radius#Prime_vertical
    """

    # Check inputs.
    xyzc = check_xyz(xyzc)

    # Check origin latitude.
    if isinstance(lat0, int):
        lat0 = float(lat0)
    if not isinstance(lat0, float):
        raise TypeError("lat0 must be a float.")

    # Check origin longitude.
    if isinstance(lon0, int):
        lon0 = float(lon0)
    if not isinstance(lon0, float):
        raise TypeError("lon0 must be a float.")

    # Check origin height.
    if isinstance(hae0, int):
        hae0 = float(hae0)
    if not isinstance(hae0, float):
        raise TypeError("hae0 must be a float.")

    # Parse inputs.
    xc = xyzc[0]
    yc = xyzc[1]
    zc = xyzc[2]

    # Flip the orientation if it is ENU.
    if ned is None:
        ned = True
    if not ned:
        zc *= -1
        temp = xc
        xc = yc + 0
        yc = temp + 0

    # Define height.
    hae = hae0 - zc

    # Initialize the latitude and longitude.
    lath = lat0 + xc/(A_E + hae)
    lonh = lon0 + yc/((A_E + hae)*np.cos(lath))

    # Iterate.
    for _ in range(3):
        # Get the sine and cosine of latitude.
        si = np.sin(lath)
        co = np.cos(lath)

        # Get the parallel and meridional radii of curvature.
        kp2 = 1 - E2*si**2
        kphi = np.sqrt(kp2)
        Rm = A_E*(1 - E2)/kphi**3
        Rt = A_E/kphi

        # Get the estimated xy position.
        xch = (Rm + hae)*(lath - lat0)
        ych = (Rt + hae)*co*(lonh - lon0)

        # Get the residual.
        xct = xc - xch
        yct = yc - ych

        # Get the inverse Jacobian.
        J11 = (3*E2*Rm*si*co/kp2)*(lath - lat0) + Rm + hae
        J12 = 0
        J21 = ((E2*co**2/kp2 - 1)*Rt - hae)*si*(lonh - lon0)
        J22 = (Rt + hae)*co
        Jdet_inv = 1/(J11*J22 - J21*J12)

        # Using the inverse Jacobian, get the residuals in lat and lon.
        latt = (J22*xct - J12*yct)*Jdet_inv
        lont = (J11*yct - J21*xct)*Jdet_inv

        # Update the latitude and longitude.
        lath = lath + latt
        lonh = lonh + lont

    return lath, lonh, hae
