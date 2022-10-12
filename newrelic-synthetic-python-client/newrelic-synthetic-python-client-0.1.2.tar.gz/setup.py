# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['newrelic',
 'newrelic.cli',
 'newrelic.nerdgraph',
 'newrelic.nerdgraph.synthetic',
 'newrelic.synthetic',
 'newrelic.utils']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['newrelic = newrelic.cli.entrypoint:main']}

setup_kwargs = {
    'name': 'newrelic-synthetic-python-client',
    'version': '0.1.2',
    'description': 'NewRelic CLI',
    'long_description': '# newrelic-synthetic-python-client\nPython lib to interact with New Relic Synthetic Monitors API using NerdGraph\n\n# Installation\n\n## Environment\n- Python 3.8 +\n- Poetry\n\n## Development\n\n```\npython3 -m venv .venv\nsource ./venv/bin/activate\n```\n\nVerify the poetry is using the virutalenv\n```\npoetry env info\n\nVirtualenv\nPython:         3.8.13\nImplementation: CPython\nPath:           /Users/the/path/of/newrelic-synthetic-python-client/.venv\nValid:          True\n\nSystem\nPlatform: darwin\nOS:       posix\nPython:   /opt/homebrew/opt/python@3.8/bin/../Frameworks/Python.framework/Versions/3.8\n```\n\nInstall the dependencies\n\n```\npoetry install\n```\n\nThis will install all the dev/non-dev dependencies.\n\n# Usage Example\n\n## Configuration file\n\nThe configuration file contains the information to interact with NewRelic API endpoint, either via RESTFul API or Graphql.\n\nCreate a JSON file contains the API Key, the example is like the following\n```json\n{\n    "endpoint": "https://api.newrelic.com/graphql",\n    "api_key": "<user_api_key>",\n    "account_id": "<numeric_account_id>"\n}\n```\nLet\'s say the file is located at `$HOME/my-account.json`. To use this file, you need to specify it in the environment variable `NEWRELIC_PYTHON_CLIENT_JSON`\n```\nexport NEWRELIC_PYTHON_CLIENT_JSON=.config/wats-ng-dev.json \n```\n\n### Configuration file places\n\nSearch order\n1. `$HOME/.newrelic-python-client.json`\n2. `$HOME/.config/newrelic-python-client.json`\n3. `$CWD/newrelic-python-client.json`\n4. Specified by environment `$NEWRELIC_PYTHON_CLIENT_JSON`\n\nThe one with larger number will overwrite the one with smaller number.\n\n1. You can put the JSON configuration file to `$HOME/.newrelic-python-client.json` and the configuration will take effect.\n2. And then you add a new file in `$HOME/.config/newrelic-python-client.json`, and this one will take effect, `$HOME/.newrelic-python-client.json` will no longer take effect.\n3. Then you add a new file in `$CWD/newrelic-python-client.json`, then only this one will take effect.\n4. And finally, if you specify the file by environment variable, the environment variable become the only one that take effect.\n\n## Log level\n\nThe default log level is set to "INFO". You can change it by updating the environment variable `NR_LOG_LEVEL`.\n\nThe possible log levels are\n- TRACE\n- DEBUG\n- INFO\n- WARNING\n- ERROR\n\nThe full list can be found in [loguru document](https://loguru.readthedocs.io/en/stable/api/logger.html) the "The severity levels" section.\n\nThe following command set the log level to TRACE and run the script.\n```\nNR_LOG_LEVEL="TRACE" python src/newrelic.py synthetic secure_credential put --key SPS_ID_TOKEN --value 123  \n```\n\n\n## Secure Credential\n### List secure credentials\n```\npython src/newrelic.py synthetic secure_credential list\n```\n\n### Update or Create secure credentials\n\n```\npython src/newrelic.py synthetic secure_credential put --key SPS_ID_TOKEN --value 123\n```\nIf the key `SPS_ID_TOKEN` already exist in your secure credentials storage, this command will update the existing credential. If the key does not exist, this command will create a new credential.\n\n## Scripted Browser Monitors\n\n### List scripted browser monitors\n\n```\nNR_LOG_LEVEL="TRACE" python src/newrelic.py synthetic scripted_browser list\n```\n\n### Update or Create scripted browser monitor\n\n```\nNR_LOG_LEVEL="INFO" python src/newrelic.py synthetic scripted_browser put --monitor-name "AUTO CREATE" \n```\n',
    'author': 'Junkai Zhang',
    'author_email': 'junkai.zhang@watchguard.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Drinkey/newrelic-synthetic-python-client',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
