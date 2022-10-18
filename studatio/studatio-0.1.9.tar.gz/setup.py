# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['studatio', 'studatio._vendor', 'studatio._vendor.icalevents']

package_data = \
{'': ['*'], 'studatio._vendor': ['icalevents-0.1.26.dist-info/*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0', 'pyperclip>=1.8.2,<2.0.0', 'tomlkit>=0.11.4,<0.12.0']

entry_points = \
{'console_scripts': ['studatio = studatio.main:main']}

setup_kwargs = {
    'name': 'studatio',
    'version': '0.1.9',
    'description': 'Personal tool for my violin teaching database',
    'long_description': "# studatio\n\n![PyPI](https://img.shields.io/pypi/v/studatio)\n\nstudatio is a Python tool for private music teachers to manage their studio's data.\n\nI am primarily developing this for my own use as a violin teacher. However, I hope for the project to become useful to\nother teachers. Currently, studatio is meant to pull iCal data about music lessons and format in a way that can be\nuseful for lesson schedules or facility reservations. I want to add support for automated facility reservations,\nbilling, and note-taking.\n\n## Installation\n\nFirst, install Python if it is not already installed. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install studatio.\n\n```bash\npip install studatio\n```\n\nOn first use, studatio will prompt you for a URL containing iCal data of your studio's calendar.\n\n## Usage\n\n```studatio``` prints and copies to clipboard a formatted list of studio events.\n\n## Contributing\n\nTo build, you must install poetry and pre-commit. Pull requests are welcome.\n\nFor major changes, please open an issue first to discuss what you would like to change or add. Documentation and test\ncoverage additions are just as welcome as changes to source code. I am an amateur programmer, but I always want to\nlearn, so if there are things that work but are not best practices, I would be eager to hear them.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n",
    'author': 'Eliza Wilson',
    'author_email': 'elizaaverywilson@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/elizaaverywilson/studatio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
