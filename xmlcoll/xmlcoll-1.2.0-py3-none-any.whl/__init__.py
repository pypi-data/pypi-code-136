"""
A package of python routines to work with data in XML format of samples.
"""
import os

xml_catalog = os.path.join(os.path.dirname(__file__), "xsd_pub/catalog")

if "XML_CATALOG_FILES" in os.environ:
    os.environ["XML_CATALOG_FILES"] += " " + xml_catalog
else:
    os.environ["XML_CATALOG_FILES"] = xml_catalog

from xmlcoll.coll import *
from xmlcoll.base import *
