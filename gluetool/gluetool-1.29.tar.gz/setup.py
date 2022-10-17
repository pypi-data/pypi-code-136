# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gluetool', 'gluetool.pylint', 'gluetool.tests']

package_data = \
{'': ['*'],
 'gluetool.tests': ['assets/parse_config/configroot/config/*',
                    'assets/parse_config/configroota/config/*',
                    'assets/parse_config/configrootb/config/*']}

install_requires = \
['Jinja2>=2.10,<3.0',
 'MarkupSafe==1.1.1',
 'Sphinx>=1.5.2,<1.6.0',
 'beautifulsoup4>=4.6.3,<5.0.0',
 'colorama>=0.3.9,<0.4.0',
 'configparser>=4.0.2,<5.0.0',
 'docutils>=0.14,<0.15',
 'lxml>=4.2.4,<5.0.0',
 'markupsafe==1.1.1',
 'mock>=3.0.5,<4.0.0',
 'mypy-extensions>=0.4.3,<0.5.0',
 'packaging>=20.9,<21.0',
 'raven>=6.9.0,<7.0.0',
 'requests-toolbelt>=0.8.0,<0.9.0',
 'requests==2.26.0',
 'ruamel.yaml>=0.16.12,<0.17.0',
 'six>=1.12.0,<2.0.0',
 'tabulate>=0.8.2,<0.9.0',
 'urlnormalizer>=1.2.0,<2.0.0']

extras_require = \
{':python_version >= "2.7" and python_version < "2.8"': ['enum34>=1.1.6,<2.0.0',
                                                         'ruamel.yaml.clib==0.2.2',
                                                         'typing>=3.7.4,<4.0.0',
                                                         'zipp==1.2.0',
                                                         'future==0.18.2'],
 ':python_version >= "2.7" and python_version < "2.8" or python_version >= "3.7" and python_version < "4.0"': ['typing-extensions>=3.7.4,<4.0.0'],
 ':python_version >= "3.6" and python_version < "4.0"': ['zipp>=3.5.0,<4.0.0']}

entry_points = \
{'console_scripts': ['gluetool = gluetool.tool:main',
                     'gluetool-html-log = gluetool.html_log:main'],
 'gluetool.modules': ['.bash_completion = '
                      'gluetool_modules.bash_completion:BashCompletion',
                      '.dep_list = gluetool_modules.dep_list:DepList',
                      '.yaml_pipeline = '
                      'gluetool_modules.yaml_pipeline:YAMLPipeline']}

setup_kwargs = {
    'name': 'gluetool',
    'version': '1.29',
    'description': 'Python framework for constructing command-line pipelines.',
    'long_description': 'gluetool - A tool for gluing together one-file python modules in a sequential command-line pipeline\n---------------------------------------------------------------------------------------------------\n\n``gluetool`` is a command line centric generic framework useable for glueing modules into pipeline\n\n\n.. image:: https://travis-ci.org/gluetool/gluetool.svg?branch=master\n    :target: https://travis-ci.org/gluetool/gluetool\n\n.. image:: https://codecov.io/gh/gluetool/gluetool/branch/master/graph/badge.svg\n     :target: https://codecov.io/gh/gluetool/gluetool\n     :alt: Code coverage\n\n.. image:: https://requires.io/github/gluetool/gluetool/requirements.svg?branch=master\n     :target: https://requires.io/github/gluetool/gluetool/requirements/?branch=master\n     :alt: Requirements Status\n\n.. image:: https://readthedocs.org/projects/gluetool/badge/?version=latest\n     :target: http://gluetool.readthedocs.io/en/latest/?badge=latest\n     :alt: Documentation Status\n\n\nDocumentation\n-------------\n\nFor more information see documentation:\n\nhttp://gluetool.readthedocs.io/\n',
    'author': 'Miloš Prchlik',
    'author_email': 'mprchlik@redhat.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gluetool.readthedocs.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
}


setup(**setup_kwargs)
