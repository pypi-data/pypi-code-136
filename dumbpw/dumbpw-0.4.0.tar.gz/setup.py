# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dumbpw']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'deal>=4.19.1,<5.0.0']

entry_points = \
{'console_scripts': ['dumbpw = dumbpw.cli:cli']}

setup_kwargs = {
    'name': 'dumbpw',
    'version': '0.4.0',
    'description': 'A bad password generator for bad websites with bad password policies',
    'long_description': 'dumbpw\n======================\n|LANGUAGE| |VERSION| |BUILD| |MAINTAINED| |MAINTAINABILITY|\n|LICENSE| |STYLE|\n\n.. |BUILD| image:: https://github.com/rpdelaney/dumbpw/actions/workflows/integration.yaml/badge.svg\n   :target: https://github.com/rpdelaney/dumbpw/actions/workflows/integration.yaml\n   :alt: build status\n.. |LICENSE| image:: https://img.shields.io/badge/license-Apache%202.0-informational\n   :target: https://www.apache.org/licenses/LICENSE-2.0.txt\n.. |MAINTAINED| image:: https://img.shields.io/maintenance/yes/2022?logoColor=informational\n.. |VERSION| image:: https://img.shields.io/pypi/v/dumbpw\n   :target: https://pypi.org/project/dumbpw\n.. |STYLE| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n.. |LANGUAGE| image:: https://img.shields.io/pypi/pyversions/dumbpw\n.. |MAINTAINABILITY| image:: https://img.shields.io/codeclimate/maintainability-percentage/rpdelaney/dumbpw\n   :target: https://codeclimate.com/github/rpdelaney/dumbpw\n\nTo create and remember passwords for online services, the best practice for\nmost folks online is to use a password management tool such as `Bitwarden\n<https://bitwarden.com/>`_ to generate long, cryptographically random\npasswords. Then, a very strong passphrase is used to lock the password manager.\n\nUnfortunately, in a misguided attempt to encourage users to choose better\npasswords, many websites and apps enforce `restrictive password policies <https://github.com/duffn/dumb-password-rules>`_.\nThese policies inhibit users from using cryptographically random\npassword generators: a long, high-entropy password is more likely to\nviolate such rules, which means a security-savvy user may have to attempt\nseveral "random" passwords before one is accepted. This punishes users\nwho are trying to follow best practices.\n\nEnter dumbpw. dumbpw allows you to configure a set of rules, and then it will\ngenerate a cryptographically secure password that conforms to those dumb rules.\n\nIf all you need is a password generator, **you should not use this**.\n\nInstallation\n------------\n\n.. code-block :: console\n\n    pip3 install dumbpw\n\nUsage\n-----\n\n.. code-block :: console\n\n    $ dumbpw --help\n    Usage: dumbpw [OPTIONS] LENGTH\n\n    Options:\n    --version                       Show the version and exit.\n    --min-uppercase INTEGER         The minimum number of uppercase characters.\n    --min-lowercase INTEGER         The minimum number of lowercase characters.\n    --min-digits INTEGER            The minimum number of digit characters.\n    --min-specials INTEGER          The minimum number of special characters.\n    --blocklist TEXT                Characters that may not be in the password.\n                                    [default: \'";]\n    --allow-repeating / --reject-repeating\n                                    Allow or reject repeating characters in the\n                                    password.  [default: reject-repeating]\n    --specials TEXT                 Non-alphanumeric characters that may be in\n                                    the password. Pass \'-\' to read from standard\n                                    input.\n    --help                          Show this message and exit.\n\nKnown issues\n------------\n* dumbpw uses `secrets <https://docs.python.org/3/library/secrets.html>`_\n  to generate passwords. If the generated string doesn\'t meet the given\n  requirements, dumbpw discards it and generates another, until one passes.\n  Therefore, if you ask dumbpw to generate a long password with high minimums,\n  it will run for a very long time before terminating.\n* Likewise, if your minimums require characters that are banned in the\n  blocklist option, dumbpw will run forever.\n* The author is neither a cryptographer, nor a security expert. There has\n  been no formal, independent, external security review of this software. As\n  explained in the LICENSE, the author assumes no responsibility or liability\n  for your use of this software.\n\nRelated tools\n-------------\n* Apple\'s `Password Rules Validation Tool <https://developer.apple.com/password-rules/>`_\n\n============\nDevelopment\n============\n\nTo install development dependencies, you will need `poetry <https://docs.pipenv.org/en/latest/>`_\nand `pre-commit <https://pre-commit.com/>`_.\n\n.. code-block :: console\n\n    pre-commit install --install-hooks\n    poetry install && poetry shell\n\n`direnv <https://direnv.net/>`_ is optional, but recommended for convenience.\n',
    'author': 'Ryan Delaney',
    'author_email': 'ryan.patrick.delaney+git@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/dumbpw',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
