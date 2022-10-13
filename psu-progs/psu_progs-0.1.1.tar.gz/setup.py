# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['psu_progs']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'pyserial>=3.5,<4.0']

entry_points = \
{'console_scripts': ['korad-charge-lithium-ion = '
                     'psu_progs.charge_lithium_ion:charge']}

setup_kwargs = {
    'name': 'psu-progs',
    'version': '0.1.1',
    'description': 'CLI tools for Korad power supplies, including lithium ion battery charging',
    'long_description': "# psu-progs\n\n[![PyPI version](https://badge.fury.io/py/psu-progs.svg)](https://badge.fury.io/py/psu-progs)\n\nA collection of utilities to put a computer-connected power supplies to good use.\n\nThe extraordinarily compact collection includes only a CLI tool for charging lithium-ion batteries with a Korad PSU.\n\n\n# Installation\n```shell\npip install psu-progs\n```\n\n# Quick-show-me-a-thing\n```shell\n# Charge a 1400mAh lithium-ion battery, with a Korad PSU connected at /dev/ttyACM0\nkorad-charge-lithium-ion -p /dev/ttyACM0 -c 1.4\n```\n\n# Full command help\n```\nUsage: korad-charge-lithium-ion [OPTIONS]\n\n  Charge a Li-ion battery using a Korad K300XP power supply\n\nOptions:\n  -p, --port DEVICE              Name of serial device the power supply can be\n                                 communicated through, e.g. /dev/ttyACM0\n                                 [default: /dev/ttyUSB1; required]\n  -c, --capacity FLOAT           Labeled capacity of battery, in amp hours.\n                                 [required]\n  --charge-current FLOAT         Current to use while in the constant-current\n                                 charging phase, in amps. If not specified,\n                                 this defaults to half the battery_capacity.\n  --charge-voltage FLOAT         Voltage to use while in constant-voltage\n                                 phase. For Li-ion cells, this value should be\n                                 ≤4.2.  [default: 4.2]\n  --charge-cutoff-ratio FLOAT    Ratio of the charge_current used to derive\n                                 the value of measured output current at which\n                                 to stop charging.  [default: 0.1]\n  --channel INT                  Which channel to output power from (for power\n                                 supplies with multiple channels).  [default:\n                                 0; 0<=x<=1]\n  --num-samples INT              When measuring current, use the average of\n                                 this many number of samples. Using a value\n                                 over 1 is recommended, as anomalous blips may\n                                 be measured. This also addresses low readings\n                                 when output is first enabled.  [default: 3;\n                                 x>=0]\n  --max-successive-failures INT  After this number of continuous errors are\n                                 encountered while attempting to read the\n                                 output current, stop charging.  [default: 5;\n                                 x>=0]\n  --help                         Show this message and exit.\n```\n\n# Developing\nThis package uses poetry for dependency management. To get started hacking around the codebase:\n\n1. Create a new virtualenv (or skip this step and let poetry do it for you)\n2. `pip install poetry`\n3. `poetry install`\n4. Good luck!\n\n# Contributing\nIf you have other utilities you'd like to add, or other PSUs you'd like to support, pull requests are welcomed! I may not be able to physically test all contributions, but I sure can review and merge :)\n",
    'author': 'Zach "theY4Kman" Kanzler',
    'author_email': 'they4kman@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/theY4Kman/psu-progs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
