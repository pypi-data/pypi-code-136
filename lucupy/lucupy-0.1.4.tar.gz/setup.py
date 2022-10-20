# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lucupy',
 'lucupy.decorators',
 'lucupy.helpers',
 'lucupy.minimodel',
 'lucupy.observatory',
 'lucupy.observatory.abstract',
 'lucupy.observatory.gemini',
 'lucupy.sky',
 'lucupy.timeutils',
 'lucupy.types']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=5.1,<6.0', 'pytz>=2022.2,<2023.0']

setup_kwargs = {
    'name': 'lucupy',
    'version': '0.1.4',
    'description': 'Lucuma core package for the Gemini Automated Scheduler at: https://github.com/gemini-hlsw/scheduler',
    'long_description': "Lucupy\n#########\n\nThis package contains data structures and functions to support all the microservices that make up the Schedule app\nfor the Gemini Program Plataform (and other auxiliary services such as Env and Resource)\n\nContent\n-------\n\n- Minimodel: A small version of GPP's data model. This allows for any services to use common data structures to model programs, observations, etc.\n- Helpers: A collection of functions that helps with the handling of data.\n- Observatory: An API that allows Observatory-specific behaviour to be added to a service (or sub-service: e.g Collector)\n- Sky: A library that calculates night events for the use of visibility in Observations\n- Time Utils: Time handling functions\n- Types: A collection of variables to use with Python typing\n- Decorators: A collection of decorators (Currently empty)\n\nCopyright (c) 2016-2022 Association of Universities for Research in Astronomy, Inc. (AURA)\nFor license information see LICENSE or https://opensource.org/licenses/BSD-3-Clause\n",
    'author': 'Sergio Troncoso',
    'author_email': 'sergio.troncoso@noirlab.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gemini-hlsw/lucupy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
