import os
from astropy.io import fits
#import def_read_STSCI
#base_directory = os.environ['LMC_WINDS']
#data_directory = os.path.join(base_directory,'Data','HST','dr5','')
#file = ''

def read_STSCI(directory='',file=''):
	"""
    This definition reads in the header information from the STSCI fits files from the ULLYSES program
    Parameters
    ----------
    file :Insert the name of the file from which you want to extract data from
    Returns
    -------
    STSCI_info : dictionary
        This dictionary holds the wavelengths, fluxes, flux errors, target name, ra, dec, instrument, and diffraction grating for the STSCI
        file. You can access a specific value in the dictionary by read_STSCI('hlsp_ullyses_fuse_fuv_bi173_lwrs_dr5_cspec.fits')['RA'] which 
        returns the RA.

    Example on How to Run Code
    --------------------------
    read_STSCI('hlsp_ullyses_fuse_fuv_bi173_lwrs_dr5_cspec.fits') 
    This will return the whole dictionary 

    Written by April Horton 10/17/2022

    """

	STSCI_info = dict()
	spectrum = fits.open(directory+file)
	wl=spectrum[1].data['WAVELENGTH'][0]
	STSCI_info['WAVELENGTH'] = wl

	flux=spectrum[1].data['FLUX'][0]
	STSCI_info['FLUX'] = flux

	flux_err=spectrum[1].data['ERROR'][0]
	STSCI_info['FLUXERR'] = flux_err


	return STSCI_info




#print(read_STSCI('hlsp_ullyses_fuse_fuv_bi173_lwrs_dr5_cspec.fits')['RA'])
