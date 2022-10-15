
    ########################
    ##  healpix.py        ##
    ##  Chieh-An Lin      ##
    ##  2022.10.15        ##
    ########################

## Python
import sys

## Third party
import numpy as np
import astropy.io.fits as fits
try:
  import healpy as hp
except:
  hp = None

## Custom
import pylinc.core as cf

################################################################################
## Functions - rotation and projection

def rotate(ra, dec=None, lonlat=True, rot_mat=np.diag(np.ones(3))):
  """
  Rotate points on the sky with regard to a rotation matrix

  Parameters
  ----------
  ra : float or (1, N) or (2, N) float array
    Right ascension or theta of the original points

  dec : float or (1, N) float array, optional
    Declination or phi of the original points

  lonlat : boolean, optional
    If lonlat == True, take and return ra and dec.
    Otherwise, theta and phi.

  rot_mat : (3, 3) float array, optional
    Rotation matrix

  Returns
  -------
  radec : (2,) or (2, N) float array
    radec[0] = new ra in [deg]
    radec[1] = new dec in [deg]
  """
  if dec is None:
    dec = ra[1]
    ra  = ra[0]
  u_xyz = hp.dir2vec(ra, dec, lonlat=lonlat)
  u_xyz = np.dot(rot_mat, u_xyz)
  radec = hp.vec2dir(u_xyz, lonlat=lonlat)
  return radec

def rotate_RADEC(ra, dec=None, rot_mat=np.diag(np.ones(3)), sign=0):
  """
  Rotate points on the sky with regard to a rotation matrix

  Parameters
  ----------
  ra : float or (1, N) or (2, N) float array
    Right ascension of the original points

  dec : float or (1, N) float array, optional
    Declination of the original points

  rot_mat : (3, 3) float array, optional
    Rotation matrix

  Returns
  -------
  radec : (2,) or (2, N) float array
    radec[0] = new ra in [deg]
    radec[1] = new dec in [deg]
  """
  if dec is None:
    dec = ra[1]
    ra  = ra[0]
  u_xyz     = hp.dir2vec(ra, dec, lonlat=True)
  u_xyz     = np.dot(rot_mat, u_xyz)
  radec    = hp.vec2dir(u_xyz, lonlat=True)
  radec[0] = cf.adjustRA(radec[0], half=180.0, sign=sign)
  return radec

def projector(center):
  proj = hp.projector.GnomonicProj(rot=(center[0], center[1]))
  proj.set_flip('geo')
  return proj

def patchProjector(nside, patch, nest=False, rot_mat=np.diag(np.ones(3))):
  u_xyz = hp.pix2vec(nside, patch, nest=nest)
  u_xyz = rot_mat.dot(u_xyz)
  center = hp.vec2dir(u_xyz, lonlat=True)
  proj = projector(center)
  return proj

def project(proj, ra, dec=None):
  """
  Parameters
  ----------
  proj : healpy projector
    Module which execute the projection
  ra : float or (1, N) or (2, N) float array
    Right ascension of the original points
  dec : float or (1, N) float array, optional
    Declination of the original points

  Returns
  -------
  theta_xy : (2,) or (2, N) float array
    theta_xy[0] = theta_x in [arcmin]
    theta_xy[1] = theta_y in [arcmin]
  """
  if dec is None:
    dec = ra[1]
    ra = ra[0]
  theta_xy = np.array(proj.ang2xy(ra, dec, lonlat=True)) ## [rad]
  theta_xy *= cf.RADIAN_TO_ARCMIN
  return theta_xy

def deproject(proj, theta_x, theta_y=None, sign=0):
  """
  Parameters
  ----------
  proj : healpy projector
    Module which execute the projection

  theta_x : float or float array
    If theta_y is None, theta_xy[0] = theta_x in [arcmin]
                        theta_xy[1] = theta_y in [arcmin].
    Otherwise, theta_x is theta_x in [arcmin].

  theta_y : float or float array, optional
    theta_y in [arcmin]

  sign : int, optional
    Option to adjust the returned ra value range
      -1 = adjust ra to [-360, 0[
       0 = do nothing
       1 = adjust ra to [0, 360[

  Returns
  -------
  radec : (2,) or (2, N) float array
    radec[0] = ra in [deg]
    radec[1] = dec in [deg]
  """
  if theta_y is None:
    theta_y = theta_x[1]
    theta_x = theta_x[0]
  radec = np.array(proj.xy2ang(theta_x*cf.ARCMIN_TO_RADIAN, theta_y*cf.ARCMIN_TO_RADIAN, lonlat=True)) ## [deg]
  radec[0] = cf.adjustRA(radec[0], half=180.0, sign=sign)
  return radec

################################################################################
## Functions - position conversion

def patchToUXYZ(nside, patch, nest=False, rot_mat=np.diag(np.ones(3))):
  u_xyz = np.array(hp.pix2vec(nside, patch))
  u_xyz = rot_mat.dot(u_xyz)
  return u_xyz

def uXYZToPatch(nside, u_x, u_y=None, u_z=None, nest=False, inv_rot_mat=np.diag(np.ones(3))):
  if u_y is None:
    u_z = u_x[2]
    u_y = u_x[1]
    u_x = u_x[0]
  u_xyz = inv_rot_mat.dot([u_x, u_y, u_z])
  patch = hp.vec2pix(nside, u_xyz[0], u_xyz[1], u_xyz[2], nest=nest)
  return patch

def patchToRADEC(nside, patch, nest=False, lonlat=True, rot_mat=np.diag(np.ones(3))):
  u_xyz  = hp.pix2vec(nside, patch, nest=nest)
  u_xyz  = rot_mat.dot(u_xyz)
  radec = hp.vec2dir(u_xyz, lonlat=lonlat)
  return radec

def RADECToPatch(nside, ra, dec=None, nest=False, lonlat=True, inv_rot_mat=np.diag(np.ones(3))):
  if dec is None:
    dec = ra[1]
    ra  = ra[0]
  u_xyz = hp.dir2vec(ra, dec, lonlat=lonlat)
  u_xyz = inv_rot_mat.dot(u_xyz)
  patch = hp.vec2pix(nside, u_xyz[0], u_xyz[1], u_xyz[2], nest=nest)
  return patch

def patchToThetaXY(proj, nside, patch, nest=False, rot_mat=np.diag(np.ones(3))):
  radec = patchToRADEC(nside, patch, nest=nest, rot_mat=rot_mat)
  theta_xy = project(proj, radec)
  return theta_xy

def thetaXYToPatch(proj, nside, theta_x, theta_y=None, nest=False, inv_rot_mat=np.diag(np.ones(3))):
  radec = deproject(proj, theta_x, theta_y=theta_y)
  patch = RADECToPatch(nside, radec, nest=nest, inv_rot_mat=inv_rot_mat)
  return patch

################################################################################
## Functions - HEALPix conversion

def nsideToDeg(nside):
  return hp.nside2resol(nside) * cf.RADIAN_TO_DEGREE

def nsideToArcmin(nside):
  return hp.nside2resol(nside) * cf.RADIAN_TO_ARCMIN

def nsideToDegSq(nside):
  return nsideToDeg(nside)**2

def nsideToArcminSq(nside):
  return nsideToArcmin(nside)**2

def nsideToL(nside):
  return cf.TWO_PI / hp.nside2resol(nside)

def nsideToVoxel(nside, z, dz):
  """
  Returns
  -------
  dw : float
    radial size

  dl : float
    transverse size

  dv : float
    volume
  """
  dw = cf.dw_over_dz(z) * dz
  w  = cf.comovDist(z)
  theta = hp.nside2resol(nside) ## [rad]
  dl = w * theta
  dv = dl**2 * dw
  return dw, dl, dv

def nsideToVoxel2(param, nside, z, dz):
  """
  Returns
  -------
  dw : float
    radial size

  dl : float
    transverse size

  dv : float
    volume
  """
  dw = cf.dw_over_dz_2(param, z) * dz
  w  = cf.comovDist_2(param, z)
  theta = hp.nside2resol(nside) ## [rad]
  dl = w * theta
  dv = dl**2 * dw
  return dw, dl, dv

def pixelToPatch(nside_pat, nside_pix, pix, nest=False):
  """
  Return the patch ring number of a given pixel.

  Parameters
  ----------
  nside_pat : int
    nside of the patch

  nside_pix : int
    nside of the pixel

  pix : int or (N,) int array
    ring or nest number of the pixel

  nest : bool, optional
    consider nest

  Returns
  -------
  patch : int or (N,) int array
    ring or nest number of the patch
  """
  pix = pix if nest == True else hp.ring2nest(nside_pix, pix)
  length = (nside_pix // nside_pat)**2
  patch = pix // length
  patch = patch if nest == True else hp.nest2ring(nside_pat, patch)
  return patch

def patchToPixels(nside_pat, nside_pix, patch, nest=False, sort=False):
  """
  Return all pixel ring or nest numbers - a given patch.

  Parameters
  ----------
  nside_pat : int
    nside of the patch

  nside_pix : int
    nside of the child patch

  patch : int
    ring or nest number of the patch

  nest : bool, optional
    consider nest

  sort : bool, optional
    sort the returned array

  Returns
  -------
  pix : int array
    ring or nest numbers of all pixels
  """
  patch = patch if nest == True else hp.ring2nest(nside_pat, patch)
  length = (nside_pix // nside_pat)**2
  pix = np.arange(patch*length, (patch+1)*length)
  pix = pix if nest == True else hp.nest2ring(nside_pix, pix)
  if sort == True:
    pix.sort()
  return pix

def nsideToLevels(nside):
  belt_length = 4 * nside
  nb_levels_in_belt = 2 * nside - 1
  len_arr = [4*i for i in range(1, nside+1)] + [belt_length for i in range(nb_levels_in_belt)] + [4*i for i in range(nside, 0, -1)]
  cum_len_arr = [0] + len_arr
  len_arr = np.array(len_arr)
  cum_len_arr = np.array(cum_len_arr).cumsum()
  return len_arr, cum_len_arr

def patchToCap(nside, patch, nest=False):
  patch = hp.nest2ring(nside, patch) if nest == True else patch
  v1 = 2 * nside * (nside + 1)
  v2 = 2 * nside * (5 * nside - 1)

  if np.isscalar(patch) == True:
    return -1 + int(patch < v2) + int(patch < v1)

  patch = np.array(patch)
  cap = np.zeros_like(patch, dtype=int) - 1
  cap += patch < v2
  cap += patch < v1
  return cap

def levelToPatches(nside, level, nest=False):
  len_arr, cum_len_arr = nsideToLevels(nside)
  patch_list = list(range(cum_len_arr[level], cum_len_arr[level+1]))
  return patch_list

def patchToLevel(nside, patch, nest=False):
  len_arr, cum_len_arr = nsideToLevels(nside)
  patch = hp.nest2ring(nside, patch) if nest == True else patch

  if np.isscalar(patch) == True:
    ind = patch >= cum_len_arr
    level = ind.sum() - 1
    return level

  ind = np.array([pat >= cum_len_arr for pat in patch])
  level = ind.sum(axis=1) - 1
  return level

def isBaseBoundary(nside, patch, nest=False):
  len_arr, cum_len_arr = nsideToLevels(nside)
  patch = hp.nest2ring(nside, patch) if nest == True else patch

  if np.isscalar(patch) == True:
    patch = np.fmin(patch, 12*nside*nside-1-patch) ## Reindex the south cap
    ind = patch >= cum_len_arr
    level = ind.sum() - 1
  else:
    patch = [np.fmin(pat, 12*nside*nside-1-pat) for pat in patch]
    ind = np.array([pat >= cum_len_arr for pat in patch])
    level = ind.sum(axis=1) - 1

  cap_threshold = cum_len_arr[nside] ## Block the belt
  rest = patch - cum_len_arr[level]
  j = rest % (level+1)

  ind = (patch < cap_threshold) * ((j == 0) + (j == level))
  return ind

def isBaseBoundary_all(nside):
  bool_list_1 = [np.zeros(length, dtype=bool) for length in range(1, nside+1) for offset in range(4)]
  for l in bool_list_1:
    l[0]  = True
    l[-1] = True
  bool_list_3 = [np.zeros(length, dtype=bool) for length in range(nside, 0, -1) for offset in range(4)]
  for l in bool_list_3:
    l[0]  = True
    l[-1] = True

  belt_length = 4 * nside
  nb_levels_in_belt = 2 * nside - 1
  bool_list_2 = np.zeros(belt_length*nb_levels_in_belt, dtype=bool)
  bool_list = np.concatenate(bool_list_1 + [bool_list_2] + bool_list_3)
  return bool_list

################################################################################
## Functions - Cartesian ordering

## Cartesian <--(a)--> i_pix & j_pix <--(b)--> local nest <--(c)--> pixel <--(d)--> ra & dec
## (a) Simple algebra
## (b) Implemented here
## (c) Implemented here
## (d) Implemented above

## (b) forward
def ijPixToLocalNest(resol, i_pix, j_pix):
  half_nb_bits = int(np.log2(resol))
  local_nest = 0
  for i in range(half_nb_bits):
    k = 2**i
    local_nest += np.bitwise_and(i_pix, k) * k
    local_nest += np.bitwise_and(j_pix, k) * k * 2
  return local_nest

## (b) backward
def localNestToIJPix(resol, local_nest):
  half_nb_bits = int(np.log2(resol))
  i_pix = 0
  j_pix = 0
  for i in range(half_nb_bits):
    k = 2**i
    i_pix += np.bitwise_and(local_nest, (k**2)) // k
    j_pix += np.bitwise_and(local_nest, (2 * k**2)) // k
  j_pix //= 2
  ij_pix = np.array([i_pix, j_pix])
  return ij_pix

## (ab) forward
def CartesianToLocalNest(resol, carte):
  """
  Convert Cartesian ordering to local nest ordering

  Cartesian ordering:    local nest ordering:
       0  1  2  3             0  1  4  5
       4  5  6  7             2  3  6  7
       8  9 10 11             8  9 12 13
      12 13 14 15            10 11 14 15

  Parameters
  ----------
  resol : int
    Resolution of the Cartesian grid
  carte : int array
    Cartesian ordering number

  Returns
  -------
  local_nest : int array
    Local nest ordering number
  """
  i_pix = carte % resol
  j_pix = carte // resol
  local_nest = ijPixToLocalNest(resol, i_pix, j_pix)
  return local_nest

## (ab) backward
def localNestToCartesian(resol, local_nest):
  """
  Convert local nest ordering to Cartesian ordering

  local nest ordering:    Cartesian ordering:
       0  1  4  5              0  1  2  3
       2  3  6  7              4  5  6  7
       8  9 12 13              8  9 10 11
      10 11 14 15             12 13 14 15

  Parameters
  ----------
  resol : int
    resolution of the Cartesian grid
  local_nest : int array
    local nest ordering number

  Returns
  -------
  carte : int array
    Cartesian ordering number
  """
  ij_pix = localNestToIJPix(resol, local_nest)
  carte = ij_pix[0] + ij_pix[1] * resol
  return carte

def resolToIJPix(resol):
  local_nest = np.arange(resol*resol)
  ij_pix = localNestToIJPix(resol, local_nest)
  return ij_pix

def resolToLocalNest(resol):
  carte = np.arange(resol*resol)
  local_nest = CartesianToLocalNest(resol, carte)
  return local_nest

## (c) forward
def localNestToPixel(nside_pat, nside_pix, patch, local_nest, nest=False):
  pat_nest = patch if nest == True else hp.ring2nest(nside_pat, patch)
  length = (nside_pix // nside_pat)**2
  pix = local_nest + pat_nest * length
  pix = pix if nest == True else hp.nest2ring(nside_pix, pix)
  return pix

## (c) backward
def pixelToLocalNest(nside_pat, nside_pix, pix, nest=False):
  pix = pix if nest == True else hp.ring2nest(nside_pix, pix)
  length = (nside_pix // nside_pat)**2
  local_nest = pix % length
  return local_nest

## (abc) forward
def CartesianToPixel(nside_pat, nside_pix, patch, carte, nest=False):
  resol = nside_pix // nside_pat
  local_nest = CartesianToLocalNest(resol, carte)
  pix = localNestToPixel(nside_pat, nside_pix, patch, local_nest, nest=nest)
  return pix

## (abc) backward
def pixelToCartesian(nside_pat, nside_pix, pix, nest=False):
  local_nest = pixelToLocalNest(nside_pat, nside_pix, pix, nest=nest)
  resol = nside_pix // nside_pat
  carte = localNestToCartesian(resol, local_nest)
  return carte

## (abcd) forward
def CartesianToRADEC(nside_pat, nside_pix, patch, carte, nest=False, lonlat=True, rot_mat=np.diag(np.ones(3))):
  resol = nside_pix // nside_pat
  local_nest = CartesianToLocalNest(resol, carte)
  pix = localNestToPixel(nside_pat, nside_pix, patch, local_nest, nest=nest)
  radec = patchToRADEC(nside_pix, pix, nest=nest, lonlat=lonlat, rot_mat=rot_mat)
  return radec

## (abcd) backward
def RADECToCartesian(nside_pat, nside_pix, ra, dec=None, nest=False, lonlat=True, inv_rot_mat=np.diag(np.ones(3))):
  pix = RADECToPatch(nside_pix, ra, dec=dec, nest=nest, lonlat=lonlat, inv_rot_mat=inv_rot_mat)
  local_nest = pixelToLocalNest(nside_pat, nside_pix, pix, nest=nest)
  resol = nside_pix // nside_pat
  carte = localNestToCartesian(resol, local_nest)
  return carte

################################################################################
## Functions - HEALPix grid

def makeSelfGrid(nside, patch, resol, nest=False):
  """
  Return a grid inside a given patch.

  Parameters
  ----------
  nside : int
    nside of the patch

  patch : int
    ring or nest number of the patch

  resol : int
    resolution of the grid

  nest : bool, optional
    consider nest

  Returns
  -------
  grid : (3, N) array
    grid[0] = i_pix, 0 <= i < resol
    grid[1] = j_pix, 0 <= j < resol
    grid[2] = ring or nest number
  """
  patch = patch if nest == True else hp.ring2nest(nside, patch)
  nside_pix = nside * resol
  pix = patchToPixels(nside, nside_pix, patch, nest=True, sort=False)
  pix = pix if nest == True else hp.nest2ring(nside_pix, pix)
  ij_pix = resolToIJPix(resol)
  grid = np.array([ij_pix[0], ij_pix[1], pix], dtype=int)
  return grid

def __rotateGrid(grid, resol, base, ngb_base):
  """
  Compute everything in nest
  """
  if base == ngb_base:
    return grid
  if base in [4,5,6,7] or ngb_base in [4,5,6,7]:
    return grid

  diff = (ngb_base - base) % 4

  if (diff == 2):
    ## Rotate 180 degrees
    return np.array([resol - 1 - grid[0], resol - 1 - grid[1]])

  if (diff == 3 and base < 4) or (diff == 1 and base >= 8):
    ## Rotate counter-clockwise
    return np.array([grid[1], resol - 1 - grid[0]])

  if (diff == 1 and base < 4) or (diff == 3 and base >= 8):
    ## Rotate clockwise
    return np.array([resol - 1 - grid[1], grid[0]])

  return grid

def __translateGrid(grid, resol, i):
  """
  Compute everything in nest
  """
  if i in [7, 0, 1]:
    grid[0] -= resol
  elif i in [3, 4, 5]:
    grid[0] += resol

  if i in [5, 6, 7]:
    grid[1] -= resol
  elif i in [1, 2, 3]:
    grid[1] += resol
  return grid

def __cutGrid(grid, resol, buff):
  """
  Compute everything in nest
  """
  ind  = (grid[0] >= -buff) * (grid[0] < resol+buff) * (grid[1] >= -buff) * (grid[1] < resol+buff)
  grid = grid.T[ind].T
  return grid

def __makeNeighborGrid(grid_orig, nside, pat_nest, ngbNest, resol, buff, i):
  """
  Compute everything in nest
  """
  nside_pix = nside * resol
  pix_nest = patchToPixels(nside, nside_pix, ngbNest, nest=True, sort=False)
  base = pixelToPatch(1, nside, pat_nest)
  ngb_base = pixelToPatch(1, nside, ngbNest)

  grid = __rotateGrid(grid_orig, resol, base, ngb_base)
  grid = __translateGrid(grid, resol, i)
  grid = np.insert(grid, 2, pix_nest, axis=0)
  grid = __cutGrid(grid, resol, buff)
  return grid

def makeBufferGrid(nside, patch, resol, buff, nest=False):
  """
  Return the grid of the buffer area of a given patch.

  Parameters
  ----------
  nside : int
    nside of the patch
  patch : int
    ring or nest number of the patch
  resol : int
    resolution of the grid
  buff : int
    buffer size in [pix]
  nest : bool, optional
    consider nest

  Returns
  -------
  grid : (3, N) array
    grid[0] = i_pix, < 0 or >= resol
    grid[1] = j_pix, < 0 or >= resol
    grid[2] = ring or nest number
  """
  patch = patch if nest == True else hp.ring2nest(nside, patch)
  neighbors = hp.get_all_neighbours(nside, patch, nest=True)
  grid_orig = np.array(resolToIJPix(resol))
  grid_list = [__makeNeighborGrid(grid_orig.copy(), nside, patch, neighbors[i], resol, buff, i)
               for i in range(8) if neighbors[i] != -1]
  grid = np.concatenate(grid_list, axis=1)
  grid[2] = grid[2] if nest == True else hp.nest2ring(nside*resol, grid[2])
  return grid

def patchToGrid(nside, patch, resol, buff, nest=False):
  """
  Cut a patch into Cartesian coordinates and their ring or nest numbers.
  Support the buffer area, which requires information of neighbors.

  Parameters
  ----------
  nside : int
    nside of the patch
  patch : int
    ring or nest number of the patch
  resol : int
    resolution of the grid
  buff : int
    buffer size in [pix]
  nest : bool, optional
    consider nest

  Returns
  -------
  grid : (3, N) array
    grid[0] = i_pix, -buff <= i < resol+buff
    grid[1] = j_pix, -buff <= i < resol+buff
    grid[2] = ring or nest number

  Example
  -------
  >>> buff = 1
  >>> grid = hpf.patchToGrid(2, 14, 2, buff)
  >>> stock = np.zeros((4, 4), dtype=float) + np.nan
  array([[ nan,  nan,  nan,  nan],
         [ nan,  nan,  nan,  nan],
         [ nan,  nan,  nan,  nan],
         [ nan,  nan,  nan,  nan]])
  >>> stock[grid[1]+buff, grid[0]+buff] = grid[2]
  >>> stock
  array([[108.,  92.,  77.,  61.],
         [ 91.,  76.,  60.,  45.],
         [ 75.,  59.,  44.,  28.],
         [ 58.,  43.,  27.,  nan]])

  which stand for:
     58  43  27  nan
     75  59  44  28
     91  76  60  45
    108  92  77  61
  """
  grid = makeSelfGrid(nside, patch, resol, nest=nest)
  if buff > 0:
    grid_buff = makeBufferGrid(nside, patch, resol, buff, nest=nest)
    grid = np.concatenate([grid, grid_buff], axis=1)

  order = grid[0].argsort(kind='mergesort')
  grid[0] = grid[0][order]
  grid[1] = grid[1][order]
  grid[2] = grid[2][order]

  order = grid[1].argsort(kind='mergesort')
  grid[0] = grid[0][order]
  grid[1] = grid[1][order]
  grid[2] = grid[2][order]
  return grid

def saveFitsHPGridPos(prefix, nside, patch, resol, buff, rot_mat=np.diag(np.ones(3))):
  nside_pix = nside * resol
  grid = patchToGrid(nside, patch, resol, buff, nest=False)
  radec = patchToRADEC(nside_pix, grid[2], rot_mat=rot_mat)
  proj = patchProjector(nside, patch, rot_mat)
  theta_xy = project(proj, radec)

  hdu1 = fits.PrimaryHDU()
  hdu2 = fits.BinTableHDU.from_columns([
    fits.Column(name='I',    format='I', unit='-       ', array=grid[0]),
    fits.Column(name='J',    format='I', unit='-       ', array=grid[1]),
    fits.Column(name='RING', format='K', unit='-       ', array=grid[2]),
    fits.Column(name='ra',   format='E', unit='deg',      array=radec[0]),
    fits.Column(name='dec',  format='E', unit='deg',      array=radec[1]),
    fits.Column(name='THX',  format='E', unit='arcmin',   array=theta_xy[0]),
    fits.Column(name='THY',  format='E', unit='arcmin',   array=theta_xy[1])
  ])

  hdr = hdu2.header
  hdr.update(
    TTYPE1=(hdr['TTYPE1'], 'i_pix'),
    TTYPE2=(hdr['TTYPE2'], 'j_pix'),
    TTYPE3=(hdr['TTYPE3'], 'ring nb of the pixel'),
    TTYPE4=(hdr['TTYPE4'], 'ra'),
    TTYPE5=(hdr['TTYPE5'], 'dec'),
    TTYPE6=(hdr['TTYPE6'], 'projected position theta_x'),
    TTYPE7=(hdr['TTYPE7'], 'projected position theta_y')
  )
  hdr.append(('COMMENT', None),                                         bottom=True)
  hdr.append(('RESOL',   resol,            '[pix] map resolution'),     bottom=True)
  hdr.append(('BUFFER',  buff,             '[pix] border buffer size'), bottom=True)
  hdr.append(('RAMIN',   radec[0].min(),   '[deg]'),                    bottom=True)
  hdr.append(('RAMAX',   radec[0].max(),   '[deg]'),                    bottom=True)
  hdr.append(('DECMIN',  radec[1].min(),   '[deg]'),                    bottom=True)
  hdr.append(('DECMAX',  radec[1].max(),   '[deg]'),                    bottom=True)
  hdr.append(('THXMIN',  theta_xy[0].min(), '[arcmin]'),                 bottom=True)
  hdr.append(('THXMAX',  theta_xy[0].max(), '[arcmin]'),                 bottom=True)
  hdr.append(('THYMIN',  theta_xy[1].min(), '[arcmin]'),                 bottom=True)
  hdr.append(('THYMAX',  theta_xy[1].max(), '[arcmin]'),                 bottom=True)

  name = '{}HPGridPos_patch{:04d}.fits'.format(prefix, patch)
  fits.HDUList([hdu1, hdu2]).writeto(name, overwrite=True)
  print('Saved \"{}\"'.format(name))
  return

################################################################################
## Functions - patch sampling

def decompose(nside, patch, nest=False):
  len_arr, cum_len_arr = nsideToLevels(nside)
  cap = patchToCap(nside, patch, nest=nest)
  patch = hp.nest2ring(nside, patch) if nest == True else patch ## Require ring

  ## Determine level
  if np.isscalar(patch) == True:
    ind = patch >= cum_len_arr
    level = ind.sum() - 1
  else:
    ind = np.array([pat >= cum_len_arr for pat in patch])
    level = ind.sum(axis=1) - 1

  ## Determine length, offset, j
  rest = patch - cum_len_arr[level]
  length = len_arr[level] // 4
  offset = (rest // length + 2) % 4 - 2
  j = rest % length

  info = np.array([cap, level, length, offset, j])
  return info

def recombine(nside, cap, level=None, length=None, offset=None, j=None):
  if level is None:
    n = cap.shape[0]
    if n == 5:
      j      = cap[4]
      offset = cap[3]
      length = cap[2]
      level  = cap[1]
      cap    = cap[0]
    elif n == 4:
      j      = cap[3]
      offset = cap[2]
      length = cap[1]
      level  = cap[0]
    elif n == 3:
      j      = cap[2]
      offset = cap[1]
      level  = cap[0]
    else:
      sys.exit('Array dimension error')

  len_arr, cum_len_arr = nsideToLevels(nside)
  offset = (offset + 4) % 4
  patch = cum_len_arr[level] + offset * len_arr[level] // 4 + j
  return patch

def adjustRA_boundary(ra, half=180.0):
  if ra[1] > ra[3]:
    if ra[3] == -half:
      ra = ra % (2.0*half)
    else:
      ra = ra % (2.0*half) - 2.0*half
  return ra

def patchBoundary(nside, patch, nest=False, lonlat=False, step=512):
  info   = decompose(nside, patch, nest=nest)
  cap    = info[0]
  level  = info[1]
  length = info[2]
  offset = info[3]
  j      = info[4]

  ## Get z & psi of the corners
  u_xyz     = hp.boundaries(nside, patch, nest=nest)
  theta_phi = hp.vec2dir(u_xyz, lonlat=False)
  phi       = adjustRA_boundary(theta_phi[1], half=np.pi)
  z         = np.cos(theta_phi[0])
  psi       = phi / cf.HALF_PI - offset ## Normalization

  ## Define normalized and offset ra
  dl    = 1.0 / float(nside)
  dpsi  = step + 1
  p_line = lambda psi, l: 1.0 - (l/psi)**2 / 3.0
  b_line = lambda psi, l: 4.0/3.0 * (0.5 - l + psi)
  psi_nw = np.linspace(psi[1], psi[0], dpsi)
  psi_ne = np.linspace(psi[0], psi[3], dpsi)
  psi_sw = np.linspace(psi[1], psi[2], dpsi)
  psi_se = np.linspace(psi[2], psi[3], dpsi)

  boundary = []

  ## North cap
  if cap == 1:
    l_nw = j * dl
    l_ne = (length-1-j) * dl
    l_SW = (length-j) * dl
    l_se = (j+1) * dl

    if j == 0:
      z_arr_nw = np.linspace(z[0], z[1], dpsi)
      x_arr_nw = np.zeros_like(z_arr_nw, dtype=float)
      boundary.append([x_arr_nw, z_arr_nw])
    else:
      z_arr_nw = p_line(psi_nw, l_nw)
      boundary.append([psi_nw, z_arr_nw])

    if j == level:
      z_arr_ne = np.linspace(z[3], z[0], dpsi)
      x_arr_ne = np.ones_like(z_arr_ne, dtype=float)
      boundary.append([x_arr_ne, z_arr_ne])
    else:
      z_arr_ne = p_line(1.0-psi_ne, l_ne)
      boundary.append([psi_ne, z_arr_ne])

    if level < nside-1:
      z_arr_sw = p_line(1.0-psi_sw, l_SW)
      z_arr_se = p_line(psi_se, l_se)
      boundary.append([psi_sw, z_arr_sw])
      boundary.append([psi_se, z_arr_se])
    else:
      z_arr_sw = b_line(1.0-psi_sw, l_SW)
      z_arr_se = b_line(psi_se, l_se)
      boundary.append([psi_sw, z_arr_sw])
      boundary.append([psi_se, z_arr_se])

    if level == 0:
      x_arr_n = np.linspace(0.0, 1.0, dpsi)
      z_arr_n = np.ones_like(x_arr_n, dtype=float)
      boundary.append([x_arr_n, z_arr_n])

  ## South cap
  if cap == -1:
    l_nw = (length-j) * dl
    l_ne = (j+1) * dl
    l_SW = j * dl
    l_se = (length-1-j) * dl

    if level > 3*nside-1:
      z_arr_nw = p_line(1.0-psi_nw, l_nw)
      z_arr_ne = p_line(psi_ne, l_ne)
      boundary.append([psi_nw, -z_arr_nw])
      boundary.append([psi_ne, -z_arr_ne])
    else:
      z_arr_nw = b_line(1.0-psi_nw, l_nw)
      z_arr_ne = b_line(psi_ne, l_ne)
      boundary.append([psi_nw, -z_arr_nw])
      boundary.append([psi_ne, -z_arr_ne])

    if j == 0:
      z_arr_sw = np.linspace(z[1], z[2], dpsi)
      x_arr_sw = np.zeros_like(z_arr_nw, dtype=float)
      boundary.append([x_arr_sw, z_arr_sw])
    else:
      z_arr_sw = p_line(psi_sw, l_SW)
      boundary.append([psi_sw, -z_arr_sw])

    if j == 4*nside-2 - level:
      z_arr_se = np.linspace(z[2], z[3], dpsi)
      x_arr_se = np.ones_like(z_arr_se, dtype=float)
      boundary.append([x_arr_se, z_arr_se])
    else:
      z_arr_se = p_line(1.0-psi_se, l_se)
      boundary.append([psi_se, -z_arr_se])

    if level == 4*nside-2:
      x_arr_n = np.linspace(0.0, 1.0, dpsi)
      z_arr_n = -np.ones_like(x_arr_n, dtype=float)
      boundary.append([x_arr_n, z_arr_n])

  ## Belt
  if cap == 0:
    l_nw = ((level+1-length)//2 + j) * dl
    l_ne = ((level-length)//2 + length-j) * dl
    l_SW = ((level-length)//2 + length-j + 1) * dl
    l_se = ((level+1-length)//2 + j + 1) * dl

    z_arr_nw = b_line(psi_nw, l_nw)
    z_arr_ne = b_line(1.0-psi_ne, l_ne)
    z_arr_sw = b_line(1.0-psi_sw, l_SW)
    z_arr_se = b_line(psi_se, l_se)

    boundary.append([psi_nw, z_arr_nw])
    boundary.append([psi_ne, z_arr_ne])
    boundary.append([psi_sw, z_arr_sw])
    boundary.append([psi_se, z_arr_se])

  factor      = 90.0 if lonlat == True else cf.HALF_PI
  boundary    = np.array(boundary).swapaxes(0, 1) ## From (4, 2, 512) to (2, 4, 512)
  boundary[0] = (boundary[0] + offset) * factor
  boundary[1] = 90.0 - np.arccos(boundary[1]) * cf.RADIAN_TO_DEGREE if lonlat == True else boundary[1]
  return boundary

def __capSampling(nside, N, level, length, j, z_0):
  c_line = lambda psi, l: 1.0 - (l/psi)**2 / 3.0
  c_area = lambda psi_0, psi, l: (1.0-z_0) * (psi-psi_0) + l**2/3.0 * (1.0/psi-1.0/psi_0)
  b_line = lambda psi, l: 4.0/3.0 * (0.5 - l + psi)

  ## Determine corners
  dummy      = -1.0
  j2         = float(j)
  length2    = float(length)
  corner_psi = [dummy, j2/length2, (j2+1.0)/(length2+1.0), (j2+1.0)/length2]
  corner_psi[0] = j2 / (length2 - 1.0)                if (level > 0)         else corner_psi[0]
  corner_psi[2] = 0.5 * (corner_psi[1] + corner_psi[3]) if (level == nside -1) else corner_psi[2]

  ## Determine psi
  psi0_arr    = np.array([corner_psi[1], 1.0-corner_psi[3], 1.0-corner_psi[2], corner_psi[2]])
  psi0_arr[0] = dummy if (j == 0)     else psi0_arr[0]
  psi0_arr[1] = dummy if (j == level) else psi0_arr[1]

  ## Determine l
  dl   = 1.0 / float(nside)
  l_arr = np.zeros(4, dtype=float)
  l_arr[0] = j2 * dl
  l_arr[1] = (length2-1.0-j2) * dl
  l_arr[2] = l_arr[1] + dl
  l_arr[3] = l_arr[0] + dl

  ## Determine zone areas & update
  half_denom = 3.0 * nside**2
  a_arr      = [1.0 / (2.0 * half_denom)] * 4
  if (level == 0 and nside > 1):
      a_arr[2] = -c_area(1.0-corner_psi[2], 1.0-corner_psi[1], l_arr[2])
      a_arr[3] = -c_area(    corner_psi[2],     corner_psi[3], l_arr[3])

  else:
    if (level < nside -1):
      a_arr[2] = -c_area(1.0-corner_psi[2], 1.0-corner_psi[1], l_arr[2])
      a_arr[3] = -c_area(    corner_psi[2],     corner_psi[3], l_arr[3])

    if (j == 0):
      a_arr[0] = 0.0
      a_arr[1] =  c_area(1.0-corner_psi[3], 1.0-corner_psi[0], l_arr[1])

    elif (j == level):
      a_arr[0] =  c_area(    corner_psi[1],     corner_psi[0], l_arr[0])
      a_arr[1] = 0.0

    else:
      a_arr[0] =  c_area(    corner_psi[1],     corner_psi[0], l_arr[0])
      a_arr[1] =  c_area(1.0-corner_psi[3], 1.0-corner_psi[0], l_arr[1])

  a_cum = np.array([0.0] + a_arr).cumsum()

  ## Original sampling functions:
  ##   cSampP = lambda A, l, psi_0: (A +(1.0-z_0)*psi_0+l**2/(3.0*psi_0) + np.sqrt((A +(1.0-z_0)*psi_0+l**2/(3.0*psi_0))**2 - 4.0*(1-z_0)*l**2/3.0)) * 0.5 / (1.0 - z_0)
  ##   cSampM = lambda A, l, psi_0: (A +(1.0-z_0)*psi_0+l**2/(3.0*psi_0) - np.sqrt((A +(1.0-z_0)*psi_0+l**2/(3.0*psi_0))**2 - 4.0*(1-z_0)*l**2/3.0)) * 0.5 / (1.0 - z_0)
  ## Belows are simplification.
  cst1 = (1.0 - z_0) * psi0_arr + l_arr**2 / (3.0 * psi0_arr)
  cst2 = 4.0/3.0 * (1 - z_0) * l_arr**2
  cst3 = 0.5 / (1.0 - z_0) ## This is a scalar.
  cst4 = 4.0/3.0 * (0.5 - l_arr) - z_0
  cst5 = (cst4 + 4.0/3.0*psi0_arr)**2
  c_samp_p = lambda a, cst1, cst2: (a + cst1 + np.sqrt((a + cst1)**2 - cst2)) * cst3
  c_samp_m = lambda a, cst1, cst2: (a + cst1 - np.sqrt((a + cst1)**2 - cst2)) * cst3
  b_samp_m = lambda a, cst4, cst5: 0.75 * (-cst4 - np.sqrt(cst5 + 8.0/3.0*a))

  ## Sample and determine which zone
  p    = np.random.uniform(0.0, a_cum[-1], N)
  q    = np.random.rand(N)
  p2   = np.array([p]).T
  ind  = p2 >= a_cum
  ind  = ind.sum(axis=1) - 1
  rest = p - a_cum[ind]
  l    = l_arr[ind]

  ind1 = ind < 2
  ind2 = ind >= 2
  ind3 = (ind == 1) + (ind == 2)

  ## Transform into psi & z
  psi       = np.zeros_like(rest, dtype=float)
  psi[ind1] = rest[ind1] * half_denom                                if level == 0       else c_samp_p( rest[ind1], cst1[ind][ind1], cst2[ind][ind1])
  psi[ind2] = b_samp_m(-rest[ind2], cst4[ind][ind2], cst5[ind][ind2]) if level == nside-1 else c_samp_m(-rest[ind2], cst1[ind][ind2], cst2[ind][ind2])
  z         = np.zeros_like(rest, dtype=float)
  z[ind1]   = q[ind1] / half_denom                                   if level == 0       else (c_line(psi[ind1], l[ind1]) - z_0) * q[ind1]
  z[ind2]   = (b_line(psi[ind2], l[ind2]) - z_0) * q[ind2]           if level == nside-1 else (c_line(psi[ind2], l[ind2]) - z_0) * q[ind2]
  psi[ind3] = 1.0 - psi[ind3]

  return z, psi

def __beltSampling(nside, N):
  """
  Pixels in the belt are all diamond shapes in the phi-z space.
  The width is 1/nside and the height is 4/3nside.
  """
  psi_half = 0.5
  z_half = 2.0 / 3.0
  psi = np.random.uniform(-psi_half, psi_half, N)
  z = np.random.uniform(0.0, z_half, N)

  ind1 = (4.0 * np.fabs(psi) > 3.0 * z)
  ind2 = psi > 0.0

  psi[ind1*ind2]    -= psi_half
  psi[ind1*(~ind2)] += psi_half
  z[~ind1]          -= z_half
  z   /= float(nside)
  psi /= float(nside)
  return z, psi

def patchSampling(nside, patch, N, nest=False, lonlat=True):
  info   = decompose(nside, patch, nest=nest)
  cap    = info[0]
  level  = info[1]
  length = info[2]
  offset = info[3]
  j      = info[4]

  ## Get z0
  ctr_theta_phi = patchToRADEC(nside, patch, nest=nest, lonlat=False)
  z_0 = np.cos(ctr_theta_phi[0])

  ## Sample
  if cap == 1:
    z, psi = __capSampling(nside, N, level, length, j, z_0)
    z += z_0
    phi = (psi + offset) * cf.HALF_PI
  elif cap == 0:
    z, psi = __beltSampling(nside, N)
    z += z_0
    phi = psi * cf.HALF_PI + cf.adjustRA(ctr_theta_phi[1], half=np.pi, sign=0)
  else:
    z, psi = __capSampling(nside, N, 4*nside-2-level, length, length-1-j, -z_0)
    z = z_0 - z
    phi = (1.0 - psi + offset) * cf.HALF_PI

  if N == 1:
    z = z[0]
    phi = phi[0]

  ## Conversion
  pos = cf.spheToCeles(np.arccos(z), phi) if lonlat == True else np.array([phi, z])
  return pos

def patchSampling2(nside, patch, N, nest=False, lonlat=True):
  u_xyz = hp.boundaries(nside, patch, nest=nest)
  theta_phi = hp.vec2dir(u_xyz, lonlat=False)
  phi = adjustRA_boundary(theta_phi[1], half=np.pi)
  z = np.cos(theta_phi[0])

  z_min = z.min()
  z_max = z.max()
  phi_min = phi.min()
  phi_max = phi.max()
  stock = []

  while (len(stock) < N):
    z2 = np.random.uniform(z_min, z_max)
    phi2 = np.random.uniform(phi_min, phi_max)
    theta2 = np.arccos(z2)
    pat2 = hp.ang2pix(nside, theta2, phi2, nest=nest)

    if pat2 == patch:
      pos = cf.spheToCeles(theta2, phi2) if lonlat == True else [phi2, z2]
      stock.append(pos)

  stock = stock[0] if N == 1 else stock
  stock = np.array(stock).T
  return stock

################################################################################
## Functions - mask sampling

def makeRandCat_Poisson(mask, n_samp, verbose=True):
  nb_pix = mask.size
  nside = hp.npix2nside(nb_pix)
  pix_area = nsideToArcminSq(nside) ## [arcmin^2]

  pix = np.arange(nb_pix, dtype=int)
  pix = pix[mask]
  nb_act_pix = pix.size
  mask_area = nb_act_pix * pix_area ## [arcmin^2]

  n_expected = n_samp * pix_area
  nb_samp_arr  = np.random.poisson(lam=n_expected, size=nb_act_pix)
  ind = nb_samp_arr > 0
  pix = pix[ind]
  nb_samp_arr  = nb_samp_arr[ind]

  if verbose:
    print('nside of pixel        = {:d}'.format(nside))
    print('Nb of active pixel    = {:d}'.format(nb_act_pix))
    print('Nb of samples         = {:d}'.format(sum(nb_samp_arr)))
    print('Nb density of samples = {:f} [arcmin^-2]'.format(sum(nb_samp_arr)/mask_area))

  ra  = []
  dec = []

  for i, N in enumerate(nb_samp_arr):
    pos = patchSampling(nside, pix[i], N)
    pos = pos.reshape(2, -1)
    ra.append(pos[0])
    dec.append(pos[1])

  ra    = np.concatenate(ra)
  dec   = np.concatenate(dec)
  radec = np.array([ra, dec])
  return radec

def makeRandCat_randPos(mask, nbSamp, verbose=True):
  nb_pix = mask.size
  nside = hp.npix2nside(nb_pix)
  pix_area = nsideToArcminSq(nside) ## [arcmin^2]

  pix = np.arange(nb_pix, dtype=int)
  pix = pix[mask]
  nb_act_pix = pix.size
  mask_area = nb_act_pix * pix_area ## [arcmin^2]

  ind_samp = np.random.randint(nb_act_pix, size=nbSamp)
  nb_samp_arr = np.bincount(ind_samp, minlength=nb_act_pix)
  ind = nb_samp_arr > 0
  pix = pix[ind]
  nb_samp_arr = nb_samp_arr[ind]

  if verbose:
    print('nside of pixel        = {:d}'.format(nside))
    print('Nb of active pixel    = {:d}'.format(nb_act_pix))
    print('Nb of samples         = {:d}'.format(sum(nb_samp_arr)))
    print('Nb density of samples = {:f} [arcmin^-2]'.format(sum(nb_samp_arr)/mask_area))

  ra = []
  dec = []

  for i, n in enumerate(nb_samp_arr):
    pos = patchSampling(nside, pix[i], n)
    pos = pos.reshape(2, -1)
    ra.append(pos[0])
    dec.append(pos[1])

  ra = np.concatenate(ra)
  dec = np.concatenate(dec)
  radec = np.array([ra, dec])
  return radec

def makeRandCat_fullSky(nbSamp):
  phi = np.random.uniform(-np.pi, np.pi, nbSamp)
  z = np.random.uniform(-1.0, 1.0, nbSamp)
  radec = cf.spheToCeles(np.arccos(z), phi)
  return radec

################################################################################
## Functions - full map manipulation

def loadFitsFullMap(name, verbose=True):
  full = fits.getdata(name, 1).field(0).flatten()
  if verbose == True:
    print('Loaded \"{}\"'.format(name))
  return full

def saveFitsFullMap(name, full, verbose=True):
  full = full.astype(np.float32)
  nb_rows = full.size // 1024
  full = full.reshape(nb_rows, 1024)
  nside = hp.npix2nside(full.size)

  hdu1 = fits.PrimaryHDU()
  hdu2 = fits.BinTableHDU.from_columns([
    fits.Column(name='VALUE', format='1024E', unit='-       ', array=full)
  ])

  hdr = hdu2.header
  hdr.append(('COMMENT',  'HEALPIX pixelisation'),                                        bottom=True)
  hdr.append(('ORDERING', 'RING    ',    'Pixel ordering scheme'),                        bottom=True)
  hdr.append(('COORDSYS', 'C       ',    'Ecliptic, Galactic or Celestial (equatorial)'), bottom=True)
  hdr.append(('NSIDE',    nside,         'nside of the pixel'),                           bottom=True)
  hdr.append(('FIRSTPIX', 0,             'First pixel # (0 based)'),                      bottom=True)
  hdr.append(('LASTPIX',  12*nside**2-1, 'Last pixel # (0 based)'),                       bottom=True)
  hdr.append(('INDXSCHM', 'IMPLICIT',    'Indexing: IMPLICIT or EXPLICIT'),               bottom=True)

  fits.HDUList([hdu1, hdu2]).writeto(name, overwrite=True)
  if verbose == True:
    print('Saved \"{}\"'.format(name))
  return

def fullMapToPatch(full, nside_pat, patch, nest=False):
  nside_pix = hp.npix2nside(full.size)
  resol = nside_pix // nside_pat
  pat_nest = patch if nest == True else hp.ring2nest(nside_pat, patch)

  ## Cartesian to ring
  ind = resolToLocalNest(resol)
  ind += pat_nest * resol * resol
  ind = hp.nest2ring(nside_pix, ind)

  data = full[ind]
  return data

def loadPatchFromFullMap(name, nside_pat, patch, nest=False, verbose=True):
  full = loadFitsFullMap(name, verbose=verbose)
  data = fullMapToPatch(full, nside_pat, patch, nest=nest)
  return data

def increaseResolution(full1, nside2):
  nside1 = hp.npix2nside(full1.size)
  if nside1 >= nside2:
    print('Resolution is already high enough; do nothing')
    return full1

  nb_pix_2 = 12 * nside2 * nside2
  pix2 = np.arange(nb_pix_2, dtype=np.int64)
  pix1 = pixelToPatch(nside1, nside2, pix2)
  del pix2
  full2 = full1[pix1]
  del pix1
  return full2

def printAreaFromFullMap(name):
  full = loadFitsFullMap(name)
  full = np.fmin(full, 1)
  nside = hp.npix2nside(full.size)
  area = full.sum() * nsideToDegSq(nside)
  print('Area = {:f} [deg^2]'.format(area))
  return

## Taken from the function alm_getidx from healpy _sphtools.pyx, written in cython
def getAlmIndex(l_max, l, m):
  return m*(2*l_max+1-m)//2+l

def saveNpyAlmFromMap(name_in, name_out, l_max, verbose=True):
  full = loadFitsFullMap(name_in, verbose=verbose)
  alm = hp.map2alm(full, lmax=l_max, iter=1, pol=False, use_weights=True)
  np.save(name_out, alm)
  if verbose == True:
    print('Saved \"{}\"'.format(name_out))
  return

def saveFitsMapFromAlm(name_in, name_out, nside, verbose=True):
  alm = np.load(name_in)
  data = hp.alm2map(alm, nside, pol=False, verbose=False)
  if verbose == True:
    saveFitsFullMap(name_out, data, verbose=verbose)
  return

def kappaToGamma(kappa):
  nside = hp.npix2nside(kappa.size)
  l_max = 3 * nside - 1
  a_lm  = hp.map2alm(kappa, lmax=l_max, iter=1, pol=False, use_weights=True)

  for l in range(0, 2):
    for m in range(0, l+1):
      ind = getAlmIndex(l_max, l, m)
      a_lm[ind] = 0.0

  for l in range(2, l_max+1):
    factor = -np.sqrt((l + 2.0) * (l - 1.0) / (l * (l + 1.0)))
    for m in range(0, l+1):
      ind = getAlmIndex(l_max, l, m)
      a_lm[ind] *= factor

  b_lm  = np.zeros_like(a_lm, dtype=complex)
  gamma = hp.alm2map_spin([a_lm, b_lm], nside, 2, l_max, mmax=l_max)
  return gamma

## End of file
################################################################################
