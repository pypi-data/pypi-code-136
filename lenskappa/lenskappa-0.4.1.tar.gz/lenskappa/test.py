from itertools import count
from lenskappa.catalog.filter import MinValueFilter
from lenskappa.counting import RatioCounter
from lenskappa.catalog import MaxValueFilter
from lenskappa.catalog import SingleValueParam

from astropy.coordinates import SkyCoord
import astropy.units as u

from heinlein import load_dataset
from heinlein.region import Region

if __name__ == "__main__":

    # Lenskappa expects standard names for catalog columns. It can handle
    # Non-standard names using paramater maps like this one.
    # The key is the standard name, while the value is the name in the catalog
    # Paramater maps also contain parameters that are needed to compute weights,
    # Such as the redshift of the source (z_s)
    z_s_param = SingleValueParam('z_s', 1.523)
    comparison_dataset = load_dataset("des")
    aperture = 120*u.arcsec
    center = SkyCoord(62.0905, -53.8999, unit="deg")
    lens_region = Region.circle(center, aperture)

    #Read in the catalog for your field of interest. Currently, only CSV files are supported
    print("reading lens field")

    column_aliases = {"DNF_Z": "z_gal"}
    comparison_dataset.add_aliases("catalog", column_aliases)
    field_data = comparison_dataset.get_data_from_region(lens_region, dtypes=["catalog", "mask"])

    cat = field_data["catalog"]

    ra = cat['ra']
    dec = cat['dec']
    z = cat['DNF_Z']
    mag = cat['MAG_AUTO_I']


    # The HSC W02 only has full coverage in about half of its area
    # So we create a box defining the edge of what we want to compare to
    comparison_region = Region.box(30, -35, 40, -30)
    #Sky regions take the center of the region as an argument (I plan to remove this soon)

    #Initialize the comparison field
    #survey.add_params(pars)

    #Define the region corresponding to the lens field
    #The radius of this region will be used when comparing to the control field

    #Place a filter on the catalogs
    #The first parameter is the name in the actual catalog, or the standard name (assuming it has been mapped as above)
    #This example removes all objects with i-band magnitude > 24
    #And all objects more distance than z = 1.523
    zmax_filter = MaxValueFilter('z_gal', 2.375)
    magmax_filter = MaxValueFilter('MAG_AUTO_I', 22.5)
    mindist_filter = MinValueFilter('r', min=6*u.arcsec)

    #Initialize the counter object. mask=True means the counter will take the
    #bright star masks into account when computing the number counts
    counter = RatioCounter(field_data, comparison_dataset, lens_region, comparison_region, mask=True)

    #Add the catalog filters to the counter, which will automatically apply them.
    #An "absolute" filter is applied to the catalogs before any other work is done.
    #which = 'both' just means the filters will be to both the control and lens catalogs
    counter.add_catalog_filter(zmax_filter, name='zmax', filter_type='periodic', catalogs='all')
    counter.add_catalog_filter(magmax_filter, name='magmax', filter_type='periodic', catalogs='all')
    counter.add_catalog_filter(mindist_filter, name='mindist', filter_type='periodic', catalogs='all')
    counter.add_weight_params({'z_s': 2.375})

    counter.get_weights(['gal', 'zweight', 'oneoverr'], output_file="lenskappa_test.csv", num_samples=1000, threads=8, overwrite=True, meds=True)
    #The first parameter in get_weight_ratios indicates which weights to compute
    #For now it's best to just leave this on all.
    
