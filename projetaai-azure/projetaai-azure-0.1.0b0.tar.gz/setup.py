# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['projetaai_azure',
 'projetaai_azure.cli',
 'projetaai_azure.converters',
 'projetaai_azure.runners',
 'projetaai_azure.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'adlfs>=2022.9.1,<2023.0.0',
 'azure-ai-ml==0.1.0b4',
 'azure-cli==2.36.0',
 'azureml-core==1.45.0',
 'azureml-pipeline-core==1.45.0',
 'click>=8.1.3,<9.0.0',
 'kedro-projetaai==0.1.0b1',
 'kedro>=0.18.2,<0.19.0',
 'pandas>=1.3,<2.0',
 'pyarrow>=9.0.0,<10.0.0',
 'requirements-parser>=0.5.0,<0.6.0',
 'tomli>=2.0.1,<3.0.0',
 'typing-extensions>=4.3.0,<5.0.0',
 'universal-pathlib>=0.0.20,<0.0.21']

extras_require = \
{':platform_system == "Windows"': ['pywin32>=304,<305']}

entry_points = \
{'projetaai.ci': ['azure = projetaai_azure.plugin:ci_starters'],
 'projetaai.cli': ['azure = projetaai_azure.plugin:AzureCLI']}

setup_kwargs = {
    'name': 'projetaai-azure',
    'version': '0.1.0b0',
    'description': 'Enables Azure services integration with ProjetaAi/Kedro',
    'long_description': '# ProjetaAi Azure\nProjetaAi plugin to enable Kedro integration with Azure services.\n\n## Wip\n\n- Credential assignment\n- Batch endpoint\n- Realtime endpoint\n\n## Usable\n\n- Blob Gen2 credential registration: `kedro credential create azure`\n    - Datastore credential retrivial when running a pipeline in AzureML\n- Pipeline conversion: `kedro pipeline create azure`\n    - Environment creation (gets updated automatically)\n    - Drafts gets updated too\n- Scheduling (weekly): `kedro pipeline azure schedule`\n    - Requires pipeline to be published\n    - Updates current schedule if exists\n- Draft publishing: `kedro pipeline azure publish`\n    - Updates endpoint default pipeline after first call\n    - Forwards schedules if current published exists\n\n> Use `--help` with any of these commands in order to know what arguments are required\n',
    'author': 'Ipiranga',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
