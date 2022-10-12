from itertools import count
from os import replace
from lenskappa.catalog.filter import MinValueFilter
from lenskappa.catalog.params import QuantCatalogParam
from lenskappa.counting import SingleCounter
from lenskappa.datasets.surveys import ms
from lenskappa.catalog import MaxValueFilter
from lenskappa.catalog.sampling import GaussianDistributionArray
import numpy as np


import astropy.units as u

if __name__ == "__main__":

    weights = ['gal', 'zweight', 'oneoverr', 'zoverr']
    zmax_filter = MaxValueFilter('z_gal', 1.523)
    magmax_filter = MaxValueFilter('mag_SDSS_i', 24.0)
    mindist_filter = MinValueFilter('r', 5*u.arcsec)
    mils = ms()

    dist_array = GaussianDistributionArray(relative=True, target='z_gal')
    dist_array.generate_grid(['z_gal', 'mag_SDSS_i'], [ [0, 1.5],[18, 24]], bins=[100,50])
    
    z_gal_axis = np.linspace(0, 1.5, 100)
    mag_axis = np.linspace(18, 24, 50)
    rng = np.random.default_rng()
    params = [QuantCatalogParam('z_spec', 'z_gal')]

    for z in z_gal_axis:
        for mag in mag_axis:
            center = rng.uniform(-0.1, 0.1)
            width = rng.uniform(0.01, 0.02)
            dist_array.add_distribution({'z_gal': z, 'mag_SDSS_i': mag}, center,width)


    ct = SingleCounter(mils, False)
    output_file = "ms_1_1.csv"
    mils.load_catalogs_by_field(1,1,z_s = 1.523,)
    mils.attach_dist_array(dist_array, "z_gal")

    ct.add_catalog_filter(zmax_filter, 'zmax')
    ct.add_catalog_filter(magmax_filter, 'magmax')
    ct.add_catalog_filter(mindist_filter, 'mindist', filter_type='periodic')
    ct.get_weights(output_positions=True, weights=weights, output_file = output_file, overlap=6, overwrite=True, n_samples=50)
