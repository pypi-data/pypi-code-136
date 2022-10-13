# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['freebox_api', 'freebox_api.api']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3,<4', 'urllib3>=1.26.6,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=3.3,<5.0']}

entry_points = \
{'console_scripts': ['freebox_api = freebox_api.__main__:main']}

setup_kwargs = {
    'name': 'freebox-api',
    'version': '1.0.0',
    'description': 'Provides asynchronous authentication and access to Freebox servers',
    'long_description': "freebox-api\n===========\n\n|PyPI| |GitHub Release| |Python Version| |License|\n\n|Read the Docs| |Tests| |Codecov| |GitHub Activity|\n\n|pre-commit| |Black|\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/freebox-api.svg\n   :target: https://pypi.org/project/freebox-api/\n   :alt: PyPI\n.. |GitHub Release| image:: https://img.shields.io/github/release/hacf-fr/freebox-api.svg\n   :target: https://github.com/hacf-fr/freebox-api/releases\n   :alt: GitHub Release\n.. |Python Version| image:: https://img.shields.io/pypi/pyversions/freebox-api\n   :target: https://pypi.org/project/freebox-api\n   :alt: Python Version\n.. |License| image:: https://img.shields.io/pypi/l/freebox-api\n   :target: https://opensource.org/licenses/GPL-3.0\n   :alt: License\n.. |Read the Docs| image:: https://img.shields.io/readthedocs/freebox-api/latest.svg?label=Read%20the%20Docs\n   :target: https://freebox-api.readthedocs.io/\n   :alt: Read the documentation at https://freebox-api.readthedocs.io/\n.. |Tests| image:: https://github.com/hacf-fr/freebox-api/workflows/Tests/badge.svg\n   :target: https://github.com/hacf-fr/freebox-api/actions?workflow=Tests\n   :alt: Tests\n.. |Codecov| image:: https://codecov.io/gh/hacf-fr/freebox-api/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/hacf-fr/freebox-api\n   :alt: Codecov\n.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white\n   :target: https://github.com/pre-commit/pre-commit\n   :alt: pre-commit\n.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Black\n.. |GitHub Activity| image:: https://img.shields.io/github/commit-activity/y/hacf-fr/freebox-api.svg\n   :target: https://github.com/hacf-fr/freebox-api/commits/master\n   :alt: GitHub Activity\n\n\nFeatures\n--------\n\nEasily manage your freebox in Python using the Freebox OS API.\nCheck your calls, manage your contacts, configure your dhcp, disable your wifi, monitor your LAN activity and many others, on LAN or remotely.\n\nfreebox-api is a python library implementing the freebox OS API. It handles the authentication process and provides a raw access to the freebox API in an asynchronous manner.\n\nThis project is based on fstercq/freepybox, which provides the same features as freebox-api in a synchronous manner.\n\n\nRequirements\n------------\n\n* TODO\n\n\nInstallation\n------------\n\nYou can install *freebox-api* via pip_ from PyPI_:\n\n.. code:: console\n\n   $ pip install freebox-api\n\nOr manually download the last version from github and install it with Poetry_\n\n.. code:: console\n\n   $ git clone https://github.com/hacf-fr/freebox-api.git\n   $ python poetry install\n\n.. _Poetry: https://python-poetry.org/\n\n\n\nUsage\n-----\n\n.. code:: python\n\n   # Import the freebox-api package.\n   from freebox_api import Freepybox\n\n   async def reboot()\n      # Instantiate the Freepybox class using default options.\n      fbx = Freepybox()\n\n      # Connect to the freebox with default options.\n      # Be ready to authorize the application on the Freebox.\n      await fbx.open('192.168.0.254')\n\n      # Do something useful, rebooting your freebox for example.\n      await fbx.system.reboot()\n\n      # Properly close the session.\n      await fbx.close()\n\nHave a look at the example.py_ for a more complete overview.\n\n.. _example.py: tests/example.py\n\nNotes on HTTPS\n--------------\n\nWhen you access a Freebox with its default-assigned domain (ending in ``fbxos.fr``), the library verifies its\ncertificate by automatically trusting the Freebox certificate authority. If you want to avoid this, you can\n`setup a custom domain name`_ which will be associated with a Let's Encrypt certificate.\n\n.. _setup a custom domain name: https://www.freenews.fr/freenews-edition-nationale-299/freebox-9/lacces-distant-a-freebox-os-sameliore-https\n\n\nResources\n---------\n\nFreebox OS API documentation : http://dev.freebox.fr/sdk/os/\n\n\nContributing\n------------\n\nContributions are very welcome.\nTo learn more, see the `Contributor Guide`_.\n\n\nLicense\n-------\n\nDistributed under the terms of the `GNU GPL v3`_ license,\n*freebox-api* is free and open source software.\n\n\nIssues\n------\n\nIf you encounter any problems,\nplease `file an issue`_ along with a detailed description.\n\n\nCredits\n-------\n\nThis project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.\n\n\n.. _@cjolowicz: https://github.com/cjolowicz\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _GNU GPL v3: https://opensource.org/licenses/GPL-3.0\n.. _PyPI: https://pypi.org/\n.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n.. _file an issue: https://github.com/hacf-fr/freebox-api/issues\n.. _pip: https://pip.pypa.io/\n.. github-only\n.. _Contributor Guide: CONTRIBUTING.rst\n",
    'author': 'stilllman',
    'author_email': 'luc_touraille@yahoo.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hacf-fr/freebox-api',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.4,<4.0.0',
}


setup(**setup_kwargs)
