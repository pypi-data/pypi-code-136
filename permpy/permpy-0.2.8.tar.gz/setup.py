# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['permpy',
 'permpy.InsertionEncoding',
 'permpy.PegPermutations',
 'permpy.RestrictedContainer',
 'permpy.deprecated']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.1.2,<8.0.0']

setup_kwargs = {
    'name': 'permpy',
    'version': '0.2.8',
    'description': 'A package for analyzing permutation patterns.',
    'long_description': '# permpy\n\nPermPy is a user-friendly Python library for maniupulating permutation patterns and permutation classes. See [Wikipedia](https://en.wikipedia.org/wiki/Permutation_pattern) for an introduction to permutation patterns.\n\n## Installation\n\nInstall `permpy` with `pip`:\n\n```bash\n$ python -m pip install permpy\n```\n\n## Usage \n\n`permpy` contains a number of useful Python classes including `permpy.Permutation`, which represents a permutation and can determine containment.\n```python\n>>> from permpy import Permutation\n>>> p = Permutation(1324)\n>>> q = Permutation(123)\n>>> q <= p\nTrue\n>>> r = Permutation(321)\n>>> r <= p\nFalse\n>>> S = pp.PermSet.all(6)\n>>> S\nSet of 720 permutations\n>>> S.total_statistic(pp.Perm.num_inversions)\n5400\n>>> S.total_statistic(pp.Perm.num_descents)\n1800\n>>> from permpy import AvClass\n>>> A = AvClass([132])\n>>> for S in A:\n...     print(S)\n... \nSet of 1 permutations\nSet of 1 permutations\nSet of 2 permutations\nSet of 5 permutations\nSet of 14 permutations\nSet of 42 permutations\nSet of 132 permutations\nSet of 429 permutations\nSet of 1430 permutations \n```\n\n## Build Instructions\nFor a summary of how PermPy is built, go [here](https://py-pkgs.org/03-how-to-package-a-python#summary-and-next-steps).\n```bash\n$ python -m poetry build\n$ python -m poetry publish\n```\n\n## Test Instructions\n\nTo run tests, run\n```bash\n$ python -m poetry build\n$ python -m poetry shell\n$ python -m pytest tests/\n```\n\nTo build and install locally, run\n```bash\n$ python -m poetry install\n$ python -m poetry shell\n$ python\n>>> import permpy\n>>>\n```',
    'author': 'Michael Engen',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
