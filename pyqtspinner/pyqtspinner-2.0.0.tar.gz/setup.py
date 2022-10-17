# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyqtspinner']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>5.8']

entry_points = \
{'console_scripts': ['pyqtspinner-conf = pyqtspinner.configurator:main']}

setup_kwargs = {
    'name': 'pyqtspinner',
    'version': '2.0.0',
    'description': 'Waiting spinner for PyQt5',
    'long_description': '# QtWaitingSpinner\n\n[![PyPI version](https://badge.fury.io/py/pyqtspinner.svg)](https://badge.fury.io/py/pyqtspinner)\n\nQtWaitingSpinner is a highly configurable, custom Qt widget for showing "waiting" or\n"loading" spinner icons in Qt applications, e.g. the spinners below are all\nQtWaitingSpinner widgets differing only in their configuration:\n\n![waiting spinner](https://raw.githubusercontent.com/z3ntu/QtWaitingSpinner/gh-pages/waiting-spinners.gif)\n\nThe widget is pretty customizable:\n\n![examples](https://raw.githubusercontent.com/fbjorn/QtWaitingSpinner/master/static/examples.png)\n\n### Installation\n\n`pip install pyqtspinner`\n\n### Configuration\n\nThe following properties can all be controlled directly through their corresponding\nsetters:\n\n- Color of the widget\n- "Roundness" of the lines\n- Speed (rotations per second)\n- Number of lines to be drawn\n- Line length\n- Line width\n- Radius of the spinner\'s "dead space" or inner circle\n- The percentage fade of the "trail"\n- The minimum opacity of the "trail"\n\n### Usage\n\nYou can easily adjust spinner settings by running:\n\n```bash\npyqtspinner-conf\n```\n\n![configuration](https://raw.githubusercontent.com/fbjorn/QtWaitingSpinner/master/static/config.png)\n\nMake the spinner you would like and press "show init args" button. It will generate the\ncode snippet which is almost ready-to-use:\n\n```python\nWaitingSpinner(\n    parent,\n    roundness=100.0,\n    opacity=3.141592653589793,\n    fade=80.0,\n    radius=10,\n    lines=20,\n    line_length=10,\n    line_width=2,\n    speed=1.5707963267948966,\n    color=(0, 0, 0)\n)\n```\n\nAs an alternative example, the code below will create a spinner that (1) blocks all user\ninput to the main application for as long as the spinner is active, (2) automatically\ncenters itself on its parent widget every time "start" is called and (3) makes use of\nthe default shape, size and color settings.\n\n```python\nspinner = QtWaitingSpinner(self, True, True, Qt.ApplicationModal)\nspinner.start() # starts spinning\n```\n\nEnjoy!\n\n### Thanks:\n\nto [@z3ntu](https://github.com/z3ntu) for the groundwork. to\n[@snowwlex](https://github.com/snowwlex) for the widget itself.\n',
    'author': 'Denis',
    'author_email': 'fbjorn@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fbjorn/QtWaitingSpinner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
