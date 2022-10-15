
    ########################
    ##  core.py           ##
    ##  Chieh-An Lin      ##
    ##  2022.10.15        ##
    ########################

## Python
import json
import datetime as dtt
import calendar as cld
import collections as clt
import platform

## Third party
import numpy as np
import scipy as sp
import pandas as pd

## Custom

################################################################################
## Constants

HALF_PI            = 1.5707963267948966
TWO_PI             = 6.2831853071795865
FOUR_PI            = 12.566370614359172
FOUR_PI_OVER_THREE = 4.1887902047863909
PI_SQ              = 9.8696044010893586
PI_INV             = 0.31830988618379067

DEGREE_TO_RADIAN   = np.pi / 180.0
RADIAN_TO_DEGREE   = 180.0 / np.pi
ARCMIN_TO_RADIAN   = DEGREE_TO_RADIAN / 60.0
RADIAN_TO_ARCMIN   = RADIAN_TO_DEGREE * 60.0

EPS_NUM = 1e-12

################################################################################
## Configuration name

bird_tag = [
  'anser', 'buceros', 'corvus', 'diomedea', 'egretta',
  'falco', 'gallus', 'hirundo', 'icterus', 'jacana',
  'larus', 'milvus', 'numida', 'oriolus', 'pavo',
  'raphus', 'strix', 'turdus', 'upupa', 'vultur',
  'zosterops'
]

################################################################################
## Class - table

class Table:
  def __str__(self):
    return str(self.data)

  def __getitem__(self, ind):
    return self.data.iloc[ind]

  def getCol(self, col):
    return self.data[col].values

  def getColList(self):
    return list(self.data.columns)

  def getNbRows(self):
    return self.data.shape[0]

  def getNbCol(self):
    return self.data.shape[1]

  def selectEqual(self, col, value):
    ind = self.getCol(col) == value
    return self[ind]

  def reduce(self, col, value):
    ind = self.getCol(col) == value
    self.data = self.data[ind]
    return

################################################################################
## Functions - I/O

def loadAscii(name, sep=None, cmt='#', verbose=True):
  """
  Load a space-separated table in ASCII format.

  Parameters
  ----------
  name : str
    Path of the file to load.
  sep : str, optional
    Character for sepearation. (default: None)
  cmt : str, optional
    Character for comments. (default: '#')
  verbose : bool, optional
    Print message out or not. (default: True)

  Returns
  -------
  array_like
    Loaded table whose dimension is presented as (column, row).
  """
  data = np.loadtxt(name, comments=cmt, delimiter=sep)
  if verbose:
    print('Loaded \"{}\"'.format(name))
  return data.T

def saveAscii(name, data, verbose=True):
  """
  Save a space-separated table in ASCII format.

  Parameters
  ----------
  name : str
    Path to save the file.
  data : array_like
    Table to save whose dimension is (row, column).
  verbose : bool
    Print message out or not.

  Returns
  -------
  None
  """
  f = open(name, 'w')

  for row in data:
    for value in row:
      f.write(' {: e} '.format(value))
    f.write('\n')
  f.close()

  if verbose:
    print('Saved \"{}\"'.format(name))
  return

def loadNpy(name, verbose=True, **kwargs):
  """
  Load a file in NumPy format.

  Parameters
  ----------
  name : str
    Path of the file to load.
  verbose : bool, optional
    Print message out or not. (default: True)
  kwargs : dict
    Other keyword arguments.

  Returns
  -------
  data : NumPy object
    Loaded data.
  """
  try:
    data = np.load(name, **kwargs)
  except ValueError:
    try:
      data = np.load(name, allow_pickle=True, **kwargs).item()
    except ValueError:
      data = np.load(name, allow_pickle=True, **kwargs)

  if verbose:
    print('Loaded \"{}\"'.format(name))
  return data

def saveNpy(name, data, verbose=True, **kwargs):
  """
  Save a file in NumPy format.

  Parameters
  ----------
  name : str
    Path to save the file.
  data : object
    Any NumPy object.
  verbose : bool
    Print message out or not.
  kwargs : dict
    Other keyword arguments.

  Returns
  -------
  None
  """
  np.save(name, data, **kwargs)
  if verbose:
    print('Saved \"{}\"'.format(name))
  return

def loadCsv(name, verbose=True, **kwargs):
  """
  Load a file in csv format.

  Parameters
  ----------
  name : str
    Path of the file to load.
  verbose : bool, optional
    Print message out or not. (default: True)
  kwargs : dict
    Other keyword arguments.

  Returns
  -------
  data : Pandas DataFrame
    Loaded data.
  """
  if 'dtype' not in kwargs:
    kwargs['dtype'] = {}
  if 'sep' not in kwargs:
    kwargs['sep'] = ','
  if 'comment' not in kwargs:
    kwargs['comment'] = '#'
  if 'skipinitialspace' not in kwargs:
    kwargs['skipinitialspace'] = True
  if 'encoding' not in kwargs:
    kwargs['encoding'] = 'utf-8'

  data = pd.read_csv(name, **kwargs)
  if verbose:
    print('Loaded \"{}\"'.format(name))
  return data

def saveCsv(name, data, is_df=True, verbose=True, **kwargs):
  """
  Save a file in csv format.

  Parameters
  ----------
  name : str
    Path to save the file.
  data : dict or Pandas DataFrame
    Data to save.
  is_df : bool
    ``data`` is already a Pandas DataFrame or not.
  verbose : bool
    Print message out or not.
  kwargs : dict
    Other keyword arguments.

  Returns
  -------
  None
  """
  if not is_df:
    data = pd.DataFrame(data)
  if 'index' not in kwargs:
    kwargs['index'] = False

  data.to_csv(name, **kwargs)
  if verbose:
    print('Saved \"{}\"'.format(name))
  return

def loadJson(name, verbose=True):
  """
  Load a file in json format.

  Parameters
  ----------
  name : str
    Path of the file to load.
  verbose : bool, optional
    Print message out or not. (default: True)

  Returns
  -------
  data : dict
    Loaded data presented as a dictionary.
  """
  file_ = open(name, 'r')
  data = json.load(file_)
  file_.close()
  if verbose:
    print('Loaded \"{}\"'.format(name))
  return data

def loadJsonAsTable(name, verbose=True, **kwargs):
  """
  Load a table in json format.

  Parameters
  ----------
  name : str
    Path of the file to load.
  verbose : bool, optional
    Print message out or not. (default: True)
  kwargs : dict
    Other keyword arguments.

  Returns
  -------
  data : Pandas DataFrame
    Loaded table as a data frame.
  """
  if 'dtype' not in kwargs:
    kwargs['dtype'] = {}
  if 'encoding' not in kwargs:
    kwargs['encoding'] = 'utf-8'

  data = pd.read_json(name, **kwargs)
  if verbose:
    print('Loaded \"{}\"'.format(name))
  return data

def saveJson(name, data, verbose=True):
  """
  Save a file in json format.

  Parameters
  ----------
  name : str
    Path to save the file.
  data : dict
    Data to save.
  verbose : bool
    Print message out or not.

  Returns
  -------
  None
  """
  file_ = open(name, 'w')
  json.dump(data, file_)
  file_.close()
  if verbose:
    print('Saved \"{}\"'.format(name))
  return

def _getIndList_markdown(level, block):
  if level == 1:
    tag1 = '# '
    tag2 = '==='
  elif level == 2:
    tag1 = '## '
    tag2 = '---'
  elif level == 3:
    tag1 = '### '
  elif level == 4:
    tag1 = '#### '
  elif level == 5:
    tag1 = '##### '

  ind_list = []

  for i, line in enumerate(block):
    if len(line) >= len(tag1) and line[:len(tag1)] == tag1:
      ind_list.append((i, False))
    elif level <= 2 and len(line) >= 3 and line[:3] == tag2:
      ind_list.append((i-1, True))

  ind_list.append((len(block), False))
  if ind_list[0][0] > 0:
    ind_list = [(-1, False)] + ind_list
  return ind_list

def _getTitle_markdown(level, block, ind, variant=False):
  if ind < 0:
    return ''

  title = block[ind]
  if variant:
    title = title.strip()
  else:
    title = title[level:].strip()
  return title

def _cleanEmptyLines_markdown(block):
  count1 = 0
  count2 = len(block)
  while count1 < len(block) and block[count1] == '\n':
    count1 += 1
  while count2 > 0 and block[count2-1] == '\n':
    count2 -= 1
  return block[count1:count2]

def _recursive_markdown(level, block, clean=True):
  if level >= 6:
    return block

  ind_list = _getIndList_markdown(level, block)
  if len(ind_list) == 2 and ind_list[0][0] < 0:
    if clean:
      block2 = _cleanEmptyLines_markdown(block)
    return block2

  block_dict = {}
  for begin, end in zip(ind_list[:-1], ind_list[1:]):
    title = _getTitle_markdown(level, block, begin[0], variant=begin[1])
    b_ind = begin[0] + 1 + int(begin[1])
    e_ind = end[0]
    block2 = _recursive_markdown(level+1, block[b_ind:e_ind], clean=clean)
    if title != '' or block2 != []:
      block_dict[title] = block2
  return block_dict

def loadMarkdown(name, verbose=True):
  """
  Load a file in markdown format.

  Parameters
  ----------
  name : str
    Path of the file to load.
  verbose : bool, optional
    Print message out or not. (default: True)

  Returns
  -------
  data : dict
    Loaded data.
  """
  f = open(name, 'r')
  stock = [line for line in f]
  f.close()

  data = _recursive_markdown(1, stock)

  if verbose:
    print('Loaded \"{}\"'.format(name))
  return data

################################################################################
## Functions - time

def printTime(start, stop):
  duration = stop - start
  hours = int(duration / 3600.0)
  remain = duration % 3600.0
  minutes = int(remain / 60.0)
  seconds = remain % 60.0

  if hours == 0:
    if minutes == 0:
      print('Computation time = {:.2f} secs'.format(duration))
    else:
      print('Computation time = {:d} m {:d} s'.format(minutes, int(seconds)))
  else:
    print('Computation time = {:d} h {:d} m {:d} s'.format(hours, minutes, int(seconds)))
  return

def printTime_str(start, stop, string):
  duration = stop - start
  hours = int(duration / 3600.0)
  remain = duration % 3600.0
  minutes = int(remain / 60.0)
  seconds = remain % 60.0

  if hours == 0:
    if minutes == 0:
      print('{} time = {:.2f} secs'.format(string, duration))
    else:
      print('{} time = {:d} m {:d} s'.format(string, minutes, int(seconds)))
  else:
    print('{} time = {:d} h {:d} m {:d} s'.format(string, hours, minutes, int(seconds)))
  return

################################################################################
## Functions - environment

def getPythonVersion():
  return platform.python_version()

def getUserName():
  import getpass
  return getpass.getuser()

def getHostName():
  return platform.node()

################################################################################
## Functions - handy conversion

def asFloat(a, copy=True):
  if np.isscalar(a):
    return float(a)
  if type(a) is list:
    return np.array(a, dtype=float)
  return a.astype(float, copy=copy)

def asInt(a, copy=True):
  if np.isscalar(a):
    return int(a)
  if type(a) is list:
    return np.array(a, dtype=int)
  return a.astype(int, copy=copy)

def celesToSphe(ra, dec=None):
  if dec is None:
    dec = ra[1]
    ra  = ra[0]
  theta = (90 - dec) * DEGREE_TO_RADIAN
  phi   = ra * DEGREE_TO_RADIAN
  return np.array([theta, phi])

def spheToCeles(theta, phi=None):
  if phi is None:
    phi = theta[1]
    theta  = theta[0]
  ra  = phi * RADIAN_TO_DEGREE
  dec = 90 - theta * RADIAN_TO_DEGREE
  return np.array([ra, dec])

def adjustRA(ra, half=180.0, sign=0):
  """
  Adjust the range of values of RA.

  Parameters
  ----------
  RA : float or float array
    Right ascension.
  half : float
    Half of the range of angle values.
  sign : int
    -1 = adjust RA to [-2*half, 0[
     0 = adjust RA to [-half, half[
     1 = adjust RA to [0, 2*half[
  """
  if sign > 0:
    return ra % (2.0*half)
  if sign < 0:
    return ra % (2.0*half) - 2.0*half
  return (ra + half) % (2.0*half) - half

def rotate_2D(theta_x, theta_y=None, rot_ang=0.0):
  """
  Rotate points in a 2-D plane

  Parameters
  ----------
  theta_x : (1, N) or (2, N) float array
    x positions or (x, y) positions.
  theta_y : (1, N) float array, optional
    y positions.
  rotAng : float, optional
    Rotation angle in degree.

  Returns
  -------
  thetaXY : (2, N) float array
    New (x, y) positions.
  """
  if theta_y is None:
    theta_y = theta_x[1]
    theta_x = theta_x[0]
  rot_ang = rot_ang * DEGREE_TO_RADIAN
  rotMat = np.array([[np.cos(rot_ang), -np.sin(rot_ang)], [np.sin(rot_ang), np.cos(rot_ang)]])
  thetaXY = rotMat.dot([theta_x, theta_y])
  return thetaXY

def pairIndex(n, i, j):
  ind = (n + (n+1-i)) * i // 2
  ind += j - i
  return ind

def singleIndexToPair(n, ind):
  remain = ind
  row = n
  i = 0
  while remain >= row:
    remain -= row
    row -= 1
    i += 1
  j = remain + i
  return i, j

################################################################################
## Functions - date conversion

def ISODateToOrd(iso):
  return dtt.date.fromisoformat(iso).toordinal()

def ordDateToISO(ord_):
  return dtt.date.fromordinal(ord_).isoformat()

def DDMMYYYYSlashToOrd(ddmmyyyy_slash):
  split = [int(str_) for str_ in ddmmyyyy_slash.split('/')]
  return dtt.date(split[2], split[1], split[0]).toordinal()

def ordDateToDDMMYYYYSlash(ord_):
  date = dtt.date.fromordinal(ord_)
  return '{:02d}/{:02d}/{:04d}'.format(date.day, date.month, date.year)

def YYYYMMDDDotToOrd(yyyymmdd_dot):
  iso = yyyymmdd_dot.replace('.', '-')
  return ISODateToOrd(iso)

def ordDateToYYYYMMDDDot(ord_):
  date = dtt.date.fromordinal(ord_)
  return '{:04d}.{:02d}.{:02d}'.format(date.year, date.month, date.day)

def ordDateToMMMD(ord_):
  date = dtt.date.fromordinal(ord_)
  return '{} {:d}'.format(numMonthToAbbr(date.month), date.day)

def DDMMYYYYSlashToISO(ddmmyyyy_slash):
  split = [int(str_) for str_ in ddmmyyyy_slash.split('/')]
  return '{:04d}-{:02d}-{:02d}'.format(split[2], split[1], split[0])

################################################################################
## Functions - month & day conversion

def numMonthToAbbr(num):
  return cld.month_abbr[num]

def numMonthToFull(num):
  return cld.month_name[num]

def abbrMonthToNum(abbr):
  dict_ = {v: k for k, v in enumerate(cld.month_abbr)}
  return dict_[abbr]

def abbrMonthToFull(abbr):
  dict_ = {v: k for k, v in enumerate(cld.month_abbr)}
  full = numMonthToFull(dict_[abbr])
  return full

def fullMonthToNum(full):
  dict_ = {v: k for k, v in enumerate(cld.month_name)}
  return dict_[full]

def fullMonthToAbbr(full):
  dict_ = {v: k for k, v in enumerate(cld.month_name)}
  abbr = numMonthToAbbr(dict_[full])
  return abbr

def numWeekdayToAbbr(num):
  return cld.day_abbr[num]

def numWeekdayToFull(num):
  return cld.day_name[num]

def abbrWeekdayToNum(abbr):
  dict_ = {v: k for k, v in enumerate(cld.day_abbr)}
  return dict_[abbr]

def abbrWeekdayToFull(abbr):
  dict_ = {v: k for k, v in enumerate(cld.day_abbr)}
  full = numWeekdayToFull(dict_[abbr])
  return full

def fullWeekdayToNum(full):
  dict_ = {v: k for k, v in enumerate(cld.day_name)}
  return dict_[full]

def fullWeekdayToAbbr(full):
  dict_ = {v: k for k, v in enumerate(cld.day_name)}
  abbr = numWeekdayToAbbr(dict_[full])
  return abbr

################################################################################
## Functions - histogram

def centerOfBins(bins, area=False):
  bins = np.array(bins, dtype=float)
  left = bins[:-1]
  right = bins[1:]
  if area is True:
    return np.sqrt(0.5 * (left**2 + right**2))
  return 0.5 * (left + right)

def makeHist(data, bins, wgt=None, factor=1.0, pdf=False):
  """
  Make the histogram such that the output can be plotted directly.

  Parameters
  ----------
  data : array-like

  bins : (1, N) float array
    Bin edges.

  factor : float, optional
    Rescaling factor for the histogram.

  pdf : bool, optional
    Make the output a pdf, i.e. normalized by the binwidth & the total counts.

  Returns
  -------
  n_arr : (1, N) float array
    Number counts, could be rescaled.

  ctr_bins : (1, N) float array
    Center of the bins.
    n_arr & ctr_bins have the same size.
  """
  n_arr, bins = np.histogram(data, bins, weights=wgt)
  ctr_bins = centerOfBins(bins)

  if pdf == True:
    n_arr = asFloat(n_arr) / (float(sum(n_arr)) * (bins[1:] - bins[:-1]))
  else:
    n_arr = asFloat(n_arr) * factor

  return n_arr, ctr_bins

def pdfToCdf(x_arr, pdf):
  dx  = x_arr[1] - x_arr[0]
  cdf = 0.5 * dx * (pdf[1:] + pdf[:-1])
  cdf = np.cumsum(cdf)
  cdf = np.insert(cdf, 0, 0.0)
  cdf /= cdf[-1]
  return cdf

def histToCdf(n_arr):
  cdf = np.cumsum(n_arr)
  cdf = np.insert(cdf, 0, 0.0)
  cdf /= cdf[-1]
  return cdf

def cdfToPdf(x_cdf, cdf, x_pdf):
  dx_pdf = x_pdf[1] - x_pdf[0]
  pdf_bins = np.insert(x_pdf, 0, x_pdf[0]-dx_pdf) + 0.5*dx_pdf
  import scipy.interpolate as itp
  inter = itp.interp1d(x_cdf, cdf, bounds_error=False, fill_value=(0.0, 1.0))
  pdf = inter(pdf_bins)
  pdf = pdf[1:] - pdf[:-1]
  pdf /= np.sum(pdf) * dx_pdf
  return pdf

def cdfToHist(x_arr, cdf, bins):
  import scipy.interpolate as itp
  inter = itp.interp1d(x_arr, cdf, bounds_error=False, fill_value=(0.0, 1.0))
  n_arr = inter(bins)
  n_arr = n_arr[1:] - n_arr[:-1]
  return n_arr

def pdfToHist(x_arr, pdf, bins):
  cdf = pdfToCdf(x_arr, pdf)
  n_arr = cdfToHist(x_arr, cdf, bins)
  return n_arr

def histToPdf(bins, n_arr, x_arr):
  cdf = histToCdf(n_arr)
  pdf = cdfToPdf(bins, cdf, x_arr)
  return pdf

def makeNewPdf(x_arr_1, pdf_1, x_arr_2):
  cdf = pdfToCdf(x_arr_1, pdf_1)
  pdf_2 = cdfToPdf(x_arr_1, cdf, x_arr_2)
  return pdf_2

def makeNewHist(bins_1, n_arr_1, bins_2):
  cdf = histToCdf(n_arr_1)
  n_arr_2 = cdfToHist(bins_1, cdf, bins_2)
  return n_arr_2

def makeDiscreteHist(value_list):
  value_hist = clt.Counter(value_list)
  value_hist = sorted(value_hist.items(), key=lambda t: t[1], reverse=True)
  return value_hist

################################################################################
## Functions - grid

def XYToGrid(x_arr, y_arr):
  """
  Create a mesh grid from x and y axes.

  Parameters
  ----------
  x_arr : (1, N) float array
    x-axis of the grid.

  y_arr : (1, N) float array
    y-axis of the grid.

  Returns
  -------
  grid : (2, N) float array
    grid[0] = x-coordinates of the mesh grid.
    grid[1] = y-coordinates of the mesh grid.
  """
  x_mat, y_mat = np.meshgrid(x_arr, y_arr)
  grid = np.array([x_mat.flatten(), y_mat.flatten()])
  return grid

def limitsToGrid(x_min, x_max=None, dx=None, y_min=None, y_max=None, dy=None, pixel=True):
  """
  Create a mesh grid from interval parameters.

  Parameters
  ----------
  x_min : float or float sequence
    If float, lower limit of the grid along the x-axis.
    Otherwise, a sequence of size 3 or 6 containing (x_min, x_max, dx) or (x_min, x_max, dx, y_min, y_max, dy).

  x_max : float, optional
    Upper limit of the grid along the x-axis.

  dx : float, optional
    Gap of the grid along the x-axis.

  y_min : float, optional
    Lower limit of the grid along the y-axis.

  y_max : float, optional
    Upper limit of the grid along the y-axis.

  dy : float, optional
    Gap of the grid along the y-axis.

  pixel : bool, optional
    If True, return the center of pixels of the grid.
    Otherwise, return the vertices of the grid.

  Returns
  -------
  x_arr : (1, N) float array
    x-axis of the grid.

  y_arr : (1, N) float array
    y-axis of the grid.

  grid : (2, N) float array
    grid[0] = x-coordinates of the mesh grid.
    grid[1] = y-coordinates of the mesh grid.
  """
  if dx is None:
    if len(x_min) == 6:
      return limitsToGrid(x_min[0], x_min[1], x_min[2], x_min[3], x_min[4], x_min[5], pixel=pixel)
    return limitsToGrid(x_min[0], x_min[1], x_min[2], x_min[0], x_min[1], x_min[2], pixel=pixel)

  y_min = x_min if y_min is None else y_min
  y_max = x_max if y_max is None else y_max
  dy = dx if dy is None else dy

  if pixel is True:
    x_arr = np.arange(x_min+0.5*dx, x_max, dx)
    y_arr = np.arange(y_min+0.5*dy, y_max, dy)
  else:
    x_arr = np.arange(x_min, x_max+dx*EPS_NUM, dx)
    y_arr = np.arange(y_min, y_max+dy*EPS_NUM, dy)

  grid = XYToGrid(x_arr, y_arr)
  return x_arr, y_arr, grid

################################################################################
## Functions - sampling

def jackknife(fct, data):
  n = data.shape[0]
  x_0 = fct(data)

  ind_list = ~np.diag(np.ones(n, dtype=bool))
  x_list = [fct(data[ind]) for ind in ind_list]
  x_list = np.array(x_list)

  err = np.sum((x_list - x_0)**2, axis=0) * (n-1) / n
  err = np.sqrt(err)
  return err

def sampleWithRate(size, rate):
  p = np.random.rand(size)
  ind = p < rate
  return ind

def sampleExactNumber(size, nb):
  n = np.random.choice(size, nb)
  ind = np.zeros(size, dtype=bool)
  ind[n] = True
  return ind

## A good example to keep
## def sampleExactNumber(size, nb):
##   p = np.random.rand(size)
##   t = np.sort(p)[nb]
##   ind = p < t
##   return ind

################################################################################
## Notes - KDE

"""
  ## Setup testing data
  n = 200
  d = 2
  factor = (n * (d + 2) / 4.)**(-1. / (d + 4))
  np.random.seed(142857)
  x = np.random.randn(n)
  y = np.random.randn(n) * 0.25
  data = np.array([x, y])

  ## Make grid
  x_range = [-3, 3, 0.02]
  y_range = [-3, 3, 0.02]
  x_arr, y_arr, grid = cf.limitsToGrid(x_range[0], x_range[1], x_range[2], y_range[0], y_range[1], y_range[2], pixel=True)

  ## Anisotropic solution - scipy
  import scipy.stats as stats
  factor = (n * (d + 2) / 4.)**(-1. / (d + 4))
  kde_1 = sp.stats.gaussian_kde(data, bw_method='silverman')
  kde_2 = sp.stats.gaussian_kde(data, bw_method=factor)

  ## kde_1(grid) & kde_2(grid) agree
  ## bandwidth = factor * std
  ## data.shape = (d, n)

  ## Isotropic solution - sklearn
  import sklearn.neighbors as ngb
  kde_3 = ngb.KernelDensity(bandwidth=factor*std, kernel='gaussian')
  kde_3.fit(data.T) or kde_3.fit(data[:, np.newaxis])

  ## factor*std is bandwidth with std
  ## kde_1(x) & kde_2(x) & np.exp(kde_3.score_samples(data.T)) agree if the data are isotropic

  ## If you want to customize bandwidth without std, use kde_2.
  ## If you want to customize bandwidth with std, use kde_3.

  ## Weighting
  kde_2 = sp.stats.gaussian_kde(data, bw_method=factor, weights=wgt)
  kde_3.fit(data.T, sample_weight=wgt)

  ## Ways to customize bandwidth:
  ## kde_4 = ngb.KernelDensity(bandwidth=factor*s, kernel='gaussian')
  ## kde_4.fit(data.T)
  ## kde_5 = sp.stats.gaussian_kde(data, bw_method=factor)
  ## kde_5.covariance *= s**2/std**2
  ## kde_5.inv_cov *= std**2/s**2
  ## kde_5._norm_factor *= s/std
"""

################################################################################
## Functions - norm and distance

def norm1_2D(x, y):
  return np.fabs(x) + np.fabs(y)

def norm_2D(x, y):
  return np.sqrt(x**2 + y**2)

def normSup_2D(x, y):
  return np.fmax(np.fabs(x), np.fabs(y))

def dist1_2D(x1, y1, x2, y2):
  return norm1_2D(x1-x2, y1-y2)

def dist_2D(x1, y1, x2, y2):
  return norm_2D(x1-x2, y1-y2)

def distSup_2D(x1, y1, x2, y2):
  return normSup_2D(x1-x2, y1-y2)

def norm_3D(x, y, z):
  return np.sqrt(x**2 + y**2 + z**2)

def dist_3D(x1, y1, z1, x2, y2, z2):
  return norm_3D(x1-x2, y1-y2, z1-z2)

def spheDist(ra_1, dec_1, ra_2, dec_2):
  """
  Parameters
  ----------
  RA1, DEC1, RA2, DEC2 : float or float array
    Equatorial coordinates in [deg].

  Returns
  -------
  dist : float or float array
    Spherical distance in [rad].
  """
  ra_rad_1 = ra_1  * DEGREE_TO_RADIAN
  dec_rad_1 = dec_1 * DEGREE_TO_RADIAN
  ra_rad_2 = ra_2  * DEGREE_TO_RADIAN
  dec_rad_2 = dec_2 * DEGREE_TO_RADIAN

  ## Compute the scalar product
  x = np.cos(ra_rad_1) * np.cos(dec_rad_1) * np.cos(ra_rad_2) * np.cos(dec_rad_2)
  y = np.sin(ra_rad_1) * np.cos(dec_rad_1) * np.sin(ra_rad_2) * np.cos(dec_rad_2)
  z = np.sin(dec_rad_1) * np.sin(dec_rad_2)
  scalar = np.fmin(1.0, x + y + z)
  dist = np.arccos(scalar)
  return dist

################################################################################
## Functions - reference change

def rotMat_3D(theta, phi, deg=True):
  """
  Get rotation matrix in 3D.

  Parameters
  ----------
  theta : float
    Polar angle.
  phi : float
    Azimuthal angle.
  deg : bool, optional
    Angles in [degree] or not. (default: True)

  Returns
  -------
  rot_mat : (3, 3) float array
    Rotation matrix.
  """
  if deg:
    theta *= DEGREE_TO_RADIAN
    phi *= DEGREE_TO_RADIAN

  cos_theta = np.cos(theta)
  sin_theta = np.sin(theta)
  cos_phi = np.cos(phi)
  sin_phi = np.sin(phi)

  rot_mat = np.array([[cos_phi, -sin_phi, 0], [sin_phi, cos_phi, 0], [0, 0, 1]])
  rot_mat = rot_mat.dot([[cos_theta, 0, sin_theta], [0, 1, 0], [-sin_theta, 0, cos_theta]])
  return rot_mat

def refChgMat_3D(vect):
  """
  Get reference change matrix given a polar vector.

  Parameters
  ----------
  vect : (3,) float array
    Polar vector of the new reference in the old coordinates.

  Returns
  -------
  ref_chg_mat : (3, 3) float array
    Reference change matrix.
  inv_ref_chg_mat :(3, 3) float array
    Inverse reference change matrix.
  """
  cos_theta = vect[2]
  sin_theta = np.sqrt(1 - cos_theta**2)
  if abs(sin_theta) < EPS_NUM:
    cos_phi = 1
    sin_phi = 0
  else:
    cos_phi = vect[0] / sin_theta
    sin_phi = vect[1] / sin_theta
  ref_chg_mat = np.array([[cos_phi, -sin_phi, 0], [sin_phi, cos_phi, 0], [0, 0, 1]])
  ref_chg_mat = ref_chg_mat.dot([[cos_theta, 0, sin_theta], [0, 1, 0], [-sin_theta, 0, cos_theta]])
  inv_ref_chg_mat = np.linalg.pinv(ref_chg_mat)
  return ref_chg_mat, inv_ref_chg_mat

def changeReference_3D(pt_arr, ctr, inv_ref_chg_mat):
  """
  Apply reference change to a point array.

  Parameters
  ----------
  pt_arr : (3, N) float array
    Point array to be applied.
  ctr : (3,) float array
    Center of the new reference in the old coordinates.
  inv_ref_chg_mat : (3, 3) float array
    Inverse reference change matrix.

  Returns
  -------
  new_pt_arr : (3, N) float array
    Coordinates of the point array in the new reference.
  """
  new_pt_arr = (pt_arr.T - ctr).T
  new_pt_arr = inv_ref_chg_mat.dot(new_pt_arr)
  new_pt_arr = (new_pt_arr.T + ctr).T
  return new_pt_arr

def rotateInAnotherRef_3D(pt_arr, ctr, ref_chg_mat, rot_mat):
  """
  Apply rotation to a point array in a different reference.

  Parameters
  ----------
  pt_arr : (3, N) float array
    Point array to be applied.
  ctr : (3,) float array
    Center of the new reference in the old coordinates.
  ref_chg_mat : (3, 3) float array
    Reference change matrix.
  rot_mat : (3, 3) float array
    Rotation matrix in the new reference.

  Returns
  -------
  new_pt_arr : (3, N) float array
    Coordinates of the point array in the new reference.
  """
  inv_ref_chg_mat = np.linalg.pinv(ref_chg_mat)

  new_pt_arr = (pt_arr.T - ctr).T
  new_pt_arr = inv_ref_chg_mat.dot(new_pt_arr)
  new_pt_arr = rot_mat.dot(new_pt_arr)
  new_pt_arr = ref_chg_mat.dot(new_pt_arr)
  new_pt_arr = (new_pt_arr.T + ctr).T
  return new_pt_arr

################################################################################
## Functions - likelihood

def NToOneMinusP(n_sigma):
  return sp.stats.norm.cdf(n_sigma) - sp.stats.norm.sf(n_sigma)

def NToP(n_sigma):
  return 2 * sp.stats.norm.sf(n_sigma)

def pToN(p_value):
  return sp.stats.norm.isf(0.5 * p_value)

def findLevel(like, n_sigma_list=[1, 2]):
  ind = np.isnan(like)
  pdf = like[~ind].flatten()
  pdf = np.sort(pdf, kind='mergesort')
  total = pdf.sum()
  pdf /= total

  cdf = np.insert(pdf.cumsum(), 0, 0)
  ind_list = np.arange(cdf.size)
  import scipy.interpolate as itp
  inter = itp.interp1d(cdf, ind_list, bounds_error=True) #, fill_value='extrapolate')
  level_list = []
  nb_list = []

  for n_sigma in n_sigma_list:
    target = 2 * sp.stats.norm.sf(n_sigma)
    ind = inter(target)
    level = pdf[int(ind)] * total - EPS_NUM
    level_list.append(level)
    nb_list.append(pdf.size-ind)
  return level_list, nb_list

def standardInterval(data, wgt=None):
  if wgt is None:
    mean = np.mean(data)
    std  = np.std(data, ddof=1)
  else:
    mean = np.average(data, weights=wgt)
    std  = np.sqrt(np.cov(data, ddof=1, aweights=wgt))
  return mean, std, std

def quantileInterval(data, wgt=None):
  sf1 = sp.stats.norm.sf(1)

  if wgt is None:
    quan_l = np.percentile(data, sf1*100)
    median = np.median(data)
    quan_u = np.percentile(data, (1-sf1)*100)

  else:
    perm = np.argsort(data, kind='mergesort')
    data_perm = data[perm]
    wgt_perm = wgt[perm]
    cum_wgt_perm = wgt_perm.cumsum()

    thres_l = cum_wgt_perm[-1] * sf1
    thres_c = cum_wgt_perm[-1] * 0.5
    thres_u = cum_wgt_perm[-1] * (1-sf1)

    ind_l1 = np.sum(cum_wgt_perm < thres_l)
    ind_l2 = np.sum(cum_wgt_perm <= thres_l)
    ind_c1 = np.sum(cum_wgt_perm < thres_c)
    ind_c2 = np.sum(cum_wgt_perm <= thres_c)
    ind_u1 = np.sum(cum_wgt_perm < thres_u)
    ind_u2 = np.sum(cum_wgt_perm <= thres_u)

    quan_l = 0.5 * (data_perm[ind_l1] + data_perm[ind_l2])
    median = 0.5 * (data_perm[ind_c1] + data_perm[ind_c2])
    quan_u = 0.5 * (data_perm[ind_u1] + data_perm[ind_u2])

  err_l = median - quan_l
  err_u = quan_u - median
  return median, err_l, err_u

def credibleInterval(data, grid=None, wgt=None):
  if grid is None:
    lower = data.min()
    upper = data.max()
    delta = upper - lower
    lower -= 0.05 * delta
    upper += 0.05 * delta
    grid = np.linspace(lower, upper, 5001)

  kernel = sp.stats.gaussian_kde(data, 'silverman', weights=wgt)
  like = kernel(grid)
  ind = like.argmax()
  max_ = grid[ind]

  level_list, _ = findLevel(like, [1]) ## 1 sigma
  level = level_list[0]
  stock = []

  for i in range(like.size-1):
    if (level - like[i]) * (level - like[i+1]) <= 0:
      r = (level - like[i]) / (like[i+1] - like[i])
      stock.append((i, r))

  if len(stock) % 2 != 0:
    print('Max position:', ind, ',', max_)
    print('Index positions:', stock)
    raise AssertionError('There might be some numerical errors in credibleInterval.')

  if len(stock) > 2:
    print('WARNING: not only one interval')
    stock2 = []
    for i, _ in enumerate(stock[:-1]):
      if (ind - stock[i][0]) * (ind - stock[i+1][0]) <= 0:
        stock2.append(stock[i])
        stock2.append(stock[i+1])
        break
  else:
    stock2 = stock

  cred  = [(1-r)*grid[i] + r*grid[i+1] for i, r in stock2]
  err_l = max_ - cred[0]
  err_u = cred[1] - max_
  return max_, err_l, err_u

def HPDInterval(data, post, wgt=None):
  if wgt is None:
    wgt = np.ones_like(data, dtype=float) / data.size
  sum_wgt = wgt.sum()
  threshold = 1 - 2*sp.stats.norm.sf(1) ## 0.68
  threshold *= sum_wgt

  ind  = np.argmax(post)
  max_ = data[ind]
  ind  = np.argsort(post)[::-1]

  for i in range(3, ind.size):
    ind_u    = ind[:i]
    lower_u  = data[ind_u].min()
    upper_u  = data[ind_u].max()
    sum_wgt_u = wgt[(lower_u <= data) & (data <= upper_u)].sum()

    if sum_wgt_u >= threshold:
      ind_l    = ind[:i-1]
      lower_l  = data[ind_l].min()
      upper_l  = data[ind_l].max()
      sum_wgt_l = wgt[(lower_l <= data) & (data <= upper_l)].sum()

      ## Interpolate between this sample and the last at the target coverage
      t = (threshold - sum_wgt_l) / (sum_wgt_u - sum_wgt_l)
      hpd_l  = (1-t) * lower_l + t * lower_u
      hpd_u  = (1-t) * upper_l + t * upper_u
      break

  err_l = max_ - hpd_l
  err_u = hpd_u - max_
  return max_, err_l, err_u

################################################################################
## Functions - wavelength

def wavelengthToRgb(wavelength, gamma=0.8):
  """
  http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
  """
  bool1 = (wavelength >= 380.0) * (wavelength < 440.0)
  bool2 = (wavelength >= 440.0) * (wavelength < 490.0)
  bool3 = (wavelength >= 490.0) * (wavelength < 510.0)
  bool4 = (wavelength >= 510.0) * (wavelength < 580.0)
  bool5 = (wavelength >= 580.0) * (wavelength < 645.0)
  bool6 = (wavelength >= 645.0) * (wavelength < 750.0)

  attenuation = bool1 * (0.3 + 0.7 * (np.fmax(wavelength, 380.0) - 380.0) / (440.0 - 380.0))\
              + bool6 * (0.3 + 0.7 * (750.0 - np.fmin(wavelength, 750.0)) / (750.0 - 645.0))

  r = bool1 * ((440.0 - np.fmin(wavelength, 440.0)) / (440.0 - 380.0) * attenuation) ** gamma\
    + bool4 * ((np.fmax(wavelength, 510.0) - 510.0) / (580.0 - 510.0)) ** gamma\
    + bool5 * 1.0\
    + bool6 * attenuation ** gamma

  g = bool2 * ((np.fmax(wavelength, 440.0) - 440.0) / (490.0 - 440.0)) ** gamma\
    + bool3 * 1.0\
    + bool4 * 1.0\
    + bool5 * ((645.0 - np.fmin(wavelength, 645.0)) / (645.0 - 580.0)) ** gamma

  b = bool1 * attenuation ** gamma\
    + bool2 * 1.0\
    + bool3 * ((510.0 - np.fmin(wavelength, 510.0)) / (510.0 - 490.0)) ** gamma

  a = (bool1 + bool2 + bool3 + bool4 + bool5 + bool6) * 1.0

  return np.array([r, g, b, a])

## End of file
################################################################################
