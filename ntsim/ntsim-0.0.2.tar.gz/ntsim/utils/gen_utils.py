import numpy as np
def unit_vector(v):
    v_norm = np.ones(v.shape[0])
    np.sqrt(np.sum(np.power(v,2), axis=1), out=v_norm)
    zero_cond = v_norm==0.
    v_norm[zero_cond] = np.ones(v_norm[zero_cond].shape)
    v = (v.T/v_norm.T).T
    return v

def uniform_random_vector_in_cone(axis,costheta,eps=1e-10):
    # generate orthogonal random vector
    axis = unit_vector(axis)
    u = np.random.rand(axis.shape[0],axis.shape[1])
    ul = np.sum(u*axis,axis=1)
    ul = axis*ul.reshape(axis.shape[0],1)
    u = u - ul
    u = unit_vector(u)
    v = np.cross(u,axis)
    v = unit_vector(v)
    print(costheta,costheta.shape,axis.shape)
    z = np.random.uniform(costheta,1,(axis.shape[0],))
    phi = 2*np.pi*np.random.uniform(0,1,(axis.shape[0],))

    sintheta = np.sqrt(1-z**2)
    cosphi = np.cos(phi)
    sinphi = np.sin(phi)
    v_new = sintheta[:,None]*(cosphi[:,None]*u+sinphi[:,None]*v)+costheta[:,None]*axis

    c = np.sum(v_new*axis,axis=1)
    mask = c < costheta-eps
    if mask.any():
        print('uniform_random_vector_in_cone ',len(c[mask]))
        check1 = np.sum(u*axis,axis=1)
        check2 = np.sum(v*axis,axis=1)
        check3 = np.sum(u*v,axis=1)
        print('axis.shape',axis.shape)
        print('u.shape',u.shape)
        print('v.shape',v.shape)
        print('v_new.shape',v_new.shape)
        print(check1,check2,check3)
        print('costheta',costheta/c-1)

    return v_new


def rotate_vectors(r,dir,dir0):
    from scipy.spatial.transform import Rotation as R
    dir0 = np.array(dir0)
    phi = np.arctan2(dir0[1],dir0[0])
    theta = np.arccos(dir0[2]/np.sqrt(np.sum(dir0*dir0)))
    phi_d = np.tile([0,0,phi],(len(dir[:,0]),1))
    theta_d = np.tile([0,theta,0],(len(dir[:,0]),1))
    t = R.from_rotvec(phi_d)
    t1 = R.from_rotvec(theta_d)
    r = t.apply(t1.apply(r))
    dir = t.apply(t1.apply(dir))
    return r, dir


def translate_vectors(r, r0):
#    a = np.tile(r0, (r.shape[0],r.shape[1],1))
    r = r + r0
    return r, dir


def align_unit_vectors(a,b):
    # find rotation R: R*a = b
    from scipy.spatial.transform import Rotation
    a = unit_vector(a)
    b = unit_vector(b)
    c = np.cross(a,b)
    c = unit_vector(c)
    cosine = np.sum(a*b,axis=1)
    angle = np.arccos(cosine)
#    print(c.shape,angle.shape)
    rot = Rotation.from_rotvec(c*angle[:,None])
    return rot

def uniform_random_vector_in_cone_old(axis,angle):
    from scipy.spatial.transform import Rotation
    # axis = cone center
    # angle = cone angle (in radians)
    # algorithm from https://math.stackexchange.com/questions/56784/generate-a-random-direction-within-a-cone

    # generate random v1 around (0,0,1) on the sphere segment with theta  in (angle,1)
    z = np.random.uniform(np.cos(angle),1,axis.shape[0])
    phi = 2*np.pi*np.random.uniform(0,1,axis.shape[0])
    v1 = np.array([np.sqrt(1-z**2)*np.cos(phi),np.sqrt(1-z**2)*np.sin(phi),z]).T

    axis = unit_vector(axis)
    # make the vector product of cone axis with unit_z = (0,0,1): orth = unit_z x axis
    unit_z = np.array([0.,0.,1.])
    orth = np.cross(unit_z,axis)
    # check
    mask = np.sum(orth*orth,axis=1) != 0.0
    orth = unit_vector(orth)
#    print(orth)
    # rotate generated random vector v1 around orth by angle between unit_z and axis.
    # This way cone axis will be centered on axis instead of (0,0,1)
    cosines = np.sum(axis*unit_z,axis=1)
    axis_angle = np.arccos(cosines).reshape(cosines.shape[0],1)
    rot = Rotation.from_rotvec(axis_angle * orth)
#    print(rot.as_dcm())

    new_v = rot.apply(v1)
#    a = rot.apply(unit_z)
    c = np.sum(new_v*axis,axis=1)
    mask = np.arccos(c)>angle
    if mask.any():
        print('uniform_random_vector_in_cone ',orth)
    return new_v

def generate_cherenkov_spectrum(lambda_min,lambda_max,sample):
    # generate wavelength spectrum 1/lambda^2 in (lambda_min,lambda_max) according to
    # 1/lambda = 1/lambda_min - u*(1/lambda_min-1/lambda_max), where u = uniform in (0,1)
    u = np.random.uniform(0,1,sample)
    x = 1/lambda_min - u*(1/lambda_min-1/lambda_max)
    return 1/x

def searchsorted2d(a,b):
    m,n = a.shape
    max_num = np.maximum(a.max() - a.min(), b.max() - b.min()) + 1
    r = max_num*np.arange(a.shape[0])[:,None]
    p = np.searchsorted( (a+r).ravel(), (b+r).ravel(), side='left' ).reshape(m,-1)
    return p - n*(np.arange(m)[:,None])

def axes_bounds(x,y,z):
    return [axis_bounds(x), axis_bounds(y), axis_bounds(z)]

def axis_bounds(x):
    return [np.min(x),np.max(x)]
