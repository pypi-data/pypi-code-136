# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oagdedupe',
 'oagdedupe.block',
 'oagdedupe.cluster',
 'oagdedupe.db',
 'oagdedupe.distance',
 'oagdedupe.fastapi',
 'oagdedupe.labelstudio',
 'oagdedupe.postgres']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=13.15.1,<14.0.0',
 'SQLAlchemy>=1.4.39,<2.0.0',
 'Sphinx>=5.1.1,<6.0.0,!=5.2.0.post0',
 'dependency-injector>=4.40.0,<5.0.0',
 'diagrams>=0.21.1,<0.22.0',
 'fastapi[all]>=0.79.0,<0.80.0',
 'flake8>=4.0.1,<5.0.0',
 'graphviz>=0.19.0,<0.20.0',
 'ipykernel>=6.13.0,<7.0.0',
 'jellyfish>=0.9.0,<0.10.0',
 'matplotlib>=3.5.1,<4.0.0',
 'modAL>=0.4.1,<0.5.0',
 'myst-parser>=0.18.0,<0.19.0',
 'nbconvert>=6.5.1,<7.0.0',
 'networkx>=2.8,<3.0',
 'numpy>=1.22.1,<2.0.0',
 'pandas>=1.4.2,<2.0.0',
 'pathos>=0.2.9,<0.3.0',
 'pre-commit>=2.20.0,<3.0.0',
 'protobuf>=3.20.2,<4.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pydantic[dotenv]>=1.10.2,<2.0.0',
 'pytest>=7.1.2,<8.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'ray>=1.13.0,<2.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'sphinx-rtd-theme>=1.0.0,<2.0.0',
 'tqdm>=4.58.0,<5.0.0']

extras_require = \
{'book': ['autodocsumm>=0.2.9,<0.3.0']}

setup_kwargs = {
    'name': 'oagdedupe',
    'version': '0.2.1',
    'description': 'oagdedupe is a Python library for scalable entity resolution, using active learning to learn blocking configurations, generate comparison pairs, then clasify matches.',
    'long_description': '# oagdedupe  \n\n```\nThis project is under active development.\n```\n\noagdedupe is a Python library for scalable entity resolution, using active \nlearning to learn blocking configurations, generate comparison pairs, \nthen clasify matches. \n\n# installation<a name="#installation"></a>\n\n```\n# PyPI\npip install oagdedupe\n```\n\n# documentation<a name="#documentation"></a>\n\nYou can find the documentation of oagdedupe at https://deduper.readthedocs.io/en/latest/, \nwhere you can find: \n\n- [Installation and Getting Started](https://deduper.readthedocs.io/en/latest/usage/installation.html)\n- [Examples](https://deduper.readthedocs.io/en/latest/examples/example_dedupe.html)\n- the [API reference](https://deduper.readthedocs.io/en/latest/dedupe/api.html)\n- [User Guide / Methodology](https://deduper.readthedocs.io/en/latest/userguide/intro.html)\n\n',
    'author': 'Chansoo Song',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chansooligans/oagdedupe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
