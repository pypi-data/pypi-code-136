# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['video_io', 'video_io.client']

package_data = \
{'': ['*']}

install_requires = \
['jmespath>=1.0.1,<2.0.0',
 'opencv-python>=4.6.0',
 'tenacity>=8.1.0,<9.0.0',
 'urllib3>=1.26.12,<2.0.0',
 'wf-cv-utils>=3.4.0',
 'wf-fastapi-auth0>=1.0',
 'wf-honeycomb-io>=2.0.0']

setup_kwargs = {
    'name': 'wf-video-io',
    'version': '3.2.0',
    'description': 'Library for working with video files and interacting with the wildflower video-service',
    'long_description': '# video_io\n\nTools for accessing Wildflower video data\n\n## Task list\n* Add ability to request concatenation of videos\n',
    'author': 'Paul J DeCoursey',
    'author_email': 'paul@decoursey.net>, Theodore Quinn <ted.quinn@wildflowerschools.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
