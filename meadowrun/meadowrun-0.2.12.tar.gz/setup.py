# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['meadowrun',
 'meadowrun._vendor',
 'meadowrun._vendor.aiodocker',
 'meadowrun._vendor.fastcdc',
 'meadowrun._vendor.gcloud',
 'meadowrun._vendor.gcloud.aio',
 'meadowrun._vendor.gcloud.aio.auth',
 'meadowrun._vendor.gcloud.aio.storage',
 'meadowrun._vendor.platformdirs',
 'meadowrun.aws_integration',
 'meadowrun.aws_integration.management_lambdas',
 'meadowrun.azure_integration',
 'meadowrun.azure_integration.mgmt_functions',
 'meadowrun.azure_integration.mgmt_functions.azure_core',
 'meadowrun.azure_integration.mgmt_functions.clean_up',
 'meadowrun.azure_integration.mgmt_functions.vm_adjust',
 'meadowrun.deployment',
 'meadowrun.func_worker',
 'meadowrun.gcp_integration',
 'meadowrun.k8s_integration']

package_data = \
{'': ['*'], 'meadowrun': ['docker_files/*']}

install_requires = \
['aiobotocore>=2.1.2,<3.0.0',
 'aiofiles>=0.6.0,<0.7.0',
 'aiohttp>=3.8.0,<4.0.0',
 'asyncssh>=2.11.0,<3.0.0',
 'backoff>=1.0.0,<3.0.0',
 'boto3>=1.21.21,<2.0.0',
 'chardet>=2.0,<4.1',
 'cloudpickle>=2.0.0,<3.0.0',
 'cryptography>=2.0.0,<37.0.0',
 'filelock>=3.6.0,<4.0.0',
 'future>=0.17.0,<0.18.3',
 'kubernetes-asyncio>=24.2.0,<25.0.0',
 'protobuf>=3.18.1,<4.0.0',
 'psutil>=5.8.0,<6.0.0',
 'pyasn1-modules==0.2.1',
 'pyjwt>=1.5.3,<3.0.0',
 'requests>=2.27.1,<3.0.0',
 'rsa>=3.1.4,<5.0.0',
 'six>=1.11.0,<2.0.0',
 'typing-extensions>=4.1.1,<5.0.0']

entry_points = \
{'console_scripts': ['meadowrun-local = '
                     'meadowrun.run_job_local_main:command_line_main',
                     'meadowrun-manage-azure-vm = '
                     'meadowrun.manage:main_azure_vm',
                     'meadowrun-manage-ec2 = meadowrun.manage:main_ec2']}

setup_kwargs = {
    'name': 'meadowrun',
    'version': '0.2.12',
    'description': 'The easiest way to run python code on one or more remote machines',
    'long_description': "# ![Meadowrun](meadowrun-logo-full.svg)\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/meadowrun) ![PyPI](https://img.shields.io/pypi/v/meadowrun)  ![PyPI - Downloads](https://img.shields.io/pypi/dm/meadowrun) ![Conda](https://img.shields.io/conda/v/meadowdata/meadowrun) ![Conda](https://img.shields.io/conda/dn/meadowdata/meadowrun?label=conda%20downloads)\n\n[![Join the chat at https://gitter.im/meadowdata/meadowrun](https://badges.gitter.im/meadowdata/meadowrun.svg)](https://gitter.im/meadowdata/meadowrun?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n\n\n\nMeadowrun is a library for data scientists and data engineers who run python code on\nAWS, Azure, or Kubernetes. Meadowrun:\n\n- scales from a single function to thousands of distributed tasks.\n- syncs your local code and libraries for a faster, easier iteration loop. Edit your\n  code and rerun your analysis without worrying about building packages or Docker\n  images.\n- optimizes for cost, choosing the cheapest instance types and turning them off when\n  they're no longer needed.\n  \nFor more context, see our [case\nstudes](https://docs.meadowrun.io/en/stable/case_studies/) of how Meadowrun is used in\nreal life, or see the [project homepage](https://meadowrun.io)\n\nTo get started, go to our [documentation](https://docs.meadowrun.io), or [join the chat\non Gitter](https://gitter.im/meadowdata/meadowrun)\n\n## Quickstart\n\nFirst, install Meadowrun using pip:\n\n```\npip install meadowrun\n```\n\nNext, assuming you've [configured the AWS\nCLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)\nand are a root/administrator user, you can run:\n\n```python\nimport meadowrun\nimport asyncio\n\nprint(\n    asyncio.run(\n        meadowrun.run_function(\n            lambda: sum(range(1000)) / 1000,\n            meadowrun.AllocEC2Instance(),\n            meadowrun.Resources(logical_cpu=1, memory_gb=8, max_eviction_rate=80),\n            meadowrun.Deployment.mirror_local()\n        )\n    )\n)\n```\n\n[The documentation](https://docs.meadowrun.io) has examples of how to use other package\nmanagers (conda, poetry), and other platforms (Azure, GKE, Kubernetes).\n",
    'author': 'Richard Lee',
    'author_email': 'hrichardlee@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/meadowdata/meadowrun',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
