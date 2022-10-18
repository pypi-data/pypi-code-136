# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zntrack',
 'zntrack.core',
 'zntrack.core.functions',
 'zntrack.dvc',
 'zntrack.interface',
 'zntrack.meta',
 'zntrack.metadata',
 'zntrack.project',
 'zntrack.utils',
 'zntrack.zn']

package_data = \
{'': ['*']}

install_requires = \
['dot4dict>=0.1.1,<0.2.0',
 'dvc>=2.12.0,<3.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pygit2>=1.9,<1.11',
 'pyyaml>=6.0,<7.0',
 'tqdm>=4.64.0,<5.0.0',
 'zninit>=0.1.1',
 'znjson>=0.2.1,<0.3.0']

setup_kwargs = {
    'name': 'zntrack',
    'version': '0.4.3',
    'description': 'Create, Run and Benchmark DVC Pipelines in Python',
    'long_description': '[![coeralls](https://coveralls.io/repos/github/zincware/ZnTrack/badge.svg)](https://coveralls.io/github/zincware/ZnTrack)\n[![codecov](https://codecov.io/gh/zincware/ZnTrack/branch/main/graph/badge.svg?token=ZQ67FXN1IT)](https://codecov.io/gh/zincware/ZnTrack)\n[![Maintainability](https://api.codeclimate.com/v1/badges/f25e119bbd5d5ec74e2c/maintainability)](https://codeclimate.com/github/zincware/ZnTrack/maintainability)\n![PyTest](https://github.com/zincware/ZnTrack/actions/workflows/pytest.yaml/badge.svg)\n[![PyPI version](https://badge.fury.io/py/zntrack.svg)](https://badge.fury.io/py/zntrack)\n[![code-style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black/)\n[![Documentation](https://readthedocs.org/projects/zntrack/badge/?version=latest)](https://zntrack.readthedocs.io/en/latest/?badge=latest)\n[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zincware/ZnTrack/HEAD)\n[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6472851.svg)](https://doi.org/10.5281/zenodo.6472851)\n[![ZnTrack](https://img.shields.io/badge/Powered%20by-ZnTrack-%23007CB0)](https://zntrack.readthedocs.io/en/latest/)\n\n\n\n\n![Logo](https://raw.githubusercontent.com/zincware/ZnTrack/main/docs/source/img/zntrack.png)\n\n# Parameter Tracking for Python\n\nZnTrack [zɪŋk træk] is an easy-to-use package for tracking parameters and creating computational graphs for your Python\nprojects.\nWhat is a parameter? Anything set by a user in your code, for example, the number of\nlayers in a neural network or the window size of a moving average.\nZnTrack works by storing the values of parameters in Python classes and functions and\nmonitoring how they change for several different runs.\nThese changes can then be compared graphically to see what effect they had on your\nworkflow.\nBeyond the standard tracking of parameters in a project, ZnTrack can be used to deploy\njobs with a set of different parameter values, avoid the re-running of code components\nwhere parameters have not changed, and to identify computational bottlenecks.\n\n## Example\nZnTrack is based on [DVC](https://dvc.org).\nWith ZnTrack a DVC Node on the computational graph can be written as a Python class.\nDVC Options, such as parameters, input dependencies and output files are defined as class attributes.\n\nThe following example shows a Node to compute a random number between 0 and a user defined maximum.\n\n````python\nfrom zntrack import Node, zn\nfrom random import randrange\n\n\nclass HelloWorld(Node):\n    """Define a ZnTrack Node"""\n    # parameter to be tracked\n    max_number: int = zn.params()\n    # parameter to store as output\n    random_number: int = zn.outs()\n    \n    def run(self):\n        """Command to be run by DVC"""\n        self.random_number = randrange(self.max_number)\n````\n\nThis Node can then be put on the computational graph (writing the `dvc.yaml` and `params.yaml` files) by calling `write_graph()`. \nThe graph can then be executed e.g., through `dvc repro`.\n\n````python\nHelloWorld(max_number=512).write_graph()\n````    \n\nOnce `dvc repro` is called, the results, i.e. the random number can be accessed directly by the Node object.\n```python\nhello_world = HelloWorld.load()\nprint(hello_world.random_numer)\n```\nAn overview of all the ZnTrack features as well as more detailed examples can be found in the [ZnTrack Documentation](https://zntrack.readthedocs.io/en/latest/).\n\n## Wrap Python Functions\nZnTrack also provides tools to convert a Python function into a DVC Node.\nThis approach is much more lightweight compared to the class-based approach with only a reduced set of functionality.\nTherefore, it is recommended for smaller nodes that do not need the additional toolset that the class-based approach provides.\n\n````python\nfrom zntrack import nodify, NodeConfig\nimport pathlib\n\n@nodify(outs=pathlib.Path("text.txt"), params={"text": "Lorem Ipsum"})\ndef write_text(cfg: NodeConfig):\n    cfg.outs.write_text(\n        cfg.params.text\n    )\n# build the DVC graph\nwrite_text()\n````\n\nThe ``cfg`` dataclass passed to the function provides access to all configured files\nand parameters via [dot4dict](https://github.com/zincware/dot4dict). The function body\nwill be executed by the ``dvc repro`` command or if ran via `write_text(run=True)`.\nAll parameters are loaded from or stored in ``params.yaml``.\n\n# Technical Details\n\n\n## ZnTrack as an Object-Relational Mapping for DVC\n\nOn a fundamental level the ZnTrack package provides an easy-to-use interface for DVC directly from Python.\nIt handles all the computational overhead of reading config files, defining outputs in the `dvc.yaml` as well as in the script and much more.\n\nFor more information on DVC visit their [homepage](https://dvc.org/doc).\n\n\nInstallation\n============\n\nInstall the stable version from PyPi via\n\n````shell\npip install zntrack\n```` \n\nor install the latest development version from source with:\n\n````shell\ngit clone https://github.com/zincware/ZnTrack.git\ncd ZnTrack\npip install .\n````\n\nCopyright\n=========\n\nThis project is distributed under the [Apache License Version 2.0](https://github.com/zincware/ZnTrack/blob/main/LICENSE).\n\n## Similar Tools\nThe following (incomplete) list of other projects that either work together with ZnTrack or can achieve similar results with slightly different goals or programming languages.\n\n- [DVC](https://dvc.org/) - Main dependency of ZnTrack for Data Version Control.\n- [dvthis](https://github.com/jcpsantiago/dvthis) - Introduce DVC to R.\n- [DAGsHub Client](https://github.com/DAGsHub/client) - Logging parameters from within .Python \n- [MLFlow](https://mlflow.org/) - A Machine Learning Lifecycle Platform.\n- [Metaflow](https://metaflow.org/) - A framework for real-life data science.\n- [Hydra](https://hydra.cc/) - A framework for elegantly configuring complex applications\n',
    'author': 'zincwarecode',
    'author_email': 'zincwarecode@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0.0',
}


setup(**setup_kwargs)
