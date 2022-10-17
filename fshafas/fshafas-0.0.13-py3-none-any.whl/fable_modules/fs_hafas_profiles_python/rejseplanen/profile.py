from __future__ import annotations
from ...fs_hafas_python.context import (Profile, Profile__set__locale_Z721C83C5, Profile__set__timezone_Z721C83C5, Profile__set__endpoint_Z721C83C5, Profile__set_salt_Z721C83C5, Profile__set_cfg_Z3219B2F8, Profile__set_baseRequest_Z42C91061, Profile__set__products_Z4ED450D4, Profile__set_departuresGetPasslist_Z1FBCCD16, Profile__set_departuresStbFltrEquiv_Z1FBCCD16, Profile__set__trip_6FCE9E49, Profile__set__radar_6FCE9E49, Profile__set__lines_6FCE9E49, Profile__set__remarks_6FCE9E49, Profile__set__reachableFrom_6FCE9E49)
from ...fs_hafas_python.profile import default_profile
from ...fs_hafas_python.types_raw_hafas_client import Cfg
from .products import products
from .request import request

profile: Profile = default_profile()

Profile__set__locale_Z721C83C5(profile, "da-DK")

Profile__set__timezone_Z721C83C5(profile, "Europe/Copenhagen")

Profile__set__endpoint_Z721C83C5(profile, "https://mobilapps.rejseplanen.dk/bin/iphone.exe")

Profile__set_salt_Z721C83C5(profile, "")

Profile__set_cfg_Z3219B2F8(profile, Cfg("GPA", None))

Profile__set_baseRequest_Z42C91061(profile, request)

Profile__set__products_Z4ED450D4(profile, products)

Profile__set_departuresGetPasslist_Z1FBCCD16(profile, False)

Profile__set_departuresStbFltrEquiv_Z1FBCCD16(profile, False)

Profile__set__trip_6FCE9E49(profile, True)

Profile__set__radar_6FCE9E49(profile, True)

Profile__set__lines_6FCE9E49(profile, False)

Profile__set__remarks_6FCE9E49(profile, False)

Profile__set__reachableFrom_6FCE9E49(profile, False)

__all__ = ["profile"]

