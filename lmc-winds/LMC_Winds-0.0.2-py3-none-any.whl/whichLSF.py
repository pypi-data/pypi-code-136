#
import numpy as np
from astropy import units as u
from astropy.io import fits
from astropy.time import Time

def which_lsf(file_name, rest_wave): 
    """
   This takes the HST spectrum in fits format, reads the header and print the useful information about the resolution, instrument,     and LSF, if applicable, corresponding to the line of interest
    file_name : input fits file    
    rest_wave : rest wavelength in Angstrom corresponding to the lines of interest (e.g., 1302.1685 for O I 1302)
  
    Returns
    -------
    Instrument ID, Filter ID, CENWAVE, Life Position 
    """
     
    #The moves to Lifetime Position 2 (LP2), Lifetime Position 3 (LP3), and Lifetime Position 4 (LP4) 
    #occurred on July 23, 2012, February 9, 2015, and October 2, 2017, respectively
    LP2 = Time('2012-07-23')
    LP3 = Time('2015-02-09')
    LP4 = Time('2017-10-02')
    LP2.format = 'mjd'
    LP3.format = 'mjd'
    LP4.format = 'mjd'
    LP2,LP3,LP4=56131.0,57062.0,58028.0


    hdul=fits.open(file_name)
    field=hdul[2].data
    wave_diff=[]
    for i in field['CENWAVE']:
        j=float(i)-rest_wave
        j=abs(j)
        wave_diff.append(j)  
    min_value=min(wave_diff)
    which=wave_diff.index(min_value)
    
    

    if field['MJD_MID'][which]<LP2:
       life_position = ('LP1')
    if LP2<field['MJD_MID'][which]<LP3:
       life_position = ('LP2')
    if LP3<field['MJD_MID'][which]<LP4:
       life_position = ('LP3')
    if field['MJD_MID'][which]>LP4:
       life_position = ('LP4')

    print ("Instrument, GRATING, CENWAVE, SPECRES, LIFE POSITION")
    print (field['INSTRUMENT'][which], field['DISPERSER'][which], field['CENWAVE'][which],field['SPECRES'][which], life_position)