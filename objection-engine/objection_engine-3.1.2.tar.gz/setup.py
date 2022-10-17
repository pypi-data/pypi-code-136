# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['objection_engine', 'objection_engine.beans']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.1.0,<10.0.0',
 'ffmpeg-python>=0.2.0,<0.3.0',
 'fonttools>=4.33.3,<5.0.0',
 'google-cloud-translate>=2.0.1,<3.0.0',
 'matplotlib>=3.5.1,<4.0.0',
 'moviepy>=1.0.3,<2.0.0',
 'numpy>=1.19.3,<2.0.0',
 'opencv-python>=4.5.5,<5.0.0',
 'praw>=7.5.0,<8.0.0',
 'pydub>=0.25.1,<0.26.0',
 'spacy>=3.1.4,<4.0.0',
 'spaw>=0.2,<0.3',
 'textblob>=0.17.1,<0.18.0',
 'tinydb>=4.7.0,<5.0.0']

setup_kwargs = {
    'name': 'objection-engine',
    'version': '3.1.2',
    'description': 'Library that turns comment chains into ace attorney scenes, used in several bots',
    'long_description': 'None',
    'author': 'Luis Mayo Valbuena',
    'author_email': 'luismayovalbuena@outlook.es',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
