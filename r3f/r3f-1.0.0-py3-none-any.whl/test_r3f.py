import numpy as np
import matplotlib.pyplot as plt
import r3f

# --------------------
# General Array Checks
# --------------------

def input_vector(func):
    try: # wrong vector type
        vec = [1, 2, 4]
        func(vec)
        assert False
    except TypeError:
        assert True
    try: # wrong vector dimensions
        vec = np.random.randn(3, 3, 3)
        func(vec)
        assert False
    except TypeError:
        assert True
    try: # wrong vector shape
        vec = np.eye(2)
        func(vec)
        assert False
    except ValueError:
        assert True


def input_axang(func):
    try: # wrong axis type
        ax = [1, 2, 4]
        func(ax, 1.0)
        assert False
    except TypeError:
        assert True
    try: # wrong axis dimensions
        ax = 5
        func(ax, 1.0)
        assert False
    except TypeError:
        assert True
    try: # wrong axis shape
        ax = np.eye(2)
        func(ax, 1.0)
        assert False
    except ValueError:
        assert True
    try: # wrong angle type
        ax = np.array([1, 2, 3])
        func(ax, [1.0])
        assert False
    except TypeError:
        assert True
    try: # angle dimensions too many
        ax = np.array([[1, 2], [3, 4], [5, 6]])
        ang = np.array([[1, 2], [3, 4], [5, 6]])
        func(ax, ang)
        assert False
    except TypeError:
        assert True
    try: # axis dimensions too few
        ax = np.array([1, 2, 3])
        ang = np.array([0.1, 0.2, 0.3])
        func(ax, ang)
        assert False
    except TypeError:
        assert True
    try: # length mismatch
        ax = np.array([[1, 2], [3, 4], [5, 6]])
        ang = np.array([0.1, 0.2, 0.3])
        func(ax, ang)
        assert False
    except ValueError:
        assert True


def input_rpy(func):
    A = np.random.randn(3, 1)
    v = np.array([0.1, 0.2, 0.3])
    s = 5.0
    try: # wrong p value
        func(2.0, 3.0, 2.0)
        assert False
    except ValueError:
        assert True
    try: # wrong p values
        func(v, v*10, v)
        assert False
    except ValueError:
        assert True
    try: # wrong r dimensions
        func(A, v, v)
        assert False
    except TypeError:
        assert True
    try: # wrong p dimensions
        func(v, np.zeros(3, 3), v)
        assert False
    except TypeError:
        assert True
    try: # wrong y dimensions
        func(v, v, A)
        assert False
    except TypeError:
        assert True
    try: # length mismatch
        func(v, v, np.array([1, 1, 1, 1]))
        assert False
    except ValueError:
        assert True
    try: # type mismatch
        func(2.0, v, 3.0)
        assert False
    except TypeError:
        assert True


def input_dcm(func):
    # Check is_square.
    A = np.array([1, 2, 3])
    B = np.array([
        [1, 3, 6],
        [7, 5, 2]])
    C = np.array([
        [1, 3, 6],
        [7, 5, 2],
        [9, 11, 13]])
    assert r3f.is_square(A) is False
    assert r3f.is_square(B) is False
    assert r3f.is_square(C) is True
    assert r3f.is_square(C, 2) is False
    D = np.array([
        [[1, 3, 6],
        [7, 5, 2],
        [9, 11, 13]],
        [[13, 1, 11],
        [3, 9, 6],
        [2, 7, 5]]])
    assert r3f.is_square(D) is True

    # Check is_ortho.
    A = np.eye(3)
    B = np.eye(3)
    B[2, 2] += 1e-7
    C = np.eye(3)
    C[2, 2] += 1e-8
    assert r3f.is_ortho(A) is True
    assert r3f.is_ortho(B) is False
    assert r3f.is_ortho(C) is True
    try:
        D = np.array([2, 3, 5])
        r3f.is_ortho(D)
        assert False
    except:
        assert True 
    E = np.array([
        [[1, 3, 6],
        [7, 5, 2],
        [9, 11, 13]],
        [[13, 1, 11],
        [3, 9, 6],
        [2, 7, 5]]])
    assert r3f.is_ortho(E) is False
    F = np.array([
        [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]],
        [[0, 0, -1],
        [0, 1, 0],
        [1, 0, 0]]])
    assert r3f.is_ortho(F) is True


def input_quat(func):
    try: # wrong type
        func([1, 2, 3, 4])
        assert False
    except TypeError:
        assert True
    try: # wrong dimensions
        func(np.array([[[0]]]))
        assert False
    except ValueError:
        assert True
    try: # wrong length
        func(np.array([1, 2, 3]))
        assert False
    except ValueError:
        assert True

# -----------------------------------
# Attitude-representation Conversions
# -----------------------------------

def test_axis_angle_vector():
    # Test inputs.
    input_axang(r3f.axis_angle_to_vector)
    input_vector(r3f.vector_to_axis_angle)

    # rotation about positive vector
    ax = np.array([1, 1, 1])
    ang = 2
    vec = r3f.axis_angle_to_vector(ax, ang)
    assert vec[0] == 2
    assert vec[1] == 2
    assert vec[2] == 2

    # multiple rotations
    ax = np.array([
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1]])
    ang = np.array([2, 2, 2, 2])
    vec = r3f.axis_angle_to_vector(ax, ang)
    print(vec)
    assert (vec == np.array([
        [2, 0, 0, 2],
        [0, 2, 0, 2],
        [0, 0, 2, 2]])).all()

    # single rotation
    c = np.array([1, 2, 4])
    ax, ang = r3f.vector_to_axis_angle(c)
    AX = np.array([0.21821789023599238127, 0.43643578047198476253,
         0.87287156094396952506])
    assert np.allclose(ax, AX)
    assert np.allclose(ang, 4.58257569495584000659)

    # multiple rotations
    d = np.array([
        [1, 2],
        [1, 2],
        [1, 2]])
    ax, ang = r3f.vector_to_axis_angle(d)
    rt3 = np.sqrt(3)
    rt12 = np.sqrt(12)
    assert np.allclose(ang, np.array([rt3, rt12]))
    assert np.allclose(ax[:, 0], 1/rt3)
    assert np.allclose(ax[:, 1], 2/rt12)
    d1 = r3f.axis_angle_to_vector(ax, ang)
    assert np.allclose(d, d1)


def test_rpy_axis_angle():
    # Test inputs.
    input_rpy(r3f.rpy_to_axis_angle)
    input_axang(r3f.axis_angle_to_rpy)

    # Test individual axes.
    ax, ang = r3f.rpy_to_axis_angle(0, 0, np.pi/4)
    assert np.allclose(ax, np.array([0, 0, 1]))
    assert np.allclose(ang, np.pi/4)
    ax, ang = r3f.rpy_to_axis_angle(0, np.pi/4, 0)
    assert np.allclose(ax, np.array([0, 1, 0]))
    assert np.allclose(ang, np.pi/4)
    ax, ang = r3f.rpy_to_axis_angle(np.pi/4, 0, 0)
    assert np.allclose(ax, np.array([1, 0, 0]))
    assert np.allclose(ang, np.pi/4)

    # Test vectorized reciprocity.
    N = 3
    R = np.random.uniform(-np.pi, np.pi, N)
    P = np.random.uniform(-np.pi/2 + r3f.TOL, np.pi/2 - r3f.TOL, N)
    Y = np.random.uniform(-np.pi, np.pi, N)
    ax, ang = r3f.rpy_to_axis_angle(R, P, Y)
    r, p, y = r3f.axis_angle_to_rpy(ax, ang)
    assert np.allclose(r, R)
    assert np.allclose(p, P)
    assert np.allclose(y, Y)


def test_dcm_axis_angle():
    # Test inputs.
    input_dcm(r3f.dcm_to_axis_angle)
    input_axang(r3f.axis_angle_to_dcm)
    
    # Define common angle and cosine and sine.
    ang = np.pi/4
    co = np.cos(ang)
    si = np.sin(ang)

    # Test individual axes.
    C = np.array([[co, si, 0], [-si, co, 0], [0, 0, 1]])
    C_p = r3f.axis_angle_to_dcm(np.array([0, 0, 1]), ang)
    assert np.allclose(C, C_p)
    ax1, ang1 = r3f.dcm_to_axis_angle(C_p)
    assert np.allclose(np.array([0, 0, 1]), ax1)
    assert np.allclose(ang, ang1)
    C = np.array([[co, 0, -si], [0, 1, 0], [si, 0, co]])
    C_p = r3f.axis_angle_to_dcm(np.array([0, 1, 0]), ang)
    assert np.allclose(C, C_p)
    ax1, ang1 = r3f.dcm_to_axis_angle(C_p)
    assert np.allclose(np.array([0, 1, 0]), ax1)
    assert np.allclose(ang, ang1)
    C = np.array([[1, 0, 0], [0, co, si], [0, -si, co]])
    C_p = r3f.axis_angle_to_dcm(np.array([1, 0, 0]), ang)
    assert np.allclose(C, C_p)
    ax1, ang1 = r3f.dcm_to_axis_angle(C_p)
    assert np.allclose(np.array([1, 0, 0]), ax1)
    assert np.allclose(ang, ang1)

    # Test vectorized reciprocity (requires positive axes).
    N = 5
    ax = np.abs(np.random.randn(3, N))
    nm = np.linalg.norm(ax, axis=0)
    ax /= nm
    ang = np.random.randn(N)
    C = r3f.axis_angle_to_dcm(ax, ang)
    ax1, ang1 = r3f.dcm_to_axis_angle(C)
    assert np.allclose(ax, ax1)
    assert np.allclose(ang, ang1)


def test_quat_axis_angle():
    # Test inputs.
    input_quat(r3f.quat_to_axis_angle)
    input_axang(r3f.axis_angle_to_quat)

    # axis angle to quat
    a = np.array([1, 1, 1])/np.sqrt(3) # normalized
    q1 = r3f.axis_angle_to_quat(a, np.pi)
    assert np.allclose(q1, np.array([0, 1, 1, 1])/np.sqrt(3))
    b = np.array([2, 2, 2])/np.sqrt(12) # normalized
    q2 = r3f.axis_angle_to_quat(b, np.pi)
    assert np.allclose(q2, np.array([0, 2, 2, 2])/np.sqrt(12))

    # backwards (requires normalized start)
    ax, ang = r3f.quat_to_axis_angle(q1)
    assert np.allclose(a, ax)
    assert np.allclose(np.pi, ang)

    # Test vectorized reciprocity.
    A = np.column_stack((a, b))
    Q = np.column_stack((q1, q2))
    assert np.allclose(r3f.axis_angle_to_quat(A, np.pi), Q)
    PI = np.array([np.pi, np.pi])
    assert np.allclose(r3f.axis_angle_to_quat(A, PI), Q)


def test_dcm_rpy():
    # Test inputs.
    input_dcm(r3f.dcm_to_rpy)
    input_rpy(r3f.rpy_to_dcm)

    # Build a random DCM.
    R = np.random.uniform(-np.pi, np.pi)
    P = np.random.uniform(-np.pi/2 + r3f.TOL, np.pi/2 - r3f.TOL)
    Y = np.random.uniform(-np.pi, np.pi)

    # Get rotation matrix.
    C_1g = np.array([
        [np.cos(Y), np.sin(Y), 0],
        [-np.sin(Y), np.cos(Y), 0],
        [0, 0, 1]])
    C_21 = np.array([
        [np.cos(P), 0, -np.sin(P)],
        [0, 1, 0],
        [np.sin(P), 0, np.cos(P)]])
    C_b2 = np.array([
        [1, 0, 0],
        [0, np.cos(R), np.sin(R)],
        [0, -np.sin(R), np.cos(R)]])
    C_bg = C_b2 @ C_21 @ C_1g

    # Check DCM to RPY.
    r, p, y = r3f.dcm_to_rpy(C_bg)
    assert np.allclose(r, R)
    assert np.allclose(p, P)
    assert np.allclose(y, Y)

    # Test vectorized reciprocity.
    N = 5
    R = np.random.uniform(-np.pi, np.pi, N)
    P = np.random.uniform(-np.pi/2 + r3f.TOL, np.pi/2 - r3f.TOL, N)
    Y = np.random.uniform(-np.pi, np.pi, N)
    C = r3f.rpy_to_dcm(R, P, Y)
    r, p, y = r3f.dcm_to_rpy(C)
    assert np.allclose(r, R)
    assert np.allclose(p, P)
    assert np.allclose(y, Y)


def test_quat_rpy():
    # Test inputs.
    input_quat(r3f.quat_to_rpy)
    input_rpy(r3f.rpy_to_quat)

    # This set of tests relies on previous tests.

    # Test forward path.
    N = 5
    R = np.random.uniform(-np.pi, np.pi, N)
    P = np.random.uniform(-np.pi/2 + r3f.TOL, np.pi/2 - r3f.TOL, N)
    Y = np.random.uniform(-np.pi, np.pi, N)
    ax, ang = r3f.rpy_to_axis_angle(R, P, Y)
    q1 = r3f.axis_angle_to_quat(ax, ang)
    q2 = r3f.rpy_to_quat(R, P, Y)
    assert np.allclose(q1, q2)

    # Test backward path.
    r, p, y = r3f.quat_to_rpy(q2)
    assert np.allclose(r, R)
    assert np.allclose(p, P)
    assert np.allclose(y, Y)


def test_quat_dcm():
    # Test inputs.
    input_quat(r3f.quat_to_dcm)
    input_dcm(r3f.dcm_to_quat)

    # This set of tests relies on previous tests.
    N = 5
    R = np.random.uniform(-np.pi, np.pi, N)
    P = np.random.uniform(-np.pi/2 + r3f.TOL, np.pi/2 - r3f.TOL, N)
    Y = np.random.uniform(-np.pi, np.pi, N)
    q1 = r3f.rpy_to_quat(R, P, Y)
    C1 = r3f.rpy_to_dcm(R, P, Y)
    C2 = r3f.quat_to_dcm(q1)
    assert np.allclose(C1, C2)

    # Test reciprocity.
    q2 = r3f.dcm_to_quat(C2)
    assert np.allclose(q1, q2)


def test_rot():
    irt2 = 1/np.sqrt(2)

    C = np.array([
        [irt2, irt2, 0],
        [-irt2, irt2, 0],
        [0, 0, 1]])
    assert np.allclose(r3f.rot(45, 2, True), C)

    B = np.array([
        [irt2, 0, -irt2],
        [0, 1, 0],
        [irt2, 0, irt2]])
    assert np.allclose(r3f.rot(45, 1, True), B)

    A = np.array([
        [1, 0, 0],
        [0, irt2, irt2],
        [0, -irt2, irt2]])
    assert np.allclose(r3f.rot(45, 0, True), A)

    R = r3f.rot([45, 45, 45], [2, 1, 0], True)
    assert np.allclose(R, A @ B @ C)

# ---------------------------
# Reference-frame Conversions
# ---------------------------

def test_ecef_geodetic():
    # Test single point.
    xyze = r3f.geodetic_to_ecef(0.0, 0.0, 0.0)
    assert np.allclose(xyze, np.array([r3f.A_E, 0, 0]))
    lat, lon, hae = r3f.ecef_to_geodetic(xyze)
    assert np.allclose(np.array([lat, lon, hae]), np.zeros(3))

    # Build original data.
    N = 10
    lat = np.random.uniform(-np.pi/2 + r3f.TOL, np.pi/2 - r3f.TOL, size=N)
    lon = np.random.uniform(-np.pi, np.pi, size=N)
    hae = np.random.uniform(-10e3, 100e3, size=N)

    # Test vectorized reciprocity.
    xyze = r3f.geodetic_to_ecef(lat, lon, hae)
    Lat, Lon, Hae = r3f.ecef_to_geodetic(xyze)
    assert np.allclose(lat, Lat)
    assert np.allclose(lon, Lon)
    assert np.allclose(hae, Hae)


def test_ecef_tangent():
    # Test single point.
    xyze = np.array([r3f.A_E, 0, r3f.B_E])
    xyze0 = np.array([r3f.A_E, 0, 0])
    xyzt = r3f.ecef_to_tangent(xyze, xyze0)
    XYZT = np.array([r3f.B_E, 0, 0])
    assert np.allclose(xyzt, XYZT)
    XYZE = r3f.tangent_to_ecef(XYZT, xyze0)
    assert np.allclose(xyze, XYZE)

    # Build original data.
    N = 10
    lat = np.random.uniform(-np.pi/2 + r3f.TOL, np.pi/2 - r3f.TOL, size=N)
    lon = np.random.uniform(-np.pi, np.pi, size=N)
    hae = np.random.uniform(-10e3, 100e3, size=N)
    xyze = r3f.geodetic_to_ecef(lat, lon, hae)

    # Test vectorized reciprocity.
    xyzt = r3f.ecef_to_tangent(xyze)
    XYZE = r3f.tangent_to_ecef(xyzt, xyze[:, 0])
    assert np.allclose(xyze, XYZE)


def test_geodetic_curlin():
    # Test single point.
    xyzc = r3f.geodetic_to_curlin(np.pi/4, 0, 1000, 0, 0, 0)
    assert xyzc[0] > 0
    assert xyzc[1] == 0
    assert xyzc[2] == -1000
    lat, lon, hae = r3f.curlin_to_geodetic(xyzc, 0, 0, 0)
    assert np.allclose(np.pi/4, lat)
    assert np.allclose(0, lon)
    assert np.allclose(1000, hae)

    # Build original data.
    N = 10
    lat = np.random.uniform(-np.pi/2 + r3f.TOL, np.pi/2 - r3f.TOL, size=N)
    lon = np.random.uniform(-np.pi, np.pi, size=N)
    hae = np.random.uniform(-10e3, 100e3, size=N)
    xyze = r3f.geodetic_to_curlin(lat, lon, hae)

    # Test vectorized reciprocity.
    Lat, Lon, Hae = r3f.curlin_to_geodetic(xyze, lat[0], lon[0], hae[0])
    assert np.allclose(lat, Lat)
    assert np.allclose(lon, Lon)
    assert np.allclose(hae, Hae)


#def test_curlin_geodetic():
#
#    # Original data
#    dphi = 15*(np.pi/180)
#    dlam = 15*(np.pi/180)
#    dhae = 10e3
#
#    phiO = np.random.uniform(-np.pi/2 + dphi, np.pi/2 - dphi)
#    lamO = np.random.uniform(-np.pi + dlam, np.pi - dlam)
#    haeO = np.random.uniform(-10e3 + dhae, 40e3 - dhae)
#
#    N = 1000
#    phi = phiO + np.random.uniform(-dphi, dphi, size=N)
#    lam = lamO + np.random.uniform(-dlam, dlam, size=N)
#    hae = haeO + np.random.uniform(-dhae, dhae, size=N)
#
#    # NavUtils test
#    xc1 = np.zeros(N)
#    yc1 = np.zeros(N)
#    zc1 = np.zeros(N)
#    phi1 = np.zeros(N)
#    lam1 = np.zeros(N)
#    hae1 = np.zeros(N)
#    llhO = np.array([phiO, lamO, haeO])
#    for n in range(N):
#        llh = np.array([phi[n], lam[n], hae[n]])
#        pc = core.llh_to_ned(llhO, llh)
#        xc1[n] = pc[0]
#        yc1[n] = pc[1]
#        zc1[n] = pc[2]
#        llh0 = core.ned_to_llh(llhO, pc)
#        phi1[n] = llh0[0]
#        lam1[n] = llh0[1]
#        hae1[n] = llh0[2]
#
#    # r3f test
#    xc2, yc2, zc2 = r3f.geodetic_to_curlin(phi, lam, hae, phiO, lamO, haeO,
#            ned=True)
#    phi2, lam2, hae2 = r3f.curlin_to_geodetic(xc2, yc2, zc2, phiO, lamO, haeO,
#            ned=True)
#
#    del_xc = np.sqrt(np.mean((xc1 - xc2)**2))
#    del_yc = np.sqrt(np.mean((yc1 - yc2)**2))
#    del_zc = np.sqrt(np.mean((zc1 - zc2)**2))
#
#    print(f"x,y,z diffs: {del_xc} {del_yc} {del_zc}")
#
#    er_phi1 = np.sqrt(np.mean((phi - phi1)**2))
#    er_lam1 = np.sqrt(np.mean((lam - lam1)**2))
#    er_hae1 = np.sqrt(np.mean((hae - hae1)**2))
#    
#    print("NavUtils errors:")
#    print(f"   phi errors: {er_phi1}")
#    print(f"   lam errors: {er_lam1}")
#    print(f"   hae errors: {er_hae1}")
#
#    er_phi2 = np.sqrt(np.mean((phi - phi2)**2))
#    er_lam2 = np.sqrt(np.mean((lam - lam2)**2))
#    er_hae2 = np.sqrt(np.mean((hae - hae2)**2))
#
#    print("r3f errors:")
#    print(f"   phi errors: {er_phi2}")
#    print(f"   lam errors: {er_lam2}")
#    print(f"   hae errors: {er_hae2}")
#
#    phi = np.pi/4
#    lam = np.pi/6
#    hae = 10e3
#    xc, yc, zc = r3f.geodetic_to_curlin(phi, lam, hae, np.pi/6, 0, 0,
#            ned=True)
#    phip, lamp, haep = r3f.curlin_to_geodetic(xc, yc, zc, np.pi/6, 0, 0,
#            ned=True)
#    print("Single result: %f, %f, %f" % (phi - phip, lam - lamp, hae - haep))
#
#
#def test_tangent_geodetic():
#
#    # Original data
#    dphi = 3*(np.pi/180)
#    dlam = 3*(np.pi/180)
#    dhae = 1e3
#
#    phiO = np.random.uniform(-np.pi/2 + dphi, np.pi/2 - dphi)
#    lamO = np.random.uniform(-np.pi + dlam, np.pi - dlam)
#    haeO = np.random.uniform(-10e3 + dhae, 40e3 - dhae)
#    xeO, yeO, zeO = r3f.geodetic_to_ecef(phiO, lamO, haeO)
#
#    N = 1000
#    phi = phiO + np.random.uniform(-dphi, dphi, size=N)
#    lam = lamO + np.random.uniform(-dlam, dlam, size=N)
#    hae = haeO + np.random.uniform(-dhae, dhae, size=N)
#    xe, ye, ze = r3f.geodetic_to_ecef(phi, lam, hae)
#
#    # NavUtils test
#    xt0 = np.zeros(N)
#    yt0 = np.zeros(N)
#    zt0 = np.zeros(N)
#    xe0 = np.zeros(N)
#    ye0 = np.zeros(N)
#    ze0 = np.zeros(N)
#    peO = np.array([xeO, yeO, zeO])
#    for n in range(N):
#        pe = np.array([xe[n], ye[n], ze[n]])
#        pt = core.ecef_to_ned(peO, pe)
#        xt0[n] = pt[0]
#        yt0[n] = pt[1]
#        zt0[n] = pt[2]
#        pe0 = core.ned_to_ecef(peO, pt)
#        xe0[n] = pe0[0]
#        ye0[n] = pe0[1]
#        ze0[n] = pe0[2]
#
#    # r3f test
#    xt1, yt1, zt1 = r3f.ecef_to_tangent(xe, ye, ze, xeO, yeO, zeO)
#    xe1, ye1, ze1 = r3f.tangent_to_ecef(xt1, yt1, zt1, xeO, yeO, zeO)
#
#    plt.figure()
#    plt.plot(xt0, yt0)
#    plt.plot(xt1, yt1)
#    plt.show()
#
#    del_xt = np.sqrt(np.mean((xt0 - xt1)**2))
#    del_yt = np.sqrt(np.mean((yt0 - yt1)**2))
#    del_zt = np.sqrt(np.mean((zt0 - zt1)**2))
#
#    print(f"x,y,z diffs: {del_xt} {del_yt} {del_zt}")
#
#    er_xe0 = np.sqrt(np.mean((xe - xe0)**2))
#    er_ye0 = np.sqrt(np.mean((ye - ye0)**2))
#    er_ze0 = np.sqrt(np.mean((ze - ze0)**2))
#
#    er_xe1 = np.sqrt(np.mean((xe - xe1)**2))
#    er_ye1 = np.sqrt(np.mean((ye - ye1)**2))
#    er_ze1 = np.sqrt(np.mean((ze - ze1)**2))
#
#    print(f"phi errors: {er_xe0} {er_xe1}")
#    print(f"lam errors: {er_ye0} {er_ye1}")
#    print(f"hae errors: {er_ze0} {er_ze1}")
