from shapely import geometry
from heinlein import  Region
from heinlein import load_dataset
import astropy.units as u
import time

hsc  = load_dataset("hsc")

hsc_center = (141.23246, 2.32358)
reg = Region.circle(hsc_center, 120*u.arcsec)
a = hsc.mask_fraction(reg)


des = load_dataset("des")


des_center = (13.4349,-20.2091)
reg = Region.circle(des_center, 120*u.arcsec)
a = des.mask_fraction(reg)
