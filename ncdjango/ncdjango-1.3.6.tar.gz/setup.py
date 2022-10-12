# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ncdjango',
 'ncdjango.geoprocessing',
 'ncdjango.geoprocessing.tasks',
 'ncdjango.interfaces',
 'ncdjango.interfaces.arcgis',
 'ncdjango.interfaces.arcgis_extended',
 'ncdjango.interfaces.data',
 'ncdjango.management',
 'ncdjango.management.commands',
 'ncdjango.migrations']

package_data = \
{'': ['*'], 'ncdjango.geoprocessing': ['test_data/*']}

install_requires = \
['Django>=2.2.0',
 'Fiona',
 'Pillow>=9.0.1,<10.0.0',
 'Shapely>=1.7.0',
 'celery>=5.2.3,<6.0.0',
 'django-tastypie>=0.14.0,<0.15.0',
 'djangorestframework',
 'netCDF4>=1.5.3',
 'numpy>=1.21.5,<1.22.0',
 'ply',
 'pyproj',
 'rasterio',
 'requests',
 'trefoil>=0.3.2,<0.4.0']

setup_kwargs = {
    'name': 'ncdjango',
    'version': '1.3.6',
    'description': 'A NetCDF mapserver app for Django',
    'long_description': '# ncdjango\n\nNcdjango turns [Django](https://www.djangoproject.com/) projects into map servers backed by\n[NetCDF](http://www.unidata.ucar.edu/software/netcdf/docs/faq.html#whatisit) datasets. It can be added Django project\nto provide various web interfaces to NetCDF data and geoprocessing tools written in Python which operate on NetCDF data.\n\n# Why?\nThis project grew out of a need for a map server capable of delivering time-series raster data from NetCDF data, with\nenough extensibility to support different web APIs for the same map service. The result is a Django app which adds a\nrange of map service capabilities to a Django project. Currently, ncdjango includes a partial implementation of the\n[ArcGIS REST API](http://resources.arcgis.com/en/help/rest/apiref/) with the added feature of per-request styling.\nIt also includes a data interface which can provide summary information about service data and generate class breaks\n(equal, quantile, or natural breaks) based on the service data.\n\nNcdjango provides an admin API for creating and managing map services, and a geoprocessing framework which allows\nclients to execute processing jobs against NetCDF result. Job results can be automatically published as new services,\nmeaning that a web client could call a geoprocessing job, and upon its completion, show the processed results in a map.\n\n# Use cases\nNcdjango is used to provide map services of NetCDF data for [Data Basin](https://databasin.org). Data Basin users can\nupload NetCDF datasets and view and share them in a web map, all with no programming or server coniguration. Example:\n[NARCCAP Monthly Average Maximum Daily Temperature](https://databasin.org/maps/new#datasets=7445377234b84b279225f8ebdd31d3ff)\n\nIt is also used in the [Seedlot Selection Tool](https://seedlotselectiontool.org/sst/) both to provide map services\nof NetCDF data, and to implement the geoprocessing needs for the tool and map services of the results.\n\n# Documentation\nFull documentation available [here](http://ncdjango.readthedocs.io/en/latest/).\n',
    'author': 'Conservation Biology Institute',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
