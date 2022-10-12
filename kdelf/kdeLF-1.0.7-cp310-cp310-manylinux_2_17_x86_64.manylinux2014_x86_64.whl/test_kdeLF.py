## define your own f_lim function in this file: 

H0,Om0 = 71, 0.27
flux,alpha= 0.03950732, 0.75 
Mpc=3.0857E+022
c=299792.458

import os
import numpy as np
from astropy.cosmology import FlatLambdaCDM


cosmo = FlatLambdaCDM(H0=H0, Om0=Om0)
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Load data
data = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    'examples/data/test_sample.dat'))
        
## your own f_lim function : 
def f_lim(z):
    St=flux
    dist=cosmo.luminosity_distance(z)
    ans=dist.value
    return np.log10(4*np.pi*(ans*Mpc)**2*St*1E-26/(1.0+z)**(1.0-alpha)) 

from kdeLF import kdeLF
test=kdeLF.KdeLF(sample_file=data,solid_angle=0.45565237,H0=H0, Om0=Om0,zbin=[0.0,0.2],f_lim=f_lim,adaptive=False)
test.get_optimal_h(initial_bandwidths=[0.15,0.15])
test.get_lgLF()

