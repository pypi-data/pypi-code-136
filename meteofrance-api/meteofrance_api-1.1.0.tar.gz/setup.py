# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['meteofrance_api', 'meteofrance_api.model']

package_data = \
{'': ['*']}

install_requires = \
['pytz>=2020.4', 'requests>=2.25.1,<3.0.0', 'urllib3>=1.26.6,<2.0.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.11"': ['typing-extensions>=3.7.4,<5.0.0']}

entry_points = \
{'console_scripts': ['meteofrance-api = meteofrance_api.__main__:main']}

setup_kwargs = {
    'name': 'meteofrance-api',
    'version': '1.1.0',
    'description': 'Python client for Météo-France API.',
    'long_description': "Météo-France Python API\n=======================\n\nClient Python pour l'API Météo-France. | Python client for Météo-France API.\n\n|PyPI| |GitHub Release| |Python Version| |License|\n\n|Read the Docs| |Tests| |Codecov| |GitHub Activity|\n\n|pre-commit| |Black|\n\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/meteofrance-api\n   :target: https://pypi.org/project/meteofrance-api/\n   :alt: PyPI\n.. |GitHub Release| image:: https://img.shields.io/github/release/hacf-fr/meteofrance-api.svg\n   :target: https://github.com/hacf-fr/meteofrance-api/releases\n   :alt: GitHub Release\n.. |Python Version| image:: https://img.shields.io/pypi/pyversions/meteofrance-api\n   :target: https://pypi.org/project/meteofrance-api/\n   :alt: Python Version\n.. |License| image:: https://img.shields.io/pypi/l/meteofrance-api\n   :target: https://opensource.org/licenses/MIT\n   :alt: License\n.. |Read the Docs| image:: https://img.shields.io/readthedocs/meteofrance-api/latest.svg?label=Read%20the%20Docs\n   :target: https://meteofrance-api.readthedocs.io/\n   :alt: Read the documentation at https://meteofrance-api.readthedocs.io/\n.. |Tests| image:: https://github.com/hacf-fr/meteofrance-api/workflows/Tests/badge.svg\n   :target: https://github.com/hacf-fr/meteofrance-api/actions?workflow=Tests\n   :alt: Tests\n.. |Codecov| image:: https://codecov.io/gh/hacf-fr/meteofrance-api/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/hacf-fr/meteofrance-api\n   :alt: Codecov\n.. |GitHub Activity| image:: https://img.shields.io/github/commit-activity/y/hacf-fr/meteofrance-api.svg\n   :target: https://github.com/hacf-fr/meteofrance-api/commits/master\n   :alt: GitHub Activity\n.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white\n   :target: https://github.com/pre-commit/pre-commit\n   :alt: pre-commit\n.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Black\n\nYou will find English README content in the section `For English speaking users`_.\n\nVous trouverez le contenu francophone du README dans la section `Pour les francophones`_.\n\nPour les francophones\n---------------------\n\nDescription\n^^^^^^^^^^^\n\nCe package Python permet de gérer la communication avec l'API non publique de\nMétéo-France utilisée par les applications mobiles officielles.\n\nLe client permet:\n\n* Rechercher des lieux de prévisions.\n* Accéder aux prévisions météorologiques horaires ou quotidiennes.\n* Accéder aux prévisions de pluie dans l'heure quand disponibles.\n* Accéder aux alertes météo pour chaque département français et d'Andorre. Deux\n  bulletins sont disponibles : un synthétique et un second avec l'évolution des alertes\n  pour les prochaines 24 heures (exemple `ici <https://vigilance.meteofrance.fr/fr/gers>`_).\n\nCe package a été développé avec l'intention d'être utilisé par `Home-Assistant <https://home-assistant.io/>`_\nmais il peut être utilisé dans d'autres contextes.\n\nInstallation\n^^^^^^^^^^^^\n\nPour utiliser le module Python ``meteofrance`` vous devez en premier installer\nle package en utilisant pip_ depuis PyPI_:\n\n.. code:: console\n\n   $ pip install meteofrance-api\n\n\nVous pouvez trouver un exemple d'usage dans un module Python en regardant\n`le test d'intégration <tests/test_integrations.py>`_.\n\nContribuer\n^^^^^^^^^^\n\nLes contributions sont les bienvenues. Veuillez consulter les bonnes pratiques\ndétaillées dans `CONTRIBUTING.rst`_.\n\n\nFor English speaking users\n--------------------------\n\nDescription\n^^^^^^^^^^^^\n\nThis Python package manages the communication with the private Météo-France API\nused by the official mobile applications.\n\nThe client allows:\n\n* Search a forecast location.\n* Fetch daily or hourly weather forecast.\n* Fetch rain forecast within the next hour if available.\n* Fetch the weather alerts or phenomenoms for each French department or Andorre.\n  Two bulletin are availabe: one basic and an other advanced with the timelaps evolution\n  for the next 24 hours (example `here <https://vigilance.meteofrance.fr/fr/gers>`_).\n\nThis package have been developed to be used with `Home-Assistant <https://home-assistant.io/>`_\nbut it can be used in other contexts.\n\nInstallation\n^^^^^^^^^^^^\n\nTo use the ``meteofrance`` Python module, you have to install this package first via\npip_ from PyPI_:\n\n.. code:: console\n\n   $ pip install meteofrance-api\n\nYou will find an example ot usage in a Python program in the `integration test <tests/test_integrations.py>`_.\n\nContributing\n^^^^^^^^^^^^\n\nContributions are welcomed. Please check the guidelines in `CONTRIBUTING.rst`_.\n\nCredits\n-------\n\nThis project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.\n\n.. _@cjolowicz: https://github.com/cjolowicz\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _PyPI: https://pypi.org/\n.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n.. _pip: https://pip.pypa.io/\n\n.. github-only\n.. _CONTRIBUTING.rst: CONTRIBUTING.rst\n",
    'author': 'oncleben31',
    'author_email': 'oncleben31@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hacf-fr/meteofrance-api',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.4,<4.0.0',
}


setup(**setup_kwargs)
