# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['myccli', 'myccli.terraform', 'myccli.terraform.resources']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.70,<2.0.0',
 'dnspython>=2.2.1,<3.0.0',
 'myc>=0.1.2,<0.2.0',
 'requests>=2.28.1,<3.0.0',
 'toml>=0.10.2,<0.11.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['myc = myccli.main:run_cli']}

setup_kwargs = {
    'name': 'myccli',
    'version': '0.1.4',
    'description': 'Mycelium CLI',
    'long_description': 'Mycelium CLI\n============\n\n### What is Mycelium?\n\nMycelium is a framework that helps you easily write highly scalable (microservice) applications.\n\nMycelium automatically generates **Terraform** from your code, and handles load balancing for you.\n\nThe goal is to write your code without thinking about the infrastructure as if it was a simple monolithic application, and then have Mycelium decide on how to split your app into components, handle load balancing, communication between components, etc...\n\n### How to use Mycelium?\nImport this [runtime library](https://github.com/BizarreCake/myc) into your app and use it to annotate your code with service hints/constraints.\n\nThe more this framework evolves, the less help you will have to give in the form annotations.\n\nFinally, invoke this CLI (`myc` command) and watch it automatically generate Terraform for you (and optionally deploy it for you).\n\n### Example Usage\n\nCreate an empty Poetry application with `myc` (runtime) as dependency and `myccli` (compiler) as a development dependency.\n\nAdd some package (e.g. `test_app`) to your project with `__init__.py` containing:\n\n```python\nfrom myc import Mycelium\n\napp = Mycelium()\nfoo_service = app.create_service("foo")\nbar_service = app.create_service("bar")\n\n@foo_service.fastapi.get("/")\ndef foo():\n    return f\'The answer is: {bar()}\'\n\n@bar_service.fastapi.get("/")\ndef bar():\n    return 42\n```\n\nThen run `myc compile test_app:app` to generate Terraform, followed by `myc deploy` to deploy your app!\n\nWhat will happen:\n* A Dockerfile will be generated for each service\n* Docker images will be built and pushed to a private ECR repository\n    * *Temporary caveat*: The framework expects you to have a repository called `mycelium` in your AWS region of choice (an update will come soon to have this repo created automatically)\n* Two ECS services will be created in a new cluster for `foo` and `bar` services.\n* The call to `bar()` in `foo` function will be transformed to an HTTP get request!\n\n### Limitations\n\nThis project is in its earliest stages, and feature count is limited at the moment.\nThe framework (currently) assumes projects to use Poetry as a package manager\n\n#### Currently supported features:\n* AWS as a cloud provider\n* ECS as a platform in AWS (Lambda support will come very soon)\n* Poetry as the package manager\n\nMore will come soon!\n\n### Upcoming Features\n\n* Dynamic and static load measurements to determine optimal load balancing strategy\n* Support more cloud providers: Google Cloud, Azure, etc...\n* Support more service platforms: AWS Lambda, EC2, etc...\n* Support more package managers other than Poetry\n* Flexible serialization/deserialization strategies\n* Command to launch dashboard to watch:\n    * Service topology\n    * Aggregated logs\n    * Load balancing metrics\n',
    'author': 'Jacob Zhitomirsky',
    'author_email': 'bizarrecake@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/BizarreCake/myccli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
