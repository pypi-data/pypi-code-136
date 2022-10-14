# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tracarbon',
 'tracarbon.cli',
 'tracarbon.emissions',
 'tracarbon.exporters',
 'tracarbon.hardwares',
 'tracarbon.hardwares.data',
 'tracarbon.locations',
 'tracarbon.locations.data']

package_data = \
{'': ['*']}

install_requires = \
['aiocache>=0.11.1,<0.12.0',
 'aiohttp>=3.8.1,<4.0.0',
 'ec2-metadata>=2.10.0,<3.0.0',
 'loguru>=0.6.0,<0.7.0',
 'msgpack>=1.0.4,<2.0.0',
 'psutil>=5.9.1,<6.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'typer>=0.4.1,<0.7.0',
 'ujson>=5.3.0,<6.0.0']

extras_require = \
{'datadog': ['datadog>=0.44.0,<0.45.0'],
 'promotheus': ['prometheus-client>=0.14.1,<0.15.0']}

entry_points = \
{'console_scripts': ['tracarbon = tracarbon.cli:main']}

setup_kwargs = {
    'name': 'tracarbon',
    'version': '0.3.2',
    'description': "Tracarbon is a Python library that tracks your device's energy consumption and calculates your carbon emissions.",
    'long_description': '![Alt text](logo.png?raw=true "Tracarbon logo")\n\n![example workflow](https://github.com/fvaleye/tracarbon/actions/workflows/build.yml/badge.svg)\n[![pypi](https://img.shields.io/pypi/v/tracarbon.svg?style=flat-square)](https://pypi.org/project/tracarbon/)\n[![doc](https://img.shields.io/badge/docs-python-blue.svg?style=for-the-badgee)](https://fvaleye.github.io/tracarbon)\n[![licence](https://img.shields.io/badge/license-Apache--2.0-green)](https://github.com/fvaleye/tracarbon/blob/main/LICENSE.txt)\n\n\n## 📌 Overview\nTracarbon is a Python library that tracks your device\'s energy consumption and calculates your carbon emissions.\n\nIt detects your location and your device automatically before starting to export measurements to an exporter. \nIt could be used as a CLI with already defined metrics or programmatically with the API by defining the metrics that you want to have.\n\nRead more in this [article](https://medium.com/@florian.valeye/tracarbon-track-your-devices-carbon-footprint-fb051fcc9009).\n\n## 📦 Where to get it\n\n```sh\n# Install Tracarbon\npip install tracarbon\n```\n\n```sh\n# Install one or more exporters from the list\npip install \'tracarbon[datadog]\'\n```\n\n### 🔌 Devices: energy consumption\n| **Devices** |                                    **Description**                                    |\n|-------------|:-------------------------------------------------------------------------------------:|\n| Mac         |    ✅ Global energy consumption of your Mac (must be plugged into a wall adapter).     |\n| Linux       | ❌ Not yet implemented. See [#184](https://github.com/hubblo-org/scaphandre/pull/184). |\n| Windows     | ❌ Not yet implemented. See [#184](https://github.com/hubblo-org/scaphandre/pull/184). |\n\n| **Cloud Provider** |                                                                                                  **Description**                                                                                                  |\n|--------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|\n| AWS                | ✅ Use the hardware\'s usage with the EC2 instances carbon emissions datasets of [cloud-carbon-coefficients](https://github.com/cloud-carbon-footprint/cloud-carbon-coefficients/blob/main/data/aws-instances.csv). |\n| GCP                |                                                                                              ❌ Not yet implemented.                                                                                               |\n| Azure              |                                                                                              ❌ Not yet implemented.                                                                                               |\n\n\n## 📡 Exporters\n| **Exporter** |          **Description**          |\n|--------------|:---------------------------------:|\n| Stdout       |   Print the metrics in Stdout.    |\n| JSON         | Write the metrics in a JSON file. |\n| Promotheus   |  Send the metrics to Promotheus.  |\n| Datadog      |   Send the metrics to Datadog.    |\n\n### 🗺️ Locations\n| **Location** |                                                                     **Description**                                                                     | **Source**                                                                                                                                                    |\n|--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| Worldwide    | Get the latest co2g/kwh in near real-time using the CO2 Signal API. See [here](http://api.electricitymap.org/v3/zones) for the list of available zones. | [CO2Signal API](https://www.co2signal.com)                                                                                                                    |\n| Europe       |                        Static file created from the European Environment Agency Emission for the co2g/kwh in European countries.                        | [EEA website](https://www.eea.europa.eu/data-and-maps/daviz/co2-emission-intensity-9#tab-googlechartid_googlechartid_googlechartid_googlechartid_chart_11111) |\n| AWS          |                                                     Static file of the AWS Grid emissions factors.                                                      | [cloud-carbon-coefficients](https://github.com/cloud-carbon-footprint/cloud-carbon-coefficients/blob/main/data/grid-emissions-factors-aws.csv)                |\n\n### ⚙️ Configuration\nThe environment variables can be set from an environment file `.env`.\n\n| **Parameter**                 | **Description**                                                                |\n|-------------------------------|:-------------------------------------------------------------------------------|\n| TRACARBON_CO2SIGNAL_API_KEY   | The api key received from [CO2 Signal](https://www.co2signal.com).             |\n| TRACARBON_METRIC_PREFIX_NAME  | The prefix to use in all the metrics name.                                     |\n| TRACARBON_INTERVAL_IN_SECONDS | The interval in seconds to wait between the metrics evaluation.                |\n| TRACARBON_LOG_LEVEL           | The level to use for displaying the logs.                                      |\n\n## 🔎 Usage\n\n**Request your API key**\n- Go to https://www.co2signal.com/ and get your free API key (for non-commercial use only) for getting the latest carbon intensity from your location in near-real time.\n- Set your API key in the environment variables, in the `.env` file or directly in the configuration.\n- If you would like to start without an API key, it\'s possible, the carbon intensity will be loaded statistically from a file.\n- Launch Tracarbon 🚀\n\n**Command Line**\n```sh\ntracarbon run\n```\n\n**API**\n```python\nfrom tracarbon import TracarbonBuilder, TracarbonConfiguration\n\nconfiguration = TracarbonConfiguration() # Your configuration\ntracarbon = TracarbonBuilder(configuration=configuration).build()\ntracarbon.start()\n# Your code\ntracarbon.stop()\n\nwith tracarbon:\n    # Your code\n```\n\n## 💻 Development\n\n**Local: using Poetry**\n```sh\nmake init\nmake test-unit\n```\n\n## 🛡️ Licence\n[Apache License 2.0](https://raw.githubusercontent.com/fvaleye/tracarbon/main/LICENSE.txt)\n\n## 📚 Documentation\nThe documentation is hosted here: https://fvaleye.github.io/tracarbon/documentation\n',
    'author': 'Florian Valeye',
    'author_email': 'fvaleye@github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
