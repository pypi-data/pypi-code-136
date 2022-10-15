# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['prgconfig']
install_requires = \
['toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'prgconfig',
    'version': '1.0.0',
    'description': 'Configuration manager using toml language.',
    'long_description': '[![pipeline status](https://gitlab.com/remytms/prgconfig/badges/master/pipeline.svg)](https://gitlab.com/remytms/prgconfig/pipelines)\n[![coverage report](https://gitlab.com/remytms/prgconfig/badges/master/coverage.svg)](https://gitlab.com/remytms/prgconfig/pipelines)\n[![licence](https://img.shields.io/pypi/l/prgconfig.svg)](https://www.gnu.org/licenses/gpl.html)\n[![version](https://img.shields.io/pypi/v/prgconfig.svg)](https://pypi.org/project/prgconfig)\n[![python](https://img.shields.io/pypi/pyversions/prgconfig.svg)](https://pypi.org/project/prgconfig)\n\nprgconfig\n=========\n\nprgconfig is a little library that ease the manage of configuration\nfile written in [toml](https://toml.io). It comes with nice default. The\nminimum you have to specify is your program name then it does the rest.\nIt aims to fit to standard in use for location of configuration file. It\nis also totally configurable to fit your needs.\n\n\nInstallation\n------------\n\nRecommended installation is by using `pip`:\n\n```sh\npip install prgconfig\n```\n\n\nUsage\n-----\n\n`PrgConfig` is a dict like object.\n\nBasic example:\n\n```python\nfrom prgconfig import PrgConfig\n\nconfig = PrgConfig("prgname")\n\nconfig.load()\n\nprint(config["section"]["key"])\n```\n\nSee the constructor of `PrgConfig` class to get an idea of possible\nconfiguration.\n\n\nRoadmap\n-------\n\nSee [issues with the `enhancement` tag](https://gitlab.com/remytms/prgconfig/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=enhancement)\n',
    'author': 'Rémy Taymans',
    'author_email': 'remytms@tsmail.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/remytms/prgconfig',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
