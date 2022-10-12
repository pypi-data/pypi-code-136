from itertools import count
from lenskappa.catalog import SkyCatalog2D, catalog
from lenskappa.catalog.filter import MinValueFilter
from lenskappa.counting import RatioCounter
from lenskappa.datasets.surveys import hsc
from lenskappa.spatial import SkyRegion, CircularSkyRegion
from lenskappa.catalog import MaxValueFilter, ColumnLimitFilterWithReplacement
from lenskappa.catalog import QuantCatalogParam, SingleValueParam
from lenskappa.catalog import GaussianDistribution
from lenskappa.catalog.starmask import RegStarMask


from astropy.coordinates import SkyCoord
import astropy.units as u
from shapely import geometry
import logging
import time

if __name__ == "__main__":

    # Lenskappa expects standard names for catalog columns. It can handle
    # Non-standard names using paramater maps like this one.
    # The key is the standard name, while the value is the name in the catalog
    # Paramater maps also contain parameters that are needed to compute weights,
    # Such as the redshift of the source (z_s)
    m_gal_param = QuantCatalogParam('demp_sm', 'm_gal', is_log=True)
    z_gal_param = QuantCatalogParam('demp_photoz_best', 'z_gal')
    z_s_param = SingleValueParam('z_s', 1.523)
    ra_param = QuantCatalogParam('ra', 'ra', u.deg)
    dec_param = QuantCatalogParam('dec', 'dec', u.deg)
    pars = [m_gal_param, z_gal_param, z_s_param, ra_param, dec_param]

    aperture = 120*u.arcsec
    center = SkyCoord(141.23246, 2.32358, unit="deg")
    lens_region = CircularSkyRegion(center, aperture)

    #Read in the catalog for your field of interest. Currently, only CSV files are supported
    mask_center = SkyCoord(141.322290699 , 2.23142829201, unit="deg")
    print("reading lens field")
    lens_field = SkyCatalog2D.read_csv("/Users/patrick/Documents/Documents/Work/Research/LensEnv/0924/weighting/lens_cat.csv", params=pars)
    lens_mask = RegStarMask.from_file("/Users/patrick/Documents/Documents/Work/Research/LensEnv/HSC/HSC-SSP_brightStarMask_Arcturus/reg/patches/9807/BrightStarMask-9807-4,4-HSC-I.reg", mask_center)
 
    # The HSC W02 only has full coverage in about half of its area
    # So we create a box defining the edge of what we want to compare to
    box = geometry.box(30.5, -3.0, 33.5, -1.5)
    region = SkyRegion(box.centroid, box)
    #Sky regions take the center of the region as an argument (I plan to remove this soon)

    #Initialize the comparison field
    print("reading survey data")
    survey = hsc("W02_test", frame=region, params=pars, bind=True)
    #survey.add_params(pars)

    #Define the region corresponding to the lens field
    #The radius of this region will be used when comparing to the control field

    #Place a filter on the catalogs
    #The first parameter is the name in the actual catalog, or the standard name (assuming it has been mapped as above)
    #This example removes all objects with i-band magnitude > 24
    #And all objects more distance than z = 1.523
    zmax_filter = MaxValueFilter('z_gal', 1.523)
    magmax_filter = MaxValueFilter('i_cmodel_mag', 24)
    mindist_filter = MinValueFilter('r', min=5*u.arcsec)

    #Initialize the counter object. mask=True means the counter will take the
    #bright star masks into account when computing the number counts

    reg = survey.generate_circular_tile(aperture)
    s_cat = survey.get_objects(reg)

    print(s_cat)
    masked_cat = lens_mask.mask_external_catalog(s_cat, reg, lens_region) 
    print(masked_cat)