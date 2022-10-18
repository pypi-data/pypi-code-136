# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysolarfocus', 'pysolarfocus.components', 'pysolarfocus.components.base']

package_data = \
{'': ['*']}

install_requires = \
['pymodbus==2.5.3']

setup_kwargs = {
    'name': 'pysolarfocus',
    'version': '2.0.4',
    'description': 'Unofficial, local Solarfocus client',
    'long_description': "# pysolarfocus: Python Client for Solarfocus eco<sup>_manager-touch_</sup>\n\n## What's Supported \n\n### Software Version\n\nThis integration has been tested with Solarfocus eco<sup>manager-touch</sup> version `21.040`.\n\n### Solarfocus Components\n\n| Components | Supported |\n|---|---|\n| Heating Circuit 1 (_Heizkreis_)| :white_check_mark: |\n| Buffer 1 (_Puffer_) | :white_check_mark: |\n| Solar (_Solar_)| :x:|\n| Boiler 1 (_Boiler_) | :white_check_mark: |\n| Heatpump (_Wärmepumpe_) | :white_check_mark: |\n| Biomassboiler (_Kessel_) | :white_check_mark: | \n\n_Note: The number of supported Heating Circuits, Buffers, and Boilers could be extended in the future_\n\n## Usage\n\n```python\nfrom pymodbus.client import ModbusTcpClient as ModbusClient\nfrom pysolarfocus import SolarfocusAPI,PORT,Systems\n\n# Create a Modbus client\nclient = ModbusClient(IP, port=PORT)\nclient.connect()\n\n# Create the Solarfocus API client\nsolarfocus = SolarfocusAPI(client, Systems.Vampair)\n\n# Fetch the values\nsolarfocus.update()\n\n# Print the values\nprint(solarfocus.buffer)\nprint(solarfocus.heating_circuit)\n```\n",
    'author': 'Jeroen Laverman',
    'author_email': 'jjlaverman@web.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lavermanjj/pysolarfocus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
