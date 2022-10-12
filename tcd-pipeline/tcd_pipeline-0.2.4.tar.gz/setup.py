# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tcd_pipeline',
 'tcd_pipeline.commands',
 'tcd_pipeline.config',
 'tcd_pipeline.rules',
 'tcd_pipeline.templates']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'click>=8.1.3,<9.0.0', 'jsonpath-ng>=1.5.3,<2.0.0']

entry_points = \
{'console_scripts': ['tcd-pipeline = tcd_pipeline.__main__:cli']}

setup_kwargs = {
    'name': 'tcd-pipeline',
    'version': '0.2.4',
    'description': '',
    'long_description': '# TCD pipeline tool\n\nCLI tool for convert TCD pipelines to ArgoWrokflows manifests.\n\n---\n\n## Build\n\nBuild instruction can be found at [BUILD.md](BUILD.md)\n\n---\n\n## Release\n\nRelease instruction and history can be found at [RELEASE.md](RELEASE.md)\n\n---\n\n## Install\n\n```sh\npip install tcd-pipeline\n```\n\n---\n\n## Usage\n\nRunning from installed\n\n```sh\ntcd-pipeline --help\n```\n\nRunning with python module\n\n```sh\npython -m tcd_pipeline\n```\n',
    'author': 'chitchai',
    'author_email': 'chitchaic@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
