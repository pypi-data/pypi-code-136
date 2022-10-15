
    ########################
    ##  cosmo.py          ##
    ##  Chieh-An Lin      ##
    ##  2022.10.15        ##
    ########################

## Python

## Third party
import numpy as np
import scipy as sp
import astropy.io.fits as fits

## Custom
import pylinc.core as cf

################################################################################
## Constants

LIGHT_SPEED        = 299792458.                         ## [m/s]
CRITICAL_DENSITY   = 2.7753619786618317e+11             ## [M_sol h^2 / Mpc^3]
HUBBLE_DISTANCE    = 2997.92458                         ## [Mpc/h] LIGHT SPEED is in [m/s], so we should write H_0 in 100000 h [m/s/Mpc]
FOUR_PI_G_OVER_C2  = 6.0135402045290702e-19             ## [Mpc / M_sol]
FULL_SKY           = 4 * np.pi * cf.RADIAN_TO_DEGREE**2 ## [deg^2]

################################################################################
## Functions - cosmological calculations

def E_sq_of_z(z):
  return 0.72 + 0.28 * (1.0+z)**3

def E_sq_of_z_2(param, z):
  return param.Omega_de + param.Omega_m * (1+z)**3

def E_of_z(z):
  return np.sqrt(E_sq_of_z(z))

def E_of_z_2(param, z):
  return np.sqrt(E_sq_of_z_2(param, z))

def dw_over_dz(z):
  return HUBBLE_DISTANCE / E_of_z(z)

def dw_over_dz_2(param, z):
  return HUBBLE_DISTANCE / E_of_z_2(param, z)

def comovDist(z):
  integrand = lambda x: 1.0 / E_of_z(x)
  value = sp.integrate.quad(integrand, 0, z)
  return HUBBLE_DISTANCE * value[0]

def comovDist2(param, z):
  integrand = lambda x: 1.0 / E_of_z_2(param, x)
  value = sp.integrate.quad(integrand, 0, z)
  return HUBBLE_DISTANCE * value[0]

def comovVol(z, dz, area):
  w = comovDist(z)
  dv = w**2 * area * dz * dw_over_dz(z)
  return dv

def comovVol2(param, z, dz, area):
  w  = comovDist2(param, z)
  dv = w**2 * area * dz * dw_over_dz_2(param, z)
  return dv

def growthFct(z):
  integrand = lambda x: 1.0 / (x * E_of_z(1.0/x-1.0))**3.0
  value = sp.integrate.quad(integrand, 0, 1.0/(1.0+z)) ## Integrate over a
  return 2.5 * 0.28 * E_of_z(z) * value[0]

def growthFct2(P, z):
  integrand = lambda x: 1.0 / (x * E_of_z_2(P, 1.0/x-1.0))**3.0
  value = sp.integrate.quad(integrand, 0, 1.0/(1.0+z)) ## Integrate over a
  return 2.5 * P.Omega_m * E_of_z_2(P, z) * value[0]

def thetaToK(z, theta):
  w = comovDist(z)
  k = cf.TWO_PI / (w * theta * cf.ARCMIN_TO_RADIAN)
  print('At z = {:f}: {:f} arcmin = {:f} h/Mpc'.format(z, theta, k))
  return

def kToTheta(z, k):
  w = comovDist(z)
  theta = cf.TWO_PI / (k * w) * cf.RADIAN_TO_ARCMIN
  print('At z = {:f}: {:f} h/Mpc = {:f} arcmin'.format(z, k, theta))
  return

################################################################################
## Functions - FITS

"""
def saveFitsBinTable(RADEC):
  hdu_1 = fits.PrimaryHDU()
  hdu_2 = fits.BinTableHDU.from_columns([
    fits.Column(name='RA',  format='E', unit='deg     ', array=RADEC[0]),
    fits.Column(name='DEC', format='E', unit='deg     ', array=RADEC[1])
  ])
  name = 'randCat_type0.fits'
  fits.HDUList([hdu_1, hdu_2]).writeto(name, overwrite=True)
  print('Saved \"{}\"'.format(name))
"""

def renameColumns(name_in, name_out, col_list_old, col_list_new):
  """
  Rename columns and output new file.
  """
  hdr  = fits.getheader(name_in, 1)
  data = fits.getdata(name_in, 1)

  for i, col_old in enumerate(col_list_old):
    data.columns.change_name(col_old, col_list_new[i])

  nb_rows = data.size
  hdu_1 = fits.PrimaryHDU()
  hdu_2 = fits.BinTableHDU.from_columns(data.columns, header=hdr, nrows=nb_rows)

  fits.HDUList([hdu_1, hdu_2]).writeto(name_out, overwrite=True)
  print('Saved \"{}\"'.format(name_out))
  return

def combineTables(name_in_1, name_in_2, name_out):
  """
  Combine two tables with the same columns into one.
  """
  data1 = fits.getdata(name_in_1, 1)
  data2 = fits.getdata(name_in_2, 1)

  nb_rows = data1.size + data2.size
  hdr = fits.getheader(name_in_1, 1)
  hdu_1 = fits.PrimaryHDU()
  hdu_2 = fits.BinTableHDU.from_columns(data1.columns, header=hdr, nrows=nb_rows)

  for i in range(len(data1.columns)):
    hdu_2.data.field(i)[          :data1.size] = data1.field(i)
    hdu_2.data.field(i)[data1.size:nb_rows]     = data2.field(i)

  fits.HDUList([hdu_1, hdu_2]).writeto(name_out, overwrite=True)
  print('Saved \"{}\"'.format(name_out))
  return

def combineTables_list(name_list_in, name_out):
  """
  Combine two tables with the same columns into one.
  """
  nb_rows = [0]
  stock  = []

  for name in name_list_in:
    data = fits.getdata(name, 1)
    nb_rows.append(data.size)
    stock.append(data)

  nb_rows = np.cumsum(nb_rows)
  hdr = fits.getheader(name, 1)
  hdu_1 = fits.PrimaryHDU()
  hdu_2 = fits.BinTableHDU.from_columns(stock[0].columns, header=hdr, nrows=nb_rows[-1])

  for j in range(len(stock)):
    for i in range(len(stock[0].columns)):
      hdu_2.data.field(i)[nb_rows[j]:nb_rows[j+1]] = stock[j].field(i)

  fits.HDUList([hdu_1, hdu_2]).writeto(name_out, overwrite=True)
  print('Saved \"{}\"'.format(name_out))
  return

def divideTable(name, name_out_1, name_out_2, fct_ind):
  """
  Divide a table into two with different number of rows.
  """
  hdr = fits.getheader(name, 1)
  data = fits.getdata(name, 1)

  ind = fct_ind(data)
  data_1 = data[ind]
  data_2 = data[~ind]
  nb_row_1 = data_1.size
  nb_row_2 = data_2.size

  hdr_2 = hdr.copy()
  hdu_1 = fits.PrimaryHDU()
  hdu_2 = fits.BinTableHDU.from_columns(data_1.columns, header=hdr, nrows=nb_row_1)
  hdu_3 = fits.BinTableHDU.from_columns(data_2.columns, header=hdr_2, nrows=nb_row_2)

  for i in range(len(data_1.columns)):
    hdu_2.data.field(i)[:nb_row_1] = data_1.field(i)
    hdu_3.data.field(i)[:nb_row_2] = data_2.field(i)

  fits.HDUList([hdu_1, hdu_2]).writeto(name_out_1, overwrite=True)
  print('Saved \"{}\"'.format(name_out_1))

  fits.HDUList([hdu_1, hdu_3]).writeto(name_out_2, overwrite=True)
  print('Saved \"{}\"'.format(name_out_2))
  return

def mergeTables(name_in_1, name_in_2, name_out):
  """
  Merge two tables with the same number of rows into one.
  """
  hdr_1 = fits.getheader(name_in_1, 1)
  hdr_2 = fits.getheader(name_in_2, 1)
  data_1 = fits.getdata(name_in_1, 1)
  data_2 = fits.getdata(name_in_2, 1)

  #TODO How to merge headers?
  nb_rows = data_1.size
  merged_col = data_1.columns + data_2.columns

  hdu_1 = fits.PrimaryHDU()
  hdu_2 = fits.BinTableHDU.from_columns(merged_col, header=hdr_1, nrows=nb_rows)

  fits.HDUList([hdu_1, hdu_2]).writeto(name_out, overwrite=True)
  print('Saved \"{}\"'.format(name_out))
  return

def splitTable(name_in, name_out_1, name_out_2):
  """
  Split a table into two with different columns.
  """
  print('To be implemented') #TODO
  return

## End of file
################################################################################
