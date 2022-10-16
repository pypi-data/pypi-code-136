# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['merkly', 'merkly.utils']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0',
 'pylint>=2.14.5,<3.0.0',
 'pysha3>=1.0.2,<2.0.0',
 'pytest-watcher>=0.2.3,<0.3.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['lint = scripts.poetry:lint', 'w-t = scripts.poetry:w_t']}

setup_kwargs = {
    'name': 'merkly',
    'version': '0.5.2',
    'description': '🌳 The simple and easy implementation of Merkle Tree',
    'long_description': '# 🌳 Merkly\n\nThe **simple and easy** implementation of **Python Merkle Tree**\n\n---\n\n[![CodeQL](https://github.com/olivmath/merkly/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/olivmath/merkly/actions/workflows/codeql-analysis.yml)\n[![Lint](https://github.com/olivmath/merkly/actions/workflows/lint.yml/badge.svg)](https://github.com/olivmath/merkly/actions/workflows/lint.yml)\n[![Test](https://github.com/olivmath/merkly/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/olivmath/merkly/actions/workflows/test.yml)\n[![PyPI](https://img.shields.io/pypi/v/merkly)](https://pypi.org/project/merkly/)\n\n![GitHub last commit](https://img.shields.io/github/last-commit/olivmath/merkly)\n![GitHub commit activity](https://img.shields.io/github/commit-activity/m/olivmath/merkly)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/merkly)](https://pypi.org/project/merkly/)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/merkly)](https://pypi.org/project/merkly/)\n![PyPI - License](https://img.shields.io/pypi/l/merkly)\n\n## Table of Contents\n\n- [Credits](#credits)\n- [How to install](#how-to-install)\n- [How it works](#how-it-works)\n- [How to use](#how-to-use)\n- [Roadmap](#roadmap)\n- [Contributing](#contributing)\n- [License](#license)\n\n## Credits\n\n[![GitHub Contributors Image](https://contrib.rocks/image?repo=olivmath/merkly)](https://github.com/olivmath/merkly/graphs/contributors)\n\n## How to install\n\n```\npoetry add merkly\n```\n\n```\npip install merkly\n```\n\n## How to works\n\n- *We use keccak-256 under-the-hood*\n\nThis library provides a clean and easy to use implementation of the Merkle Tree with the following features:\n\n- Create Leaf\n- Create Root\n- Create Proof\n- Verify Proof\n\n<img width="2216" alt="merkle-tree" src="https://user-images.githubusercontent.com/50037567/193623013-3c2888d1-441f-45a1-97fe-6e275edde847.png">\n\n\n## How to Use\n\n**Create a Merkle Tree**\n\n```python\nfrom merkly.mtree import MerkleTree\n\n# create a Merkle Tree\nmtree = MerkleTree([\'a\', \'b\', \'c\', \'d\']\n\n# show original input\nassert mtree.raw_leafs == [\'a\', \'b\', \'c\', \'d\']\n\n# show leafs \nassert mtree.leafs == []\n```\n\n\n**Create a Root**\n\n```python\nfrom merkly.mtree import MerkleTree\n\n# create a Merkle Tree\nmtree = MerkleTree([\'a\', \'b\', \'c\', \'d\'])\n\n# get root of tree\nassert mtree.root == ""\n```\n\n**Create Proof of a leaf**\n```python\nfrom merkly.mtree import MerkleTree\n\n# create a Merkle Tree\nmtree = MerkleTree([\'a\', \'b\', \'c\', \'d\'])\n\n# get proof of a leaf\nassert mtree.proof("b") == []\n```\n\n**Verify Proof of a leaf**\n```python\nfrom merkly.mtree import MerkleTree\n\n# create a Merkle Tree\nmtree = MerkleTree([\'a\', \'b\', \'c\', \'d\'])\n\n# get proof of a leaf\np = mtree.proof("b")\n\n# verify your proof\nassert mtree.verify(p) == True\n```\n\n\n## Roadmap\n\n| Feature | Status | Priority |\n|-|-|-|\n| Create Root | ✅ | 🔥 |\n| Create Proof | ✅ | 🔥 |\n| Verify Proof | ✅ | 🔥 |\n| Support **[OpenZeppelin](https://docs.openzeppelin.com/contracts/4.x/utilities#verifying_merkle_proofs)** | ⏰ | 🔥 |\n| Compatible with **[MerkleTreeJs](https://github.com/miguelmota/merkletreejs)** | ⏰ | 🔥 |\n| Use any Hash function | ⏰ | 🧐 |\n| Leafs of any size | ⏰ | 🧐 |\n\n## Contributing\n\n- Before read a code of conduct: **[CODE_OF_CONDUCT](CODE_OF_CONDUCT.md)**\n- Follow the guide of development: **[CONTRIBUTING](CONTRIBUTING.md)**\n\n## License\n\n[MIT](LICENSE)\n\n<!-- https://math.mit.edu/research/highschool/primes/materials/2018/Kuszmaul.pdf -->\n',
    'author': 'Lucas Oliveira',
    'author_email': 'olivmath@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/olivmath/merkly.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
