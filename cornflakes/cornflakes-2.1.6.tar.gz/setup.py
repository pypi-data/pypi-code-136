# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cornflakes',
 'cornflakes.cli',
 'cornflakes.click',
 'cornflakes.config',
 'cornflakes.decorator',
 'cornflakes.logging']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1',
 'click>=8.1.3,<9.0.0',
 'rich-rst>=1.1.7,<2.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['cornflakes = cornflakes.__main__:main']}

setup_kwargs = {
    'name': 'cornflakes',
    'version': '2.1.6',
    'description': 'Create generic any easy to manage Configs for your Project',
    'long_description': 'cornflakes\n==========\n\n|PyPI| |Python Version| |License| |Read the Docs| |Build| |Tests| |Codecov|\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/cornflakes.svg\n   :target: https://pypi.org/project/cornflakes/\n   :alt: PyPI\n.. |Python Version| image:: https://img.shields.io/pypi/pyversions/cornflakes\n   :target: https://pypi.org/project/cornflakes\n   :alt: Python Version\n.. |License| image:: https://img.shields.io/github/license/semmjon/cornflakes\n   :target: https://opensource.org/licenses/Apache2.0\n   :alt: License\n.. |Read the Docs| image:: https://img.shields.io/readthedocs/cornflakes/latest.svg?label=Read%20the%20Docs\n   :target: https://cornflakes.readthedocs.io\n   :alt: Read the documentation at https://cornflakes.readthedocs.io\n.. |Build| image:: https://github.com/semmjon/cornflakes/workflows/Build%20cornflakes%20Package/badge.svg\n   :target: https://github.com/semmjon/cornflakes/actions?workflow=Package\n   :alt: Build Package Status\n.. |Tests| image:: https://github.com/semmjon/cornflakes/workflows/Run%20cornflakes%20Tests/badge.svg\n   :target: https://github.com/semmjon/cornflakes/actions?workflow=Tests\n   :alt: Run Tests Status\n.. |Codecov| image:: https://codecov.io/gh/semmjon/cornflakes/branch/release-1.4.5/graph/badge.svg?token=FY72EIXI82\n   :target: https://codecov.io/gh/semmjon/cornflakes\n   :alt: Codecov\n\n.. code::\n\n   pip install cornflakes\n\nInformation\n-----------\n\nThis package was created by starting C ++ methods to incorporate into my\npython implementations.\n\nTo make things easier for me, lightweight public libraries were included\n(especially to carry out string operations):\n\n* hash-library\n* strtk\n\nThe following methods have currently been implemented:\n\n* ini_load (flexible and ligthweigh ini to dict parser, Faster Than Configparser)\n* eval_type (method to parse strings in python-types e.g. int \\| bool \\| timestamp\n* simple_hmac (vectorized c++ hmac implementation)\n* default_ca_path (python function to find a default ssl / ca certificate path)\n\nIn the future the following will be implemented: - more hash methods -\nc++ optimized grep methods - c++ optimized url-tools methods\n\nCurrently, the package was only tested for Linux ## Usage\n\n.. code:: python\n\n   from cornflakes import ini_load, default_ca_path, eval_type\n\n   ini_load(files={"s3_configs": ["examples/config/aws_config",\n                                  "examples/config/aws_credentials",\n                                  "examples/config/.s3cfg"]},\n            sections=["default", "qa"],\n            keys={"signurl_use_https": ["signurl_use_https"],\n                  "aws_access_key_id": ["access_key"],\n                  "aws_secret_access_key": ["secret_key"],\n                  "endpoint_url": ["endpoint-url", "host_base"],\n                  "region_name": ["bucket_location", "region", "aws_default_region"],\n                  "service_name": ["service_name"],\n                  "verify": ["ca_certs", "aws_ca_bundle", "ca_bundle"],},\n            defaults={\n                "region_name": "us-east-1",\n                "signurl_use_https": True,\n                "verify": default_ca_path(),\n                "service_name": "s3",\n            })\n\nDevelopment\n-----------\n\nPrerequisites\n~~~~~~~~~~~~~\n\n-  A compiler with C++17 support\n-  Pip 10+ or CMake >= 3.4 (or 3.8+ on Windows, which was the first\n   version to support VS 2015)\n-  Python 3.8+\n\nCommands\n~~~~~~~~~~~~\n\nJust clone this repository and pip install. Note the ``--recursive``\noption which is needed for the pybind11 submodule:\n\n.. code::\n\n   git clone --recursive https://gitlab.blubblub.tech/sgeist/cornflakes.git\n\nInstall the package using makefiles:\n\n.. code::\n\n   make install\n\nBuild dist using makefiles:\n\n.. code::\n\n   make dist\n\nRun tests (pytest) using makefiles:\n\n.. code::\n\n   make test\n\n\nRun all tests using makefiles:\n\n.. code::\n\n   make test-all\n\nRun lint using makefiles:\n\n.. code::\n\n   make lint\n\nCreate dev venv:\n\n.. code::\n\n   python -m venv .venv\n   source .venv/bin/activate\n   pip install cookietemple ninja pre-commit poetry\n\nBump Version using cookietemple:\n\n.. code::\n\n   cookietemple bump-version "<version(e.g 0.0.1)>"\n\nRun lint using cookietemple:\n\n.. code::\n\n   cookietemple lint .\n\nInstall pre-commit:\n\n.. code::\n\n   pre-commit install\n\nUpdate pre-commit:\n\n.. code::\n\n   pre-commit update -a\n\nRun pre-commit:\n\n.. code::\n\n   pre-commit run -a\n\nPublish\n~~~~~~~\n\nIts not recommended publish manually (use git-ci or github workflows instead).\n\n.. code::\n\n   make publish\n',
    'author': 'Semjon Geist',
    'author_email': 'semjon.geist@ionos.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sgeist/cornflakes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
