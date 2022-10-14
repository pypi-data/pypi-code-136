# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bioat']

package_data = \
{'': ['*']}

install_requires = \
['cleo>=0.8.1,<0.9.0',
 'fire>=0.4.0,<0.5.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'pip>=22.2.2,<23.0.0',
 'pysam==0.19.1',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['bioat = bioat._cli:main']}

setup_kwargs = {
    'name': 'bioat',
    'version': '0.1.1.2',
    'description': "Bioinformatic toolkit with python (It's still under development!)",
    'long_description': '# BioinformaticAnalysisTools\n\n## Introduction\nA bioinformatic python toolkit accelerated with rust!\n\n- Author: Hua-nan ZHAO @Tsinghua University\n- E-Mail: hermanzhaozzzz@gmail.com\n\n## Installation\n```shell\npip install bioat\n```\n\n## unit testing\n```shell\ncd tests\npython -m pytest\n# or\npoetry run pytest\n```\n## usage\n\n\n## history\n\n\n\n\n',
    'author': 'Herman Zhao',
    'author_email': 'hermanzhaozzzz@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hermanzhaozzzz/BioinformaticAnalysisTools',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
