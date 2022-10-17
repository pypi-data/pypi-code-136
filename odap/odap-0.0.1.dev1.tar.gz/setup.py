# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['odap', 'odap.common', 'odap.feature_factory', 'odap.segment_factory']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'odap',
    'version': '0.0.1.dev1',
    'description': 'ODAP framework',
    'long_description': "# ODAP Framework\n\n## Overview\n\nODAP is a lightweight framework for writing features, creating and exporting\nsegments to various destinations (e.g. Facebook, Salesforce, etc.)\n\nBoth SQL and Pyspark syntax is supported.\n\nIt's build on top of the Databricks platform.\n\nYou can try the framework right now by cloning [demo project](https://github.com/DataSentics/features-factory-demo) to your Databricks Workspace.\n\n## Documentation\nFor documentation see [ODAP Documentation](https://datasentics.notion.site/ODAP-framework-f6ed0a95140d48c69b642b568c6db85f).\n\n## Development\nThere are two main components (sub-packages)\n- `feature_factory` - responsible for features development and orchestration\n- `segment_factory` - responsible for segments creation and exports\n\n### DBR & Python\nDBR 10.4+ with python 3.8+ are supported\n\n### Dependency management\nUse `poetry` as main dependency management tool\n\n### Linting & Formatting\n- pylint\n- pyre-check\n- black\n\n### Code style\n- functions-only python (no dependency injection)\n- try to avoid classes as much as possible\n- data classes are OK\n- no `__init__.py` files\n- keep the `src` directory in root\n- project config is raw YAML\n- use type hinting as much as possible\n",
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
