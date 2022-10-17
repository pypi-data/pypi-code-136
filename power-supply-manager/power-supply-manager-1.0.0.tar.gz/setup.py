# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['power_supply_manager']

package_data = \
{'': ['*']}

install_requires = \
['coloredlogs>=15.0.1,<16.0.0',
 'dearpygui==1.6.2',
 'matplotlib>=3.6.0,<4.0.0',
 'python-vxi11>=0.9,<0.10']

entry_points = \
{'console_scripts': ['power-supply-manager = '
                     'power_supply_manager.power_supply_manager:app',
                     'psm = power_supply_manager.power_supply_manager:app']}

setup_kwargs = {
    'name': 'power-supply-manager',
    'version': '1.0.0',
    'description': 'Power Supply Manager',
    'long_description': '# Power Supply Manager\n\n\n![](./power_supply_manager_1.png)\n![](./power_supply_manager_2.png)\n\n## Description\nControl multiple networked power supplies from the same graphical application. Features:\n\n* Connect to multiple bench-top power supply units over Ethernet (VXI11 or LXI protocols)\n* Four ways to control power output:\n  * Individual channels\n  * Group any combination of channels to power simultaneously\n  * Define power on/off sequences with configurable time delays in between\n  * Power all channels on/off simultaneously\n* Real-time plots showing voltage and current measurements from each channel.\n* Set voltage, current, over-voltage protection, over-current protection, and 4-wire control settings.\n* Log voltage and current measurements to CSV files.\n* Save and load multi-device configuration files to quickly restore settings.\n\n## Installation\n\n### Install from PyPI (recommended)\n\n1. Install pip package:\n  ```\n  pip install power-supply-manager\n  ```\n\n  Make sure the pip installation directory is on your system PATH:\n  * Linux / MacOS: Typically `$HOME/.local/bin`, `/usr/bin`, or `/usr/local/bin`\n  * Windows: Typically `<Python install dir>\\Scripts` or `C:\\Users\\<username>\\AppData\\Roaming\\Python\\Python<vers>\\Scripts`\n\n2. Run application:\n  ```\n  power-supply-manager\n  ```\n\n### Install from GitLab\n\n1. Install the repository:\n\n  ```\n  git clone https://gitlab.com/d7406/power-supply-manager.git\n  ```\n2. Install [Poetry](https://python-poetry.org)\n3. Setup virtual environment using Poetry:\n  ```\n  poetry install\n  ```\n4. Run application:\n  ```\n  poetry run python power_supply_manager/power_supply_manager.py\n  ```\n\n## Contributing\nWe welcome contributions and suggestions to improve this application. Please submit an issue or merge request [here](https://gitlab.com/d7406/power-supply-manager)\n\n## Authors and acknowledgment\n[DevBuildZero, LLC](http://devbuildzero.com)\n\n## License\nThis software is provided for free under the MIT open source license:\n\nCopyright 2022 DevBuildZero, LLC\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of \nthis software and associated documentation files (the "Software"), to deal in \nthe Software without restriction, including without limitation the rights to \nuse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies \nof the Software, and to permit persons to whom the Software is furnished to do \nso, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all \ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR \nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS\nFOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR \nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER \nIN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN \nCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n',
    'author': 'Willie Marchetto',
    'author_email': 'willie@devbuildzero.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
