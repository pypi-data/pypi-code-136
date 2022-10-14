# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gwcelery',
 'gwcelery.conf',
 'gwcelery.data',
 'gwcelery.data.first2years',
 'gwcelery.email',
 'gwcelery.igwn_alert',
 'gwcelery.kafka',
 'gwcelery.sentry',
 'gwcelery.sentry.integrations',
 'gwcelery.tasks',
 'gwcelery.tests',
 'gwcelery.tests.data',
 'gwcelery.tests.data.llhoft',
 'gwcelery.tests.data.llhoft.fail',
 'gwcelery.tests.data.llhoft.fail.L1',
 'gwcelery.tests.data.llhoft.omegascan',
 'gwcelery.tests.data.llhoft.pass',
 'gwcelery.tests.data.llhoft.pass.H1',
 'gwcelery.tools',
 'gwcelery.util',
 'gwcelery.voevent']

package_data = \
{'': ['*'], 'gwcelery': ['static/*', 'static/vega/*', 'templates/*']}

install_requires = \
['adc-streaming>=2.2.0',
 'astropy>=4.3.1',
 'bilby-pipe>=1.0.6',
 'celery[redis]>=5.1',
 'click>=7',
 'comet',
 'confluent-kafka>=1.9.2,<2.0.0',
 'dnspython',
 'flask-caching',
 'flask>=2.2',
 'gracedb-sdk>=0.1.5',
 'gwdatafind>=1.1.1',
 'gwpy>=2.0.1',
 'healpy',
 'hop-client>=0.7.0',
 'igwn-alert>=0.2.2',
 'imapclient',
 'importlib-metadata',
 'jinja2>=2.11.2',
 'lalsuite>=6.82',
 'ligo-followup-advocate>=1.1.6',
 'ligo-gracedb>=2.7.5',
 'ligo-raven>=2.0',
 'ligo-segments',
 'ligo.em-bright>=1.0',
 'ligo.skymap>=0.4.0',
 'lscsoft-glue',
 'lxml',
 'numpy',
 'p-astro>=1.0.1',
 'pesummary',
 'pygcn>=1.0.1',
 'python-ligo-lw>=1.8.3,<2.0.0',
 'safe-netrc',
 'sentry-sdk[flask,tornado]',
 'service-identity',
 'voeventlib>=1.2',
 'werkzeug>=0.15.0',
 'zstandard']

extras_require = \
{'doc': ['pep517', 'sphinx>=4.0'],
 'test': ['fastavro>=1.6.1,<2.0.0',
          'pytest-celery',
          'pytest-cov',
          'pytest-flask',
          'pytest-socket']}

entry_points = \
{'celery.commands': ['condor = gwcelery.tools.condor:condor',
                     'flask = gwcelery.tools.flask:flask',
                     'nagios = gwcelery.tools.nagios:nagios'],
 'console_scripts': ['gwcelery = gwcelery:main',
                     'gwcelery-condor-submit-helper = '
                     'gwcelery.tools.condor_submit_helper:main']}

setup_kwargs = {
    'name': 'gwcelery',
    'version': '2.0.0',
    'description': 'Hipster pipeline for annotating LIGO events',
    'long_description': '.. image:: https://gwcelery.readthedocs.io/en/latest/_static/logo-0.5x.png\n   :alt: GWCelery logo\n\nGWCelery\n========\n\nGWCelery is a simple and reliable package for annotating and orchestrating\nLIGO/Virgo alerts, built from widely used open source components.\n\nSee the `quick start installation instructions <https://gwcelery.readthedocs.io/en/latest/quickstart.html>`_,\nthe full `documentation <https://gwcelery.readthedocs.io/en/latest/>`_, or the\n`contributing guide <https://gwcelery.readthedocs.io/en/latest/contributing.html>`_.\n\nFeatures\n--------\n\n- `Easy installation with pip <https://gwcelery.readthedocs.io/en/latest/quickstart.html>`_\n- Lightning fast distributed task queue powered by\n  `Celery <http://celeryproject.org>`_ and `Redis <https://redis.io>`_\n- Tasks are defined by `small, self-contained Python functions <https://git.ligo.org/emfollow/gwcelery/tree/main/gwcelery/tasks>`_\n- `Lightweight test suite <https://git.ligo.org/emfollow/gwcelery/tree/main/gwcelery/tests>`_ using mocks of external services\n- `Continuous integration <https://git.ligo.org/emfollow/gwcelery/pipelines>`_\n- `One environment variable to switch from playground to production GraceDB server <https://gwcelery.readthedocs.io/en/latest/configuration.html>`_\n- `Browser-based monitoring console <https://gwcelery.readthedocs.io/en/latest/monitoring.html>`_\n',
    'author': 'Leo Singer',
    'author_email': 'leo.singer@ligo.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://git.ligo.org/emfollow/gwcelery',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
