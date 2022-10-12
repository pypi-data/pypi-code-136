# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torch_semiring_einsum']

package_data = \
{'': ['*']}

install_requires = \
['pynvml>=11.0.0,<12.0.0',
 'torch>=1.1.0,<2.0.0',
 'typing-extensions>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'torch-semiring-einsum',
    'version': '1.1.0',
    'description': 'Extensible PyTorch implementation of einsum that supports multiple semirings',
    'long_description': 'Semiring Einsum\n===============\n\nThis is an extensible PyTorch implementation of\n[einsum](https://pytorch.org/docs/master/generated/torch.einsum.html)\nthat supports multiple semirings.\n\n[Read the full documentation here.](https://bdusell.github.io/semiring-einsum/)\n',
    'author': 'Brian DuSell',
    'author_email': 'bdusell@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://bdusell.github.io/semiring-einsum/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
