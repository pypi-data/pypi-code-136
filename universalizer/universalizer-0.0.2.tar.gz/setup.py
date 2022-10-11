# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['universalizer']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'curies>=0.1.5,<0.2.0',
 'kgx>=1.7.0,<2.0.0',
 'oaklib>=0.1.45,<0.2.0',
 'prefixmaps>=0.1.3,<0.2.0',
 'sssom>=0.3.16,<0.4.0']

entry_points = \
{'console_scripts': ['universalizer = universalizer.cli:cli']}

setup_kwargs = {
    'name': 'universalizer',
    'version': '0.0.2',
    'description': 'Provides functions for knowledge graph cleanup and identifier normalization.',
    'long_description': '# universalizer\n\nThe KG-Hub Universalizer provides functions for knowledge graph cleanup and identifier normalization.\n\n## Installation\n\nInstall with `pip`:\n\n```\npip install universalizer\n```\n\nOR\n\nInstall with Poetry.\n\n```\ngit clone https://github.com/Knowledge-Graph-Hub/universalizer.git\ncd universalizer\npoetry install\n```\n\n## Usage\n\nWith KGX format node and edge files in the same directory:\n\n```\nuniversalizer run path/to/directory\n```\n\nOr, if they\'re in a single tar.gz file:\n\n```\nuniversalizer run -c graph.tar.gz\n```\n\n### ID and category mapping\n\nSSSOM-format maps are supported. Use a single map file:\n\n```\nuniveralizer run -m poro-mp-exact-1.0.sssom.tsv path/to/directory\n```\n\nor a whole directory of them:\n\n```\nuniveralizer run -m path/to/mapfiles path/to/directory\n```\n\nTo map node categories as well as identifiers, use the `-u` flag:\n\n```\nuniveralizer run -m path/to/mapfiles path/to/directory -u\n```\n\nFor SSSOM maps from `subject_id` to `object_id`, subject node IDs will be remapped to object IDs.\n\nIf the `object_category` value is specified the node\'s category ID will be remapped as well.\n\nNote that this will complete node normalization *and* ID remapping.\n\nMaps should use the normalized form (e.g., specify "FBbt:00005201", not "FBBT:00005201", even if the latter form is in the input graph.)\n',
    'author': 'caufieldjh',
    'author_email': 'j.harry.caufield@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Knowledge-Graph-Hub/universalizer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
