# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kedro_aim',
 'kedro_aim.aim',
 'kedro_aim.config',
 'kedro_aim.framework',
 'kedro_aim.framework.cli',
 'kedro_aim.framework.hooks',
 'kedro_aim.io',
 'kedro_aim.io.artifacts',
 'kedro_aim.template']

package_data = \
{'': ['*'], 'kedro_aim.template': ['config/*']}

install_requires = \
['aim>=3.14.1,<4.0.0', 'kedro>=0.18.0', 'pydantic>=1.10.2,<2.0.0']

entry_points = \
{'kedro.hooks': ['aim_hook = kedro_aim.framework.hooks.aim_hook:aim_hook'],
 'kedro.project_commands': ['kedro_aim = kedro_aim.framework.cli.cli:commands']}

setup_kwargs = {
    'name': 'kedro-aim',
    'version': '0.1.2',
    'description': 'A plugin to integrate the mlops plattform aim into your kedro project',
    'long_description': '# Kedro Aim\n\n[![PyPI version](https://badge.fury.io/py/kedro-aim.svg)](https://badge.fury.io/py/kedro-aim)\n[![Python version](https://img.shields.io/badge/python-3.8|3.9|3.10-blue.svg)](https://pypi.org/project/kedro/)\n[![Documentation Status](https://readthedocs.org/projects/kedro-aim/badge/?version=latest)](https://kedro-aim.readthedocs.io/en/latest/?badge=latest)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![Publish Package to PyPI](https://github.com/AnH0ang/kedro-aim/actions/workflows/publish.yml/badge.svg)](https://github.com/AnH0ang/kedro-aim/actions/workflows/publish.yml)\n[![Testing](https://github.com/AnH0ang/kedro-aim/actions/workflows/testing.yml/badge.svg)](https://github.com/AnH0ang/kedro-aim/actions/workflows/testing.yml)\n[![codecov](https://codecov.io/gh/AnH0ang/kedro-aim/branch/master/graph/badge.svg?token=X94NV660A9)](https://codecov.io/gh/AnH0ang/kedro-aim)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## 📝 Description\n\n`kedro-aim` is a [kedro-plugin](https://kedro.readthedocs.io/en/stable/extend_kedro/plugins.html) that enables tracking of metrics and parameters with [Aim](https://aimstack.io/) from within Kedro.\nKedro is a great tool for data engineering and data science, but it lacks a clear way to track metrics and parameters.\nAim is a great tool for tracking metrics and parameters, but it lacks a clear way to integrate with Kedro.\nThis plugin aims to solve both problems.\n\n![Aim Screenshot](./static/img/aim-screenshot.png)\n\n## 🎖 Features\n\n- Automatic Registration of Aim `Run` in Data Catalog\n- Tracking of Artifact with Aim DataSet\n- Configuration over `aim.yml`\n\n## ⚙️ Installation\n\nInstall the package with `pip`:\n\n```bash\npip install kedro-aim\n```\n\n## 💡 Usage Examples\n\nThe plugin automatically registers a [Run](https://aimstack.readthedocs.io/en/latest/refs/sdk.html#aim.sdk.run.Run) instance in the DataCatalog under the name `run` which can be accessed by all nodes to log metrics and parameters.\nThis run instance can be used track metrics and parameters in the same way as in any other [python project](https://aimstack.readthedocs.io/en/latest/quick_start/supported_types.html)\n\nFirst you need to initilize the `aim.yml` config file inside your pre-existing Kedro project.\nThis can be done by running the following command:\n\n```shell\nkedro aim init\n```\n\nIn order to use `aim` inside a node you need to pass the run object as a argument of the function.\nInside the function you can access the run object and use it to log metrics and parameters.\n\n```python\n# nodes.py\nimport pandas as pd\nfrom aim import Run\n\n\ndef logging_in_node(run: Run, data: pd.DataFrame) -> None:\n    # track metric\n    run.track(0.5, "score")\n\n    # track parameter\n    run["parameter"] = "abc"\n```\n\nWhen defining the pipeline, you need to pass the `run` dataset as a input to the node.\nThe `run` dataset will be automatically created by `kedro-aim` and added to the DataCatalog.\nAs a result, the `run` dataset will be passed to the node as an argument.\n\n```python\n# pipeline.py\nfrom kedro.pipeline import node, Pipeline\nfrom kedro.pipeline.modular_pipeline import pipeline\n\n\ndef create_pipeline(**kwargs) -> Pipeline:\n    return pipeline(\n        [\n            node(\n                func=logging_in_node,\n                inputs=["run", "input_data"],\n                outputs=None,\n                name="logging_in_node",\n            )\n        ]\n    )\n```\n\n## 🧰 Config File\n\nThe module is configured via the `aim.yml` file which should be placed inside the `conf/base` folder.\nA default config file can be generated using the `kedro aim init` command from the shell.\n\nYou can enable the schema validation in your VSCode IDE to enable real-time validation, autocompletion and see information about the different fields in your catalog as you write it. To enable this, make sure you have the [YAML plugin](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) installed.\nThen enter the following in your `settings.json` file:\n\n```json\n{\n  "yaml.schemas": {\n    "https://raw.githubusercontent.com/AnH0ang/kedro-aim/master/static/jsonschema/kedro_aim_schema.json": "**/*aim*.yml"\n  }\n}\n```\n\n## 🙏 Acknowledgement\n\nThis project was inspired by the work of [kedro-mlflow](https://github.com/Galileo-Galilei/kedro-mlflow) which is a plugin for Kedro that enables tracking of metrics and parameters with [MLflow](https://mlflow.org/) from within Kedro.\n',
    'author': 'An Hoang',
    'author_email': 'anhoang31415@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://kedro-aim.readthedocs.io',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
