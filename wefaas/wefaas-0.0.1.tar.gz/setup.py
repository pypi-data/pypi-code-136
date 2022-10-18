# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wefaas', 'wefaas.api', 'wefaas.components', 'wefaas.core', 'wefaas.export']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.85.1,<0.86.0',
 'pydantic>=1.10.2,<2.0.0',
 'typer>=0.6.1,<0.7.0',
 'uvicorn>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['wefaas_cli = wefaas.cli:cli']}

setup_kwargs = {
    'name': 'wefaas',
    'version': '0.0.1',
    'description': 'Turn python function into microservice.',
    'long_description': '<!-- markdownlint-disable MD033 MD041 -->\n<h1 align="center">\n    wefass\n</h1>\n\n<p align="center">\n    <strong>Instantly turn your Python function into production-ready microservice.</strong>\n</p>\n\n<p align="center">\n    <a href="https://pypi.org/project/wefaas/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/wefaas?color=green&style=flat"></a>\n    <a href="https://pypi.org/project/wefaas/" title="Python Version"><img src="https://img.shields.io/badge/Python-3.8%2B-blue&style=flat"></a>\n    <a href="https://github.com/weanalyze/orpyter/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-Apache2.0-blue.svg"></a>\n</p>\n\n<p align="center">\n  <a href="#getting-started">Getting Started</a> •\n  <a href="#license">License</a> •\n  <a href="https://github.com/weanalyze/orpyter/releases">Changelog</a>\n</p>\n\nInstantly turn your Python function into production-ready microservice. \n\n<sup>Pre-alpha Version: Not feature-complete and only suggested for experimental usage.</sup>\n\n---\n\n## Highlights\n\n- \U0001fa84&nbsp; Turn functions into production-ready services within seconds.\n- 🔌&nbsp; Auto-generated HTTP API based on FastAPI.\n- 📦&nbsp; Deploy microservice into weanalye FaaS cloud.\n- 🧩&nbsp; Reuse pre-defined templates & combine with existing components.\n- 📈&nbsp; Instantly deploy and scale for production usage.\n\n## Getting Started\n\n### Installation\n\n> _Requirements: Python 3.8+._\n\n```bash\npip install wefaas\n```\n\n### Usage\n\n1. A simple orpyter-compatible function could look like this:\n\n    ```python\n    from pydantic import BaseModel\n\n    class Input(BaseModel):\n        message: str\n\n    class Output(BaseModel):\n        message: str\n\n    def hello_world(input: Input) -> Output:\n        """Returns the `message` of the input data."""\n        return Output(message=input.message)\n    ```\n\n    _💡 An wefaas-compatible function is required to have an `input` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The input and output models are specified via [type hints](https://docs.python.org/3/library/typing.html)._\n\n2. Copy this code to a file, e.g. `my_function.py`\n3. Run the HTTP API server from command-line:\n\n    ```bash\n    wefaas serve my_function:hello_world\n    ```\n    _In the output, there\'s a line that shows where your web service is being served, on your local machine._\n4. Deploy the service into weanalyze cloud from command-line:\n\n    ```bash\n    wefass login -u admin --gateway faas.weanalyze.co\n    wefaas deploy my_function:hello_world \n    ```\n    _In the output, there\'s a line that shows where your web service is being served, on your local machine._\n5. Find out more usage information in the [Features](#features) section or get inspired by our [examples](#examples).\n\n## License\n\nApache-2.0 License.\n',
    'author': 'jiandong',
    'author_email': 'jiandong@weanalyze.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
