# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ms2ml',
 'ms2ml.data',
 'ms2ml.data.adapters',
 'ms2ml.data.parsing',
 'ms2ml.metrics']

package_data = \
{'': ['*']}

install_requires = \
['lark>=1.1.2,<2.0.0',
 'lxml>=4.9.1,<5.0.0',
 'numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pyteomics>=4.5.5,<5.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'uniplot>=0.7.0,<0.8.0']

extras_require = \
{':python_version > "3.8" and python_version < "3.11"': ['psims>=1.2.0,<2.0.0'],
 ':python_version >= "3.8" and python_version < "3.11"': ['torch>=1.12.1,<2.0.0',
                                                          'pandas-stubs>=1.4.4.220919,<2.0.0.0']}

setup_kwargs = {
    'name': 'ms2ml',
    'version': '0.0.3',
    'description': 'Provides an intermediate layer between mass spec data and ML applications, such as encoding.',
    'long_description': 'None',
    'author': 'J. Sebastian Paez',
    'author_email': 'jspaezp@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
