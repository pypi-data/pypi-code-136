# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skyplane',
 'skyplane.cli',
 'skyplane.cli.cli_impl',
 'skyplane.cli.experiments',
 'skyplane.cli.usage',
 'skyplane.compute',
 'skyplane.compute.aws',
 'skyplane.compute.azure',
 'skyplane.compute.gcp',
 'skyplane.gateway',
 'skyplane.obj_store',
 'skyplane.replicate',
 'skyplane.utils']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=4.1.0',
 'pandas>=1.0.0',
 'paramiko>=2.7.2',
 'rich>=9.0.0',
 'sshtunnel>=0.3.0',
 'typer>=0.4.0']

extras_require = \
{':extra == "aws" or extra == "all"': ['boto3>=1.16.0'],
 'all': ['azure-identity>=1.0.0',
         'azure-mgmt-authorization>=1.0.0',
         'azure-mgmt-compute>=24.0.0',
         'azure-mgmt-network>=10.0.0',
         'azure-mgmt-resource>=11.0.0',
         'azure-mgmt-storage>=11.0.0',
         'azure-mgmt-subscription>=1.0.0',
         'azure-storage-blob>=12.0.0',
         'google-api-python-client>=2.0.2',
         'google-auth>=2.0.0',
         'google-cloud-compute>=1.0.0',
         'google-cloud-storage>=1.30.0'],
 'azure': ['azure-identity>=1.0.0',
           'azure-mgmt-authorization>=1.0.0',
           'azure-mgmt-compute>=24.0.0',
           'azure-mgmt-network>=10.0.0',
           'azure-mgmt-resource>=11.0.0',
           'azure-mgmt-storage>=11.0.0',
           'azure-mgmt-subscription>=1.0.0',
           'azure-storage-blob>=12.0.0'],
 'gateway': ['flask>=2.1.2,<3.0.0',
             'lz4>=4.0.0,<5.0.0',
             'pynacl>=1.5.0,<2.0.0',
             'pyopenssl>=22.0.0,<23.0.0',
             'werkzeug>=2.1.2,<3.0.0'],
 'gcp': ['google-api-python-client>=2.0.2',
         'google-auth>=2.0.0',
         'google-cloud-compute>=1.0.0',
         'google-cloud-storage>=1.30.0'],
 'solver': ['cvxpy[cvxopt]>=1.1.0',
            'graphviz>=0.15',
            'matplotlib>=3.0.0',
            'numpy>=1.19.0']}

entry_points = \
{'console_scripts': ['skylark = skyplane.cli.cli:app',
                     'skyplane = skyplane.cli.cli:app']}

setup_kwargs = {
    'name': 'skyplane-nightly',
    'version': '0.2.0.dev20221014',
    'description': 'Skyplane efficiently transports data between cloud regions and providers.',
    'long_description': '<picture>\n    <source srcset="docs/_static/logo-dark-mode.png" media="(prefers-color-scheme: dark)">\n    <img src="docs/_static/logo-light-mode.png" width="300" />\n</picture>\n\n[![Join Slack](https://img.shields.io/badge/-Join%20Skyplane%20Slack-blue?logo=slack)](https://join.slack.com/t/skyplaneworkspace/shared_invite/zt-1cxmedcuc-GwIXLGyHTyOYELq7KoOl6Q)\n[![integration-test](https://github.com/skyplane-project/skyplane/actions/workflows/integration-test.yml/badge.svg)](https://github.com/skyplane-project/skyplane/actions/workflows/integration-test.yml)\n[![docker](https://github.com/skyplane-project/skyplane/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/skyplane-project/skyplane/actions/workflows/docker-publish.yml)\n[![docs](https://readthedocs.org/projects/skyplane/badge/?version=latest)](https://skyplane.readthedocs.io/en/latest/?badge=latest)\n\n**🔥 Blazing fast bulk data transfers between any cloud 🔥**\n\nSkyplane is a tool for blazingly fast bulk data transfers between object stores in the cloud. It provisions a fleet of VMs in the cloud to transfer data in parallel while using compression and bandwidth tiering to reduce cost.\n\nSkyplane is:\n1. 🔥 Blazing fast ([110x faster than AWS DataSync](https://skyplane.org/en/latest/benchmark.html))\n2. 🤑 Cheap (4x cheaper than rsync)\n3. 🌐 Universal (AWS, Azure and GCP)\n\nYou can use Skyplane to transfer data: \n* between object stores within a cloud provider (e.g. AWS us-east-1 to AWS us-west-2)\n* between object stores across multiple cloud providers (e.g. AWS us-east-1 to GCP us-central1)\n* between local storage and cloud object stores (experimental)\n\nSkyplane supports all major public clouds including AWS, Azure, and GCP. It can also transfer data between any combination of these clouds:\n\n<img src="docs/_static/supported-destinations.png" width="384" />\n\n# Using Skyplane\n\nThe easiest way to use Skyplane is to use the CLI. `skyplane cp` supports any local path or cloud object store destination as an argument.\n\n```bash\n# copy files between two AWS S3 buckets\n$ skyplane cp -r s3://... s3://...\n\n# copy files from an AWS S3 bucket to a GCP GCS bucket\n$ skyplane cp -r s3://... gs://...\n\n# copy files from a local directory to/from a cloud object store\n$ skyplane cp -r /path/to/local/files gs://...\n```\n\nSkyplane also supports incremental copies via `skyplane sync`:    \n```bash\n# copy changed files from S3 to GCS\n$ skyplane sync s3://... gcs://...\n```\n\n`skyplane sync` will diff the contents of the source and destination and only copy the files that are different or have changed. It will not delete files that are no longer present in the source so it\'s always safe to run `skyplane sync`.\n\n### Accelerating transfers with multiple VMs\n\nWith default arguments, Skyplane sets up a one VM (called gateway) in the source and destination regions. We can further accelerate the transfer by using more VMs.\n\nTo double the transfer speeds by using two VMs in each region, run:\n```bash\n$ skyplane cp -r s3://... s3://... -n 2\n```\n\nWith 8 VMs per region, Skyplane is capable of moving data at up to 50Gbps.\n\nIf you do not have enough vCPU capacity in each region, you may get a InsufficientVCPUException. Either request more vCPUs or reduce the number of parallel VMs.\n\n### ⚠️ Ensure the VMs that Skyplane starts are terminated\nSkyplane will automatically attempt to terminate VMs that it starts, but to double check and forcefuly terminate all VMs, run `skyplane deprovision`.\n\n# How Skyplane works\nSkyplane is based on research at UC Berkeley into accelerated networks between cloud providers. Our NSDI 2023 paper is upcoming, but a [technical talk](https://skyplane.org/en/latest/architecture.html) is available.\n\n<img src="docs/_static/skyplane-data-plane.png" width="384" />\n\nUnder the hood, Skyplane starts a fleet of VMs in the source and destination regions. It then uses a custom TCP protocol to accelerate the transfer between the VMs. Skyplane may use a L7 overlay network to route traffic around congested network hot spots. Notably, Skyplane does all this from a simple CLI interface.\n\n# Getting started\n\n## Installation\nWe recommend installation from PyPi:\n```\n$ pip install skyplane[aws]\n\n# install support for other clouds as needed:\n#   $ pip install skyplane[azure]\n#   $ pip install skyplane[gcp]\n#   $ pip install skyplane[all]\n```\n\nSkyplane supports AWS, Azure, and GCP. You can install Skyplane with support for one or more of these clouds by specifying the corresponding extras. To install two out of three clouds, you can run `pip install skyplane[aws,azure]`.\n\n*GCP support on the M1 Mac*: If you are using an M1 Mac with the arm64 architecture and want to install GCP support for Skyplane, you will need to install as follows\n`GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1 GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 pip install skyplane[aws,gcp]`\n\n## Authenticating with cloud providers\n\nTo transfer files from cloud A to cloud B, Skyplane will start VMs (called gateways) in both A and B. The CLI therefore requires authentication with each cloud provider. Skyplane will infer credentials from each cloud providers CLI. Therefore, log into each cloud.\n\n### Setting up AWS credentials\n\nTo set up AWS credentials on your local machine, first [install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).\n\nAfter installing the AWS CLI, configure your AWS IAM access ID and secret with `aws configure` ([more details](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html#getting-started-quickstart-new)).\n<!-- <details>\n<summary>"aws configure" output</summary>\n<br>\n \n```bash\n$ aws configure\nAWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE\nAWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY\nDefault region name [None]: us-west-2\nDefault output format [None]: json\n```\n</details> -->\n\n### Setting up GCP credentials\nTo set up GCP credentials on your local machine, first [install the gcloud CLI](https://cloud.google.com/sdk/docs/install-sdk).\n\nAfter installing the gcloud CLI, configure your GCP CLI credentials with `gcloud auth` as follows\n```bash\n$ gcloud auth login\n$ gcloud auth application-default login\n```\nEnsure the GCP Compute Engine, Storage Engine, Cloud Resource Manager, and IAM APIs are enabled for the project.\n\n### Setting up Azure credentials\n\nTo set up Azure credentials on your local machine, first [install the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).\n\nAfter installing the Azure CLI, configure your Azure CLI credentials with `az login` as follows:\n```bash\n$ az login\n```\n\nSkyplane should now be able to authenticate with Azure although you may need to pass your subscription ID to `skyplane init` later.\n\n## Importing cloud credentials into Skyplane\n\nAfter authenticating with each cloud provider, you can run `skyplane init` to create a configuration file for Skyplane.\n\n```bash\n$ skyplane init\n```\n<details>\n<summary>skyplane init output</summary>\n<br>\n\n```\n$ skyplane init\n\n====================================================\n _____ _   ____   _______ _       ___   _   _  _____\n/  ___| | / /\\ \\ / / ___ \\ |     / _ \\ | \\ | ||  ___|\n\\ `--.| |/ /  \\ V /| |_/ / |    / /_\\ \\|  \\| || |__\n `--. \\    \\   \\ / |  __/| |    |  _  || . ` ||  __|\n/\\__/ / |\\  \\  | | | |   | |____| | | || |\\  || |___\n\\____/\\_| \\_/  \\_/ \\_|   \\_____/\\_| |_/\\_| \\_/\\____/\n====================================================\n\n\n(1) Configuring AWS:\n    Loaded AWS credentials from the AWS CLI [IAM access key ID: ...XXXXXX]\n    AWS region config file saved to /home/ubuntu/.skyplane/aws_config\n\n(2) Configuring Azure:\n    Azure credentials found in Azure CLI\n    Azure credentials found, do you want to enable Azure support in Skyplane? [Y/n]: Y\n    Enter the Azure subscription ID: [XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX]:\n    Azure region config file saved to /home/ubuntu/.skyplane/azure_config\n    Querying for SKU availbility in regions\n    Azure SKU availability cached in /home/ubuntu/.skyplane/azure_sku_mapping\n\n(3) Configuring GCP:\n    GCP credentials found in GCP CLI\n    GCP credentials found, do you want to enable GCP support in Skyplane? [Y/n]: Y\n    Enter the GCP project ID [XXXXXXX]:\n    GCP region config file saved to /home/ubuntu/.skyplane/gcp_config\n\nConfig file saved to /home/ubuntu/.skyplane/config\n```\n\n</details>\n',
    'author': 'Skyplane authors',
    'author_email': 'skyplaneproject@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://skyplane.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
