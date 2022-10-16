# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['secrets_env', 'secrets_env.auth', 'secrets_env.cli', 'secrets_env.config']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'hvac>=0.11.2,<0.12.0',
 'keyring>=23.3.0,<24.0.0',
 'requests>=2.21.0,<3.0.0']

extras_require = \
{'all': ['PyYAML>=5.1.2,<7'],
 'all:python_version < "3.11"': ['tomli>=1.1.0,<3'],
 'toml:python_version < "3.11"': ['tomli>=1.1.0,<3'],
 'yaml': ['PyYAML>=5.1.2,<7']}

entry_points = \
{'console_scripts': ['secrets.env = secrets_env.cli:main'],
 'poetry.application.plugin': ['poetry-secrets-env-plugin = '
                               'secrets_env.poetry:SecretsEnvPlugin']}

setup_kwargs = {
    'name': 'secrets-env',
    'version': '0.9.0',
    'description': 'Put secrets from Vault to environment variables',
    'long_description': '# Secrets.env 🔓\n\n[![PyPI version](https://img.shields.io/pypi/v/secrets.env)](https://pypi.org/project/secrets.env/)\n![Python version](https://img.shields.io/pypi/pyversions/secrets.env)\n[![test result](https://img.shields.io/github/workflow/status/tzing/secrets.env/Tests)](https://github.com/tzing/secrets.env/actions/workflows/test.yml)\n\nPut secrets from [Vault](https://www.vaultproject.io/) KV engine to environment variables like a `.env` loader, without not landing data on disk.\n\n![screenshot](./docs/screenshot.png)\n\nSecurity is important, but don\'t want it to be a stumbling block. We love secret manager, but the practice of getting secrets for local development could be a trouble.\n\nThis app is built to *plug in* secrets into development without landing data on disk, easily reproduce the environment, and reduce the risk of uploading the secrets to the server.\n\n\n## Usage\n\nInstall, add config, and run.\n\n### Install\n\nThis app is available on [PyPI](https://pypi.org/project/secrets.env/):\n\n```bash\n# simple install\npip install secrets.env -E all\n\n# OR add as poetry global plugin\npoetry self add secrets.env -E toml\n```\n\nFolowing extras avaliable:\n\n* `all` - *install everything below*\n* `yaml` - supporting YAML config\n* `toml` - supporting TOML config, includes `pyproject.toml`\n\nIf none of them are selected, this app only supports the config in JSON format.\n\n### Add config\n\nThis app could read vault URL and authentication information from various source:\n\n```bash\nexport SECRETS_ENV_ADDR=\'https://example.com\'\nexport SECRETS_ENV_METHOD=\'token\'\nexport SECRETS_ENV_TOKEN=\'example-token\'\n```\n\nBut we must list the desired secret path and key in the config file:\n\n```json\n{\n  "secrets": {\n    "EXAMPLE": {\n      "path": "secrets/example",\n      "key": "foo"\n    }\n  }\n}\n```\n\n**Read \'Configure\' section below for more details.**\n\n### Run\n\nThis app could be used as a command line tool, or a [poetry plugin](https://python-poetry.org/docs/master/plugins/).\n\n* As a CLI tool\n\n  ```bash\n  secrets.env run -- some-app-that-needs-secret --args foo bar\n  ```\n\n  It loads the secrets, run the command, then forget the secrets.\n\n* As a poetry plugin\n\n  ```bash\n  poetry run some-app-that-needs-secret --args foo bar\n  ```\n\n  This app will pull the secrets from vault on poetry command [run](https://python-poetry.org/docs/cli/#run) and [shell](https://python-poetry.org/docs/cli/#shell).\n\n\n\n## Configure\n\n### Configuration file\n\nThis app searches for the file that matches following names in the current working directory and parent folders, and load the config from it. When there are more than one exists, the first one would be selected according to the order here:\n\n1. `.secrets-env.toml`[^1]\n2. `.secrets-env.yaml`[^2]\n3. `.secrets-env.yml`[^2]\n4. `.secrets-env.json`\n5. `pyproject.toml`[^1]\n\n[^1]: TOML format is only supported when either [tomllib](https://docs.python.org/3.11/library/tomllib.html) or [tomli](https://pypi.org/project/tomli/) is installed.\n[^2]: YAML format is only supported when [PyYAML](https://pypi.org/project/PyYAML/) is installed.\n\nAn example config in YAML format:\n\n```yaml\n# `source` configured the connection info to vault.\n# All values in this section could be overwritten by environment variable, so\n# it is possible to run secrets.env app without this section.\nsource:\n  # Address to vault\n  # Could be replaced using environment variable `SECRETS_ENV_ADDR` or `VAULT_ADDR`\n  url: https://example.com/\n\n  # Authentication info\n  # Schema for authentication could be complex, read section below.\n  auth:\n    method: okta\n    username: user@example.com\n\n  # Transport layer security (TLS) configurations.\n  # All keys under this section are optional.\n  tls:\n    # Server side certificate for verifying responses.\n    ca_cert: /path/ca.cert\n\n    # Client side certificate for communicating with vault server.\n    client_cert: /path/client.cert\n    client_key: /path/client.key\n\n# `secrets` lists the environment variable name, and the path the get the secret value\nsecrets:\n  # The key (VAR1) is the environment variable name to install the secret\n  VAR1:\n    # Path to read secret from vault\n    path: kv/default\n\n    # Path to identify which value to extract, as we may have multiple values in\n    # single secret in KV engine.\n    # For nested structure, join the keys with dots.\n    key: example.to.value\n\n  # Syntax sugar: path#key\n  VAR2: "kv/default#example.to.value"\n```\n\n> For most supported file format, they shared the same schema to this example. The only different is [`pyproject.toml`](./example/pyproject.toml) format- each section must placed under `tool.secrets-env` section.\n> Visit [example folder](./example/) to read the equivalent expression in each format.\n\n### Authentication\n\nVault enforce authentication during requests, so we must provide the identity in order to get the secrets.\n\n*Method*\n\nSecrets.env adapts several authentication methods. You must specify the method by either config file or the environment variable `SECRETS_ENV_METHOD`. Here\'s the format in config file:\n\n```yaml\n---\n# standard layout\n# arguments could be included in `auth:`\nsource:\n  auth:\n    method: okta\n    username: user@example.com\n\n---\n# alternative layout\n# arguments must be avaliable in other source\nsource:\n  auth: token\n```\n\n*Arguments*\n\nAuth data could be provided by various source, including:\n\n* **Config file:** Place the config value under `auth` section, use the key provided in the table.\n* **Environment variable:** In most cases, environment variable could be used to overwrite the values from config file.\n* **Keyring:** We\'re using [keyring] package to read the values from system keyring (e.g. macOS [Keychain]). For saving a value into keyring, use its [command line utility] with the system name `secrets.env`:\n\n  ```bash\n  keyring get secrets.env token/:token\n  keyring set secrets.env okta/test@example.com\n  ```\n\n  [keyring]: https://keyring.readthedocs.io/en/latest/\n  [Keychain]: https://en.wikipedia.org/wiki/Keychain_%28software%29\n  [command line utility]: https://keyring.readthedocs.io/en/latest/#command-line-utility\n\n* **Prompt:** If no data found in all other sources, it prompts user for input. You can disable it by setting environment variable `SECRETS_ENV_NO_PROMPT=True`.\n\n#### Supported methods\n\nHere\'s the argument(s), their accepted source, and corresponding keys.\n\n##### method: `token`\n\n| key   | config file | environment variable               | keyring        | helper |\n| ----- | ----------- | ---------------------------------- | -------------- | ------ |\n| token | ⛔️          | `SECRETS_ENV_TOKEN`, `VAULT_TOKEN`  | `token/:token` | ✅     |\n\n*[Token helper](https://www.vaultproject.io/docs/commands/token-helper)*: Vault CLI stores the generated token in the `~/.vault-token` file after authenticated. This app reads the token from that file, but it do not create one on authenticating using this app.\n\nTo use the helper, you can use command [`vault login`](https://www.vaultproject.io/docs/commands/login) to create one.\n\n##### method: `okta`\n\n| key      | config file | environment variable   | keyring               | prompt |\n| -------- | ----------- | ---------------------- | --------------------- | ------ |\n| username | `username`  | `SECRETS_ENV_USERNAME` | `okta/:username`      | ✅     |\n| password | ⛔️          | `SECRETS_ENV_PASSWORD` | `okta/YOUR_USER_NAME` | ✅     |\n',
    'author': 'tzing',
    'author_email': 'tzingshih@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tzing/secrets.env',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
