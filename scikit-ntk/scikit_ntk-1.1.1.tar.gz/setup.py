# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skntk']

package_data = \
{'': ['*']}

extras_require = \
{':python_version >= "3.10"': ['scikit-learn>=1.1,<2.0'],
 ':python_version >= "3.7" and python_version < "3.10"': ['scikit-learn>=1.0.0,<2.0.0']}

setup_kwargs = {
    'name': 'scikit-ntk',
    'version': '1.1.1',
    'description': "Implementation of the neural tangent kernel for scikit-learn's Gaussian process module.",
    'long_description': '## Neural Tangent Kernel for `scikit-learn` Gaussian Processes\n\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/392781/scikit-ntk/Lint,%20Build,%20Install,%20Test?label=Lint%2C%20Build%2C%20Install%2C%20Test&style=flat-square) ![PyPI](https://img.shields.io/pypi/v/scikit-ntk?style=flat-square) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/scikit-ntk?style=flat-square) ![PyPI - Downloads](https://img.shields.io/pypi/dm/scikit-ntk?style=flat-square)\n\n**scikit-ntk** is implementation of the neural tangent kernel (NTK) for the `scikit-learn` machine learning library as part of "An Empirical Analysis of the Laplace and Neural Tangent Kernels" master\'s thesis (found at [http://hdl.handle.net/20.500.12680/d504rr81v](http://hdl.handle.net/20.500.12680/d504rr81v) and [https://arxiv.org/abs/2208.03761](https://arxiv.org/abs/2208.03761)).  This library is meant to directly integrate with [`sklearn.gaussian_process`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.gaussian_process) module.  This implementation of the NTK can be used in combination with other kernels to train and predict with Gaussian process regressors and classifiers. \n\n## Installation\n\n### Dependencies\n\nscikit-ntk requires:\n* Python (>=3.7)\n* scikit-learn (>=1.0.1)\n\n\n### User installation\nIn terminal using `pip` run:\n\n```bash\npip install scikit-ntk\n```\n\n### Usage\nUsage is described in [`examples/usage.py`](https://github.com/392781/scikit-ntk/blob/master/example/usage.py); however, to get started simply import the `NeuralTangentKernel` class:\n\n```py\nfrom skntk import NeuralTangentKernel as NTK\n\nkernel_ntk = NTK(D=3, bias=0.01, bias_bounds=(1e-6, 1e6))\n```\nOnce declared, usage is the same as other `scikit-learn` kernels.\n\n## Building\nPython Poetry (>=1.2) is required if you wish to build `scikit-ntk` from source.  In order to build follow these steps:\n\n1. Clone the repository\n```bash\ngit clone git@github.com:392781/scikit-ntk.git\n```\n2. Enable a Poetry virtual environment\n```bash\npoetry shell\n```\n3. Build and install\n```bash\npoetry build\npoetry install --with dev\n```\n\n## Citation\n\nIf you use scikit-ntk in your scientific work, please use the following citation alongside the scikit-learn citations found at [https://scikit-learn.org/stable/about.html#citing-scikit-learn](https://scikit-learn.org/stable/about.html#citing-scikit-learn):\n\n```\n@mastersthesis{lencevicius2022laplacentk,\n  author  = "Ronaldas Paulius Lencevicius",\n  title   = "An Empirical Analysis of the Laplace and Neural Tangent Kernels",\n  school  = "California State Polytechnic University, Pomona",\n  year    = "2022",\n  month   = "August",\n  note    = {\\url{http://hdl.handle.net/20.500.12680/d504rr81v}}\n}\n```\n',
    'author': 'Ronaldas P Lencevičius',
    'author_email': 'contact@ronaldas.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/392781/scikit-ntk',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
