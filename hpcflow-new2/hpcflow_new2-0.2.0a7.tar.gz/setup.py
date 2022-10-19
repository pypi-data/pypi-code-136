# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hpcflow',
 'hpcflow.api',
 'hpcflow.cli',
 'hpcflow.sdk',
 'hpcflow.sdk.config',
 'hpcflow.sdk.core',
 'hpcflow.sdk.data']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0',
 'colorama>=0.4.4,<0.5.0',
 'fsspec>=2022.2.0,<2023.0.0',
 'platformdirs>=2.5.1,<3.0.0',
 'ruamel.yaml>=0.17.20,<0.18.0',
 'sentry-sdk>=1.5.8,<2.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'valida>=0.4.0,<0.5.0',
 'zarr>=2.10.3,<3.0.0']

extras_require = \
{'pyinstaller': ['pyinstaller>=5.5,<6.0']}

entry_points = \
{'console_scripts': ['hpcflow = hpcflow.cli.cli:hpcflow.CLI'],
 'pyinstaller40': ['hook-dirs = pyinstaller.__init__:get_hook_dirs']}

setup_kwargs = {
    'name': 'hpcflow-new2',
    'version': '0.2.0a7',
    'description': 'Computational workflow management',
    'long_description': '<img src="https://hpcflow.github.io/docs/stable/_static/images/logo-v2.png" width="250" alt="hpcFlow logo"/>\n\n**hpcFlow manages your scientific workflows**\n\nDocumentation: [https://hpcflow.github.io/docs](https://hpcflow.github.io/docs)\n\n## Acknowledgements\nhpcFlow was developed using funding from the [LightForm](https://lightform.org.uk/) EPSRC programme grant ([EP/R001715/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/R001715/1))\n\n\n<img src="https://lightform-group.github.io/wiki/assets/images/site/lightform-logo.png" width="150"/>\n',
    'author': 'aplowman',
    'author_email': 'adam.plowman@manchester.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
