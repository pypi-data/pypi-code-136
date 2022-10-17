# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['views_transformation_library']

package_data = \
{'': ['*']}

install_requires = \
['ingester3>=0.6.0',
 'pandas>=1.2.3,<2.0.0',
 'scikit_learn>=1.0.2,<2.0.0',
 'scipy>=1.6.2,<2.0.0',
 'stepshift>=1.2.0',
 'xarray>=0.19.0']

setup_kwargs = {
    'name': 'views-transformation-library',
    'version': '2.5.1',
    'description': 'A package containing data transformation functions used by the ViEWS team',
    'long_description': '\n# ViEWS Transformation Library\n\nThis package contains transforms made available in ViEWS cloud.  The transforms\nare all locally available, and do not depend on remote resources or\ncredentials.\n\n## Contributing: \n\nThere is an urgent need to fill this library with transforms.\nTransforms we need, that are not implemented, are listed under issues.\nPlease follow the guidelines for contributing outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) document.\n\n## Usage:\n\n```\npip install views-transformation-library\n```\n\n```\nfrom views_transformation_library.timelag import timelag\nimport viewser\n\nged_best_ns = viewser.get_variable("priogrid_month","priogrid_month.ged_best_ns",2010,2020)\nlagged_data = timelag(ged_best_ns,10)\n\nlagged_from_api = viewser.get_variable("priogrid_month","ged_best_ns",2010,2020,transforms:[\n   {"type":"tlag","args":[10]}\n])\n\nassert lagged_from_api == lagged_data\n```\n\n## API:\n\nEach transform function operates on a pandas dataframe.\n',
    'author': 'peder2911',
    'author_email': 'pglandsverk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.github.com/prio-data/views_transformation_library',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
